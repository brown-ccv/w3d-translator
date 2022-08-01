using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Collections.Generic;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.SpatialTracking;
using Unity.XR.CoreUtils;
using TMPro;

using W3D;

// TODO: Should ConvertVector3 invert z axis always?

public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
{
    // void Start(){ Main(); } // TEMP: Execute script from Unity directly

    public static void Main()
    {
        Application.logMessageReceivedThreaded += HandleLog;
        Debug.Log("Running Unity CLI");
        string xmlPath = GetXmlPathArg();

        // TEMP - hard code xml file
        // xmlPath = "../../test/everything.xml";
        xmlPath = "../../test/sample.xml"; 

        Story xml = LoadStory(xmlPath);

        // TEMP - Load test scene from play
        // InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
        // GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
        // GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];
        GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
        GameObject story = SceneManager.GetActiveScene().GetRootGameObjects()[1];

        ApplyGlobalSettings(xml.Global, xrRig, story);
        BuildWalls(xml, story.transform);

        Dictionary<string, GameObject> gameObjects = TranslateGameObjects(xml.ObjectRoot, story);

        // Save and quit
        // EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene()); // Can only be run in editor mode
        Application.logMessageReceivedThreaded -= HandleLog;
        Application.Quit();
    }


    // Get command line arguments from Python
    static string GetXmlPathArg() {
        try {
            string[] args = System.Environment.GetCommandLineArgs();
            for (int i = 0; i < args.Length; i++) {
                if (args[i] == "--xmlPath") return args[++i];
            }
            return null; // No Path given
        }
        catch (Exception e) {
            Debug.Log("Error initializing command line arguments");
            Debug.LogException(e);
            throw e;
        }
    }

    // Deserialize the xml file into a Story object
    static Story LoadStory(string xmlPath) {
        try {
            XmlSerializer serializer = new XmlSerializer(typeof(Story));
            using (XmlReader reader = XmlReader.Create(xmlPath)) 
            {
                return (Story)serializer.Deserialize(reader);
            }
        } 
        catch(FileNotFoundException e) {
            Debug.LogError($"ERROR: File at {xmlPath} not found");
            Debug.LogException(e);
            throw e;
        } 
        catch(Exception e) {
            Debug.LogError($"Error: Deserialization of file at {xmlPath} failed.");
            Debug.LogException(e);
            throw e;
        }
    }

    // Create a new scene in Unity
    static InstantiationResult InstantiateScene(string xmlPath){
        try {
            return SceneTemplateService.Instantiate(
                Resources.Load<SceneTemplateAsset>("CAVE"),
                false,
                $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(xmlPath)}.unity"
            );
        } catch(Exception e) { 
            Debug.LogError($"Error creating scene for {xmlPath}");
            Debug.LogException(e);
            throw e;
        }

    }

    // Apply camera, lighting, and tracking settings from the xml
    static void ApplyGlobalSettings(Global xml, GameObject xrRig, GameObject story) {
        Transform mainCameraT = xrRig.transform.Find("Camera Offset").Find("Main Camera");
        Transform caveCameraT = story.transform.Find("Cave Camera");

        // Load default lighting settings and delete skybox
        UnityEditor.Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
        RenderSettings.skybox = null;

        // Use color based lighting - <Background color="0, 0, 0" />
        RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
        RenderSettings.ambientLight = Xml.ConvertColor(xml.Background.ColorString);
        
        // Update CaveCamera inside of story
        W3D.Camera xmlCaveCamera = xml.CaveCamera;
        UnityEngine.Camera caveCamera = 
            caveCameraT.GetComponent<UnityEngine.Camera>();
        caveCamera.farClipPlane = xmlCaveCamera.FarClip;
        xmlCaveCamera.Placement.SetTransform(caveCamera.transform, 1f, story.transform);

        // Update Camera inside of xrRig
        W3D.Camera xmlCamera = xml.Camera;
        UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
        camera.farClipPlane = xmlCamera.FarClip;
        xrRig.transform.position = 
            // xml.Camera is really the player's position - update xrRig directly
            // xrRig is outside the Story object so we must convert to meters
            Xml.ConvertVector3(xmlCamera.Placement.PositionString) * 0.3048f;

        // Update tracking settings for the Main Camera
        TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
        bool allowRotation = xml.WandNavigation.AllowRotation;
        bool allowMovement = xml.WandNavigation.AllowMovement;
        if(!allowRotation && !allowMovement) {
            tracking.enabled = false;
            // Setting the tracking to device based re-adds the camera offset
            xrRig.GetComponent<XROrigin>().RequestedTrackingOriginMode = 
                XROrigin.TrackingOriginMode.Device;
        }
        else {
            # pragma warning disable CS8509 // (false, false) case is handled above
            tracking.trackingType = (allowRotation, allowMovement) switch {
                (true, true) => TrackedPoseDriver.TrackingType.RotationAndPosition,
                (true, false) => TrackedPoseDriver.TrackingType.RotationOnly,
                (false, true) => TrackedPoseDriver.TrackingType.PositionOnly,
            };
        }
    }

    // Create each <Placement> as an outlined GameObject 
    static void BuildWalls(Story xml, Transform storyT) {
        // Each wall is an 8" by 8" square
        Vector3[] points = {
            new Vector3(-4, 4, 0),
            new Vector3(4, 4, 0),
            new Vector3(4, -4, 0),
            new Vector3(-4, -4, 0),
        };

        foreach (Placement placement in xml.PlacementRoot)
        {
            // Objects in the "Center" space are nested directly under Story
            if(placement.Name == "Center") continue;

            // Create and position wall
            GameObject wall = new GameObject();
            wall.name = placement.Name;
            wall.SetActive(true);
            placement.SetTransform(wall.transform, 1f, storyT);

            // TODO: Add a canvas to each wall

            // Create outline
            LineRenderer outline = wall.AddComponent<LineRenderer>();
            outline.widthMultiplier = 0.01f;
            outline.useWorldSpace = false;
            outline.loop = true;
            outline.material.SetColor("_EmissionColor", Color.white);
            outline.positionCount = points.Length;
            outline.SetPositions(points);
        }
        return;
    }

    // Convert Story.ObjectRoot to a dictionary of {name: GameObject} pairs
    static Dictionary<string, GameObject> TranslateGameObjects(
        List<W3D.Object> objectList, GameObject story
    ) {
        Dictionary<string, GameObject> gameObjects = new Dictionary<string, GameObject>();
        /** Object
            name: gameObject.name
            Visible: gameObject.active
            Color: gameObject.[content].color
            Lighting: TODO (76)
            ClickThrough: TODO (76)
            AroundSelfAxis: TODO (76)
            Scale: gameObject.localScale (set in Placement.SetTransform)
        */
        foreach (W3D.Object xml in objectList)
        {   
            GameObject gameObject = new GameObject();
            gameObject.name = xml.Name;
            xml.Placement.SetTransform(gameObject.transform, xml.Scale, story.transform);
            
            // TODO LinkRoot.Link -> Add a VRCanvas (74)
            if(xml.LinkRoot is not null) {}
    
            // Add Content component(s)
            switch(xml.Content.ContentData) {
                case(Text textContent):
                    textContent.GenerateTMP(gameObject, Xml.ConvertColor(xml.ColorString));
                    break;
                case(Image imageContent):
                    // TODO: type (65)
                    break;
                case(StereoImage stereoImageContent):
                    // TODO: type (66)
                    break;
                case(Model modelContent):
                    // TODO: type (67)
                    break;
                case(W3D.Light lightContent):
                    // TODO: type (68)
                    break;
                case(W3D.ParticleSystem particleSystemContent):
                    // TODO: type (69)
                    break;
                default: break;
            }

            gameObject.SetActive(xml.Visible);
            gameObjects.Add(gameObject.name, gameObject);
        }
        return gameObjects;
    }

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        // TODO: Log errors in red
        // TODO: Log warnings in yellow
        // TODO: Don't write Exceptions to console (just logfile)
        
        // Prepend "LOG:", we check for this in the Python script
        Console.WriteLine($"LOG:{logString}");
    }
}

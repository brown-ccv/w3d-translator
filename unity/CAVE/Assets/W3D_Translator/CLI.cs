using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;
using UnityEngine.SpatialTracking;
using Unity.XR.CoreUtils;

using W3D;

public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
{
    const bool DEV = true;

    #if DEV
        void Start(){ Main(); } // TEMP: Execute script from Unity directly
    #endif

    static void Main()
    {
        Application.logMessageReceivedThreaded += HandleLog;
        Debug.Log("Running Unity CLI");
        

        #if DEV
            // string xmlPath = "../../test/everything.xml";
            string xmlPath = "../../test/sample.xml"; 
        #else
            // The path to the xml is send as a command line argument
            string xmlPath = GetXmlPathArg();  
        #endif
        Story xml = LoadStory(xmlPath);

        #if DEV
            // Create new scene and load the root GameObjects
            InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
            GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
            GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];
        #else
            GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
            GameObject story = SceneManager.GetActiveScene().GetRootGameObjects()[1];
        #endif

        ApplyGlobalSettings(xml.Global, xrRig, story);
        BuildWalls(xml, story.transform);

        // Save and quit
        #if !DEV
            // Scenes can only be saved in editor mode
            EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
        #endif
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
            Debug.Log($"Error: Deserialization of file at {xmlPath} failed.");
            Debug.LogException(e);
            throw e;
        }
    }

    // Create a new scene in Unity
    static InstantiationResult InstantiateScene(string xmlPath){
        try{
            return SceneTemplateService.Instantiate(
                Resources.Load<SceneTemplateAsset>("CAVE"),
                false,
                $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(xmlPath)}.unity"
            );
        } catch(Exception e) { 
            Debug.Log($"Error creating scene for {xmlPath}");
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
        switch(allowRotation, allowMovement) {
            case (true, true):
                tracking.trackingType = TrackedPoseDriver.TrackingType.RotationAndPosition;
                break;
            case (true, false):
                tracking.trackingType = TrackedPoseDriver.TrackingType.RotationOnly;
                break;
            case (false, true):
                tracking.trackingType = TrackedPoseDriver.TrackingType.PositionOnly;
                break;
            case (false, false):
                tracking.enabled = false;
                // Using device based tracking adds the hard-coded camera offset
                xrRig.GetComponent<XROrigin>().RequestedTrackingOriginMode = 
                    XROrigin.TrackingOriginMode.Device;
                break;
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
            // Center objects are nested directly under Story
            if(placement.Name == "Center") continue;

            // Create wall
            GameObject wall = new GameObject();
            wall.name = placement.Name;
            wall.SetActive(true);
            placement.SetTransform(wall.transform, 1f, storyT);

            #if DEV
                // Create outline
                LineRenderer outline = wall.AddComponent<LineRenderer>();
                outline.widthMultiplier = 0.01f;
                outline.useWorldSpace = false;
                outline.loop = true;
                outline.material.SetColor("_EmissionColor", Color.white);
                outline.positionCount = points.Length;
                outline.SetPositions(points);
            #endif
        }
        return;
    }

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        // Prepend "LOG:", we check for this in the Python script
        Console.WriteLine($"LOG:{logString}");
    }
}

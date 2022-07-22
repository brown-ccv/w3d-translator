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

using W3D;

public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
{
    void Start(){ Main(); } // TEMP: Execute script from Unity directly

    static void Main()
    {
        Application.logMessageReceivedThreaded += HandleLog;
        Debug.Log("Running Unity CLI");
        string xmlPath = GetXmlPathArg();

        // TEMP - hard code xml file
        // xmlPath = "../../test/everything.xml";
        xmlPath = "../../test/sample.xml"; 

        Story xml = LoadStory(xmlPath);
        Debug.Log(xml.pprint());

        // TEMP - Load test scene from play
        // InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
        // GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
        // GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];
        GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
        GameObject story = SceneManager.GetActiveScene().GetRootGameObjects()[1];

        ApplyGlobalSettings(xml.Global, xrRig, story);

        Dictionary<string, GameObject> gameObjects = TranslateGameObjects(xml.ObjectRoot, story);

        // Save and quit
        // EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
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
        // Load default lighting settings and delete skybox
        UnityEditor.Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
        RenderSettings.skybox = null;

        // Use color based lighting - <Background color="0, 0, 0" />
        RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
        RenderSettings.ambientLight = Xml.ConvertColor(xml.Background.colorString);
        
        // Update CaveCamera inside of story
        W3D.Camera xmlCaveCamera = xml.CaveCamera;
        UnityEngine.Camera caveCamera = 
            story.transform.Find("Cave Camera").GetComponent<UnityEngine.Camera>();
        caveCamera.farClipPlane = xmlCaveCamera.farClip;
        Debug.Assert(xmlCaveCamera.Placement.relativeTo == Placement.RelativeTo.Center);
        caveCamera.transform.localPosition = 
            Xml.ConvertVector3(xmlCaveCamera.Placement.positionString);

        // Update Camera inside of xrRig
        W3D.Camera xmlCamera = xml.Camera;
        UnityEngine.Camera camera = 
            xrRig.transform.GetChild(0).Find("Main Camera").GetComponent<UnityEngine.Camera>();
        camera.farClipPlane = xmlCamera.farClip;
        Debug.Assert(xmlCamera.Placement.relativeTo == Placement.RelativeTo.Center);

        // xml.Camera is really the player's position - update xrRig directly
        // xrRig is outside the Story object so we must convert to meters
        xrRig.transform.position = 
            Xml.ConvertVector3(xmlCamera.Placement.positionString) * 0.3048f;

        // Update tracking settings for the Main Camera
        TrackedPoseDriver tracking = xrRig.transform.GetChild(0).Find("Main Camera").GetComponent<TrackedPoseDriver>();
        bool allowRotation = xml.WandNavigation.allowRotation;
        bool allowMovement = xml.WandNavigation.allowMovement;
        if(!allowRotation && !allowMovement) {
            tracking.enabled = false;
        } else if(allowRotation && allowMovement) {
            tracking.trackingType = TrackedPoseDriver.TrackingType.RotationAndPosition;
        } else if(allowRotation && !allowMovement) {
            tracking.trackingType = TrackedPoseDriver.TrackingType.RotationOnly;
        } else if(!allowRotation && allowMovement) {
            tracking.trackingType = TrackedPoseDriver.TrackingType.PositionOnly;
        }
    }

    // Convert Story.ObjectRoot to a dictionary of {name: GameObject} pairs
    static Dictionary<string, GameObject> TranslateGameObjects(
        List<W3D.Object> objectList, GameObject story
    ) {
        Dictionary<string, GameObject> gameObjects = new Dictionary<string, GameObject>();
        
        
        W3D.Object xml = objectList[0]; // TEMP - Make loop
        
        /** Object
            Visible: gameObject.active
            Color: TODO
            Lighting: TODO
            ClickThrough: TODO
            AroundSelfAxis: TODO
            Scale: gameObject.localScale (Convert to vector)
            Placement.RelativeTo: gameObject.transform.parent
            Placement.Position: gameObject.transform.localPosition
            name: gameObject.name
        */
        GameObject gameObject = new GameObject();
        gameObject.name = xml.name;
        gameObject.SetActive(xml.visible);

        // Nest under Placement.RelativeTo & set local transform
        gameObject.transform.parent = story.transform.Find(xml.Placement.relativeTo.ToString());
        gameObject.transform.localPosition = Xml.ConvertVector3(xml.Placement.positionString);
        gameObject.transform.localScale = Vector3.one * xml.scale;
        gameObject.transform.localRotation = Quaternion.identity; // No local rotation
        
        // LinkRoot.Link -> Add a VRCanvas
        if(xml.LinkRoot != null) {

        }

        // Add Component(s)
        // TODO: Add the TODOs to GitHub and here
        switch(xml.Content.content) {
            case(Content.ContentType.Text): {
                Text content = (Text)xml.Content.content;
                break;
            }
            case(Content.ContentType.Image): {
                Image content = (Image)xml.Content.content;
                break;
            }
            case(Content.ContentType.StereoImage): {
                StereoImage content = (StereoImage)xml.Content.content;
                break;
            }
            case(Content.ContentType.Model): {
                Model content = (Model)xml.Content.content;
                break;
            }
            case(Content.ContentType.Light): {
                W3D.Light content = (W3D.Light)xml.Content.content;
                break;
            }
            case(Content.ContentType.ParticleSystem): {
                W3D.ParticleSystem content = (W3D.ParticleSystem)xml.Content.content;
                break;
            }
            default: break;
        }
        
        
        gameObjects.Add(gameObject.name, gameObject);
        return gameObjects;
    }

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        // Prepend "LOG:", we check for this in the Python script
        Console.WriteLine($"LOG:{logString}");
    }
}

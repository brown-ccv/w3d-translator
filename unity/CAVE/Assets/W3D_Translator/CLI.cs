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
        string xmlPath = GetXmlPathArg();

        // TEMP - hard code xml file
        // xmlPath = "../../test/everything.xml";
        xmlPath = "../../test/sample.xml"; 

        Story xml = LoadStory(xmlPath);
        Debug.Log(xml.pprint());

        // Temp - Load test scene from play
        // InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
        // GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
        // GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];
        GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
        GameObject story = SceneManager.GetActiveScene().GetRootGameObjects()[1];

        ApplyGlobalSettings(xml.Global, xrRig, story);

        // Save and quit
        // EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
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
        Debug.Assert(xmlCaveCamera.Placement.relativeTo == "Center");
        caveCamera.transform.localPosition = 
            Xml.ConvertVector3(xmlCaveCamera.Placement.positionString);

        // Update Camera inside of xrRig
        W3D.Camera xmlCamera = xml.Camera;
        UnityEngine.Camera camera = 
            xrRig.transform.GetChild(0).Find("Main Camera").GetComponent<UnityEngine.Camera>();
        camera.farClipPlane = xmlCamera.farClip;
        Debug.Assert(xmlCamera.Placement.relativeTo == "Center");

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
}

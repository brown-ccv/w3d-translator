using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.Events;
using UnityEditor.SceneTemplate;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.SpatialTracking;
using UnityEngine.UI;
using UnityEngine.Events;
using Unity.XR.CoreUtils;

using W3D;

// TODO (80): Should ConvertVector3 invert z axis always?

public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
{
    void Start(){ Main(); } // TEMP - Run script on Play

    static void Main()
    {
        Application.logMessageReceivedThreaded += HandleLog;
        Debug.Log("Running Unity CLI");
        
        // The path to the xml is send as a command line argument
        // string xmlPath = GetXmlPathArg();
        string xmlPath = "../../test/sample.xml"; 
        Story xml = LoadStory(xmlPath);

        // Create new scene and store the root GameObjects
        // InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
        // GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
        // GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];
        GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
        GameObject story = SceneManager.GetActiveScene().GetRootGameObjects()[1];

        ApplyGlobalSettings(xml.Global, xrRig, story);
        BuildWalls(xml, story.transform);
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
                return (Story)serializer.Deserialize(reader);
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
        xmlCaveCamera.Placement.SetTransform(caveCamera.transform, Vector3.one, story.transform);

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
            // Objects in the "Center" space are nested directly under Story
            if(placement.Name == "Center") continue;

            // Create and position wall
            GameObject wall = new GameObject();
            wall.name = placement.Name;
            wall.SetActive(true);
            placement.SetTransform(wall.transform, Vector3.one, storyT);

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
        ActionMethods methods = story.GetComponent<ActionMethods>();
        Dictionary<string, GameObject> gameObjects = new Dictionary<string, GameObject>();
        
        /** Object
            name: gameObject.name
            Visible: gameObject.active
            Color: gameObject.[content].color (disabledColor if <LinkRoot> is present)
            Lighting: TODO (76)
            ClickThrough: TODO (76)
            AroundSelfAxis: TODO (76)
            Scale: gameObject.localScale (set in Placement.SetTransform)
        */
        foreach (W3D.Object xml in objectList)
        {
            GameObject contentGO = xml.Content.Create(xml);

            // TODO (74): LinkRoot.Link -> Add a VRCanvas
            if(xml.LinkRoot is not null) {
                // Instantiate a new link prefab
                GameObject prefab = Instantiate(Resources.Load<GameObject>("Prefabs/canvas"));
                prefab.GetComponent<Canvas>().worldCamera = UnityEngine.Camera.main;
                
                // Set xml for canvas
                prefab.name = xml.Name;
                prefab.SetActive(xml.Visible);
                xml.Placement.SetTransform(prefab.transform, xml.GetScale(), story.transform);
                prefab.transform.localScale *= 0.1f;

                Link link = xml.LinkRoot.Link;
                GameObject buttonGO = prefab.transform.GetChild(0).gameObject;
                Button button = buttonGO.GetComponent<Button>();

                // Nest the original <Content> GameObject inside the prefab
                contentGO.transform.SetParent(buttonGO.transform, false);

                // Set xml for button
                button.targetGraphic = contentGO.GetComponent<Graphic>(); // Text, Image, etc.
                button.colors = link.SetColors(button.colors, xml.ColorString);
                

                // Add the <Action>s to onClick
                Button.ButtonClickedEvent onClick = button.onClick;
                foreach (LinkActions xmlAction in link.Actions) {
                    if(
                        xmlAction.Clicks is not null && 
                        xmlAction.Clicks.Type == Clicks.ActivationTypes.Number
                    ){
                        // Button is only activated after a certain number of clicks
                    }



                    // TODO: Each case wil add this persistent listener (class method)
                    // UnityEventTools.AddObjectPersistentListener<Button>(
                    //     onClick, 
                    //     new UnityAction<Button>(methods.DisableButton),// Call class function
                    //     button
                    // );

                    // TODO (83): Add button actions
                    switch(xmlAction.Action) {
                        case(ObjectChange objectRef):
                            // TODO 86
                            break;
                        case(GroupRef groupRef):
                            // TODO 87
                            break;
                        case(TimerChange timelineRef):
                            // TODO 88
                            break;
                        case(W3D.Event eventTriggerRef):
                            // TODO 89
                            break;
                        case(MoveCave moveCave):
                            // TODO 90
                            break;
                        case(Reference soundRef):
                            // TODO 91
                            break;
                        default:
                            if(xmlAction.Type == Actions.ActionTypes.Restart) {
                                // TODO (92): Test for "Restart" type
                            } else throw new Exception("TODO");
                            break;
                    }
                }
                link.SetRemainEnabled(methods, onClick, button);
            } else {
                contentGO.SetActive(xml.Visible);
                xml.Placement.SetTransform(contentGO.transform, xml.GetScale(), story.transform);
            }
            gameObjects.Add(contentGO.name, contentGO);
        }
        return gameObjects;
    }

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        // TODO (84): Change string based on LogType (rich color)
        // Prepending "LOG:" will print the line to the screen (checked in Python script)
        
        Console.WriteLine($"LOG:{logString}");
    }
}
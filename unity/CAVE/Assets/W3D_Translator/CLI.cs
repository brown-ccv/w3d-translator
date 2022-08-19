using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Linq;
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

// Custom Type renaming
using TType = UnityEngine.SpatialTracking.TrackedPoseDriver.TrackingType;

// TODO (80): Should ConvertVector3 invert z axis always?
// TODO (94): Make story (GO) a member variable
// TODO (94): Make (xml) a member variable
// TODO (94): Make gameObjects a member variable

namespace W3D
{
    public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
    {
        private void Start() { Main(); } // TEMP: Execute script from Unity directly

        private static Story XML;
        private static GameObject Story;
        private static readonly Dictionary<string, Object> GameObjects = new();

        public static void Main()
        {
            Application.logMessageReceivedThreaded += HandleLog;
            Debug.Log("Running Unity CLI");

            // The path to the xml is send as a command line argument
            // const string xmlPath = GetXmlPathArg();
            const string xmlPath = "../../test/sample.xml";
            LoadStory(xmlPath);

            // Create new scene and store the root GameObjects
            // InstantiationResult instantiatedScene = InstantiateScene(xmlPath);
            // GameObject xrRig = instantiatedScene.scene.GetRootGameObjects()[0];
            // story = instantiatedScene.scene.GetRootGameObjects()[1];
            GameObject xrRig = SceneManager.GetActiveScene().GetRootGameObjects()[0];
            Story = SceneManager.GetActiveScene().GetRootGameObjects()[1];

            ApplyGlobalSettings(XML.Global, xrRig);
            BuildWalls(Story.transform);
            TranslateGameObjects(XML.ObjectRoot);

            // TODO (95): Generate the <Group>s
            // TODO (96): Generate the <Timeline>s
            // TODO (97): Generate the <Sound>s
            // TODO (98): Generate the <Event>s
            // TODO (99): Generate the <ParticleAction>s

            SetLinkActions();

            // Save and quit
            // EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
            Application.logMessageReceivedThreaded -= HandleLog;
            Application.Quit();
        }

        // Get command line arguments from Python
        private static string GetXmlPathArg()
        {
            try
            {
                string[] args = Environment.GetCommandLineArgs();
                for (int i = 0; i < args.Length; i++)
                {
                    if (args[i] == "--xmlPath") { return args[++i]; }
                }
                return null; // No Path given
            }
            catch (Exception e)
            {
                Debug.Log("Error initializing command line arguments");
                Debug.LogException(e);
                return null;
            }
        }

        // Deserialize the xml file into a Story object
        private static void LoadStory(string xmlPath)
        {
            try
            {
                XmlSerializer serializer = new(typeof(Story));
                using XmlReader reader = XmlReader.Create(xmlPath);
                XML = (Story)serializer.Deserialize(reader);
            }
            catch (FileNotFoundException e)
            {
                Debug.LogError($"ERROR: File at {xmlPath} not found");
                Debug.LogException(e);
            }
            catch (Exception e)
            {
                Debug.LogError($"Error: Deserialization of file at {xmlPath} failed.");
                Debug.LogException(e);
            }
        }

        // Create a new scene in Unity
        private static InstantiationResult InstantiateScene(string xmlPath)
        {
            try
            {
                return SceneTemplateService.Instantiate(
                    Resources.Load<SceneTemplateAsset>("CAVE"),
                    false,
                    $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(xmlPath)}.unity"
                );
            }
            catch (Exception e)
            {
                Debug.LogError($"Error creating scene for {xmlPath}");
                Debug.LogException(e);
                return null;
            }
        }

        // Apply camera, lighting, and tracking settings from the xml
        private static void ApplyGlobalSettings(Global xml, GameObject xrRig)
        {
            Transform mainCameraT = xrRig.transform.Find("Camera Offset").Find("Main Camera");
            Transform caveCameraT = Story.transform.Find("Cave Camera");

            // Load default lighting settings and delete skybox
            Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
            RenderSettings.skybox = null;

            // Use color based lighting - <Background color="0, 0, 0" />
            RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
            RenderSettings.ambientLight = Xml.ConvertColor(xml.Background.ColorString);

            // Update CaveCamera inside of story
            Camera xmlCaveCamera = xml.CaveCamera;
            UnityEngine.Camera caveCamera =
                caveCameraT.GetComponent<UnityEngine.Camera>();
            caveCamera.farClipPlane = xmlCaveCamera.FarClip;
            xmlCaveCamera.Placement.SetTransform(caveCamera.transform, Vector3.one, Story.transform);

            // Update Camera inside of xrRig
            Camera xmlCamera = xml.Camera;
            UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
            camera.farClipPlane = xmlCamera.FarClip;
            xrRig.transform.position =
                // xml.Camera is really the player's position - update xrRig directly
                // xrRig is outside the Story object so we must convert to meters
                Xml.ConvertVector3(xmlCamera.Placement.PositionString) * 0.3048f;

            // Update tracking settings for the Main Camera
            TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
            switch (xml.WandNavigation.AllowRotation, xml.WandNavigation.AllowMovement)
            {
                case (true, true):
                    tracking.trackingType = TType.RotationAndPosition;
                    break;
                case (true, false):
                    tracking.trackingType = TType.RotationOnly;
                    break;
                case (false, true):
                    tracking.trackingType = TType.PositionOnly;
                    break;
                case (false, false):
                    tracking.enabled = false;
                    // Using device based tracking adds the hard-coded camera offset
                    xrRig.GetComponent<XROrigin>().RequestedTrackingOriginMode =
                        XROrigin.TrackingOriginMode.Device;
                    break;
                default: // Unreachable but fixes warning
            }
        }

        // Create each <Placement> as an outlined GameObject 
        private static void BuildWalls(Transform storyT)
        {
            // Each wall is an 8" by 8" square
            Vector3[] points = {
            new Vector3(-4, 4, 0),
            new Vector3(4, 4, 0),
            new Vector3(4, -4, 0),
            new Vector3(-4, -4, 0),
        };

            foreach (Placement placement in XML.PlacementRoot)
            {
                // Objects in the "Center" space are nested directly under Story
                if (placement.Name == "Center") { continue; }

                // Create and position wall
                GameObject wall = new()
                {
                    name = placement.Name
                };
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
        private static void TranslateGameObjects(List<Object> objectList)
        {
            /** Object
                name: gameObject.name
                Visible: gameObject.active
                Color: gameObject.[content].color (disabledColor if <LinkRoot> is present)
                Lighting: TODO (76)
                ClickThrough: TODO (76)
                AroundSelfAxis: TODO (76)
                Scale: gameObject.localScale (set in Placement.SetTransform)
            */
            foreach (Object xml in objectList)
            {
                GameObject contentGO = xml.Content.Create(xml);
                if (xml.LinkRoot is not null)
                {
                    // Instantiate a new link prefab
                    GameObject prefab = Instantiate(Resources.Load<GameObject>("Prefabs/canvas"));
                    prefab.GetComponent<Canvas>().worldCamera = UnityEngine.Camera.main;

                    // Set xml for canvas
                    prefab.name = xml.Name;
                    prefab.SetActive(xml.Visible);
                    xml.Placement.SetTransform(prefab.transform, xml.GetScale(), Story.transform);
                    prefab.transform.localScale *= 0.1f;

                    Link link = xml.LinkRoot.Link;
                    GameObject buttonGO = prefab.transform.GetChild(0).gameObject;
                    Button button = buttonGO.GetComponent<Button>();

                    // Nest the original <Content> GameObject inside the prefab
                    contentGO.transform.SetParent(buttonGO.transform, false);

                    // Set xml for button
                    button.targetGraphic = contentGO.GetComponent<Graphic>(); // Text, Image, etc.
                    button.colors = link.SetColors(button.colors, xml.ColorString);
                }
                else
                {
                    contentGO.SetActive(xml.Visible);
                    xml.Placement.SetTransform(contentGO.transform, xml.GetScale(), Story.transform);
                }
                xml.GameObject = contentGO;
                GameObjects.Add(xml.Name, xml);
            }
            return;
        }

        private static void SetLinkActions()
        {
            ActionMethods methods = Story.GetComponent<ActionMethods>();

            foreach (KeyValuePair<string, Object> pair in
                GameObjects.Where(pair => pair.Value.LinkRoot is not null)
            )
            {
                Object obj = pair.Value;
                Link link = obj.LinkRoot.Link;
                GameObject buttonGO = obj.GameObject.transform.parent.gameObject;
                Button button = buttonGO.GetComponent<Button>();

                // Add the <Action>s to onClick
                Button.ButtonClickedEvent onClick = button.onClick;
                foreach (LinkActions xmlAction in link.Actions)
                {
                    if (
                        xmlAction.Clicks is not null &&
                        xmlAction.Clicks.Type == Clicks.ActivationTypes.Number
                    )
                    {
                        // Button is only activated after a certain number of clicks
                    }

                    // TODO (83): Add button actions
                    switch (xmlAction.Action)
                    {
                        case ObjectChange objectRef:
                            // TODO 86
                            break;
                        case GroupRef groupRef:
                            // TODO 87
                            break;
                        case TimerChange timelineRef:
                            // TODO 88
                            break;
                        case Event eventTriggerRef:
                            // TODO 89
                            break;
                        case MoveCave moveCave:
                            // TODO 90
                            break;
                        case Reference soundRef:
                            // TODO 91
                            break;
                        default:
                            if (xmlAction.Type == Actions.ActionTypes.Restart)
                            {
                                // TODO 92
                            }
                            else { throw new Exception("TODO"); }
                            break;
                    }
                }
                link.SetRemainEnabled(methods, onClick, button);
            }
        }

        // Callback function when Debug.Log is called within the CLI script
        private static void HandleLog(string logString, string stackTrace, LogType type)
        {
            // TODO (84): Change string based on LogType (rich color)
            // Prepending "LOG:" will print the line to the screen (checked in Python script)

            Console.WriteLine($"LOG:{logString}");
        }
    }
}
using System;
using System.IO;
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

using XML;

// Custom Type renaming
using TType = UnityEngine.SpatialTracking.TrackedPoseDriver.TrackingType;

// TODO (80): Should ConvertVector3 invert z axis always?

namespace W3D
{
    [ExecuteInEditMode]
    public static class CLI // TEMP: MonoBehavior can be removed?
    {
        // public static ProjectPath;

        private static Root RootX;
        private static GameObject Root;
        private static GameObject XrRig;

        private static readonly Dictionary<string, (GameObject, XML.Object)> GameObjects = new();

        [MenuItem("Custom/CLI %g")]
        public static void Main()
        {
            Application.logMessageReceivedThreaded += HandleLog;
            Debug.Log("Running Unity CLI");

            // The path to the xml file is sent as a command line argument
            // const string projectPath = GetXmlPathArg();
            const string projectPath = "../../test/sample.xml";
            LoadStory(projectPath);

            // Create new scene and store the root GameObjects
            InstantiationResult instantiatedScene = InstantiateScene(projectPath);
            XrRig = instantiatedScene.scene.GetRootGameObjects()[0];
            Root = instantiatedScene.scene.GetRootGameObjects()[1];

            ApplyGlobalSettings();
            BuildWalls();
            TranslateGameObjects();

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
                    if (args[i] == "--projectPath") { return args[++i]; }
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

        // Deserialize the xml file
        private static void LoadStory(string projectPath)
        {
            try
            {
                System.Xml.Serialization.XmlSerializer serializer = new(typeof(Root));
                using var reader = System.Xml.XmlReader.Create(projectPath);
                RootX = (Root)serializer.Deserialize(reader);
            }
            catch (FileNotFoundException e)
            {
                Debug.LogError($"ERROR: File at {projectPath} not found");
                Debug.LogException(e);
            }
            catch (Exception e)
            {
                Debug.LogError($"Error: Deserialization of file at {projectPath} failed.");
                Debug.LogException(e);
            }
        }

        // Create a new scene in Unity
        private static InstantiationResult InstantiateScene(string projectPath)
        {
            try
            {
                return SceneTemplateService.Instantiate(
                    Resources.Load<SceneTemplateAsset>("CAVE"),
                    false,
                    $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(projectPath)}.unity"
                );
            }
            catch (Exception e)
            {
                Debug.LogError($"Error creating scene for {projectPath}");
                Debug.LogException(e);
                return null;
            }
        }

        // Apply camera, lighting, and tracking settings
        private static void ApplyGlobalSettings()
        {
            Global globalX = RootX.Global;
            Transform mainCameraT = XrRig.transform.Find("Camera Offset").Find("Main Camera");
            Transform caveCameraT = Root.transform.Find("Cave Camera");

            // Load default lighting settings and delete skybox
            Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
            RenderSettings.skybox = null;

            // Use color based lighting - <Background color="0, 0, 0" />
            RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
            RenderSettings.ambientLight = Xml.ConvertColor(globalX.Background.ColorString);

            // Update CaveCamera inside of story
            XML.Camera CaveCameraX = globalX.CaveCamera;
            UnityEngine.Camera caveCamera =
                caveCameraT.GetComponent<UnityEngine.Camera>();
            caveCamera.farClipPlane = CaveCameraX.FarClip;
            CaveCameraX.Placement.SetTransform(caveCamera.transform, Vector3.one, Root.transform);

            // Update Camera inside of xrRig
            XML.Camera CameraX = globalX.Camera;
            UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
            camera.farClipPlane = CameraX.FarClip;
            XrRig.transform.position =
                // CameraX is really the player's position - update xrRig directly
                // xrRig is outside the Root object so we must convert to meters
                Xml.ConvertVector3(CameraX.Placement.PositionString) * 0.3048f;

            // Update tracking settings for the Main Camera
            TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
            XROrigin xrOrigin = XrRig.GetComponent<XROrigin>();
            switch (globalX.WandNavigation.AllowRotation, globalX.WandNavigation.AllowMovement)
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
                    xrOrigin.RequestedTrackingOriginMode = XROrigin.TrackingOriginMode.Device;
                    break;
                default: // Unreachable but fixes warning
            }
        }

        // Create each <Placement> as an outlined GameObject 
        private static void BuildWalls()
        {
            // Each wall is an 8" by 8" square
            Vector3[] points = {
                new Vector3(-4, 4, 0),
                new Vector3(4, 4, 0),
                new Vector3(4, -4, 0),
                new Vector3(-4, -4, 0),
            };

            foreach (Placement placement in RootX.PlacementRoot)
            {
                // Objects in the "Center" space are nested directly under Root
                if (placement.Name == "Center") { continue; }

                // Create and position wall
                GameObject wall = new() { name = placement.Name };
                // TODO: TEST
                // wall.SetActive(true); 
                placement.SetTransform(wall.transform, Vector3.one, Root.transform);

                // Create outline
                LineRenderer outline = wall.AddComponent<LineRenderer>();
                outline.widthMultiplier = 0.01f;
                outline.useWorldSpace = false;
                outline.loop = true;
                outline.material.SetColor("_EmissionColor", Color.white);
                outline.positionCount = points.Length;
                outline.SetPositions(points);
            }
        }

        // Build the <Object>s and save them in a dictionary of {name: GameObject} pairs
        private static void TranslateGameObjects()
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
            foreach (XML.Object objectX in RootX.ObjectRoot)
            {
                GameObject contentGO = objectX.Content.Create(objectX);
                if (objectX.LinkRoot is not null)
                {
                    // Instantiate a new link prefab
                    GameObject prefab = (GameObject)PrefabUtility.InstantiatePrefab(
                        Resources.Load<GameObject>("Prefabs/canvas")
                    );
                    prefab.GetComponent<Canvas>().worldCamera = UnityEngine.Camera.main;

                    // Initialize canvas
                    prefab.name = objectX.Name;
                    prefab.SetActive(objectX.Visible);
                    objectX.Placement.SetTransform(
                        prefab.transform,
                        objectX.GetScale(),
                        Root.transform
                    );
                    prefab.transform.localScale *= 0.1f;

                    GameObject buttonGO = prefab.transform.GetChild(0).gameObject;
                    Button button = buttonGO.GetComponent<Button>();

                    // Nest the <Content> inside the prefab and initialize button
                    contentGO.transform.SetParent(buttonGO.transform, false);
                    button.targetGraphic = contentGO.GetComponent<Graphic>(); // Text, Image, etc.
                    button.colors = objectX.LinkRoot.Link.SetColors(
                        button.colors,
                        objectX.ColorString
                    );
                }
                else
                {
                    contentGO.SetActive(objectX.Visible);
                    objectX.Placement.SetTransform(contentGO.transform, objectX.GetScale(), Root.transform);
                }
                GameObjects.Add(contentGO.name, (contentGO, objectX));
            }
        }

        private static void SetLinkActions()
        {
            foreach (KeyValuePair<string, (GameObject, XML.Object)> pair in
                GameObjects.Where(pair => pair.Value.Item2.LinkRoot is not null)
            )
            {
                (GameObject go, XML.Object obj) = pair.Value;
                GameObject buttonGO = go.transform.parent.gameObject;
                Button button = buttonGO.GetComponent<Button>();
                Link link = obj.LinkRoot.Link;

                // Add the <Action>s to onClick
                Button.ButtonClickedEvent onClick = button.onClick;
                foreach (LinkActions linkActionX in link.Actions)
                {
                    Clicks clicksX = linkActionX.Clicks;
                    if (clicksX is not null &&clicksX.Type == Clicks.ActivationTypes.Number)
                    {
                        // Button is only activated after a certain number of clicks
                    }

                    // TODO (83): Add button actions
                    switch (linkActionX.Action)
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
                        case XML.Event eventTriggerRef:
                            // TODO 89
                            break;
                        case MoveCave moveCave:
                            // TODO 90
                            break;
                        case Reference soundRef:
                            // TODO 91
                            break;
                        default:
                            if (linkActionX.Type == Actions.ActionTypes.Restart)
                            {
                                // TODO 92
                            }
                            else { throw new Exception("TODO"); }
                            break;
                    }
                }
                if (!link.RemainEnabled)
                {
                    UnityEventTools.AddVoidPersistentListener(
                        onClick,
                        new UnityAction(button.GetComponent<ButtonManager>().DisableButton)
                    );
                }
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
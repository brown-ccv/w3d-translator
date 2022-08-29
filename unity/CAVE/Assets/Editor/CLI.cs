using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Unity.XR.CoreUtils;
using UnityEditor;
using UnityEditor.Events;
using UnityEditor.SceneTemplate;
using UnityEngine;
using UnityEngine.SpatialTracking;
using UnityEngine.UI;
using UnityEngine.Events;

using Writing3D;
using Writing3D.Xml;

using static Writing3D.Xml.Xml;
using static Writing3D.Translation.Helpers;
using static UnityEngine.SpatialTracking.TrackedPoseDriver;

// TODO (80): Should ConvertVector3 invert z axis always?

namespace Writing3D
{
    namespace Translation
    {
        public static class CLI
        {
            public static string ProjectPath;

            private static Root RootX;
            private static GameObject Root;
            private static GameObject XrRig;

            private static Dictionary<string, (GameObject, Xml.Object)> GameObjects;

            [MenuItem("Custom/CLI.Main %g")]
            public static void Main()
            {
                Application.logMessageReceivedThreaded += HandleLog;
                Debug.Log($"Running Unity CLI {ProjectPath}");

                // The path to the xml file is sent as a command line argument
                GetXmlPathArg();
                LoadStory();

                // Create new scene and store the root GameObjects
                InstantiationResult instantiatedScene = InstantiateScene();
                XrRig = instantiatedScene.scene.GetRootGameObjects()[0];
                Root = instantiatedScene.scene.GetRootGameObjects()[1];
                GameObjects = new Dictionary<string, (GameObject, Xml.Object)>();

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
            private static void GetXmlPathArg()
            {
                try
                {
                    string[] args = Environment.GetCommandLineArgs();
                    for (int i = 0; i < args.Length; i++)
                    {
                        if (args[i] == "--projectPath") { ProjectPath = args[++i]; }
                    }
                }
                catch (Exception e)
                {
                    Debug.Log("Error initializing command line arguments");
                    Debug.LogException(e);
                }
            }

            // Deserialize the xml file
            private static void LoadStory()
            {
                try
                {
                    System.Xml.Serialization.XmlSerializer serializer = new(typeof(Root));
                    using var reader = System.Xml.XmlReader.Create(ProjectPath);
                    RootX = (Root)serializer.Deserialize(reader);
                }
                catch (FileNotFoundException)
                {
                    Debug.LogError($"ERROR: File at {ProjectPath} not found");
                    throw;
                }
                catch
                {
                    Debug.LogError($"Error: Deserialization of file at {ProjectPath} failed.");
                    throw;
                }
            }

            // Create a new scene in Unity
            private static InstantiationResult InstantiateScene()
            {
                try
                {
                    return SceneTemplateService.Instantiate(
                        Resources.Load<SceneTemplateAsset>("CAVE"),
                        false,
                        $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(ProjectPath)}.unity"
                    );
                }
                catch (Exception e)
                {
                    Debug.LogError($"Error creating scene for {ProjectPath}");
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
                RenderSettings.ambientLight = ConvertColor(globalX.Background.ColorString);

                // Update CaveCamera inside of story
                Xml.Camera CaveCameraX = globalX.CaveCamera;
                UnityEngine.Camera caveCamera =
                    caveCameraT.GetComponent<UnityEngine.Camera>();
                caveCamera.farClipPlane = CaveCameraX.FarClip;
                CaveCameraX.Placement.SetTransform(caveCamera.transform, Vector3.one, Root.transform);

                // Update Camera inside of xrRig
                Xml.Camera CameraX = globalX.Camera;
                UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
                camera.farClipPlane = CameraX.FarClip;
                XrRig.transform.position =
                    // CameraX is really the player's position - update xrRig directly
                    // xrRig is outside the Root object so we must convert to meters
                    ConvertVector3(CameraX.Placement.PositionString) * 0.3048f;

                // Update tracking settings for the Main Camera
                TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
                XROrigin xrOrigin = XrRig.GetComponent<XROrigin>();
                switch (globalX.WandNavigation.AllowRotation, globalX.WandNavigation.AllowMovement)
                {
                    case (true, true):
                        tracking.trackingType = TrackingType.RotationAndPosition;
                        break;
                    case (true, false):
                        tracking.trackingType = TrackingType.RotationOnly;
                        break;
                    case (false, true):
                        tracking.trackingType = TrackingType.PositionOnly;
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
                    outline.material = (Material)Resources.Load(
                        "Materials/EmitWhite",
                        typeof(Material)
                    );
                    outline.widthMultiplier = 0.01f;
                    outline.useWorldSpace = false;
                    outline.loop = true;
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
                foreach (Xml.Object objectX in RootX.ObjectRoot)
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
                        objectX.Placement.SetTransform(
                            contentGO.transform,
                            objectX.GetScale(),
                            Root.transform
                        );
                    }
                    GameObjects.Add(contentGO.name, (contentGO, objectX));
                }
            }

            private static void SetLinkActions()
            {
                foreach (KeyValuePair<string, (GameObject, Xml.Object)> pair in
                    GameObjects.Where(pair => pair.Value.Item2.LinkRoot is not null)
                )
                {
                    (GameObject go, Xml.Object obj) = pair.Value;
                    GameObject buttonGO = go.transform.parent.gameObject;
                    Button button = buttonGO.GetComponent<Button>();
                    Link link = obj.LinkRoot.Link;

                    // Add the <Action>s to onClick
                    Button.ButtonClickedEvent onClick = button.onClick;
                    foreach (LinkActions linkActionX in link.Actions)
                    {
                        Clicks clicksX = linkActionX.Clicks;
                        if (clicksX is not null && clicksX.Type == Clicks.ActivationTypes.Number)
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
                            case Xml.Event eventTriggerRef:
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
                // Prepending "LOG:" will print the line to the screen in Python script)

                Console.WriteLine($"LOG:{logString}");
            }
        }
    }
}
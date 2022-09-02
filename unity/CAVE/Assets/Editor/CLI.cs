using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.SceneTemplate;
using UnityEngine;
using UnityEngine.SpatialTracking;
using UnityEngine.UI;
using UnityEngine.Events;
using Unity.XR.CoreUtils;

using Writing3D.Xml;

using static UnityEngine.SpatialTracking.TrackedPoseDriver;
using static UnityEditor.Events.UnityEventTools;

// TODO (80): Should ConvertVector3 invert z axis always?

namespace Writing3D
{
    namespace Translation
    {
        public static partial class CLI
        {
            public static string ProjectPath;

            private static Root XmlRoot;
            private static GameObject Root;
            private static GameObject XrRig;

            private static Dictionary<string, GameObject> Walls;
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
                catch (Exception)
                {
                    Debug.LogError("Error initializing command line arguments");
                    throw;
                }
            }

            // Deserialize the xml file
            private static void LoadStory()
            {
                try
                {
                    System.Xml.Serialization.XmlSerializer serializer = new(typeof(Root));
                    using var reader = System.Xml.XmlReader.Create(ProjectPath);
                    XmlRoot = (Root)serializer.Deserialize(reader);
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
                catch (Exception)
                {
                    Debug.LogError($"Error creating scene for {ProjectPath}");
                    throw;
                }
            }

            // Apply camera, lighting, and tracking settings
            private static void ApplyGlobalSettings()
            {
                Global xmlGlobal = XmlRoot.Global;
                Transform mainCameraT = XrRig.transform.Find("Camera Offset").Find("Main Camera");
                Transform caveCameraT = Root.transform.Find("Cave Camera");

                // Load default lighting settings and delete skybox
                Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
                RenderSettings.skybox = null;

                // Use color based lighting - <Background color="0, 0, 0" />
                RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
                RenderSettings.ambientLight = ConvertColor(xmlGlobal.Background.ColorString);

                // Update CaveCamera inside of root
                Xml.Camera xmlCaveCamera = xmlGlobal.CaveCamera;
                UnityEngine.Camera caveCamera =
                    caveCameraT.GetComponent<UnityEngine.Camera>();
                caveCamera.farClipPlane = xmlCaveCamera.FarClip;
                SetTransform(caveCamera.transform, xmlCaveCamera.Placement);

                // Update Camera inside of xrRig
                Xml.Camera xmlCamera = xmlGlobal.Camera;
                UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
                camera.farClipPlane = xmlCamera.FarClip;
                XrRig.transform.position =
                    // CameraX is really the player's position - update xrRig directly
                    // xrRig is outside the Root object so we must convert to meters
                    ConvertVector3(xmlCamera.Placement.PositionString) * 0.3048f;

                // Update tracking settings for the Main Camera
                TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
                XROrigin xrOrigin = XrRig.GetComponent<XROrigin>();
                switch (xmlGlobal.WandNavigation.AllowRotation, xmlGlobal.WandNavigation.AllowMovement)
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
                foreach (Placement xmlPlacement in XmlRoot.PlacementRoot)
                {
                    // Objects in the "Center" space are nested directly under Root
                    if (xmlPlacement.Name == "Center") { continue; }

                    // Create and position wall
                    GameObject wall = UnityEngine.Object.Instantiate(Resources.Load<GameObject>("Prefabs/wall"));
                    wall.name = xmlPlacement.Name;
                    SetTransform(wall.transform, xmlPlacement);
                    Walls.Add(wall.name, wall);
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
                foreach (Xml.Object xmlObject in XmlRoot.ObjectRoot)
                {
                    GameObject contentGO = CreateObject(xmlObject);
                    if (xmlObject.LinkRoot is not null)
                    {
                        Link xmlLink = xmlObject.LinkRoot.Link;

                        // Instantiate a new link prefab
                        GameObject prefab = (GameObject)PrefabUtility.InstantiatePrefab(
                            Resources.Load<GameObject>("Prefabs/canvas")
                        );
                        prefab.GetComponent<Canvas>().worldCamera = UnityEngine.Camera.main;

                        // Initialize canvas
                        prefab.name = xmlObject.Name;
                        prefab.SetActive(xmlObject.Visible);
                        SetTransform(prefab.transform, xmlObject.Placement, xmlObject.Scale);
                        prefab.transform.localScale *= 0.1f;

                        GameObject buttonGO = prefab.transform.GetChild(0).gameObject;
                        Button button = buttonGO.GetComponent<Button>();

                        // Nest the <Content> inside the prefab and initialize button
                        contentGO.transform.SetParent(buttonGO.transform, false);
                        button.targetGraphic = contentGO.GetComponent<Graphic>(); // Text, Image, etc.

                        // Set state colors
                        ColorBlock newColors = button.colors;
                        newColors.normalColor = newColors.highlightedColor =
                            ConvertColor(xmlLink.EnabledColorString);
                        newColors.pressedColor = newColors.selectedColor =
                            ConvertColor(xmlLink.SelectedColorString);
                        newColors.disabledColor = ConvertColor(xmlObject.ColorString);
                        button.colors = newColors;
                    }
                    else
                    {
                        contentGO.SetActive(xmlObject.Visible);
                        SetTransform(contentGO.transform, xmlObject.Placement, xmlObject.Scale);
                    }
                    GameObjects.Add(contentGO.name, (contentGO, xmlObject));
                }
            }

            private static void SetLinkActions()
            {
                foreach (
                    KeyValuePair<string, (GameObject, Xml.Object)> pair in
                    GameObjects.Where(pair => pair.Value.Item2.LinkRoot is not null)
                )
                {
                    (GameObject go, Xml.Object xmlObject) = pair.Value;
                    Link xmlLink = xmlObject.LinkRoot.Link;
                    GameObject buttonGO = go.transform.parent.gameObject;
                    Button button = buttonGO.GetComponent<Button>();
                    ButtonManager bm = button.GetComponent<ButtonManager>();
                    Button.ButtonClickedEvent onClick = button.onClick;

                    // Add actions
                    AddVoidPersistentListener(onClick, new UnityAction(bm.Counter));

                    // Add the <Action>s wrapper to onClick
                    foreach (LinkActions xmlLinkAction in xmlLink.Actions)
                    {
                        try { AddAction(xmlLinkAction, button); }
                        catch (Exception)
                        {
                            Debug.LogError(
                                "Unable to create action for " + xmlObject.Name +
                                ": " + JsonUtility.ToJson(xmlLinkAction)
                            );
                            throw;
                        }
                    }

                    if (!xmlLink.RemainEnabled)
                    {
                        AddVoidPersistentListener(
                            onClick,
                            new UnityAction(button.GetComponent<ButtonManager>().Disable)
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
}
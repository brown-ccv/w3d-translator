using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;

using Unity.XR.CoreUtils;

using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

using UnityEngine;
using UnityEngine.Events;
using UnityEngine.InputSystem.XR;

using Writing3D;

using static UnityEditor.Events.UnityEventTools;
using static UnityEngine.InputSystem.XR.TrackedPoseDriver;


namespace Writing3D
{
    namespace Editor
    {
        public static partial class CLI
        {
            public static string XmlPath;
            private static InstantiationResult InstantiatedScene;

            private static Xml.Root XmlRoot;
            private static GameObject Root;
            private static GameObject XROrigin;

            private static Dictionary<string, Transform> Walls;
            private static Dictionary<string, (GameObject, Xml.Object)> GameObjects;

            [MenuItem("Custom/CLI.Main %g")]
            public static void Main()
            {
                Application.logMessageReceivedThreaded += HandleLog;
                try
                {
                    if (!Application.isBatchMode) ClearConsole();

                    // Load xml file
                    GetXmlPathArg();
                    LoadXml();

                    // Create new scene and store the root GameObjects
                    Debug.Log("Instantiating Scene");
                    InstantiatedScene = InstantiateScene();

                    Root = InstantiatedScene.scene.GetRootGameObjects()[0];
                    XROrigin = InstantiatedScene.scene.GetRootGameObjects()[1].transform.Find("XR Origin").gameObject;

                    GameObjects = new Dictionary<string, (GameObject, Xml.Object)>();
                    Walls = new Dictionary<string, Transform>() { { "Center", Root.transform } };

                    // Instantiate the device simulator while testing
                    Debug.Log("Instantiate Device Simulator");
                    if (!Application.isBatchMode) InstantiateSimulator();

                    Debug.Log("Applying global settings");
                    ApplyGlobalSettings();

                    Debug.Log("Building Objects");
                    BuildWalls(); // TODO: Only build if desired?
                    TranslateGameObjects();

                    // TODO 95: Generate the <Group>s
                    // TODO 96: Generate the <Timeline>s
                    // TODO 97: Generate the <Sound>s
                    // TODO 98: Generate the <Event>s
                    // TODO 99: Generate the <ParticleAction>s

                    //Debug.Log("Applying actions");
                    SetLinkActions();

                    // Save and build scene
                    Debug.Log("Building Scene");
                    EditorSceneManager.SaveScene(InstantiatedScene.scene);
                    // BuildReport report = BuildScene();
                    // Debug.Log($"Build {report.summary.result}");
                }
                catch (Exception e)
                {
                    Debug.LogException(e);
                    File.Delete(InstantiatedScene.scene.path); // TODO: Is this deleting the meta file?
                }
                finally { Application.logMessageReceivedThreaded -= HandleLog; }
            }

            // Clear the editor console
            private static void ClearConsole()
            {
                Assembly assembly = Assembly.GetAssembly(typeof(UnityEditor.Editor));
                Type type = assembly.GetType("UnityEditor.LogEntries");
                MethodBase method = type.GetMethod("Clear");
                method.Invoke(new object(), null);
            }

            // Get command line arguments from Python
            private static void GetXmlPathArg()
            {
                try
                {
                    string[] args = Environment.GetCommandLineArgs();
                    for (int i = 0; i < args.Length; i++)
                    {
                        if (args[i] == "--xmlPath") { XmlPath = args[++i]; }
                    }
                }
                catch
                {
                    Debug.LogError("Error initializing command line arguments");
                    throw;
                }
            }

            // Deserialize the xml file
            private static void LoadXml()
            {
                try
                {
                    System.Xml.Serialization.XmlSerializer serializer = new(typeof(Xml.Root));
                    using var reader = System.Xml.XmlReader.Create(XmlPath);
                    XmlRoot = (Xml.Root)serializer.Deserialize(reader);
                }
                catch (FileNotFoundException)
                {
                    Debug.LogError($"File at {XmlPath} not found");
                    throw;
                }
                catch
                {
                    Debug.LogError($"Deserialization of file at {XmlPath} failed.");
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
                        $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(XmlPath)}.unity"
                    );
                }
                catch
                {
                    Debug.LogError($"Unable to create scene for {XmlPath}");
                    throw;
                }
            }

            // Add the XR Device simulator
            private static void InstantiateSimulator()
            {
                try
                {
                    UnityEngine.Object.Instantiate(
                        AssetDatabase.LoadAssetAtPath(
                            "Assets/Samples/XR Interaction Toolkit/2.2.0/XR Device Simulator/" +
                            "XR Device Simulator.prefab",
                            typeof(GameObject)
                        ) as GameObject,
                        XROrigin.transform.position,
                        XROrigin.transform.rotation
                    ).transform.SetAsLastSibling();
                }
                catch
                {
                    Debug.LogError($"Unable to instantiate headset simulator");
                    throw;
                }
            }

            // Apply camera, lighting, and tracking settings
            private static void ApplyGlobalSettings()
            {
                Xml.Global xmlGlobal = XmlRoot.Global;
                Transform mainCameraT = XROrigin.transform.Find("CameraOffset").Find("Main Camera");
                Transform caveCameraT = Root.transform.Find("Cave Camera");

                // Load default lighting settings and delete skybox
                Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
                RenderSettings.skybox = null;

                // Use color based lighting - <Background color="0, 0, 0" />
                RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
                RenderSettings.ambientLight = ConvertColor(xmlGlobal.Background.ColorString);

                // Update CaveCamera inside of root
                Xml.Camera xmlCaveCamera = xmlGlobal.CaveCamera;
                UnityEngine.Camera caveCamera = caveCameraT.GetComponent<UnityEngine.Camera>();
                caveCamera.farClipPlane = xmlCaveCamera.FarClip;
                SetTransform(caveCamera.transform, xmlCaveCamera.Placement);

                // Update Camera inside of XROrigin
                Xml.Camera xmlCamera = xmlGlobal.Camera;
                UnityEngine.Camera camera = mainCameraT.GetComponent<UnityEngine.Camera>();
                camera.farClipPlane = xmlCamera.FarClip;
                XROrigin.transform.position =
                    // CameraX is really the player's position - update XROrigin directly
                    // XROrigin is outside the Root object so we must convert to meters
                    ConvertVector3(xmlCamera.Placement.PositionString) * 0.3048f;

                // Update tracking settings for the Main Camera
                TrackedPoseDriver tracking = mainCameraT.GetComponent<TrackedPoseDriver>();
                Xml.WandNavigation wand = xmlGlobal.WandNavigation;
                switch (wand.AllowRotation, wand.AllowMovement)
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
                        XROrigin.GetComponent<XROrigin>().RequestedTrackingOriginMode
                            // Using device based tracking adds the hard-coded camera offset
                            = Unity.XR.CoreUtils.XROrigin.TrackingOriginMode.Device;
                        break;
                    default: // Unreachable but fixes warning
                }
            }

            // Create each <Placement> as an outlined GameObject 
            private static void BuildWalls()
            {
                foreach (Xml.Placement xmlPlacement in XmlRoot.PlacementRoot)
                {
                    string name = xmlPlacement.Name;

                    // Objects in the "Center" space are nested directly under Root
                    if (name == "Center") { continue; }

                    // Create and position wall
                    GameObject wall = UnityEngine.Object.Instantiate(Resources.Load<GameObject>("Prefabs/wall"));
                    wall.name = name;
                    SetTransform(wall.transform, xmlPlacement);
                    Walls.Add(name, wall.transform);
                }
            }

            // Build the <Object>s and save them in a dictionary of {name: GameObject} pairs
            private static void TranslateGameObjects()
            {
                /** Object
                    name: gameObject.name
                    Visible: gameObject.active
                    Color: gameObject.[content].color (disabledColor if <LinkRoot> is present)
                    Lighting: (TODO 76)
                    ClickThrough: gameObject<Collider>.enabled (opposite)
                    AroundSelfAxis: (TODO 76)
                    Scale: gameObject.localScale (set in Placement.SetTransform)
                */
                foreach (Xml.Object xmlObject in XmlRoot.ObjectRoot)
                {
                    // TODO 124: Use IBuilder syntax to build the object
                    // Separate content, transform, components, link, actions
                    GameObject go = CreateContent(xmlObject);
                    go.name = xmlObject.Name;
                    SetTransform(go.transform, xmlObject.Placement, xmlObject.Scale);
                    go.GetComponent<Renderer>().enabled = xmlObject.Visible;
                    go.GetComponent<Collider>().enabled =
                        // TODO 123: Collider always disabled if object isn't visible?
                        !xmlObject.ClickThrough && xmlObject.Visible;

                    if (xmlObject.LinkRoot is not null)
                    {
                        Xml.Link xmlLink = xmlObject.LinkRoot.Link;

                        // Add LinkManager and initialize
                        LinkManager lm = go.AddComponent<LinkManager>();
                        lm.DisabledColor = ConvertColor(xmlObject.ColorString);
                        lm.EnabledColor = ConvertColor(xmlLink.EnabledColorString);
                        lm.ActiveColor = ConvertColor(xmlLink.SelectedColorString);
                        if (xmlLink.Enabled) { lm.EnableLink(); }
                        else { lm.DisableLink(); }
                    }
                    GameObjects.Add(go.name, (go, xmlObject));
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
                    Xml.Link xmlLink = xmlObject.LinkRoot.Link;
                    LinkManager lm = go.GetComponent<LinkManager>();

                    // Add the <Action>s wrapper on activated (onTriggerDown)
                    AddVoidPersistentListener(lm.activated, new UnityAction(lm.Activate));

                    // Add the <Action>'s on deactivated (onTriggerUp)
                    AddVoidPersistentListener(
                        lm.deactivated,
                        new UnityAction(lm.Deactivate)
                    );
                    foreach (Xml.LinkActions xmlLinkAction in xmlLink.Actions)
                    {
                        try { AddAction(xmlLinkAction, lm); }
                        catch
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
                            lm.deactivated,
                            new UnityAction(lm.DisableLink)
                        );
                    }
                }
            }

            private static BuildReport BuildScene()
            {
                // TODO: Need to build for VR and for the CAVE
                // Add README file?

                string sceneName = InstantiatedScene.scene.name;
                string scenePath = InstantiatedScene.scene.path;
                return BuildPipeline.BuildPlayer(
                    new string[] { scenePath },             // Scenes to build
                    $"Builds/{sceneName}/{sceneName}.exe",  // Output path
                    BuildTarget.StandaloneWindows64,
                    BuildOptions.None
                );
            }

            // Callback function when Debug.Log is called within the CLI script
            private static void HandleLog(string logString, string stackTrace, LogType type)
            {
                // Prepending "LOG:" will print the line to the screen (Python script)
                string color = type switch
                {
                    LogType.Log => "white",
                    LogType.Warning => "yellow",
                    LogType.Error => "red",
                    LogType.Exception => "bold red",
                    _ => "white"
                };
                Console.WriteLine($"LOG:[{color}]{logString}[/{color}]");
            }
        }
    }
}
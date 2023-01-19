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

using static UnityEditor.Events.UnityEventTools;
using static UnityEngine.InputSystem.XR.TrackedPoseDriver;

namespace Writing3D
{
    namespace Editor
    {
        public static partial class CLI
        {
            public static string _XmlPath;
            private static InstantiationResult _InstantiatedScene;

            private static Xml.Root _XmlRoot;
            private static GameObject _Root;
            private static GameObject _XROrigin;
            private static GameObject _MVRManager;

            private static Dictionary<string, Transform> _WallsDict;
            private static Dictionary<string, (GameObject, Xml.Object)> _ObjectDict;

            [MenuItem("Custom/CLI.Main %g")]
            public static void Main()
            {
                // Leave CaveCamera clippingPane as default? (farClip: 1000)
                // TODO: Apply Player Settings? MiddleVR -> Editor -> MVRCustomEditor.cs (ApplyMVRSettings)
                // What position is best for MVR to start at? How does it pick up tracking?
                Application.logMessageReceivedThreaded += HandleLog;
                try
                {
                    // Clear console if testing
                    if (!Application.isBatchMode) { ClearConsole(); }

                    // Load xml file
                    GetXmlPathArg();
                    LoadXml();

                    // Create new scene and store the root GameObjects
                    // TODO: Create new scene and clone prefabs?
                    Debug.Log("Instantiating Scene");
                    _InstantiatedScene = InstantiateScene();
                    _Root = _InstantiatedScene.scene.GetRootGameObjects()[0];
                    _XROrigin
                        = _InstantiatedScene.scene.GetRootGameObjects()[1].GetNamedChild("XR Origin");
                    _MVRManager = _InstantiatedScene.scene.GetRootGameObjects()[2];

                    _ObjectDict = new Dictionary<string, (GameObject, Xml.Object)>();
                    _WallsDict = new Dictionary<string, Transform>() { { "Center", _Root.transform } };

                    // Instantiate the device simulator if testing
                    // TEMP - Not using simulator
                    //Debug.Log("Instantiating Device Simulator");
                    //if (!Application.isBatchMode) { InstantiateSimulator(); }

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

                    Debug.Log("Applying actions");
                    SetLinkActions();

                    // Save and build scene
                    //Debug.Log("Building Scene");
                    EditorSceneManager.SaveScene(_InstantiatedScene.scene);
                    // BuildReport report = BuildScene();
                    // Debug.Log($"Build {report.summary.result}");
                }
                catch (Exception e)
                {
                    Debug.LogException(e);
                    File.Delete(_InstantiatedScene.scene.path); // TODO: Is this deleting the meta file?
                }
                finally { Application.logMessageReceivedThreaded -= HandleLog; }
            }

            // Clear the editor console
            private static void ClearConsole()
            {
                var type = Assembly.GetAssembly(typeof(UnityEditor.Editor)).GetType("UnityEditor.LogEntries");
                type.GetMethod("Clear").Invoke(new object(), null);
            }

            // Get command line arguments from Python
            private static void GetXmlPathArg()
            {
                try
                {
                    string[] args = Environment.GetCommandLineArgs();
                    for (int i = 0; i < args.Length; i++)
                    {
                        if (args[i] == "--xmlPath") { _XmlPath = args[++i]; }
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
                    using var reader = System.Xml.XmlReader.Create(_XmlPath);
                    _XmlRoot = (Xml.Root)serializer.Deserialize(reader);
                }
                catch (FileNotFoundException)
                {
                    Debug.LogError($"File at {_XmlPath} not found");
                    throw;
                }
                catch
                {
                    Debug.LogError($"Deserialization of file at {_XmlPath} failed.");
                    throw;
                }
            }

            // Create a new scene in Unity
            private static InstantiationResult InstantiateScene()
            {
                try
                {
                    var caveScene = Resources.Load<SceneTemplateAsset>("CAVE");
                    string scenePath
                        = $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(_XmlPath)}.unity";
                    return SceneTemplateService.Instantiate(caveScene, false, scenePath);
                }
                catch
                {
                    Debug.LogError($"Unable to create scene for {_XmlPath}");
                    throw;
                }
            }

            // Add the XR Device simulator
            private static void InstantiateSimulator()
            {
                try
                {
                    string simPrefabPath
                        = "Assets/Samples/XR Interaction Toolkit/2.2.0/XR Device Simulator/"
                        + "XR Device Simulator.prefab";
                    GameObject sim = UnityEngine.Object.Instantiate(
                        AssetDatabase.LoadAssetAtPath(simPrefabPath, typeof(GameObject)) as GameObject,
                        _XROrigin.transform.position,
                        _XROrigin.transform.rotation
                    );
                    sim.transform.SetAsLastSibling();
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
                Xml.Global xmlGlobal = _XmlRoot.Global;
                Transform mainCameraT = _XROrigin.transform.Find("CameraOffset").Find("Main Camera");
                Transform caveCameraT = _Root.transform.Find("Cave Camera");

                // Load default lighting settings and delete skybox
                Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");
                RenderSettings.skybox = null;

                // Use color based lighting - <Background color="0, 0, 0" />
                RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
                RenderSettings.ambientLight = ConvertColor(xmlGlobal.Background.ColorString);

                // Update CaveCamera inside of root
                Xml.Camera xmlCaveCamera = xmlGlobal.CaveCamera;
                Camera caveCamera = caveCameraT.GetComponent<Camera>();
                caveCamera.farClipPlane = xmlCaveCamera.FarClip; // TODO: Remove?
                caveCamera.backgroundColor = ConvertColor(xmlGlobal.Background.ColorString, 0);
                SetTransform(caveCamera.transform, xmlCaveCamera.Placement);

                // Use CaveCamera as a template for MVR
                MVRManagerScript mvrScript = _MVRManager.GetComponent<MVRManagerScript>();
                //mvrScript.advancedProperties.TemplateCamera = caveCameraT.gameObject;

                // Update Camera inside of _XROrigin
                Xml.Camera xmlCamera = xmlGlobal.Camera;
                Camera camera = mainCameraT.GetComponent<Camera>();
                camera.farClipPlane = xmlCamera.FarClip;
                _XROrigin.transform.position =
                    // CameraX is really the player's position - update _XROrigin directly
                    // _XROrigin is outside the _Root object so we must convert to meters
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
                        _XROrigin.GetComponent<XROrigin>().RequestedTrackingOriginMode
                            // Using device based tracking adds the hard-coded camera offset
                            = XROrigin.TrackingOriginMode.Device;
                        break;
                    default:
                }
            }

            // Create each <Placement> as an outlined GameObject 
            private static void BuildWalls()
            {
                foreach (Xml.Placement xmlPlacement in _XmlRoot.PlacementRoot)
                {
                    string name = xmlPlacement.Name;

                    // Objects in the "Center" space are nested directly under _Root
                    if (name == "Center") { continue; }

                    // Create and position wall
                    GameObject wall = UnityEngine.Object.Instantiate(Resources.Load<GameObject>("Prefabs/wall"));
                    wall.name = name;
                    SetTransform(wall.transform, xmlPlacement);
                    _WallsDict.Add(name, wall.transform);
                }
            }

            // Build the <Object>s and save them in a dictionary of {name: GameObject} pairs
            private static void TranslateGameObjects()
            {
                /** Object
                    name: gameObject.name
                    Visible: gameObject.active
                    Color: gameObject.[content].color (disabledColor if <Link_Root> is present)
                    Lighting: (TODO 76)
                    ClickThrough: gameObject<Collider>.enabled (opposite)
                    AroundSelfAxis: (TODO 76)
                    Scale: gameObject.localScale (set in Placement.SetTransform)
                */
                foreach (Xml.Object xmlObject in _XmlRoot.ObjectRoot)
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

                        // Add MVRInteractable and initialize
                        MVRInteractable mvi = go.AddComponent<MVRInteractable>();
                        mvi.Grabable = false;
                        mvi.AddCollider = false;
                        AddPersistentListener(mvi.MVRWandButton, mvi.HandleMVRInteraction);
                    }
                    _ObjectDict.Add(go.name, (go, xmlObject));
                }
            }

            private static void SetLinkActions()
            {
                foreach (
                    KeyValuePair<string, (GameObject, Xml.Object)> pair in
                    _ObjectDict.Where(pair => pair.Value.Item2.LinkRoot is not null)
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

                string sceneName = _InstantiatedScene.scene.name;
                string scenePath = _InstantiatedScene.scene.path;
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
                    LogType.Assert => "blue",
                    _ => "white"
                };
                Console.WriteLine($"LOG:[{color}]{logString}[/{color}]");
            }
        }
    }
}
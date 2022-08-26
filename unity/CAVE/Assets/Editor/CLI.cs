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

using static UnityEngine.SpatialTracking.TrackedPoseDriver;
using static UnityEditor.Events.UnityEventTools;
using static UnityEditor.SceneManagement.EditorSceneManager;

using XML;
using W3D;

// TODO (80): Should ConvertVector3 invert z axis always?

namespace CLI
{
    public static class CLI
    {
        public static string ProjectPath;

        private static Root RootX;
        private static GameObject Root;
        private static GameObject XrRig;

        // TODO: Better to just find all objects with an "Object" tag?
        private static Dictionary<string, (GameObject, XML.Object)> GameObjects;

        [MenuItem("Custom/CLI.Main %g")]
        public static void Main()
        {
            Application.logMessageReceivedThreaded += HandleLog;
            Debug.Log("Running Unity CLI");

            // The path to the xml file is sent as a command line argument
            GetXmlPathArg();
            LoadStory();

            // Create new scene and store the root GameObjects
            InstantiationResult instantiatedScene = InstantiateScene();
            XrRig = instantiatedScene.scene.GetRootGameObjects()[0];
            Root = instantiatedScene.scene.GetRootGameObjects()[1];
            GameObjects = new Dictionary<string, (GameObject, XML.Object)>();

            ApplyGlobalSettings();
            BuildWalls();
            BuildGameObjects();

            // TODO (95): Generate the <Group>s
            // TODO (96): Generate the <Timeline>s
            // TODO (97): Generate the <Sound>s
            // TODO (98): Generate the <Event>s
            // TODO (99): Generate the <ParticleAction>s

            SetLinkActions();

            // Save and quit
            SaveScene(instantiatedScene.scene);
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
                default: // All cases covered
            }
        }

        // Create each <Placement> as an outlined GameObject 
        private static void BuildWalls()
        {
            foreach (Placement placement in RootX.PlacementRoot)
            {
                // Objects in the "Center" space are nested directly under Root
                if (placement.Name == "Center") { continue; }

                // Create and position wall
                GameObject wall = (GameObject)PrefabUtility.InstantiatePrefab(
                    Resources.Load<GameObject>("Prefabs/wall")
                );
                wall.name = placement.Name;
                placement.SetTransform(wall.transform, Vector3.one, Root.transform);
            }
        }

        // Build the <Object>s and save them in a dictionary of {name: GameObject} pairs
        private static void BuildGameObjects()
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
                GameObject contentGO = objectX.Create();
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
            foreach (
                KeyValuePair<string, (GameObject, XML.Object)> pair in
                GameObjects.Where(pair => pair.Value.Item2.LinkRoot is not null)
            )
            {
                (GameObject go, XML.Object obj) = pair.Value;
                Link link = obj.LinkRoot.Link;
                GameObject buttonGO = go.transform.parent.gameObject;
                Button button = buttonGO.GetComponent<Button>();
                ButtonManager bm = button.GetComponent<ButtonManager>();
                Button.ButtonClickedEvent onClick = button.onClick;

                // Add actions
                AddVoidPersistentListener(onClick, new UnityAction(bm.Counter));
                AddVoidPersistentListener(onClick, new UnityAction(bm.ExecuteActions));
                if (!link.RemainEnabled)
                {
                    AddVoidPersistentListener(
                        onClick,
                        new UnityAction(button.GetComponent<ButtonManager>().Disable)
                    );
                }

                // Add the <Action>s to onClick
                bm.Actions = new();
                foreach (LinkActions linkActionX in link.Actions)
                {
                    AddAction(linkActionX, button);
                }
            }
        }

        private static void AddAction(LinkActions linkActionX, Button button)
        {
            ButtonManager bm = button.GetComponent<ButtonManager>();
            Button.ButtonClickedEvent onClick = button.onClick;

            // GameObject reference;
            // LinkAction action = new(linkActionX);
            // switch (linkActionX.Action)
            // {
            //     case ObjectChange objChange:
            //         // Get referenced GameObject and initialize Transition
            //         reference = GameObjects[objChange.Name].Item1;
            //         action.Transition = new Transition(objChange.Transition);

            //         // Add delegate based on transition
            //         action.Delegate = action.Transition.GetDelegate(objChange.Transition.Change, reference);

            //         break;
            //     case GroupChange groupChange:
            //         // TODO: 87
            //         break;
            //     case TimerChange timerChange:
            //         // TODO: 88
            //         break;
            //     case EventChange eventChange:
            //         // TODO: 89
            //         break;
            //     case MoveCave moveCave:
            //         // TODO: 90
            //         break;
            //     case Reference soundChange:
            //         // TODO: 91
            //         break;
            //     case null:
            //         // TODO: 92
            //         break;
            //     default: break; // All cases covered
            // }
            // TODO: Store action class and delegate function? 
            // Store actions and create delegates on start?
            // bm.Actions.Add(action);
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
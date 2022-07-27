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

using W3D;

public class CLI : MonoBehaviour // TEMP: MonoBehavior can be removed?
{
    void Start(){ Main(); } // TEMP: Execute script from Unity directly

    static void Main()
    {
        Application.logMessageReceivedThreaded += HandleLog;
        Debug.Log("Running Unity CLI");
        string xmlPath = null;

        // Get command line arguments from Python
        try {
            string[] args = System.Environment.GetCommandLineArgs();
            for(int i = 0; i < args.Length; i++)
            {
                if(args[i] == "--xmlPath") {
                    xmlPath = args[i + 1];
                    break;
                }
            }
        } catch(Exception e) {
            Debug.Log("Error initializing command line arguments");
            Debug.Log(e);
            throw e;
        }

        xmlPath = "../../examples/cweditor/everything.xml"; // TEMP - hard code xml file
        // xmlPath = "../../test/sample.xml"; // TEMP - hard code xml file

        // TODO: Add try/catch for when deserialization fails
        XmlSerializer serializer = new XmlSerializer(typeof(W3D.Story));
        W3D.Story story = null;
        using (XmlReader reader = XmlReader.Create(xmlPath))
        {
            story = (W3D.Story)serializer.Deserialize(reader);
        }
        Debug.Log(story.pprint());

        foreach(EventTrigger e in story.EventRoot) {
            switch(e.TrackType){
                case EventTrigger.TrackTypes.Move: {
                    MoveTrack track = (MoveTrack)e.Tracking;
                    switch(track.Box.Movement.Data){
                        case Movement.MovementTypes.Inside: {
                            Debug.Log($"{e.Name}: Move Track Inside");
                            break;
                        }
                        case Movement.MovementTypes.Outside: {
                            Debug.Log($"{e.Name}: Move Track Outside");
                            break;
                        }
                    }
                    break;
                }
                case EventTrigger.TrackTypes.Head: {
                    HeadTrack track = (HeadTrack)e.Tracking;
                    switch(track.Direction.TargetType) {
                        case Direction.Targets.None: {
                            Debug.Log($"{e.Name}: Head Track None");
                            break;
                        }
                        case Direction.Targets.Point: {
                            Debug.Log($"{e.Name}: Head Track Point");
                            break;
                        }
                        case Direction.Targets.Direction: {
                            Debug.Log($"{e.Name}: Head Track Direction");
                            break;
                        }
                        case Direction.Targets.Object: {
                            Debug.Log($"{e.Name}: Head Track Object {((Reference)track.Direction.Target).Name}");
                            break;
                        }
                    }
                    break;
                }
            }
        }

        /********** TEMP: Leave empty for Unity IDE Development ***********/

        // Load the XML
        // XmlDocument file = new XmlDocument();
        // try {
        //     file.Load(xmlPath);
        // } catch(FileNotFoundException e) {
        //     Debug.LogError($"ERROR: File {xmlPath} not found");
        //     Debug.LogException(e);
        //     throw e;
        // } 

        // Create the Unity scene
        // InstantiationResult instantiatedScene = null;
        // try{
        //     instantiatedScene = SceneTemplateService.Instantiate(
        //         Resources.Load<SceneTemplateAsset>("CAVE"),
        //         false,
        //         $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(xmlPath)}.unity"
        //     );
        // } catch(Exception e) { 
        //     Debug.LogError($"Error creating scene for {xmlPath}");
        //     Debug.LogException(e);
        //     throw e;
        // }
        // Example(instantiatedScene.scene);

        Application.logMessageReceivedThreaded -= HandleLog;
        Application.Quit();
    }

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        // Prepend "LOG:", we check for this in the Python script
        Console.WriteLine($"LOG:{logString}");
    }

    // EXAMPLE - Add sphere at origin of each wall
    static void Example(Scene scene)
    {
        GameObject story = scene.GetRootGameObjects()[1];
        Material material = new Material(Shader.Find("Standard"));
        material.SetColor("_Color", Color.blue);
        foreach (Transform storyChild in story.transform) {
            if(Regex.IsMatch(storyChild.name, @"Wall$")) {
                GameObject Sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                Sphere.transform.SetParent(storyChild, false);
                Sphere.GetComponent<MeshRenderer>().material = material;
            }
        }

        // Save scene
        EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
    }
}

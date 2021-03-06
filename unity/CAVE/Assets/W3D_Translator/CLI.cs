using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Text.RegularExpressions;
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

        // xmlPath = "../../examples/cweditor/everything.xml"; // TEMP - hard code xml file
        xmlPath = "../../test/sample.xml"; // TEMP - hard code xml file

        // TODO: Add try/catch for when deserialization fails
        XmlSerializer serializer = new XmlSerializer(typeof(Story));
        Story story = null;
        using (XmlReader reader = XmlReader.Create(xmlPath))
        {
            story = (Story)serializer.Deserialize(reader);
        }
        Debug.Log(story.pprint());
        Debug.Log(story.Global.pprint());
        Debug.Log(story.Global.Camera.Placement);
        Debug.Log(story.Global.Camera.Placement.Axis);
        Debug.Log(story.Global.Camera.Placement.position);


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

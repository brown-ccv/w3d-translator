using System;
using System.IO;
using System.Xml.Serialization;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;
using W3D;


public class CLI : MonoBehaviour
{
    void Start(){ Main(); } // TEMP: Execute script from Unity directly

    static void Main()
    {
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

        
        // xmlPath = "../../test/sample.xml"; // TEMP: Hardcode xml file
        xmlPath = "../../examples/cweditor/everything.xml"; // TEMP - hard code xml file
        XmlSerializer serializer = new XmlSerializer(typeof(Story));
        Story story = null;
        using (StreamReader reader = new StreamReader(xmlPath))
        {
            story = (Story)serializer.Deserialize(reader);
        }
        Debug.Log(story);
        Debug.Log($"{story.ObjectRoot.Object.Count} {story.ObjectRoot.Object}");

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
        //     Console.WriteLine($"Error creating scene for {xmlPath}");
        //     Console.WriteLine(e);
        //     throw e;
        // }
        // Example(instantiatedScene.scene);
    }

    // EXAMPLE - Add sphere at origin of each wall
    // static void Example(UnityEngine.SceneManagement.Scene scene)
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

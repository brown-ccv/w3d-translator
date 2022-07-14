using System;
using System.IO;
using System.Xml;
using System.Xml.Schema;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

public class CLI : MonoBehaviour
{
    static void Start()
    {
        Application.logMessageReceivedThreaded += HandleLog;

        // GET ALL XML FILES IN THE DIRECTORY (OLD LOOP)
        DirectoryInfo dir = new DirectoryInfo("Assets/Resources/Original Project");
        FileInfo[] info = dir.GetFiles("*.xml");
        foreach (FileInfo f in info) 
        { 
            string file = f.Name;
            Debug.Log($"Translating file: {file}");

            // TODO: Remove .xml extension
            NewScene(file);
            /**
                try:
                    validate_xml(file)
                except XmlError as e:
                    typer.echo(red(e), err=True)
                else:
                    # Build and clean Story
                    story = parse(file, silence=True)
                    story.ObjectRoot = translate_objects(story.ObjectRoot.Object) 
            */
        }
 
        Application.logMessageReceivedThreaded -= HandleLog;    
    }

    static void NewScene(string scene)
    {
        // Instantiate new scene from template
        InstantiationResult instantiatedScene = SceneTemplateService.Instantiate(
            Resources.Load<SceneTemplateAsset>("CAVE"),
            false,
            $"Assets/Resources/Scenes/{scene}.unity"
        );
        GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];

        // EXAMPLE - Add sphere at origin of each wall
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

    // Callback function when Debug.Log is called within the CLI script
    static void HandleLog(string logString, string stackTrace, LogType type)
    {
        Console.WriteLine($"HandleLog: {logString}");
    }

}

using System;
using System.IO;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

public class CLI : MonoBehaviour
{
    static void Start()
    {
        Debug.Log("Initializing");
        Application.logMessageReceivedThreaded += HandleLog;

        // Create a new scene for every xml file in the original project
        string[] files = Directory.GetFiles(
            "Assets/Resources/Original Project",
            "*.xml",
            SearchOption.AllDirectories
        );
        foreach(string file in files)
        {            
            /* PYTHON VALIDATION CODE
                try:
                    validate_xml(file)
                except XmlError as e:
                    typer.echo(red(e), err=True)
                else:
                    # Build and clean Story
                    story = parse(file, silence=True)
                    story.ObjectRoot = translate_objects(story.ObjectRoot.Object) 
            */
            NewScene(file);
        }
 
        Application.logMessageReceivedThreaded -= HandleLog;    
    }

    static void NewScene(string xmlPath)
    {
        Debug.Log($"Translating [green]{Path.GetFileName(xmlPath)}[/green]");

        // Instantiate new scene from template
        InstantiationResult instantiatedScene = SceneTemplateService.Instantiate(
            Resources.Load<SceneTemplateAsset>("CAVE"),
            false,
            $"Assets/Resources/Scenes/{Path.GetFileNameWithoutExtension(xmlPath)}.unity"
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
        // Prepend "CLI:", we check for this in the Python script
        // Console.ForegroundColor = ConsoleColor.Green;
        Console.BackgroundColor = ConsoleColor.Blue;
        Console.WriteLine($"LOG:{logString}");
    }

}

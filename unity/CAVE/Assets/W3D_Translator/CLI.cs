using System;
using System.IO;
using System.Xml;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

public class CLI : MonoBehaviour
{
    static void Main()
    {
        string xmlPath = null;

        // Get command line arguments from Python
        try {
            string[] args = System.Environment.GetCommandLineArgs();
            for(int i = 0; i < args.Length; i++)
            {
                if(args[i] == "--xmlPath") xmlPath = args[++i];
            }
        } catch(Exception e) {
            Debug.Log("Error initializing command line arguments");
            Debug.Log(e);
            throw e;
        }

        // Load the XML
        try {
            XmlDocument file = new XmlDocument();
            file.Load(xmlPath);
        } catch(FileNotFoundException e) {
            Debug.LogError($"ERROR: File {xmlPath} not found");
            Debug.LogException(e);
            throw e;
        } 

        // Create the Unity scene
        // try{
        //     NewScene(xmlPath);
        // } catch(Exception e) { 
        //     Console.WriteLine($"Error creating scene for {xmlPath}");
        //     Console.WriteLine(e);
        //     throw e;
        // } 
    }

    static void NewScene(string xmlPath)
    {
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
}

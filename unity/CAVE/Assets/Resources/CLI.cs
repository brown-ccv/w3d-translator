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
    static void Main()
    {
        // Get command line arguments from Python
        string[] args = System.Environment.GetCommandLineArgs();
        // string schemaFile = null;
        string schemaFile = null;
        for(int i = 0; i < args.Length; i++)
        {
            if(args[i] == "--schemaFile") schemaFile = args[++i];
        }

        // Initialize xml schema validator
        Console.WriteLine("SCHEMA FILE " + schemaFile);
        try{
            XmlReaderSettings caveSchema = new XmlReaderSettings();
            caveSchema.ValidationType = ValidationType.Schema;
            caveSchema.ValidationEventHandler += new ValidationEventHandler(xmlValidationCallback);

            // Read xsd file and initialize schema
            XmlSchema schema = XmlSchema.Read(
                new XmlTextReader(schemaFile),
                xmlValidationCallback
            );
            caveSchema.Schemas.Add(schema);
            Console.WriteLine("SCHEMA " + schema.ToString());
            Console.WriteLine("CAVE SCHEMA", caveSchema.ToString());

            // Create a new scene for every xml file in the original project
            string[] files = Directory.GetFiles(
                "Assets/Resources/Original Project",
                "*.xml",
                SearchOption.AllDirectories
            );
            foreach(string xmlPath in files)
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
                // Validation is done on .Create
                XmlReader reader = XmlReader.Create(xmlPath, caveSchema);
                while (reader.Read()) { }

                // Create the Unity scene
                NewScene(xmlPath);
            }  

        }
        catch(Exception e) { 
            Console.WriteLine($"ERROR: Could not initialize XMl Validation from {schemaFile}");
            Console.WriteLine(e);
            throw e;
        } 
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

    static void xmlValidationCallback(object sender, ValidationEventArgs e)
    {
        Console.WriteLine($"XML Handler {sender} {e.ToString()}");
        if (e.Severity == XmlSeverityType.Warning) {
            Console.Write("WARNING: ");
            Console.WriteLine(e.Message);
        } else if (e.Severity == XmlSeverityType.Error) {
            Console.Write("ERROR: ");
            Console.WriteLine(e.Message);
        }
    }
}

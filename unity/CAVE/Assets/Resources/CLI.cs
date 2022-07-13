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
        try
        {
            XmlReaderSettings settings = new XmlReaderSettings();
            settings.Schemas.Add("http://www.contoso.com/books", "contosoBooks.xsd");
            settings.ValidationType = ValidationType.Schema;

            // GET ALL XML FILES IN THE DIRECTORY (OLD LOOP)
            DirectoryInfo dir = new DirectoryInfo("Assets/Resources/Original Project");
            FileInfo[] info = dir.GetFiles("*.xml");
            foreach (FileInfo f in info) 
            { 
                // TODO: How to get this line onto console instead of log file?
                Console.WriteLine($"Translating file: {f}");

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
                
                // XmlReader reader = XmlReader.Create("contosoBooks.xml", settings);
                // XmlDocument document = new XmlDocument();
                // document.Load(reader);

                // ValidationEventHandler eventHandler = new ValidationEventHandler(ValidationEventHandler);

                // the following call to Validate succeeds.
                // document.Validate(eventHandler);

                // // add a node so that the document is no longer valid
                // XPathNavigator navigator = document.CreateNavigator();
                // navigator.MoveToFollowing("price", "http://www.contoso.com/books");
                // XmlWriter writer = navigator.InsertAfter();
                // writer.WriteStartElement("anotherNode", "http://www.contoso.com/books");
                // writer.WriteEndElement();
                // writer.Close();

                // // the document will now fail to successfully validate
                // document.Validate(eventHandler);


                NewScene("NewScene");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }        
    }

    static void ValidationEventHandler(object sender, ValidationEventArgs e)
    {
        switch (e.Severity)
        {
            case XmlSeverityType.Error:
                Console.WriteLine("Error: {0}", e.Message);
                break;
            case XmlSeverityType.Warning:
                Console.WriteLine("Warning {0}", e.Message);
                break;
        }
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
}

using System;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

public class CreateScene : MonoBehaviour
{
    static void NewScene()
    {
        // Instantiate new scene from template
        SceneTemplateAsset caveTemplate = Resources.Load<SceneTemplateAsset>("CAVE");
        InstantiationResult instantiatedScene = SceneTemplateService.Instantiate(
            caveTemplate,
            false,
            "Assets/Scenes/TemplateScene.unity"
        );
        GameObject story = instantiatedScene.scene.GetRootGameObjects()[1];

        // EXAMPLE - Add sphere at origin of each wall
        Material material = new Material(Shader.Find("Standard"));
        material.SetColor("_Color", Color.green);
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

using System;
using UnityEngine;
using UnityEditor;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;
using UnityEditor.SceneTemplate;

public class CreateScene : MonoBehaviour
{
    static void NewScene()
    {
        SceneTemplateAsset caveTemplate = AssetDatabase.LoadAssetAtPath<SceneTemplateAsset>(
            "Assets/Resources/CAVE.scenetemplate"
        );

        // Instantiate new scene from template
        InstantiationResult instantiatedScene = SceneTemplateService.Instantiate(
            caveTemplate,
            false,
            "Assets/Scenes/TemplateScene.unity"
        );
    }
}

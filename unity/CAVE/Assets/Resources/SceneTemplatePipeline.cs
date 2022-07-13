using System;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.SceneManagement;
using UnityEditor;
using UnityEditor.SceneTemplate;
using UnityEditor.SceneManagement;

public class SceneTemplatePipeline : ISceneTemplatePipeline
{
    public virtual bool IsValidTemplateForInstantiation(SceneTemplateAsset sceneTemplateAsset)
    {
        return true;
    }

    public void BeforeTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, bool isAdditive, string sceneName)
    {
        if (sceneTemplateAsset) {
            System.Console.WriteLine(
                "Before Template Pipeline " + sceneTemplateAsset.name +
                " isAdditive: " + isAdditive +
                " sceneName: " + sceneName
            );
        }
    }

    public void AfterTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, Scene scene, bool isAdditive, string sceneName)
    {
        // Set new scene to use CAVE.lighting
        Lightmapping.lightingSettings = Resources.Load<LightingSettings>("CAVE");

        // Remove skybox and use white ambient lighting
        RenderSettings.skybox = null;
        RenderSettings.ambientMode = AmbientMode.Flat;
        RenderSettings.ambientLight = Color.white;

        // Save scene
        EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
    }
}

using System;
using UnityEngine;
using UnityEditor;
using UnityEngine.SceneManagement;
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
        // TODO: Lighting Settings aren't being copied unless I copy the actual settings
        // TODO: Copy settings and rename? Or find a way to re-attach them
        // Set new scene to use CAVE.lighting
        LightingSettings lightingSettings = Resources.Load<LightingSettings>("CAVE");
        Console.WriteLine("Loaded lighting " + lightingSettings.name);
        Lightmapping.lightingSettings = lightingSettings; // This does nothing

        // Save scene
        EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
    }
}

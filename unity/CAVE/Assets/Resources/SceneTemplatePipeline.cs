using System.IO;
using System;
using UnityEngine;
using UnityEditor;
using UnityEngine.SceneManagement;
using UnityEditor.SceneTemplate;

public class SceneTemplatePipeline : ISceneTemplatePipeline
{
    public virtual bool IsValidTemplateForInstantiation(SceneTemplateAsset sceneTemplateAsset)
    {
        return true;
    }

    public void BeforeTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, bool isAdditive, string sceneName)
    {
        if (sceneTemplateAsset)
        {
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
        LightingSettings lightingSettings = Resources.Load("CAVE") as LightingSettings;
        Console.WriteLine("Loaded lighting " + lightingSettings.name);
        Lightmapping.lightingSettings = lightingSettings; // This does nothing
    }
}

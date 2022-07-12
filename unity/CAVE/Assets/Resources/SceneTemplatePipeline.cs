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
        Console.WriteLine(
            "After Template Pipeline " + sceneTemplateAsset + 
            " scene: " + scene + 
            " isAdditive: " + isAdditive + 
            " sceneName: " + sceneName
        );
        
        // Create and use a copy of the CAVE template's lighting settings
        Console.WriteLine($"NEW DIRECTORY {Path.GetDirectoryName(sceneName)}");
        Console.WriteLine($"NEW FILENAME {Path.GetFileNameWithoutExtension(sceneName)}");
        Console.WriteLine($"NEW EXTENSION .lighting");
        String lightingPath = Path.Combine(
            Path.GetDirectoryName(sceneName),
            Path.Combine(
                Path.GetFileNameWithoutExtension(sceneName),
                ".lighting"
            )
        );
        Console.WriteLine($"NEW LIGHTING FILE {lightingPath}");
        FileUtil.CopyFileOrDirectory("Assets/Resources/CAVE.lighting", lightingPath);
        // LightingSettings Lighting = AssetDatabase.LoadAssetAtPath<LightingSettings>(
        //     lightingPath
        // );
        // Console.WriteLine("LIGHTING SETTINGS " + Lighting);
    }
}

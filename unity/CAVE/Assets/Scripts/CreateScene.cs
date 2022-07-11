using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;

public class CreateScene : MonoBehaviour
{
    static void NewScene() {
        Scene newScene = SceneManager.CreateScene("NewScene");
        // bool saveOK = EditorSceneManager.SaveScene(
        //     newScene,
        //     "Assets/Scenes/NewScene.unity"
        // );
    }
}

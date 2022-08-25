using UnityEngine;
using UnityEditor;

/** TEMPORARY FILE
    This class is a temporary file for running CLI.cs directly from the Unity Editor Window

*/
namespace W3D
{
    public class CLI_GUI : EditorWindow
    {
        [MenuItem("Custom/CLI")]
        private static void Init()
        {
            EditorWindow window = GetWindow(typeof(CLI_GUI));
            window.Show();
        }

        private void OnGUI()
        {
            if (CLI.ProjectPath is null) { CLI.ProjectPath = "../../test/sample.xml"; }

            CLI.ProjectPath = EditorGUILayout.TextField("Path: ", CLI.ProjectPath);

            if (GUILayout.Button("CLI.Main")) { CLI.Main(); }
            Repaint();
        }
    }
}
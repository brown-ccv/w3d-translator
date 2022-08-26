using UnityEngine;
using UnityEditor;

/** Custom window for running CLI.cs directly from the Unity Editor

    This is a temporary file that should be deleted from the output projects 
*/
namespace W3D
{
    // Creates 
    public class CLI_GUI : EditorWindow
    {
        [MenuItem("Custom/CLI Window")]
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
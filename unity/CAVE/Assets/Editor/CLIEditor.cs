using UnityEngine;
using UnityEditor;

#pragma warning disable IDE0051, RCS1213
namespace CLI
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
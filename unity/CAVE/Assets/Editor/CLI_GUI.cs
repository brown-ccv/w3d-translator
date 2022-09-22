using UnityEngine;
using UnityEditor;

namespace Writing3D
{
    namespace Translation
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
                if (CLI.XmlPath is null) { CLI.XmlPath = "../../test/sample.xml"; }

                CLI.XmlPath = EditorGUILayout.TextField("Path: ", CLI.XmlPath);

                if (GUILayout.Button("CLI.Main")) { CLI.Main(); }
                Repaint();
            }
        }
    }
}
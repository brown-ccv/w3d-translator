using UnityEngine;
using UnityEditor;

namespace Writing3D
{
    namespace Editor
    {
        public class CLIEditor : EditorWindow
        {
            [MenuItem("Custom/CLI Window")]
            private static void Init()
            {
                EditorWindow window = GetWindow(typeof(CLIEditor));
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
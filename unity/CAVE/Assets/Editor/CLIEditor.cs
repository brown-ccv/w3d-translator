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
                if (CLI._XmlPath is null) { CLI._XmlPath = "../../test/sample.xml"; }

                CLI._XmlPath = EditorGUILayout.TextField("Path: ", CLI._XmlPath);

                if (GUILayout.Button("CLI.Main")) { CLI.Main(); }
                Repaint();
            }
        }
    }
}
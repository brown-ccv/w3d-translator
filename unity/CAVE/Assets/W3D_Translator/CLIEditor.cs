using UnityEngine;
using UnityEditor;

/** TEMPORARY FILE

    This class is a temporary file for running CLI.cs directly from the 

*/
namespace W3D
{

    [CustomEditor(typeof(CLI))]
    public class CLIEditor : Editor
    {
        public override void OnInspectorGUI()
        {
            base.OnInspectorGUI();

            // CLI cli = (CLI)LoadAssetAtPath("W3D_Translator/CLI.cs", typeof(CLI));

            CLI.Main();

            // THis becomes CLI.path
            // myTarget.experience = EditorGUILayout.IntField("Experience", myTarget.experience);
            // EditorGUILayout.LabelField("Level", myTarget.Level.ToString());

        }
    }
}
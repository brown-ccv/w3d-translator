using UnityEditor;

using Writing3D.Transitions;

namespace Writing3D
{
    namespace Editor
    {
        [CustomEditor(typeof(Move), true)]
        public class MoveEditor : UnityEditor.Editor
        {
            private Move Move;

            private void OnEnable()
            {
                Move = target as Move;
            }

            public override void OnInspectorGUI()
            {
                serializedObject.Update();

                DrawPropertiesExcluding(
                    serializedObject,
                    "RotationType",
                    "Rotation",
                    "LookRotation"
                );

                EditorGUILayout.Space(); EditorGUILayout.Space();
                EditorGUILayout.PropertyField(serializedObject.FindProperty("RotationType"));

                switch (Move.RotationType)
                {
                    case Move.RotationTypes.Rotation:
                        EditorGUILayout.PropertyField(
                            serializedObject.FindProperty("Rotation")
                        );
                        break;
                    case Move.RotationTypes.LookAt:
                        EditorGUILayout.PropertyField(
                            serializedObject.FindProperty("LookRotation")
                        );
                        break;
                    case Move.RotationTypes.None:
                    default:
                        break;
                }
                serializedObject.ApplyModifiedProperties();
            }
        }
    }
}
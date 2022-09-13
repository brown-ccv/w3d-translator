using System;

using UnityEngine;

namespace Writing3D
{
    public class SceneManager : MonoBehaviour
    {
        private void Update()
        {
            // Quit when "ESC" is pressed
            if (Input.GetKeyDown(KeyCode.Escape)) { Application.Quit(); }
        }
    }

    [Serializable]
    public class Placement
    {
        public Transform Parent;
        public Vector3 Position;
        public object Rotation; // Euler (Type.Euler) or LookAtRotation (Type.LookAt)

        public Type RotationType;

        public Placement(Transform parent, Vector3 position)
        {
            Parent = parent;
            Position = position;
        }

        public enum Type
        {
            None,
            Euler,
            LookAt
        }

        [Serializable]
        public class LookAtRotation
        {
            public Vector3 Target;
            public Vector3 Up;

            public LookAtRotation(Vector3 target, Vector3 up)
            {
                Target = target;
                Up = up;
            }
        }
    }
}
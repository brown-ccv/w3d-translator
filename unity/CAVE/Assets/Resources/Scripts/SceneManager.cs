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
        // TODO 128: GUI should change Euler/Look Rotation based on Type
        public Transform Parent;
        public Vector3 Position;
        public Type RotationType;
        public Vector3 EulerRotation; // (Type.Euler)
        public LookAtRotation LookRotation; //(Type.LookAt)        

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
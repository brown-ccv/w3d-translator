using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Move",
            order = 2
        )]
        [Serializable]
        public class Move : Transition
        {
            // public Placement Placement;

            // TODO 128: GUI should change Euler/Look Rotation based on Type
            public Transform Parent;
            public Vector3 Position;

            public RotationTypes RotationType;
            public Vector3 EulerRotation;
            public LookAtRotation LookRotation;

            // public Move Init(Placement placement, float duration)
            // {
            //     // Placement = placement;
            //     Duration = duration;
            //     return this;
            // }

            public Move Init(
                Transform parent, Vector3 position,
                RotationTypes rotationType, Vector3 rotation
            )
            {
                Parent = parent;
                Position = position;
                RotationType = rotationType;
                EulerRotation = rotation;
                LookRotation = null;
                return this;
            }

            public Move Init(
                Transform parent, Vector3 position,
                RotationTypes rotationType, LookAtRotation rotation
            )
            {
                Parent = parent;
                Position = position;
                RotationType = rotationType;
                LookRotation = rotation;
                return this;
            }

            // TODO: Make enum nullable instead od None type (check)
            public enum RotationTypes
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
}
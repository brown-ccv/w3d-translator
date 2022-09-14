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
            public Transform Parent;
            public Vector3 Position;

            public RotationTypes RotationType;
            public Vector3 EulerRotation;
            public LookAtRotation LookRotation;

            public Move Init(
                Transform parent,
                Vector3 position,
                RotationTypes rotationType,
                object rotation,
                float duration
            )
            {
                Parent = parent;
                Position = position;
                RotationType = rotationType;
                Duration = duration;

                switch (rotationType)
                {
                    case RotationTypes.Euler:
                        EulerRotation = (Vector3)rotation;
                        break;
                    case RotationTypes.LookAt:
                        LookRotation = (LookAtRotation)rotation;
                        break;
                    case RotationTypes.None:
                    default:
                        break;
                }
                return this;
            }

            public Move Init(
                Transform parent, Vector3 position,
                (RotationTypes, Vector3) rotation, float duration
            )
            {
                Parent = parent;
                Position = position;
                RotationType = rotation.Item1;
                EulerRotation = rotation.Item2;
                Duration = duration;
                return this;
            }

            public Move Init(
                Transform parent, Vector3 position,
                (RotationTypes, LookAtRotation) rotation, float duration
            )
            {
                Parent = parent;
                Position = position;
                RotationType = rotation.Item1;
                LookRotation = rotation.Item2;
                Duration = duration;
                return this;
            }

            // TODO: Make enum nullable instead of None type (check)
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
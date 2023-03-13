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
            public Quaternion Rotation;
            public LookAt LookRotation;

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
                    case RotationTypes.None:
                        Rotation = Quaternion.identity;
                        break;
                    case RotationTypes.Rotation:
                        Rotation = Quaternion.Euler((Vector3)rotation);
                        break;
                    case RotationTypes.LookAt:
                        LookRotation = (LookAt)rotation;
                        break;
                    default: throw new Exception("Invalid rotation type");
                }
                return this;
            }

            public enum RotationTypes
            {
                None,
                Rotation,
                LookAt
            }

            [Serializable]
            public class LookAt
            {
                public Vector3 Target;
                public Vector3 Up;

                public LookAt(Vector3 target, Vector3 up)
                {
                    Target = target;
                    Up = up;
                }
            }
        }
    }
}
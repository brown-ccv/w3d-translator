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
            public Vector3 LocalPosition;
            public Quaternion LocalRotation;
            // TODO: Data and logic for MoveTransition (122)

            public Move Init(Transform parent, Vector3 localPosition, Quaternion localRotation)
            {
                Parent = parent;
                LocalPosition = localPosition;
                LocalRotation = localRotation;
                return this;
            }
        }
    }
}
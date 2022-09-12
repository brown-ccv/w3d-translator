using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Transition",
            order = 7
        )]
        [Serializable]
        public class Link : Transition
        {
            [SerializeField] public Controls Operation;

            public Link Init(Controls operation, float duration)
            {
                Operation = operation;
                Duration = duration;
                return this;
            }

            public enum Controls
            {
                On,
                Off,
                Activate,
                ActivateIfOn,
            }
        }
    }
}
using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Transition",
            order = 6
        )]
        [Serializable]
        public class Sound : Transition
        {
            [SerializeField] public Controls Operation;

            public enum Controls
            {
                None,
                Play,
                Stop,
            }
        }
    }
}
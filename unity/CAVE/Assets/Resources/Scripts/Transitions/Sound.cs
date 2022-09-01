using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
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
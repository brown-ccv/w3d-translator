using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [Serializable]
        public class Link : Transition
        {
            [SerializeField] public Controls Operation;

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
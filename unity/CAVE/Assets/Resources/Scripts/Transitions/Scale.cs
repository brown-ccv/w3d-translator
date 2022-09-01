using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [Serializable]
        public class Scale : Transition
        {
            [SerializeField] public float NewScale;
        }
    }
}
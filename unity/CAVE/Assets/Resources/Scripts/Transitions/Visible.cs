using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [Serializable]
        public class Visible : Transition
        {
            [SerializeField] public bool Enabled;
        }
    }
}
using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Visible",
            order = 1
        )]
        [Serializable]
        public class Visible : Transition
        {
            [SerializeField] public bool Enabled;
        }
    }
}
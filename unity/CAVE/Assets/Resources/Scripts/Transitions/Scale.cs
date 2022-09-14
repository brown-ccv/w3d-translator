using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Scale",
            order = 5
        )]
        [Serializable]
        public class Scale : Transition
        {
            [SerializeField] public float NewScale;
        }
    }
}
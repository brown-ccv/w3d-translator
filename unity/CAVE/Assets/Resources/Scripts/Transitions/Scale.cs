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

            // TODO: Make sure this function is different from Transition.Init
            public Scale Init(float scale)
            {
                NewScale = scale;
                return this;
            }
        }
    }
}
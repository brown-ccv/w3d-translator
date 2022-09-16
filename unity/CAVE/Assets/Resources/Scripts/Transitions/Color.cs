using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Color",
            order = 4
        )]
        [Serializable]
        public class Color : Transition
        {
            [SerializeField] public UnityEngine.Color NewColor;

            public Color Init(UnityEngine.Color color, float duration)
            {
                NewColor = color;
                Duration = duration;
                return this;
            }
        }
    }
}
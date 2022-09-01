using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [Serializable]
        public class Color : Transition
        {
            [SerializeField] public UnityEngine.Color NewColor;
        }
    }
}
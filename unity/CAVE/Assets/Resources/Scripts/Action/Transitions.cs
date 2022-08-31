using System;

using UnityEngine;

namespace Writing3D
{
    [Serializable]
    public class Transition
    {
        [SerializeField] public float Duration;

        public enum Types
        {
            Visible,
            Move,
            RelativeMove,
            Color,
            Scale,
            Sound,
            Link,
        }
    }

    [Serializable]
    public class VisibleTransition : Transition
    {
        [SerializeField] public bool Visible;
    }
}
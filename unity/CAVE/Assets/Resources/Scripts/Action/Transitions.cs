using System;

using UnityEngine;

namespace Writing3D
{
    [Serializable]
    public class Transition
    {
        [SerializeField] public float Duration;
    }

    [Serializable]
    public class VisibleTransition : Transition
    {
        [SerializeField] public bool Visible;
    }

    // public enum TransitionType
    // {
    //     Visible,
    //     Movement,
    //     MoveRelative,
    //     Color,
    //     Scale,
    //     Sound,
    //     Link,
    // }
}
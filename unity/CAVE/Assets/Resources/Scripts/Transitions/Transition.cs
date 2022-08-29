using System;

using UnityEngine;

namespace Writing3D
{
    [CreateAssetMenu(fileName = "Transition", menuName = "W3D/Transition/Transition", order = 0)]
    [Serializable]
    public abstract class Transition : ScriptableObject
    {
        [SerializeField] public float Duration;
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
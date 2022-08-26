using System;

using UnityEngine;

namespace W3D
{
    [CreateAssetMenu(fileName = "VisibleTransition", menuName = "W3D/Transition/VisibleTransition", order = 1)]
    [Serializable]
    public class VisibleTransition : Transition
    {
        [SerializeField] public bool Visible;
    }
}
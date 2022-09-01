using System;

using UnityEngine;
using UnityEngine.Events;

namespace Writing3D
{
    [CreateAssetMenu(fileName = "LinkAction", menuName = "W3D/LinkAction", order = 0)]
    [Serializable]
    public class LinkAction : ScriptableObject
    {
        [SerializeField] public object Action; // base: Action

        [SerializeField] public uint NumClicks = 1;
        [SerializeField] public bool Reset; // Initialized as false
    }

    [Serializable]
    // public class LinkActionEvent : UnityEvent<LinkAction> { }
    public class LinkActionEvent : UnityEvent { }
}
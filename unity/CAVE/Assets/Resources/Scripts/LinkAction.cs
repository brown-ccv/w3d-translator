using System;

using UnityEngine;
using UnityEngine.Events;
using Writing3D.Actions;

namespace Writing3D
{
    [CreateAssetMenu(fileName = "LinkAction", menuName = "W3D/LinkAction", order = 0)]
    [Serializable]
    public class LinkAction : ScriptableObject
    {
        [SerializeField] public uint NumClicks = 1;
        [SerializeField] public bool Reset; // Initialized as false

        [SerializeField] public ActionEvent ActionEvent = new();
    }

    [Serializable]
    public class LinkActionEvent : UnityEvent { }
}
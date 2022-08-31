using System;

using UnityEngine;

namespace Writing3D
{
    [CreateAssetMenu(fileName = "LinkAction", menuName = "W3D/LinkAction", order = 0)]
    [Serializable]
    public class LinkAction : ScriptableObject
    {
        [SerializeField] public Action Action;
        [SerializeField] public Action.Types Type;

        [SerializeField] public uint NumClicks = 1;
        [SerializeField] public bool Reset; // Initialized as false
    }
}
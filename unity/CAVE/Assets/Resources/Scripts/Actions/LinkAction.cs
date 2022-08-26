using UnityEngine;

namespace W3D
{
    [CreateAssetMenu(fileName = "LinkAction", menuName = "CAVE/LinkAction", order = 0)]
    public class LinkAction : ScriptableObject
    {
        public ActionTypes Type;
        public Action Action;

        public uint NumClicks = 1;
        public bool Reset; // Initialized as false

        public LinkAction(ActionTypes type) { Type = type; }
    }
}
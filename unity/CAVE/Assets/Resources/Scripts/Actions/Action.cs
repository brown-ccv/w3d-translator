using System;

using UnityEngine;
using UnityEngine.Events;

namespace Writing3D
{
    namespace Actions
    {
        [CreateAssetMenu(fileName = "Action", menuName = "W3D/Actions/Action", order = 0)]
        [Serializable]
        public class Action : ScriptableObject { }

        [Serializable]
        public class ActionEvent : UnityEvent { }
    }
}
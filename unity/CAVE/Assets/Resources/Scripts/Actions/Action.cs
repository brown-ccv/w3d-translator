using System;

using UnityEngine;
using UnityEngine.Events;

namespace Writing3D
{
    namespace Actions
    {
        [Serializable]
        public class Action : ScriptableObject { }

        [Serializable]
        public class ActionEvent : UnityEvent { }
    }
}
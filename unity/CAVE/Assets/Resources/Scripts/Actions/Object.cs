using System;

using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    namespace Actions
    {
        [CreateAssetMenu(fileName = "Object", menuName = "W3D/Actions/Object", order = 1)]
        [Serializable]
        public class Object : Action
        {
            public Transition Transition;
        }
    }
}
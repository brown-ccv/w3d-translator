using System;

using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    namespace Actions
    {
        [Serializable]
        public class ObjectAction : Action
        {
            [SerializeField] public Transition Transition; // base: Transition
        }
    }
}
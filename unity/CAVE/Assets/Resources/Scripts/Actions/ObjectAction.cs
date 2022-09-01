using System;

using UnityEngine;

namespace Writing3D
{
    namespace Actions
    {
        [Serializable]
        public class ObjectAction : Action
        {
            [SerializeField] public object Transition; // base: Transition
        }
    }
}
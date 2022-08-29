using System;

using UnityEngine;

namespace Writing3D
{
    [CreateAssetMenu(fileName = "ObjectAction", menuName = "W3D/Action/ObjectAction", order = 1)]
    [Serializable]
    public class ObjectAction : Action
    {
        [SerializeField] public Transition Transition;
    }
}
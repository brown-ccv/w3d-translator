using System;

using UnityEngine;

// TODO: If these don't have to be scriptable, consolidate all to Actions.cs
namespace Writing3D
{
    [Serializable]
    public abstract class Action
    {
    }

    [Serializable]
    public class ObjectAction : Action
    {
        [SerializeField] public dynamic Transition;
    }
}
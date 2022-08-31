using System;

using UnityEngine;

// TODO: If these don't have to be scriptable, consolidate all to Actions.cs
namespace Writing3D
{
    [Serializable]
    public abstract class Action
    {
        public enum Types
        {
            Object,
            Group,
            Timer,
            Sound,
            Event,
            MoveCave,
            Restart,
        }
    }

    [Serializable]
    public class ObjectAction : Action
    {
        [SerializeField] public Transition Transition;
        [SerializeField] public Transition.Types TransitionType;
    }
}
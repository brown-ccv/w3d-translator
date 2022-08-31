using System;

using UnityEngine;

namespace Writing3D
{
    // TODO: Should all of these be in the same class? Same namespace?

    [Serializable]
    public class Transition
    {
        [SerializeField] public float Duration;
    }

    // TODO: Visible, Move, Color

    [Serializable]
    public class VisibleTransition : Transition
    {
        [SerializeField] public bool Visible;
    }

    [Serializable]
    public class MoveTransition : Transition
    {
        // TODO: Placement struct? Use to update transform
    }

    [Serializable]
    public class RelativeMoveTransition : Transition
    {
        // TODO: Placement struct? Use to update transform
    }

    [Serializable]
    public class ColorTransition : Transition
    {
        [SerializeField] public Color Color;
    }

    [Serializable]
    public class ScaleTransition : Transition
    {
        [SerializeField] public float Scale;
    }

    [Serializable]
    public class SoundTransition : Transition
    {
        [SerializeField] public Controls Operation;

        public enum Controls
        {
            None,
            Play,
            Stop,
        }
    }

    [Serializable]
    public class LinkTransition : Transition
    {
        [SerializeField] public Controls Operation;

        public enum Controls
        {
            On,
            Off,
            Activate,
            ActivateIfOn,
        }
    }
}
using System;

using UnityEngine;

namespace Writing3D
{
    // TODO: Add namespace, separate files
    // TODO: Visible, Move, Color

    [Serializable]
    public class Transition
    {
        [SerializeField] public float Duration;
    }

    [Serializable]
    public class VisibleTransition : Transition
    {
        [SerializeField] public bool Visible;

        public VisibleTransition(bool visible) { Visible = visible; }
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

        public ColorTransition(Color color) { Color = color; }
    }

    [Serializable]
    public class ScaleTransition : Transition
    {
        [SerializeField] public float Scale;

        public ScaleTransition(float scale) { Scale = scale; }
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
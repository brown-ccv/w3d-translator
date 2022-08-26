using UnityEngine;
using UnityEngine.Events;

namespace W3D
{
    // TODO: Should these be structs or are classes okay?
    public abstract class Action
    {
        public ActionTypes Type;
        public UnityAction Delegate;
        public Transition Transition;

        internal Action(ActionTypes type) { Type = type; }
    }

    public enum ActionTypes
    {
        ObjectChange,
        GroupReference,
        TimerChange,
        SoundReference,
        EventReference,
        MoveCave,
        Restart,
    }

    public class LinkAction : Action
    {
        public uint NumClicks = 1;
        public bool Reset; // Initializes as false

        public LinkAction(ActionTypes type) : base(type) { }

        // public LinkAction(LinkActions xml) : base(xml.Type)
        // {
        //     Clicks clicks = xml.Clicks;
        //     if (clicks is not null && clicks.Type == Clicks.ActivationTypes.Number)
        //     {
        //         NumClicks activation = (NumClicks)clicks.Activation;
        //         NumClicks = activation.Clicks;
        //         Reset = activation.Reset;
        //     }
        // }
    }

    public class Transition
    {
        public float Duration;
        public TransitionType Type;

        public Transition(float duration, TransitionType type)
        {
            Duration = duration;
            Type = type;
        }

        // public Transition(XML.Transition transition)
        // {
        //     Duration = transition.Duration;
        //     Type = transition.Type;
        // }

        // public UnityAction GetDelegate(object change, GameObject reference)
        // {
        //     ObjectManager om = reference.GetComponent<ObjectManager>();
        //     return change switch
        //     {
        //         bool visible => delegate { om.VisibleTransition(visible, Duration); }
        //         ,
        //         _ => delegate { Debug.Log("TODO"); }
        //     };
        // }

        public enum TransitionType
        {
            Visible,
            Movement,
            MoveRelative,
            Color,
            Scale,
            Sound,
            Link,
        }
    }
}
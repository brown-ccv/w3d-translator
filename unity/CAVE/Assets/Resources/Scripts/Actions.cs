using UnityEngine;
using UnityEngine.Events;

using XML;

using static XML.Actions;
using static XML.Transition;

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

    public class LinkAction : Action
    {
        public uint NumClicks = 1;
        public bool Reset; // Initializes as false

        public LinkAction(ActionTypes type) : base(type) { }

        public LinkAction(LinkActions xml) : base(xml.Type)
        {
            Clicks clicks = xml.Clicks;
            if (clicks is not null && clicks.Type == Clicks.ActivationTypes.Number)
            {
                NumClicks activation = (NumClicks)clicks.Activation;
                NumClicks = activation.Clicks;
                Reset = activation.Reset;
            }
        }
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

        public Transition(XML.Transition transition)
        {
            Duration = transition.Duration;
            Type = transition.Type;
        }

        public static UnityAction GetDelegate(object change, GameObject reference)
        {
            return change switch
            {
                bool visible => delegate { VisibleTransition(reference, visible); }
                ,
                _ => delegate { Debug.Log("TODO"); }
            };
        }

        public static void VisibleTransition(GameObject reference, bool visible)
        {
            Debug.Log($"VisibleT {reference.name} {visible}");
            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // reference.SetActive(false); // parameters.visible
        }
    }
}
using UnityEngine;

using Writing3D.Actions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Pass action directly? For all functions
        // TODO: Private function to cast action/transition
        // public void VisibleTransition(LinkAction linkAction)
        public void VisibleTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)action;
            // Debug.Log($"VisibleT {gameObject.name} {action.name}");
            // VisibleTransition transition = (VisibleTransition)action.Transition;
            // Debug.Log($"VisibleT {gameObject.name} {transition.Visible}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(transition.Visible);
        }

        // public void MoveTransition(LinkAction linkAction)
        public void MoveTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // MoveTransition transition = (MoveTransition)action.Transition;
            // Debug.Log($"MoveT {gameObject.name}");
        }

        // public void RelativeMoveTransition(LinkAction linkAction)
        public void RelativeMoveTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // RelativeMoveTransition transition = (RelativeMoveTransition)action.Transition;
            // Debug.Log($"RelativeMoveT {gameObject.name}");
        }

        // public void ColorTransition(LinkAction linkAction)
        public void ColorTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // ColorTransition transition = (ColorTransition)action.Transition;
            // Debug.Log($"ColorT {gameObject.name} {transition.Color}");
        }

        // public void ScaleTransition(LinkAction linkAction)
        public void ScaleTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // ScaleTransition transition = (ScaleTransition)action.Transition;
            // Debug.Log($"ScaleT {gameObject.name} {transition.Scale}");
        }

        // public void SoundTransition(LinkAction linkAction)
        public void SoundTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // SoundTransition transition = (SoundTransition)action.Transition;
            // Debug.Log($"SoundT {gameObject.name} {transition.Operation}");
        }

        // public void LinkTransition(LinkAction linkAction)
        public void LinkTransition(Action action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // LinkTransition transition = (LinkTransition)action.Transition;
            // Debug.Log($"LinkT {gameObject.name} {transition.Operation}");
        }
    }
}
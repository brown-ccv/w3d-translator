using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Static function for if gameObject is a link (use tag?)
        // Need to enabled/disable the parent and children
        // TODO: Static function to figure out Content
        // e.g. ColorTransition should set text color
        public void VisibleTransition(Actions.Object action)
        {
            Visible transition = (Visible)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Enabled}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            gameObject.SetActive(transition.Enabled);
        }

        public void MoveTransition(Actions.Object action)
        {
            Move transition = (Move)action.Transition;
            Debug.Log($"MoveT {gameObject.name}");
        }

        public void RelativeMoveTransition(Actions.Object action)
        {
            // Actions.Object action = (Actions.Object)linkAction.Action;
            // RelativeMoveTransition transition = (RelativeMoveTransition)action.Transition;
            // Debug.Log($"RelativeMoveT {gameObject.name}");
        }

        public void ColorTransition(Actions.Object action)
        {
            Transitions.Color transition = (Transitions.Color)action.Transition;
            Debug.Log($"ColorT {gameObject.name} {transition.NewColor}");
        }

        public void ScaleTransition(Actions.Object action)
        {
            // Actions.Object action = (Actions.Object)linkAction.Action;
            // ScaleTransition transition = (ScaleTransition)action.Transition;
            // Debug.Log($"ScaleT {gameObject.name} {transition.Scale}");
        }

        public void SoundTransition(Actions.Object action)
        {
            // Actions.Object action = (Actions.Object)linkAction.Action;
            // SoundTransition transition = (SoundTransition)action.Transition;
            // Debug.Log($"SoundT {gameObject.name} {transition.Operation}");
        }

        public void LinkTransition(Actions.Object action)
        {
            // Actions.Object action = (Actions.Object)linkAction.Action;
            // LinkTransition transition = (LinkTransition)action.Transition;
            // Debug.Log($"LinkT {gameObject.name} {transition.Operation}");
        }
    }
}
using UnityEngine;

using Writing3D.Actions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Pass action directly? For all functions
        // TODO: Private function to cast action/transition
        public void VisibleTransition(ObjectAction action)
        {
            VisibleTransition transition = (VisibleTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Visible}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(transition.Visible);
        }

        public void MoveTransition(ObjectAction action)
        {
            MoveTransition transition = (MoveTransition)action.Transition;
            Debug.Log($"MoveT {gameObject.name}");
        }

        public void RelativeMoveTransition(ObjectAction action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // RelativeMoveTransition transition = (RelativeMoveTransition)action.Transition;
            // Debug.Log($"RelativeMoveT {gameObject.name}");
        }

        public void ColorTransition(ObjectAction action)
        {
            ColorTransition transition = (ColorTransition)action.Transition;
            Debug.Log($"ColorT {gameObject.name} {transition.Color}");
        }

        public void ScaleTransition(ObjectAction action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // ScaleTransition transition = (ScaleTransition)action.Transition;
            // Debug.Log($"ScaleT {gameObject.name} {transition.Scale}");
        }

        public void SoundTransition(ObjectAction action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // SoundTransition transition = (SoundTransition)action.Transition;
            // Debug.Log($"SoundT {gameObject.name} {transition.Operation}");
        }

        public void LinkTransition(ObjectAction action)
        {
            // ObjectAction action = (ObjectAction)linkAction.Action;
            // LinkTransition transition = (LinkTransition)action.Transition;
            // Debug.Log($"LinkT {gameObject.name} {transition.Operation}");
        }
    }
}
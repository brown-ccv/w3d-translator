using UnityEngine;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Pass action directly? For all functions
        // TODO: Private function to cast action/transition
        public void VisibleTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            VisibleTransition transition = (VisibleTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Visible}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(transition.Visible);
        }

        public void MoveTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            MoveTransition transition = (MoveTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name}");
        }

        public void RelativeMoveTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            RelativeMoveTransition transition = (RelativeMoveTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name}");
        }

        public void ColorTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            ColorTransition transition = (ColorTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Color}");
        }

        public void ScaleTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            ScaleTransition transition = (ScaleTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Scale}");
        }

        public void SoundTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            SoundTransition transition = (SoundTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Operation}");
        }

        public void LinkTransition(LinkAction linkAction)
        {
            ObjectAction action = (ObjectAction)linkAction.Action;
            LinkTransition transition = (LinkTransition)action.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Operation}");
        }
    }
}
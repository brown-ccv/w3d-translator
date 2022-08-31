using UnityEngine;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Pass action directly? For all functions
        // TODO: Private function to cast action/transition
        public void VisibleTransition(LinkAction linkAction)
        {
            VisibleTransition transition = (VisibleTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Visible}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(transition.Visible);
        }

        public void MoveTransition(LinkAction linkAction)
        {
            MoveTransition transition = (MoveTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {linkAction.Type}");
        }

        public void RelativeMoveTransition(LinkAction linkAction)
        {
            MoveTransition transition = (MoveTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {linkAction.Type}");
        }

        public void ColorTransition(LinkAction linkAction)
        {
            ColorTransition transition = (ColorTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Color}");
        }

        public void ScaleTransition(LinkAction linkAction)
        {
            ScaleTransition transition = (ScaleTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Scale}");
        }

        public void SoundTransition(LinkAction linkAction)
        {
            SoundTransition transition = (SoundTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Operation}");
        }

        public void LinkTransition(LinkAction linkAction)
        {
            LinkTransition transition = (LinkTransition)(linkAction.Action as ObjectAction)?.Transition;
            Debug.Log($"VisibleT {gameObject.name} {transition.Operation}");
        }
    }
}
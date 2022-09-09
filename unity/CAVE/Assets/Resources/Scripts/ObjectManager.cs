using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // Update the GameObject's color
        public void SetColor(UnityEngine.Color color)
        {
            // TODO: Switch based on <Content>
            GetComponent<TMPro.TextMeshPro>().color = color;
        }

        /* Transitions */

        // TODO: ObjectManager functions (121)
        // Static function for determining content and/or link?
        // e.g. ColorTransition should set text color

        public void VisibleTransition(Transition transition)
        {
            Visible visibleT = (Visible)transition;
            Debug.Log($"VisibleT {gameObject.name} {visibleT.Enabled}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            gameObject.SetActive(visibleT.Enabled);
        }

        public void MoveTransition(Transition transition)
        {
            Move moveT = (Move)transition;
            Debug.Log($"MoveT {gameObject.name}");
        }

        public void RelativeMoveTransition(Transition transition)
        {
            RelativeMove relativeMoveT = (RelativeMove)transition;
            Debug.Log($"RelativeMoveT {gameObject.name}");
        }

        public void ColorTransition(Transition transition)
        {
            Transitions.Color colorT = (Transitions.Color)transition;
            Debug.Log($"ColorT {gameObject.name} {colorT.NewColor}");
        }

        public void ScaleTransition(Transition transition)
        {
            Scale scaleT = (Scale)transition;
            Debug.Log($"ScaleT {gameObject.name} {scaleT.NewScale}");
        }

        public void SoundTransition(Transition transition)
        {
            Sound soundT = (Sound)transition;
            Debug.Log($"SoundT {gameObject.name} {soundT.Operation}");
        }

        public void LinkTransition(Transition transition)
        {
            Link linkT = (Link)transition;
            Debug.Log($"LinkT {gameObject.name} {linkT.Operation}");
        }
    }
}
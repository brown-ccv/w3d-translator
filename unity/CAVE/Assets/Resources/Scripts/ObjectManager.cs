using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // Update the GameObject's color
        public void SetColor(UnityEngine.Color color)
        {
            // TODO 125: Switch based on <Content>
            GetComponent<TMPro.TextMeshPro>().color = color;
        }

        /* Transitions */

        // TODO 121: ObjectManager functions
        // Static function for determining content and/or link?
        // e.g. ColorTransition should set text color

        // TODO 126: Pass derived class directly? Would have to change GetUnityAction
        public void VisibleTransition(Transition transition)
        {
            Visible visibleT = (Visible)transition;
            Debug.Log($"VisibleT {gameObject.name} {visibleT.Enabled}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity
            GetComponent<Renderer>().enabled = GetComponent<Collider>().enabled = visibleT.Enabled;
        }

        public void MoveTransition(Transition transition)
        {
            // Update parent
            // MoveTowards && RotateTowards in local space (parent space?)
            Placement placement = (transition as Move)?.Placement;
            Debug.Log($"RelativeMoveT {gameObject.name} {placement.Parent.name} {placement.Position}");
        }

        public void RelativeMoveTransition(Transition transition)
        {
            Placement placement = (transition as RelativeMove)?.Placement;
            Debug.Log($"RelativeMoveT {gameObject.name} {placement.Parent.name} {placement.Position}");
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
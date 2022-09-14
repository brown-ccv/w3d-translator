using UnityEngine;

using Writing3D.Transitions;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        public ContentTypes Type;

        // Update the GameObject's color
        public void SetColor(UnityEngine.Color color)
        {
            switch (Type)
            {
                case ContentTypes.Text:
                    GetComponent<TMPro.TextMeshPro>().color = color;
                    break;
                case ContentTypes.Image: // TODO 65
                case ContentTypes.StereoImage: // TODO 66
                case ContentTypes.Model: // TODO 67
                case ContentTypes.Light: // TODO 68
                case ContentTypes.ParticleSystem: // TODO 69
                case ContentTypes.Object: // TODO
                default:
                    Debug.LogError($"Unable to change color for {tag} object");
                    break;
            }
        }

        /* Transitions */

        // TODO 121: ObjectManager functions
        // Static function for determining content and/or link?
        // e.g. ColorTransition should set text color

        // TODO 126: Pass derived class directly? Would have to change GetUnityAction
        public void VisibleTransition(Transition transition)
        {
            var visible = transition as Visible;
            Debug.Log($"Visible {gameObject.name} {visible.Enabled}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity
            GetComponent<Renderer>().enabled = GetComponent<Collider>().enabled = visible.Enabled;
        }

        public void MoveTransition(Transition transition)
        {
            // Update parent
            // MoveTowards && RotateTowards in local space (parent space?)
            var move = transition as Move;
            Debug.Log($"RelativeMove {gameObject.name} {move.Parent.name} {move.Position}");
        }

        public void RelativeMoveTransition(Transition transition)
        {
            RelativeMove move = transition as RelativeMove;
            Debug.Log($"RelativeMove {gameObject.name} {move.Parent.name} {move.Position}");
        }

        public void ColorTransition(Transition transition)
        {
            var color = transition as Transitions.Color;
            Debug.Log($"Color {gameObject.name} {color.NewColor}");
        }

        public void ScaleTransition(Transition transition)
        {
            var scale = transition as Scale;
            Debug.Log($"Scale {gameObject.name} {scale.NewScale}");
        }

        public void SoundTransition(Transition transition)
        {
            var sound = transition as Sound;
            Debug.Log($"Sound {gameObject.name} {sound.Operation}");
        }

        public void LinkTransition(Transition transition)
        {
            var link = transition as Link;
            Debug.Log($"Link {gameObject.name} {link.Operation}");
        }

        public enum ContentTypes
        {
            Object, // None
            Text,
            Image,
            StereoImage,
            Model,
            Light,
            ParticleSystem,
        }
    }
}
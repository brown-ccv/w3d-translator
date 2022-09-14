using System;
using System.Collections;

using UnityEngine;
using TMPro;

using Writing3D;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        public ContentTypes Type;

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

        // Update the GameObject's color
        public void SetColor(Color color)
        {
            switch (Type)
            {
                case ContentTypes.Text:
                    GetComponent<TextMeshPro>().color = color;
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

        // Find the correct color component to change
        public dynamic GetColorComponent()
        {
            return Type switch
            {
                ContentTypes.Text => GetComponent<TextMeshPro>(),
                ContentTypes.Image => GetComponent<Renderer>(), // TODO 65
                ContentTypes.StereoImage => GetComponent<Renderer>(), // TODO 66
                ContentTypes.Model => GetComponent<Renderer>(), // TODO 67
                ContentTypes.Light => GetComponent<Renderer>(), // TODO 68
                ContentTypes.ParticleSystem => GetComponent<Renderer>(), // TODO 69
                ContentTypes.Object => GetComponent<Renderer>(), // TODO
                _ => null,
            };
        }

        /* Transitions */

        // TODO 121: ObjectManager functions
        // Static function for determining content and/or link?
        // e.g. ColorTransition should set text color

        // TODO 126: Pass derived class directly? Would have to change GetUnityAction
        public void VisibleTransition(Transitions.Transition transition)
        {
            var visible = transition as Transitions.Visible;
            // Debug.Log($"Visible {gameObject.name} {visible.Enabled}");

            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity
            GetComponent<Renderer>().enabled = GetComponent<Collider>().enabled = visible.Enabled;
        }

        public void MoveTransition(Transitions.Transition transition)
        {
            // Update parent
            // MoveTowards && RotateTowards in local space (parent space?)
            var move = transition as Transitions.Move;
            // Debug.Log($"RelativeMove {gameObject.name} {move.Parent.name} {move.Position}");
        }

        public void RelativeMoveTransition(Transitions.Transition transition)
        {
            var move = transition as Transitions.RelativeMove;
            // Debug.Log($"RelativeMove {gameObject.name} {move.Parent.name} {move.Position}");
        }

        public void ColorTransition(Transitions.Transition transition)
        {
            StartCoroutine(ChangeColor(transition as Transitions.Color));

            IEnumerator ChangeColor(Transitions.Color transition)
            {
                var component = GetColorComponent();
                var startColor = component.color;
                float t = 0;
                while (t < 1)
                {
                    t += Time.deltaTime / transition.Duration;
                    component.color = Color.Lerp(startColor, transition.NewColor, t);
                    yield return null;
                }
            }
        }

        public void ScaleTransition(Transitions.Transition transition)
        {
            var scale = transition as Transitions.Scale;
            // Debug.Log($"Scale {gameObject.name} {scale.NewScale}");
        }

        public void SoundTransition(Transitions.Transition transition)
        {
            var sound = transition as Transitions.Sound;
            // Debug.Log($"Sound {gameObject.name} {sound.Operation}");
        }

        public void LinkTransition(Transitions.Transition transition)
        {
            var link = transition as Transitions.Link;
            // Debug.Log($"Link {gameObject.name} {link.Operation}");
        }
    }
}
using System.Collections;

using TMPro;

using UnityEngine;

using RTypes = Writing3D.Transitions.Move.RotationTypes;
using Ts = Writing3D.Transitions;

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
        public void SetColor(Color color) { GetColorComponent().color = color; }

        // Find the correct color component to change
        private dynamic GetColorComponent()
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

        public void VisibleTransition(Ts.Transition transition)
        {
            var component = GetColorComponent();
            StartCoroutine((bool)(transition as Ts.Visible)?.Enabled ? FadeIn() : FadeOut());

            IEnumerator FadeIn()
            {
                GetComponent<Renderer>().enabled = true;

                // Make sure color starts transparent
                var startColor = component.color = new Color(
                    component.color.r,
                    component.color.g,
                    component.color.b,
                    0
                );
                var endColor = new Color(startColor.r, startColor.g, startColor.b, 1);
                for (float t = 0; t < 1; t += Time.deltaTime / transition.Duration)
                {
                    component.color = Color.Lerp(startColor, endColor, t);
                    yield return null;
                }
                GetComponent<Collider>().enabled = true;
            }

            IEnumerator FadeOut()
            {
                GetComponent<Collider>().enabled = false;

                var startColor = component.color;
                var endColor = new Color(startColor.r, startColor.g, startColor.b, 0);
                for (float t = 0; t < 1; t += Time.deltaTime / transition.Duration)
                {
                    component.color = Color.Lerp(startColor, endColor, t);
                    yield return null;
                }
                GetComponent<Renderer>().enabled = false;
            }
        }

        public void MoveTransition(Ts.Transition transition)
        {
            StartCoroutine(Move(transition as Ts.Move));

            IEnumerator Move(Ts.Move transition)
            {
                var transform = GetComponent<Transform>();
                transform.SetParent(transition.Parent, true); // Update hierarchy
                var startPosition = transform.localPosition;
                var startRotation =
                    transition.RotationType == RTypes.LookAt
                        ? transform.rotation
                        : transform.localRotation;

                for (float t = 0; t < 1; t += Time.deltaTime / transition.Duration)
                {
                    transform.localPosition = Vector3.Lerp(startPosition, transition.Position, t);

                    if (transition.RotationType == RTypes.LookAt)
                    {
                        transform.rotation = Quaternion.Slerp(
                            startRotation,
                            Quaternion.LookRotation(
                                transform.position -
                                    transform.root.TransformPoint(transition.LookRotation.Target),
                                 transition.LookRotation.Up


                            ),
                            t
                        );
                    }
                    else
                    {
                        transform.localRotation =
                            Quaternion.Slerp(startRotation, transition.Rotation, t);
                    }
                    yield return null;
                }
            }
        }

        // TODO 132
        public void RelativeMoveTransition(Ts.Transition transition)
        {
            var move = transition as Ts.RelativeMove;
            // Debug.Log($"RelativeMove {gameObject.name} {move.Parent.name} {move.Position}");
        }

        public void ColorTransition(Ts.Transition transition)
        {
            StartCoroutine(ChangeColor(transition as Ts.Color));

            IEnumerator ChangeColor(Ts.Color transition)
            {
                var component = GetColorComponent();
                var startColor = component.color;
                for (float t = 0; t < 1; t += Time.deltaTime / transition.Duration)
                {
                    component.color = Color.Lerp(startColor, transition.NewColor, t);
                    yield return null;
                }
            }
        }

        // TODO 133
        public void ScaleTransition(Ts.Transition transition)
        {
            var scale = transition as Ts.Scale;
            // Debug.Log($"Scale {gameObject.name} {scale.NewScale}");
        }

        // TODO 134
        public void SoundTransition(Ts.Transition transition)
        {
            var sound = transition as Ts.Sound;
            // Debug.Log($"Sound {gameObject.name} {sound.Operation}");
        }

        // TODO 135
        public void LinkTransition(Ts.Transition transition)
        {
            var link = transition as Ts.Link;
            // Debug.Log($"Link {gameObject.name} {link.Operation}");
        }
    }
}
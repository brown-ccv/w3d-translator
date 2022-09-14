using System;
using System.Collections;

using UnityEngine;
using TMPro;

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
        // Update TODOs for each specific function
        // TODO 126: Pass derived class directly? Would have to change GetUnityAction

        public void VisibleTransition(Ts.Transition transition)
        {
            var component = GetColorComponent();
            StartCoroutine(
                (bool)(transition as Ts.Visible)?.Enabled
                ? FadeIn() : FadeOut());

            IEnumerator FadeIn()
            {
                GetComponent<Renderer>().enabled = true;

                var startColor = component.color;
                var endColor = new Color(startColor.r, startColor.g, startColor.b, 1);
                float t = 0;
                while (t < 1)
                {
                    t += Time.deltaTime / transition.Duration;
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
                float t = 0;
                while (t < 1)
                {
                    t += Time.deltaTime / transition.Duration;
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
                    transition.RotationType == Ts.Move.RotationTypes.LookAt
                        ? transform.rotation
                        : transform.localRotation;
                float t = 0;
                while (t < 1)
                {
                    t += Time.deltaTime / transition.Duration;

                    // Move position
                    transform.localPosition = Vector3.Lerp(startPosition, transition.Position, t);

                    // Move rotation
                    if (transition.RotationType == Ts.Move.RotationTypes.LookAt)
                    {
                        Ts.Move.LookAtRotation lookRotation = transition.LookRotation;
                        transform.rotation = Quaternion.Slerp(
                            startRotation,
                            Quaternion.LookRotation(
                                transform.position -
                                    transform.root.TransformPoint(lookRotation.Target),
                                lookRotation.Up
                            ),
                            t
                        );
                    }
                    else
                    {
                        transform.localRotation = Quaternion.Slerp(
                            startRotation,
                            Quaternion.Euler(transition.EulerRotation),
                            t
                        );
                    }
                    yield return null;
                }
            }
        }

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
                float t = 0;
                while (t < 1)
                {
                    t += Time.deltaTime / transition.Duration;
                    component.color = Color.Lerp(startColor, transition.NewColor, t);
                    yield return null;
                }
            }
        }

        public void ScaleTransition(Ts.Transition transition)
        {
            var scale = transition as Ts.Scale;
            // Debug.Log($"Scale {gameObject.name} {scale.NewScale}");
        }

        public void SoundTransition(Ts.Transition transition)
        {
            var sound = transition as Ts.Sound;
            // Debug.Log($"Sound {gameObject.name} {sound.Operation}");
        }

        public void LinkTransition(Ts.Transition transition)
        {
            var link = transition as Ts.Link;
            // Debug.Log($"Link {gameObject.name} {link.Operation}");
        }
    }
}
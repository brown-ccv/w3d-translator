using System;
using System.IO;
using UnityEditor;
using UnityEngine;
using UnityEngine.Events;
using TMPro;

using Writing3D.Xml;
using Writing3D.Transitions;

using static UnityEngine.ScriptableObject;
using static UnityEngine.Object;
using static UnityEditor.Events.UnityEventTools;

namespace Writing3D
{
    namespace Editor
    {
        public static partial class CLI
        {
            /********** Writing3D.Xml TO UNITY CONVERSIONS    ***********/

            // Converts "[int], [int], [int]" to a UnityEngine.Color object
            private static UnityEngine.Color ConvertColor(string colorString)
            {
                string[] strings = colorString.Trim(new[] { ' ', '(', ')' }).Split(",");
                return new UnityEngine.Color(
                    float.Parse(strings[0]) / 255,
                    float.Parse(strings[1]) / 255,
                    float.Parse(strings[2]) / 255
                );
            }

            // Converts a "([float], [float], [float])" string to a UnityEngine.Vector3 object
            private static Vector3 ConvertVector3(string vectorString)
            {
                string[] strings = vectorString.Trim(new[] { ' ', '(', ')' }).Split(",");
                return new Vector3(
                    float.Parse(strings[0]),
                    float.Parse(strings[1]),
                    float.Parse(strings[2]) * -1
                );
            }

            // Converts a float to a UnityEngine.Vector3 object
            private static Vector3 ConvertScale(float scale) { return Vector3.one * scale; }

            /********** UNITY SIMPLE TYPES    ***********/

            // Converts a "([float], [float], [float])" string and an angle to a Euler angle
            private static Vector3 CreateEuler(string rotationString, float Angle)
            {
                return ConvertVector3(rotationString) * Angle;
            }

            /********** PLACEMENT ROOT    ***********/

            // Get the transform of the wall xmlPlacement is to be nested under
            private static Transform GetParent(Placement xmlPlacement)
            {
                return _WallsDict[xmlPlacement.RelativeTo.ToString()];
            }

            // Gets the converted position element from xmlPlacement
            private static Vector3 GetPosition(Placement xmlPlacement)
            {
                return ConvertVector3(xmlPlacement.PositionString);
            }

            /** Set parent GameObject and local transforms of gameObjectT
                relativeTo: [GameObject].transform.parent
                position: [GameObject].transform.localPosition
                rotationType.Axis: Rotation angle around an axis
                rotationType.LookAt: Rotate to look at target vector (world space)
                rotationType.Normal: Local rotation around a normalized vector
            */
            private static void SetTransform(
                Transform gameObjectT,
                Placement xmlPlacement,
                float scale = 1
            )
            {
                gameObjectT.localScale = ConvertScale(scale);
                gameObjectT.SetParent(GetParent(xmlPlacement), false);
                gameObjectT.localPosition = GetPosition(xmlPlacement);
                switch (xmlPlacement.Rotation)
                {
                    case Axis xmlAxis:
                        gameObjectT.localEulerAngles = CreateEuler(
                            xmlAxis.RotationString,
                            xmlAxis.Angle
                        );
                        break;
                    case LookAt xmlLookAt:
                        gameObjectT.rotation = Quaternion.LookRotation(
                            gameObjectT.position -
                                _Root.transform.TransformPoint(ConvertVector3(xmlLookAt.TargetString)),
                            ConvertVector3(xmlLookAt.UpString)
                        );
                        break;
                    case Normal xmlNormal:
                        gameObjectT.localEulerAngles = CreateEuler(
                            xmlNormal.NormalString,
                            xmlNormal.Angle
                        );
                        break;
                    default:
                        gameObjectT.localRotation = Quaternion.identity;
                        break;
                }
            }

            /********** OBJECT ROOT    ***********/

            private static GameObject CreateContent(Xml.Object xmlObject)
            {
                return xmlObject.Content.ContentData switch
                {
                    Text xmlText => CreateText(xmlText, xmlObject.ColorString),
                    Image xmlImage => new GameObject(), // TODO 65
                    StereoImage xmlStereoImage => new(), // TODO 66
                    Model xmlModel => new GameObject(), // TODO 67
                    Xml.Light xmlLight => new GameObject(), // TODO 68
                    Xml.ParticleSystem xmlParticleSystem => new GameObject(), // TODO 69
                    _ => new GameObject(),
                };
            }

            private static GameObject CreateText(Text xmlText, string colorString)
            {
                // Instantiate TextMeshPro or TextMeshProUGUI prefab
                // TODO 64: Validate prefab settings
                GameObject gameObject = Instantiate(
                    Resources.Load<GameObject>("Prefabs/text")
                );
                TMP_Text tmpText = gameObject.GetComponent<TMP_Text>();

                // Set object properties defined in the xml
                tmpText.SetText(xmlText.String);
                tmpText.horizontalAlignment = (HorizontalAlignmentOptions)xmlText.HorizontalAlignment;
                tmpText.verticalAlignment = (VerticalAlignmentOptions)xmlText.VerticalAlignment;
                tmpText.color = ConvertColor(colorString); // Vertex Color

                // Load font material
                // TODO 72: More robust path checking
                // TODO: Don't have to worry about re-throwing exceptions if handled in main
                TMP_FontAsset tmpFont = Resources.Load<TMP_FontAsset>(
                    "Materials/Fonts/" +
                    Path.GetFileNameWithoutExtension(xmlText.Font) +
                    " SDF"
                );
                if (tmpFont == null)
                {
                    // Font material hasn't been created, attempt to load from ttf file
                    try
                    {
                        Font font = AssetDatabase.LoadAssetAtPath<Font>(xmlText.Font);
                        tmpFont = TMP_FontAsset.CreateFontAsset(font);
                        tmpFont.name = Path.GetFileNameWithoutExtension(xmlText.Font);
                    }
                    catch (NullReferenceException)
                    {
                        Debug.LogWarning($"Font {xmlText.Font} failed to load");
                    }
                }

                // Add font to the TextMeshPro object
                try { tmpText.font = tmpFont; }
                catch (NullReferenceException)
                {
                    Debug.LogWarning($"Error creating font asset {xmlText.Font} for {gameObject.name}");
                    Debug.LogWarning("Defaulting to fallback font: LiberationSans SDF");
                }

                // Resize BoxCollider to the text
                gameObject.GetComponent<BoxCollider>().size =
                    new Vector3(tmpText.preferredWidth, tmpText.preferredHeight, 0);
                return gameObject;
            }

            /********** ACTIONS    ***********/

            private static void AddAction(LinkActions xmlLinkAction, LinkManager lm)
            {
                // Initialize action
                LinkAction linkAction = CreateInstance<LinkAction>();
                if (xmlLinkAction.Clicks?.Type == Clicks.ActivationTypes.Number)
                {
                    NumClicks activation = (NumClicks)xmlLinkAction.Clicks.Activation;
                    linkAction.Init(activation.Clicks, activation.Reset);
                }

                GameObject reference;
                switch (xmlLinkAction.Action)
                {
                    case ObjectChange xmlAction:
                        // Get referenced GameObject
                        reference = _ObjectDict[xmlAction.Name].Item1;

                        // Initialize the transition and add to LinkActionEvent
                        Transitions.Transition transition = GetTransition(
                            xmlAction.Transition,
                            xmlAction.Transition.Duration
                        );
                        AddObjectPersistentListener(
                            linkAction.ActionEvent,
                            transition.GetUnityAction(reference),
                            transition
                        );
                        break;
                    case GroupChange xmlAction:
                        // TODO 87
                        break;
                    case TimerChange xmlAction:
                        // TODO 88
                        break;
                    case SoundChange xmlAction:
                        // TODO 91
                        break;
                    case EventChange xmlAction:
                        // TODO 89
                        break;
                    case MoveCave xmlAction:
                        // TODO 90
                        break;
                    case null:
                        // TODO 92: Restart
                        break;
                    default:
                        throw new Exception("Invalid action type");
                }
                AddObjectPersistentListener(
                    lm.deactivated,
                    new UnityAction<LinkAction>(lm.ExecuteAction),
                    linkAction
                );
            }

            private static Transitions.Transition GetTransition(Xml.Transition xmlTransition, float duration)
            {
                return xmlTransition.Change switch
                {
                    bool visible => CreateInstance<Visible>().Init(visible, duration),
                    MovementTransition move => CreateInstance<Move>()
                        .Init(
                            GetParent(move.Placement),
                            GetPosition(move.Placement),
                            GetRotationType(move.Placement),
                            GetRotation(move.Placement),
                            duration
                        ),
                    MoveRel move => CreateInstance<RelativeMove>()
                        .Init(
                            GetParent(move.Placement),
                            GetPosition(move.Placement),
                            GetRotationType(move.Placement),
                            GetRotation(move.Placement),
                            duration
                        ),
                    string color => CreateInstance<Transitions.Color>()
                        .Init(ConvertColor(color), duration),
                    float scale => CreateInstance<Scale>().Init(scale),
                    SoundTransition operation => CreateInstance<Transitions.Sound>()
                        .Init((Transitions.Sound.Controls)operation.Type, duration),
                    LinkTransition operation => CreateInstance<Transitions.Link>()
                        .Init((Transitions.Link.Controls)operation.Type, duration),
                    _ => throw new Exception("Invalid transition type")
                };
            }

            // Get the rotation type of a Move/RelativeMove transition
            private static Move.RotationTypes GetRotationType(Placement xmlPlacement)
            {
                return xmlPlacement.RotationType switch
                {
                    Placement.RotationTypes.Null => Move.RotationTypes.None,
                    Placement.RotationTypes.Axis => Move.RotationTypes.Rotation,
                    Placement.RotationTypes.LookAt => Move.RotationTypes.LookAt,
                    Placement.RotationTypes.Normal => Move.RotationTypes.Rotation,
                    _ => throw new Exception("Invalid rotation type")
                };
            }

            // Get the rotation of a Move/RelativeMove transition
            private static object GetRotation(Placement xmlPlacement)
            {
                return xmlPlacement.Rotation switch
                {
                    Axis xmlAxis => CreateEuler(xmlAxis.RotationString, xmlAxis.Angle),
                    LookAt xmlLookAt => new Move.LookAt(
                        ConvertVector3(xmlLookAt.TargetString),
                        ConvertVector3(xmlLookAt.UpString)
                    ),
                    Normal xmlNormal => CreateEuler(xmlNormal.NormalString, xmlNormal.Angle),
                    _ => null
                };
            }
        }
    }
}
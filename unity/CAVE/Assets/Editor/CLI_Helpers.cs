using System;
using System.IO;
using UnityEditor;
using UnityEditor.Events;
using UnityEngine;
using UnityEngine.Events;
using TMPro;

using Writing3D.Xml;
using Writing3D.Actions;
using Writing3D.Transitions;

using static UnityEngine.ScriptableObject;
using static UnityEngine.Object;
using static UnityEditor.Events.UnityEventTools;

namespace Writing3D
{
    namespace Translation
    {
        public static partial class CLI
        {
            /********** Writing3D.Xml to Unity conversions    ***********/

            // Converts "[int], [int], [int]" to a UnityEngine.Color object
            public static UnityEngine.Color ConvertColor(string colorString)
            {
                string[] strings = colorString.Trim(new[] { ' ', '(', ')' }).Split(",");
                return new UnityEngine.Color(
                    float.Parse(strings[0]) / 255,
                    float.Parse(strings[1]) / 255,
                    float.Parse(strings[2]) / 255
                );
            }

            // Converts a "([float], [float], [float])" string to a UnityEngine.Vector3 object
            public static Vector3 ConvertVector3(string vectorString)
            {
                string[] strings = vectorString.Trim(new[] { ' ', '(', ')' }).Split(",");
                return new Vector3(
                    float.Parse(strings[0]),
                    float.Parse(strings[1]),
                    float.Parse(strings[2]) * -1
                );
            }

            // Converts a float to a UnityEngine.Vector3 object
            public static Vector3 ConvertScale(float scale) { return Vector3.one * scale; }

            /********** Unity simple types    ***********/

            // Converts a "([float], [float], [float])" string and an angle to a Euler angle
            public static Vector3 CreateEuler(string rotationString, float Angle)
            {
                return ConvertVector3(rotationString) * Angle;
            }

            /********** PLACEMENT ROOT    ***********/

            /** Set parent GameObject and local transforms of gameObjectT
                relativeTo: [GameObject].transform.parent
                position: [GameObject].transform.localPosition
                rotationType.Axis: Rotation angle around an axis
                rotationType.LookAt: Rotate to look at target vector (world space)
                rotationType.Normal: Local rotation around a normalized vector
            */
            public static void SetTransform(Transform gameObjectT, Placement xmlPlacement, float scale = 1)
            {
                Transform rootTransform = Root.transform;

                gameObjectT.SetParent(GetParent(xmlPlacement), false);
                gameObjectT.localPosition = ConvertVector3(xmlPlacement.PositionString);
                gameObjectT.localScale = ConvertScale(scale);

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
                                rootTransform.TransformPoint(ConvertVector3(xmlLookAt.TargetString)),
                            ConvertVector3(xmlLookAt.UpString)
                        );
                        break;
                    case Normal xmlNormal:
                        gameObjectT.localEulerAngles = CreateEuler(
                            xmlNormal.NormalString,
                            xmlNormal.Angle
                        );
                        break;
                    case null:
                        gameObjectT.localRotation = Quaternion.identity;
                        break;
                    default: break;
                }
            }

            public static Transform GetParent(Placement xmlPlacement)
            {
                return xmlPlacement.RelativeTo == Placement.PlacementTypes.Center
                        ? Root.transform // Nest under Root directly
                        : Root.transform.Find(xmlPlacement.RelativeTo.ToString());
            }

            /********** OBJECT ROOT    ***********/

            public static GameObject CreateContent(Xml.Object xmlObject)
            {
                return xmlObject.Content.ContentData switch
                {
                    Text xmlText => CreateText(xmlText, xmlObject.ColorString),
                    Image xmlImage => new GameObject(), // TODO 65
                    StereoImage xmlStereoImage => new(), // TODO 66
                    Model xmlModel => new GameObject(), // TODO 67
                    Xml.Light xmlLight => new GameObject(), // TODO 68
                    Xml.ParticleSystem xmlParticleSystem => new GameObject(), // TODO 69
                    _ => null, // Force error
                };
            }

            public static GameObject CreateText(Text xmlText, string colorString)
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

            public static void AddAction(LinkActions xmlLinkAction, LinkManager lm)
            {
                // Initialize action
                LinkAction linkAction = CreateInstance<LinkAction>();
                if (xmlLinkAction.Clicks is not null &&
                    xmlLinkAction.Clicks.Type == Clicks.ActivationTypes.Number)
                {
                    NumClicks activation = (NumClicks)xmlLinkAction.Clicks.Activation;
                    linkAction.Init(activation.Clicks, activation.Reset);
                }

                GameObject reference;
                switch (xmlLinkAction.Action)
                {
                    case ObjectChange xmlAction:
                        // Get referenced GameObject
                        reference = GameObjects[xmlAction.Name].Item1;

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
                        // TODO 87:
                        break;
                    case TimerChange xmlAction:
                        // TODO 88:
                        break;
                    case SoundChange xmlAction:
                        // TODO 91:
                        break;
                    case EventChange xmlAction:
                        // TODO 89:
                        break;
                    case MoveCave xmlAction:
                        // TODO 90:
                        break;

                    case null:
                        // TODO 92: (Restart)
                        break;
                    default:
                        linkAction = null; // Force error below, caught in CLI.cs
                        break;
                }
                AddObjectPersistentListener(
                    lm.deactivated,
                    new UnityAction<LinkAction>(lm.ExecuteAction),
                    linkAction
                );
            }

            public static Transitions.Transition GetTransition(Xml.Transition xmlTransition, float duration)
            {
                // TODO 122: Init for Move and RelativeMove
                return xmlTransition.Change switch
                {
                    bool visible => CreateInstance<Visible>().Init(visible, duration),
                    MovementTransition placement => CreateInstance<Move>(),
                    MoveRel placement => CreateInstance<RelativeMove>(),
                    string color => CreateInstance<Transitions.Color>()
                        .Init(ConvertColor(color), duration),
                    float scale => CreateInstance<Scale>().Init(scale),
                    SoundTransition operation => CreateInstance<Transitions.Sound>()
                        .Init((Transitions.Sound.Controls)operation.Type, duration),
                    LinkTransition operation => CreateInstance<Transitions.Link>()
                        .Init((Transitions.Link.Controls)operation.Type, duration),
                    _ => null // force error
                };
            }
        }
    }
}
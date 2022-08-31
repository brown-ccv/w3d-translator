using System;
using System.IO;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Events;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using TMPro;

using Writing3D.Xml;

namespace Writing3D
{
    namespace Translation
    {
        public static class Helpers
        {
            /********** Writing3D.Xml to Unity conversions    ***********/

            // Converts "[int], [int], [int]" to a UnityEngine.Color object
            public static Color ConvertColor(string colorString)
            {
                string[] strings = colorString.Trim(new[] { ' ', '(', ')' }).Split(",");
                return new Color(
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
            // public static void SetTransform(Transform gameObjectT, Placement xmlPlacement, Vector3 scale)
            public static void SetTransform(Transform gameObjectT, Placement xmlPlacement, float scale = 1)
            {
                Transform rootTransform = GameObject.Find("/Root").transform;

                gameObjectT.SetParent(
                    xmlPlacement.RelativeTo == Placement.PlacementTypes.Center
                        ? rootTransform // Nest under Root directly
                        : rootTransform.Find(xmlPlacement.RelativeTo.ToString()),
                    false
                );
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

            /********** OBJECT ROOT    ***********/

            public static GameObject CreateObject(Xml.Object xmlObject)
            {
                GameObject gameObject = xmlObject.Content.ContentData switch
                {
                    Xml.Text xmlText => CreateText(
                        xmlText,
                        xmlObject.LinkRoot is not null,
                        xmlObject.ColorString
                    ),
                    Xml.Image xmlImage => new GameObject(), // TODO (65)
                    StereoImage xmlStereoImage => new(), // TODO (66)
                    Model xmlModel => new GameObject(), // TODO (67)
                    Xml.Light xmlLight => new GameObject(), // TODO (68)
                    Xml.ParticleSystem xmlParticleSystem => new GameObject(), // TODO (69)
                    _ => new GameObject(), // TODO: - Shouldn't occur, throw error
                };
                gameObject.name = xmlObject.Name;
                gameObject.tag = "Object";
                gameObject.AddComponent<ObjectManager>();
                return gameObject;
            }

            public static GameObject CreateText(Xml.Text xmlText, bool isLink, string colorString)
            {
                // Instantiate TextMeshPro or TextMeshProUGUI prefab
                // TODO (64): Validate prefab settings
                GameObject gameObject = UnityEngine.Object.Instantiate(
                    Resources.Load<GameObject>("Prefabs/TmpText" + (isLink ? "GUI" : ""))
                );
                TMP_Text tmpText = gameObject.GetComponent<TMP_Text>();

                // Set object properties defined in the xml
                tmpText.SetText(xmlText.String);
                tmpText.horizontalAlignment = (HorizontalAlignmentOptions)xmlText.HorizontalAlignment;
                tmpText.verticalAlignment = (VerticalAlignmentOptions)xmlText.VerticalAlignment;
                tmpText.color = ConvertColor(colorString); // Vertex Color

                // Load font material
                // TODO (72): More robust path checking
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
                    catch (NullReferenceException e)
                    {
                        Debug.LogError($"Error loading font: {xmlText.Font}");
                        Debug.LogException(e);
                    }
                }

                // Add font to the TextMeshPro object
                try { tmpText.font = tmpFont; }
                catch (NullReferenceException e)
                {
                    Debug.LogWarning($"{gameObject.name} {tmpFont} {tmpText.font}");
                    Debug.LogError($"Error creating font asset {xmlText.Font} for {gameObject.name}");
                    Debug.Log("Defaulting to fallback font LiberationSans SDF");
                    Debug.LogException(e);
                }

                return gameObject;
            }

            /********** ACTIONS    ***********/

            public static void AddAction(LinkActions xmlLinkAction, Button button, Dictionary<string, (GameObject, Xml.Object)> GameObjects)
            {
                ButtonManager bm = button.GetComponent<ButtonManager>();
                Button.ButtonClickedEvent onClick = button.onClick;

                // Initialize action
                LinkAction linkAction = ScriptableObject.CreateInstance(typeof(LinkAction))
                                        as LinkAction;
                if (xmlLinkAction.Clicks is not null &&
                    xmlLinkAction.Clicks.Type == Clicks.ActivationTypes.Number)
                {
                    NumClicks activation = (NumClicks)xmlLinkAction.Clicks.Activation;
                    linkAction.NumClicks = activation.Clicks;
                    linkAction.Reset = activation.Reset;
                }

                // TODO: ButtonManager gets an event for every action/transition type (static)
                // TODO: Need to find a way to save the 

                GameObject reference = null; // TEMP - no initialization needed
                switch (xmlLinkAction.Action)
                {
                    case ObjectChange xmlAction:
                        linkAction.Type = Action.Types.Object;

                        // Get referenced GameObject and initialize Transition
                        reference = GameObjects[xmlAction.Name].Item1;

                        // TODO: LinkAction is a ScriptableObject
                        // Everything else is just a basic class (struct?)
                        ObjectAction action = new();
                        action.Transition = new Transition();

                        // TODO: Make switch (separate function)
                        // if (xmlAction.Transition.Type == Xml.Transition.TransitionType.Visible)
                        // {
                        //     VisibleTransition transition = new();
                        //     action.Transition = transition;
                        // }

                        linkAction.Action = action;

                        // TODO: Can move to bottom of switch
                        Debug.Log(bm.Actions);
                        Debug.Log(linkAction.GetType());
                        // Debug.Log(reference.GetComponent<ObjectManager>().GetType());
                        Debug.Log(reference.name + " " + reference.tag);

                        UnityEventTools.AddObjectPersistentListener(
                            bm.Actions,
                            new UnityAction<LinkAction>(reference.GetComponent<ObjectManager>().VisibleTransition),
                            linkAction
                        );
                        break;
                    case GroupChange xmlAction:
                        // TODO: 87
                        break;
                    case TimerChange xmlAction:
                        // TODO: 88
                        break;
                    case SoundChange xmlAction:
                        // TODO: 91
                        break;
                    case EventChange xmlAction:
                        // TODO: 89
                        break;
                    case MoveCave xmlAction:
                        // TODO: 90
                        break;

                    case null:
                        // TODO: 92 (Restart)
                        break;
                    default: break; // All cases covered
                }
            }
        }
    }
}
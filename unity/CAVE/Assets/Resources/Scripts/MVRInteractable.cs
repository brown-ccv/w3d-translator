using System;

using MiddleVR;
using MiddleVR.Unity;

using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

namespace Writing3D
{
    [Serializable]
    public class MVRInteractable : MVRActor
    {
        // TODO: How to use ActivateEventArgs (etc.) from XRI
        // If this is possible, is there a way to always use XRI?
        private LinkManager _LinkManager;

        public void Start() { _LinkManager = GetComponent<LinkManager>(); }

        public void HandleMVRInteraction(int button, bool isPressed)
        {
            Debug.Log($"MVR Interaction {button} {isPressed}");
            switch (button)
            {
                case 0:
                    if (isPressed)
                    {
                        Debug.Log("Activated");
                        //_LinkManager.activated.Invoke(new ActivateEventArgs());
                        _LinkManager.activated.Invoke(null);
                    }
                    else
                    {
                        Debug.Log("Deactivated");
                        //_LinkManager.deactivated.Invoke(new DeactivateEventArgs());
                        _LinkManager.deactivated.Invoke(null);
                    }
                    break;
                case 1:
                    if (isPressed)
                    {
                        Debug.Log("Selected");
                        //_LinkManager.selectEntered.Invoke(new SelectEnterEventArgs());
                        _LinkManager.selectEntered.Invoke(null);
                    }
                    else
                    {
                        Debug.Log("Deselected");
                        //_LinkManager.selectExited.Invoke(new SelectExitEventArgs());
                        _LinkManager.selectExited.Invoke(null);
                    }
                    break;
                case 2:
                    Debug.Log("Left Button");
                    break;
                case 3:
                    Debug.Log("Right Button");
                    break;
                case 4:
                case 5:
                default: break; // Buttons 4 and 5 are not conigured on our wand
            }
        }
    }
}
using System;

using UnityEngine;

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
                    if (isPressed) { _LinkManager.activated.Invoke(null); }
                    else { _LinkManager.deactivated.Invoke(null); }
                    break;
                case 1:
                    if (isPressed) { _LinkManager.selectEntered.Invoke(null); }
                    else { _LinkManager.selectExited.Invoke(null); }
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
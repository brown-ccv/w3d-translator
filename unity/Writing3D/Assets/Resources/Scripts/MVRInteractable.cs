using System;

using UnityEngine;

namespace Writing3D
{
    [Serializable]
    public class MVRInteractable : MVRActor
    {
        private LinkManager _LinkManager;

        public void Start() { _LinkManager = GetComponent<LinkManager>(); }

        public void HandleMVRInteraction(int button, bool isPressed)
        {
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
                case 2: // Left Button
                case 3: // Right Button
                case 4: // Not used in our wand
                case 5: // Not used in our wand
                default:
                    Debug.LogWarning($"Button ${button} not been implemented");
                    break;
            }
        }
    }
}
using System;

using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

namespace Writing3D
{
    [Serializable]
    public class LinkManager : XRBaseInteractable
    {
        public Color EnabledColor;
        public Color ActiveColor;
        public Color DisabledColor;
        private int _ClickCount = 0;

        public void HandleMVRInteraction(int button, bool isPressed)
        {
            Debug.Log($"MVR Interaction {button} {isPressed}");
        }

        protected void OnMVRWandButtonPressed(MVRSelection iSelection)
        {
            Debug.Log(iSelection + ": OnMVRWandButtonPressed.");
            activated.Invoke(null);
        }

        protected void OnMVRWandButtonReleased(MVRSelection iSelection)
        {
            Debug.Log(iSelection + ": OnMVRWandButtonReleased.");
            deactivated.Invoke(null);
        }

        /* ACTION FUNCTIONS */

        // Enable the GameObject as a clickable object
        public void EnableLink()
        {
            SetColor(EnabledColor);
            enabled = true;
        }

        // Disable the GameObject as a (non)clickable object
        public void DisableLink()
        {
            SetColor(DisabledColor);
            enabled = false;
        }

        // Called on trigger press
        public void Activate()
        {
            _ClickCount++;
            SetColor(ActiveColor);
        }

        // Called on trigger release
        public void Deactivate() { SetColor(EnabledColor); }

        // Execute the inner event if NumClicks has been reached
        public void ExecuteAction(LinkAction linkAction)
        {
            if (_ClickCount >= linkAction.NumClicks) { linkAction.ActionEvent.Invoke(); }
        }

        /* HELPER FUNCTIONS */

        private void SetColor(Color color) { GetComponent<ObjectManager>().SetColor(color); }
    }
}
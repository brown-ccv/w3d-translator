using System;
using System.Collections.Generic;

using UnityEngine;
using UnityEngine.UI;

namespace Writing3D
{
    [Serializable]
    public class ButtonManager : MonoBehaviour
    {
        // [SerializeField] public List<LinkActionEvent> LinkActions = new();
        [SerializeField] public LinkActionEvent LinkActionEvent = new();
        private int clickCount = 0;

        // Increase clickCount
        public void Counter() { clickCount++; }

        // Disable the Button on the GameObject this script is attached to
        public void Disable() { GetComponent<Button>().interactable = false; }

        // Execute the inner event if NumClicks has been reached
        public void ExecuteAction(LinkAction linkAction)
        {
            if (clickCount >= linkAction.NumClicks) { linkAction.ActionEvent.Invoke(); }
        }
    }
}
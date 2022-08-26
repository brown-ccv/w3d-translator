using System;
using System.Collections.Generic;

using UnityEngine;
using UnityEngine.UI;

namespace W3D
{
    [Serializable]
    public class ButtonManager : MonoBehaviour
    {
        [SerializeField]
        public List<LinkAction> Actions = new();
        private int clickCount = 0;

        // Increase clickCount
        public void Counter()
        {
            clickCount++;
            Debug.Log($"CLICKED {clickCount}");
        }

        // Disable the Button on the GameObject this script is attached to
        public void Disable() { GetComponent<Button>().interactable = false; }

        // Loop through the actions in Actions, check against NumClicks and call
        public void ExecuteActions()
        {
            foreach (LinkAction action in Actions) { action.Delegate.Invoke(); }
        }
    }
}
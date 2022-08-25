using System;
using System.Collections.Generic;

using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using UnityEditor;

namespace W3D
{
    [Serializable]
    public class ActionEvent : UnityEvent<Action> { }

    [Serializable]
    public class ButtonManager : MonoBehaviour
    {
        [SerializeField]
        public ActionEvent ActionEvent;
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
        // public class ActionEvent : UnityEvent<Action> {}
        public void ExecuteActions()
        {
        }
    }
}
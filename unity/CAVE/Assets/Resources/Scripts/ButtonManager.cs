using System;

using UnityEngine;
using UnityEngine.UI;
using UnityEditor.Events;

namespace Writing3D
{
    [Serializable]
    public class ButtonManager : MonoBehaviour
    {
        [SerializeField] public LinkActionEvent Actions = new();
        private int clickCount = 0;

        // Increase clickCount
        public void Counter() { clickCount++; }

        // Disable the Button on the GameObject this script is attached to
        public void Disable() { GetComponent<Button>().interactable = false; }

        // Loop through the actions in Actions, check against NumClicks and call
        public void ExecuteActions()
        {
            // foreach (LinkAction action in Actions) { }
            Debug.Log(Actions.GetPersistentEventCount());
            for (int i = 0; i < Actions.GetPersistentEventCount(); i++)
            {
                Debug.Log($"{Actions.GetPersistentListenerState(i)} {Actions.GetPersistentMethodName(i)} {Actions.GetPersistentTarget(i)}");
            }
            // TODO: I need this to invoke with the LinkAction already defined
            // TODO: onClick works okay with just an Invoke? What's the type?
            // Actions.Invoke();
            // GetComponent<Button>().onClick.Invoke();
        }
    }
}
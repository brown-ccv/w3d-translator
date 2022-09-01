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

        // Loop through the actions in Actions, check against NumClicks and call
        public void ExecuteAction(LinkAction linkAction)
        {
            // TODO: If I link by I I should be able to call the method in that other way?
            // foreach (LinkActionEvent action in LinkActions)
            // {
            //     // TODO: Only execute if NumClicks <= clickCount
            //     Debug.Log($"EXECUTE {action.GetType()} {action.NumClicks} {action.Reset}");
            //     UnityEngine.Object targetObject = action.GetPersistentTarget(0);
            //     System.Reflection.MethodInfo method = targetObject.GetType().GetMethod(action.GetPersistentMethodName(0));
            //     Debug.Log(method.GetParameters()[0]);
            //     action.Invoke();
            // }
            // for (int i = 0; i < Actions.GetPersistentEventCount(); i++)
            // {
            //     Debug.Log("Invoking action " + i);
            //     Actions.Invoke(clickCount);
            // }
        }
    }
}
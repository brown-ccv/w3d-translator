using System;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using Unity.XR.CoreUtils;

using W3D;

public class ActionMethods : MonoBehaviour {
    // Disable the button after it's been clicked
    public void DisableButton(Button button) {
        button.interactable = false;
    }
}
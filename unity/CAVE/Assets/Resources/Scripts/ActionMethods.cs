using UnityEngine;
using UnityEngine.UI;

namespace W3D
{
    public class ActionMethods : MonoBehaviour
    {
        // Disable the button after it's been clicked
        public void DisableButton(Button button)
        {
            button.interactable = false;
        }
    }
}
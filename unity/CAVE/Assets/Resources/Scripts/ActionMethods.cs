using UnityEngine;
using UnityEngine.UI;

# pragma warning disable RCS1110
public class ActionMethods : MonoBehaviour
{
    // Disable the button after it's been clicked
    public void DisableButton(Button button)
    {
        button.interactable = false;
    }
}
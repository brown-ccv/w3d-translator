using UnityEngine;
using UnityEngine.UI;

namespace W3D
{
    public class ButtonManager : MonoBehaviour
    {
        public void DisableButton()
        {
            GetComponent<Button>().interactable = false;
        }
    }
}
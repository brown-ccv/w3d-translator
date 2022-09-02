using UnityEngine;
using UnityEngine.UI;

namespace Writing3D
{
    public class ButtonManager : MonoBehaviour
    {
        public void DisableButton()
        {
            GetComponent<Button>().interactable = false;
        }
    }
}
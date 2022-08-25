using UnityEngine;
using UnityEngine.UI;

// TODO: Add to prefab
// TODO: Make XML namespace
namespace W3D
{
    public class ButtonManager : MonoBehaviour
    {
        private Button Button;

        private void Start()
        {
            Button = GetComponent<Button>();
        }

        public void DisableButton()
        {
            Debug.Log("Button " + Button.name);
            Button.interactable = false;
        }
    }
}
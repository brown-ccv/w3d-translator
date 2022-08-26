using UnityEngine;

namespace W3d
{
    public class W3D : MonoBehaviour
    {
        private void Update()
        {
            // Quit when "ESC" is pressed
            if (Input.GetKeyDown(KeyCode.Escape)) { Application.Quit(); }
        }
    }
}
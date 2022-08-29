using UnityEngine;

namespace Writing3D
{
    public class SceneManager : MonoBehaviour
    {
        private void Update()
        {
            // Quit when "ESC" is pressed
            if (Input.GetKeyDown(KeyCode.Escape)) { Application.Quit(); }
        }
    }
}
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

    /** Type definitions */

    public struct Placement
    {
        public Transform Parent;
        public Vector3 LocalPosition;
        // public Vector3 LocalRotation; // TODO: Does <Action> ever set rotation?
    }
}
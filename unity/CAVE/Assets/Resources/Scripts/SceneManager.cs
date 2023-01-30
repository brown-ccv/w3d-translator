using UnityEngine;

namespace Writing3D
{
    public class SceneManager : MonoBehaviour
    {
        public GameObject MVR;   // MVRManager root object
        public GameObject XR;    // XR Origin root object

        // Called when GameObject is initialized
        protected void Awake()
        {
            Debug.Log("SceneManager Awake " + MVR.activeSelf + XR.activeSelf);
            // TODO: Document that XR and MVR must be disabled in the editor

            if (Application.isEditor)
            {
                // MVR should never be enabled when in the Unity Editor
                MVR.SetActive(false);
                XR.SetActive(true);
            }
            else
            {
                // TODO: Move to START()? See if MVR is enabled?
                // Copied from MVRManagerScript.Awake() (MVRManager object)
                string[] args = System.Environment.GetCommandLineArgs();
                bool foundCfgParam = false;

                for (int i = 0; i < args.Length; i++)
                {
                    if (args[i] == "--config") { foundCfgParam = true; }
                }

                if (foundCfgParam)
                {
                    // Using MiddleVR, enable it and disable XR
                    Debug.Log("[ ] Command line argument --config found. Enabling MiddleVR");
                    MVR.SetActive(true);
                    XR.SetActive(false);
                }
                else
                {
                    // Not using MiddleVR, disable it and enable XR
                    Debug.Log("[ ] In Unity Player, command line argument --config not found. Disabling MiddleVR.");
                    MVR.SetActive(false);
                    XR.SetActive(true);
                }
            }
        }

        // Called on the frame a script it enabled (after Awake)
        protected void Start()
        {

        }

        protected void Update()
        {
            // Quit when "ESC" is pressed
            if (Input.GetKeyDown(KeyCode.Escape)) { Application.Quit(); }
        }
    }
}
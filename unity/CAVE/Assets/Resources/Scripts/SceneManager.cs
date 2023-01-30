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
            // TODO: Document that XR and MVR must be disabled in the editor
#if UNITY_EDITOR
            // In editor - activate XR
            XR.SetActive(true);
            MVR.SetActive(false);
#endif

#if UNITY_STANDALONE
            // In Windows executable - activate MVR
            XR.SetActive(false);
            MVR.SetActive(true);
#endif

#if UNITY_ANDROID
            // In Android executable - activate XR
            XR.SetActive(true);
            MVR.SetActive(false);
#endif
        }

        // Called on the frame a script it enabled (after Awake)
        protected void Start()
        {
#if UNITY_STANDALONE
            // If MVR is disabled we must activate XR
            // MVR will disable itself if called without a config file (MVRManagerScript.Awake())
            XR.SetActive(!MVR.activeInHierarchy);
#endif
        }

        protected void Update()
        {
            // Quit when "ESC" is pressed
            if (Input.GetKeyDown(KeyCode.Escape)) { Application.Quit(); }
        }
    }
}
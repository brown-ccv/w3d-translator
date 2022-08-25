using UnityEngine;

namespace W3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Should take custom transition
        public void VisibleTransition(Action parameters)
        {
            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            gameObject.SetActive(false); // parameters.visible
        }
    }
}
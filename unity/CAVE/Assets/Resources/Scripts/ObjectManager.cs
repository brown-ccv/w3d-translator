using UnityEngine;

namespace W3D
{
    public class ObjectManager : MonoBehaviour
    {
        // Move to ObjectManager
        public void VisibleTransition(bool visible, float duration)
        {
            Debug.Log($"VisibleT {gameObject.name} {visible} {duration}");
            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(false); // parameters.visible
        }
    }
}
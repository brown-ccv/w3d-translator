using UnityEngine;

namespace Writing3D
{
    public class ObjectManager : MonoBehaviour
    {
        // TODO: Pass action directly?
        public void VisibleTransition(LinkAction linkAction)
        {
            Debug.Log($"VisibleT {gameObject.name} {linkAction.Type}");
            
            // Fade In/Out and enable/disable the GameObject
            // https://owlcation.com/stem/How-to-fade-out-a-GameObject-in-Unity

            // gameObject.SetActive(false); // parameters.visible
        }
    }
}
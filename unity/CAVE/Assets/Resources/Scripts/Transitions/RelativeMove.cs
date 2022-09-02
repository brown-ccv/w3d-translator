using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/RelativeMove",
            order = 3
        )]
        [Serializable]
        public class RelativeMove : Transition
        {
            // TODO: Placement struct? Use to update transform
        }
    }
}
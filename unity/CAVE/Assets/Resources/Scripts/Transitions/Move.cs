using System;

using UnityEngine;

namespace Writing3D
{
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Move",
            order = 2
        )]
        [Serializable]
        public class Move : Transition
        {
            public Placement Placement;

            public Move Init(Placement placement, float duration)
            {
                Placement = placement;
                Duration = duration;
                return this;
            }
        }
    }
}
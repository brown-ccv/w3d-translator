using System;

using UnityEngine;
using UnityEngine.Events;

namespace Writing3D
{
    // TODO: Add namespace, separate files
    // TODO: Visible, Move, Color
    namespace Transitions
    {
        [CreateAssetMenu(
            fileName = "Transition",
            menuName = "W3D/Transitions/Transition",
            order = 0
        )]
        [Serializable]
        public class Transition : ScriptableObject
        {
            [SerializeField] public float Duration;

            public UnityAction<Transition> GetUnityAction(GameObject reference)
            {
                ObjectManager script = reference.GetComponent<ObjectManager>();
                return this switch
                {
                    Visible => new UnityAction<Transition>(script.VisibleTransition),
                    RelativeMove => new UnityAction<Transition>(script.RelativeMoveTransition),
                    Move => new UnityAction<Transition>(script.MoveTransition),
                    Color => new UnityAction<Transition>(script.ColorTransition),
                    Scale => new UnityAction<Transition>(script.ScaleTransition),
                    Sound => new UnityAction<Transition>(script.SoundTransition),
                    Link => new UnityAction<Transition>(script.LinkTransition),
                    _ => null, // force error
                };
            }
        }
    }
}
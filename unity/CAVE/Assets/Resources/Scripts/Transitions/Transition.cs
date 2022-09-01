using System;

using UnityEngine;
using UnityEngine.Events;

using Writing3D.Actions;

namespace Writing3D
{
    // TODO: Add namespace, separate files
    // TODO: Visible, Move, Color
    namespace Transitions
    {
        [Serializable]
        public class Transition : ScriptableObject
        {
            [SerializeField] public float Duration;

            public UnityAction<ObjectAction> GetUnityAction(GameObject reference)
            {
                ObjectManager script = reference.GetComponent<ObjectManager>();
                Debug.Log("CreateAction " + this);
                return this switch
                {
                    Visible => new UnityAction<ObjectAction>(script.VisibleTransition),
                    Move => new UnityAction<ObjectAction>(script.MoveTransition),
                    RelativeMove => new UnityAction<ObjectAction>(script.RelativeMoveTransition),
                    Color => new UnityAction<ObjectAction>(script.ColorTransition),
                    Scale => new UnityAction<ObjectAction>(script.ScaleTransition),
                    Sound => new UnityAction<ObjectAction>(script.SoundTransition),
                    Link => new UnityAction<ObjectAction>(script.LinkTransition),
                    _ => null, // force error
                };
            }
        }
    }
}
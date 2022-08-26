using UnityEngine;

namespace W3D
{
    [CreateAssetMenu(fileName = "Transition", menuName = "CAVE/Transition", order = 0)]
    public class Transition : ScriptableObject
    {

        public float Duration;
        public TransitionType Type;

        public Transition(TransitionType type, float duration)
        {
            Duration = duration;
            Type = type;
        }
    }

    public enum TransitionType
    {
        Visible,
        Movement,
        MoveRelative,
        Color,
        Scale,
        Sound,
        Link,
    }
}
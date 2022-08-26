using UnityEngine;

namespace W3D
{
    public abstract class Action : ScriptableObject { }

    public enum ActionTypes
    {
        ObjectChange,
        GroupReference,
        TimerChange,
        SoundReference,
        EventReference,
        MoveCave,
        Restart,
    }
}
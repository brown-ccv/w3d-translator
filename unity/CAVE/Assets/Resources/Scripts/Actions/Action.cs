using System;

using UnityEngine;

namespace W3D
{
    [CreateAssetMenu(fileName = "Action", menuName = "W3D/Action/Action", order = 0)]
    [Serializable]
    public abstract class Action : ScriptableObject { }

    // public enum ActionTypes
    // {
    //     ObjectChange,
    //     GroupReference,
    //     TimerChange,
    //     SoundReference,
    //     EventReference,
    //     MoveCave,
    //     Restart,
    // }
}
# MiddleVR Notes

## MVR Manager

- MVR Manager is the player's head position
- MVR should be in the same position as the "Main Camera" in VR's XR Origin
  - `(0, 1.36144, -1.8288)`

## Settings

- Leave `"Attach to Camera"` as `false`, MVR creates a new head camera
- Leave `"Preview Window"` as `true`, displays cluster game view in separate window
- Use `MVR Camera` prefab as the `"Template Camera"` - same settings as `XR Rig -> Main Camera`
- I think it's safe to leave anything concerning the "Screen Proximity Warning" disabled as it's easy to see how close you are to the walls inside the CAVE
- The `"VR Root Node"` parameter of the `MVR Manager` will insert that root as the center of the VR object

### MVR Manager Questions

- _Can MVR Manager be placed as a child inside `XR Origin -> Camera Offset`?_
- _Can I offset MVR's `System Center` in the hierarchy by 1.36144?_
- _Does MVR use floor or head tracking? This will determine the y offset_

## Hand Node

- MVR only uses one `HandNode` in the scene, this will be the right controller from XR Origin
- Add `"MVR Attach to Node"` to `XR Origin -> RightController -> XR Controller Right` to attach the prefab as the MVR wand
  - This should only be the model itself, the scripts will be different
  - **The controller will have to be rotated (0, 180, 0)**

## Interactions

### Joystick Navigation

Player navigation will be done by the `"MVR Navigation Wand Joystick"` script. This enables joystick movement. This is the same as the XR Controller position/rotation movement

- `Translation Speed`: Translation speed, in meters per second.
- `Rotation Speed`: Rotation speed, in degrees per second.
- `Fly`: Allow navigation up/down the y axis (**disable this**).

### Manipulation

- `"MVR Interaction Manipulation Ray"` grabs an object via the wand's raycast
- The `"MVRActor"` script is attached to any interactable object
  - `grabable` boolean for whether or not the object can be grabbed
- The wand can be configured for [Unity GUI interactions](https://www.middlevr.com/2/doc/current/TutoUnityGUI.html)
  - We don't touch this in Writing3D

#### XR Interactable

The following functions are run when an `MVRActor` is clicked on

```cs
protected void OnMVRWandButtonPressed(MVRSelection iSelection) {}
protected void OnMVRWandButtonReleased(MVRSelection iSelection) {}
MVR.DeviceMgr.IsWandButtonPressed(iIndex); // Which button was pressed
```

Unity Events can be used but the event functions follow this syntax (`"MVR Wand Button (Int32, Boolean)"`):

```c#
public void MyWandButtonReaction(int iButton, bool iPressed)
{
    if (iButton == 0 && iPressed == true) { Debug.Log("Button 0 pressed!"); }
}
```

- Button 0 fires the `Activate` events from the XR Interactable script
- Button 1 fires the `Select` events from the XR Interactable script
- _Is there a way to call the Link Manager events from the `Actor` script?_

#### XR Grabbable

The following functions are run when the wand collides with an `MVRActor`

```cs
protected void OnMVRWandEnter(MVRSelection iSelection) {} // Wand starts colliding the actor
protected void OnMVRWandHover(MVRSelection iSelection) {} // Each frame wand is inside actor
protected void OnMVRWandExit(MVRSelection iSelection) {} // Wand stops colliding the actor
```

Again, Unity Events can be used following this syntax (`"MVR Wand Touch (Boolean)"`):

```cs
public void MyWandTouchReaction(bool iTouched)
{
    if (iTouched) { Debug.Log("Started being touched by wand."); }
    else { Debug.Log("Stopped being touched by wand."); }
}
```

#### Programming Interactions

More scripting information can be found on MiddleVR's documentation: [Programming Interactions](https://www.middlevr.com/2/doc/current/UnityVRInteractions.html#programming-interactions)

## Build Settings

**MVR Manager will be disabled if the standalone player is not pased a `--config` command line argument. This will let us build for both at the same time**

- **Need a script to enable all of the MVR scripts when MVR Manager is enabled**
  - This can be attached to the MVR Manager directly?
  - All of XR Origin will be disabled? Not sure if this is necessary

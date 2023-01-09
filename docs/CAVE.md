# Unity Setup for CAVE Deployment

## Writing3D Notes

- MiddleVR references themselves and their scripts as `MVR`
- Add MVR Interactable script whenever I add a LinkManager

## MiddleVR Nodes

### Head Node

The position of the player is controlled by the `HeadNode`. This is tracked using Motive and passed into MiddleVr In practice this is the position of the glasses. The trackers have a custom offset in Motive such that the tracked position is that of the user's eyes and not the tracker balls themselves.

### Hand Node

- MVR only uses one `HandNode` in the scene, this will be the right controller from XR Origin
- Add `"MVR Attach to Node"` to `XR Origin -> RightController -> XR Controller Right` to attach the prefab as the MVR wand
  - This should only be the model itself, the scripts will be different
  - **The controller will have to be rotated (0, 180, 0)**
- MiddleVR names the main controller being used the "Wand"

Our CAVE uses an ASUS EEE Stick as our wand. It's position is tracked in Motive just like the head node. The unit comes with a left and a right stick but we are currently only using the right controller in the CAVE. It has 5 buttons

0. This trigger button is the main button in MVR. Button 9 on the controller
   - This calls the `Activate/Deactivate` events from XRI, see [XR Interactable](#xr-interactable)
1. This is the secondary trigger button of the wand. Button 8 on the controller.
   - This calls the `Select/Deselect` events from XRI, see [XR Interactable](#xr-interactable)
2. The left button on the top of the controller - button 10
3. The right button on the top of the controller - button 101
4. Not in use
5. Not in use

## MVR Manager

- MVR Manager is the player's head position
- The z position needs to be offset to the back of the CAVE
  - `(0, 0, -1.2192)`
  - _XR is based on the `<Camera>`'s position. Should this be as well?_
  - To center for development: `(1.2192, 1.2192, -1.2192)`
- `"Editor Cluster Debugging Properties"` can be configured to run MiddleVR with play mode
  - Set `Enable Editor Cluster Debugging` to `true`
  - Set `Editor Cluster ID` to the cluster name (default `ClusterServer`)
  - Set `Start other cluster nodes` to true

### Template Camera

MVR Manager will apply a template camera to all of the cameras in the scene. This should be loosely based on `"Main Camera"` from XR right but certain properties are different.

- `Background`: This is the `<Background color="">` given by the XR project.
  - The alpha MUST be set to `0`
  - Default to black, `(0, 0, 0, 0)`
- `Clipping Planes`: {`near`: 0.3, `far`: 100}

### Settings

- Leave `"Attach to Camera"` as `false`, MVR creates a new head camera
- Leave `"Preview Window"` as `true`, displays cluster game view in separate window
- Use `MVR Camera` prefab as the `"Template Camera"` - same settings as `XR Rig -> Main Camera`
- I think it's safe to leave anything concerning the "Screen Proximity Warning" disabled as it's easy to see how close you are to the walls inside the CAVE
- The `"VR Root Node"` parameter of the `MVR Manager` will insert that root as the center of the VR object

### MVR Manager Questions

- _Can MVR Manager be placed as a child inside `XR Origin -> Camera Offset`?_
- _Can I offset MVR's `System Center` in the hierarchy by 1.36144?_
- _Does MVR use floor or head tracking? This will determine the y offset_

## Interactions

### Joystick Navigation

Player navigation will be done by the `"MVR Navigation Wand Joystick"` script. This enables joystick movement. This is the same as the XR Controller position/rotation movement.

- `Translation Speed`: Translation speed, in meters per second.
- `Rotation Speed`: Rotation speed, in degrees per second.
- `Fly`: Allow navigation up/down the y axis (**disable this**).

Note that Joystick Navigation doesn't make sense for Writing3D - the CAVE shouldn't move at all

### Manipulation

- `"MVR Interaction Manipulation Ray"` grabs an object via the wand's raycast
- The `"MVRActor"` script is attached to any Interactable object
  - `grabable` boolean for whether or not the object can be grabbed
- The wand can be configured for [Unity GUI interactions](https://www.middlevr.com/2/doc/current/TutoUnityGUI.html)
  - We don't touch this in Writing3D

#### XR Interactable

The following functions are run when an `MVRActor` is clicked on with the main button:

```cs
protected void OnMVRWandButtonPressed(MVRSelection iSelection) {}
protected void OnMVRWandButtonReleased(MVRSelection iSelection) {}
MVR.DeviceMgr.IsWandButtonPressed(iIndex); // Which button was pressed
```

**Unity Events can be used but the event functions follow this syntax:** (`MVR Wand Button(Int32, Boolean)`)

```c#
public void MyWandButtonReaction(int iButton, bool iPressed)
{
    if (iButton == 0 && iPressed == true) { Debug.Log("Button 0 pressed!"); }
}
```

- Button 0 fires the `Activate` events from the XR Interactable script
- Button 1 fires the `Select` events from the XR Interactable script
- `iPressed` is roughly equal to `onButtonDown` and `onButtonUp`
- _Is there a way to call the Link Manager events from the `Actor` script?_

#### XR Grabbable

The following functions are run when the wand collides with an `MVRActor`. (We don't use grabbable interactions in Writing3D)

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

### Programming Interactions

More scripting information can be found on MiddleVR's documentation: [Programming Interactions](https://www.middlevr.com/2/doc/current/UnityVRInteractions.html#programming-interactions)

## Build Settings

**MVR Manager will be disabled if the standalone player is not passed a `--config` command line argument. This will let us build for both at the same time**

- **Need a script to enable all of the MVR scripts when MVR Manager is enabled**
  - _This can be attached to the MVR Manager directly?_
  - _All of XR Origin will be disabled? Not sure if this is necessary_
- **Make sure to build with `Mono` Scripting backend in Unity 2021. Running into errors with MVR otherwise**

## Runtime

`MVR Manager` will be automatically be disabled if the scene is run without the `--config` flag (e.g. from the MiddleVR software) which opens the door to leave the `XR Rig` enabled at all times.

### Running in XR

- MVR Manager will be disabled
- How to handle scripts?

### Running in the CAVE

- Need to disable `XR Rig`
  - Especially true because the controllers will still be visible
  - _Can I attach the MVR Wand to the controller and use that model?_

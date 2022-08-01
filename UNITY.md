# CAVE Unity Project

## Unity Development

- The origin is the middle of all objects
- Nested objects will assume the local transform of the parent object
  - Position of the object itself is still in the parent's space
- UNITY USES METERS FOR UNITS (CAVE uses ft)
  - CAVE walls are 8' (96") squares -> 2.4384 meters
  - 1ft = 0.3048m, 1m = 3.28084ft

### Unity Starter Assets

- Base project uses the "VR Project" template project that Unity provides
- Delete the Skybox (`Lighting -> Environment -> Skybox Material`)
  - Set "Environment Lighting" to "Color"
  - Set "Ambient Color" to white (255, 255, 255)
- The starter DirectionalLight can be deleted
- The starter `XRRig` stays as a root object of the project. Keep defaults.
- The entire xml project lives inside the `Story` empty game object

### VR Settings

The Unity project settings and XRRig must be adjusted for VR to work:

- The "XR Plugin Management" package should be installed by virtue of the "VR Project" template. **Version 4.2.1**. In the "XR Plug-In Management" section of the Project Settings:
  - Add the "Oculus Touch Controller Profile" to the `OpenXR -> Interaction Profiles` list
    - *HTC, Microsoft, Valve, etc support can also be enabled here*
- The "XR Interaction toolkit" package must be added my name - `com.unity.xr.interaction.toolkit`. **Version 2.0.2**
  - Download the "Starter Assets" from the samples download. This downloads the needed presets for VR interaction.
    - I moved the starter assets to the `ExampleAssets/XR InteractionToolkit` folder
- Add the "XR Origin" script to the XRRig component
  - Set the base GameObject, floor offset, and Camera GameObject from the XRRig hierarchy
  - Set the "Camera Y Offset" of the tracking to 1.36144
  - Set the Requested Tracking Mode to "Floor"
  - *This may already be added*
- Add the "Input Action Manager" script to the XRRig component
  - Add the "XRI Default Input Actions" preset to the "Action Assets" list
    - Note that this is what maps the software actions to the different hardware buttons
- Add the "XR Controller (Action Based)" script to each controller
  - "XRI Default Left Controller" preset for the LeftController object
  - "XRI Default Right Controller" preset for the RightController object

Check out [this tutorial](https://www.youtube.com/watch?v=5ZBkEYUyBWQ) for more information on VR with Unity and the XR Interaction Toolkit.

**TODO**: How to do ray based interaction? (52)

### MiddleVR Settings

In addition to the Unity XRRig, a root MiddleVR package needs to be added in order for the project to work with MiddleVR and the CAVE.

*More info to come.*

### Changes and Conversions

- The entire project lives inside the `Story` empty game object
  - Scale is 0.3048 to covert feet to meters
  - Set Y to 1.2192 so floor sits at 0, 0, 0.
- The z axis is flipped for all objects (`W3D.Xml.ConvertVector3`)
  - I'm not sure why this is the case? Seems like it's supposed to be this way?

## Globals

`CLI.ApplyGlobalSettings` applies everything inside `<Story><Global>...` to the Unity project.

### Camera and CaveCamera

- The main camera is located within the XRRig hierarchy (`XRRig -> Camera Offset -> Main Camera`).
  - `<CameraPos></CameraPos><Placement>...` sets the transform of the XRRig directly.
  - The cameras have a "Clipping Planes" setting.
    - `<CameraPos far-clip="100.0">` sets the "far clip" value.
- `<CaveCameraPos>` adds a secondary camera to the scene, named `Cave Camera`.
  - Make sure this is NOT tagged as MainCamera.
  - Make sure it does NOT have an Audio Listener
  - This camera sits inside `Story` in the hierarchy
- Unity will display the camera with the highest "Depth" value
  - Set `Main Camera` depth to 1
  - Set `Cave Camera` depth to 0

### Background

The `<Background color>...` attribute sets the background color for BOTH `Main Camera` and `CaveCamera`. The Camera's background color adjusts the scene lighting when not using a Skybox

### Wand Navigation

- `<WandNavigation>` changes settings for the `Tracked Pose Driver` component of `Main Camera`
  - `allow-rotation`: Whether or not the player can rotate in the scene
  - `allow-movement`: Whether or not the player can move in the scene
- The tracking types in Unity are "Rotation And Position", "Rotation Only", and "Position Only"
  - R & P: `<WandNavigation allow-rotation="true" allow-movement="true" />`
  - R: `<WandNavigation allow-rotation="true" allow-movement="false" />`
  - P: `<WandNavigation allow-rotation="false" allow-movement="true" />`
  - If `<WandNavigation allow-rotation="false" allow-movement="false" />`, disable `Tracked Pose Driver` and set `XR Origin` (a script attached directly to XRRig) origin mode to "Device"

### Changes and Conversions (Global)

- Everything that updates XRRig must convert the xml (feet) to Unity (meters) because it's not inside the `Story`.

## PlacementRoot

### Placement

Each `<Placement>` in `PlacementRoot` is an empty GameObject. PlacementRoot is the same for all projects, see [minimuim.xml](examples/cweditor/minimum.xml):

```xml
<PlacementRoot>
    <Placement name="Center">
        <RelativeTo>Center</RelativeTo>
        <!-- Rotate 0 degrees around the y axis -->
        <Position>(0.0, 0.0, 0.0)</Position>
        <Axis rotation="(0.0, 1.0, 0.0)" angle="0.0"/>
    </Placement>
    <Placement name="FrontWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the y axis pointed upwards -->
        <!-- The object is in front of the origin. Note that Position is (0, 0, 4) in Unity.  -->
        <!-- <Axis rotation="(0.0, 1.0, 0.0)" angle="0.0" /> -->
        <Position>(0.0, 0.0, -4.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="LeftWall">
        <RelativeTo>Center</RelativeTo>
          <!-- Look at the origin with the y axis pointed upwards -->
          <!-- The object is to the left of the origin so it must rotate to do so -->
          <!-- <Axis rotation="(0.0, 1.0, 0.0)" angle="270.0" /> -->
        <Position>(-4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="RightWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the y axis pointed upwards -->
        <!-- The object is to the right of the origin so it must rotate to do so -->
        <!-- <Axis rotation="(0.0, 0.0, 0.0)" angle="90.0" /> -->
        <Position>(4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="FloorWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the z axis pointed upwards -->
        <!-- The object is below the origin so it must rotate to do so. Note that by rotating over the X axis the Z axis now points downward. -->
        <!-- <Axis rotation="(1.0, 0.0, 0.0)" angle="90.0" /> -->
        <Position>(0.0, -4.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 0.0, -1.0)"/>
    </Placement>
</PlacementRoot>
```

- `RelativeTo`: Which wall inside `PlacementRoot` the object is a child of in the hierarchy  
  - Objects that are `<RelativeTo>Center</RelativeTo>` are children of `Story`.
- `Position`: Local Position
- [Axis || LookAt || Normal]
  - `Axis`: The objects rotation around a specified axis
    - `rotation`: The axis around which the rotation takes place
    - `angle`: The rotation angle of the object, in degrees
  - `LookAt`: Object is rotated to look at a specified point (in `Story` space)
    - `target`: The position the object is looking at
    - `up`: Which direction (world space) is considered up (+y)
  - `Normal`: *Same as LookAt but with a normalized vector?*
    - `normal`: A normalized vector
    - `angle`: The rotation angle of the object, in degrees

### Changes and Conversions (Placement)

- The entire project lives inside the `Story` empty game object
  - Scale is 0.3048 to covert feet to meters
  - Set Y to 1.2192 so floor sits at 0, 0, 0.
- Each wall is an empty game object
  - Set position and rotation for project specific `RelativeTo` placements later on
- The z axis is flipped for the front wall (+4 not -4)
- We need to convert `LookAt` and `Normal` from world space to local rotation - essentially making everything an `Axis` object.
  - Converting an `Axis` tag to Unity: `Axis.Rotation * Axis.Angle`
  - *See the comments in the XML above*

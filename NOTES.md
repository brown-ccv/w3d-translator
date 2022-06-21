# W3D Translator Notes

I want to jot down a bunch of notes regarding the XML and what they'll look like in Unity.

## Unity Development

- The origin is the middle of all objects
- Nested objects will assume the local transform of the parent object

## PlacementRoot

Each `<Placement>` in `PlacementRoot` is a Plane. Note that a scale(1,1,1) plane translates to =/- position(5, 5, 5). PlacementRoot should be the same for all projects:

```xml
<PlacementRoot>
    <Placement name="Center">
        <RelativeTo>Center</RelativeTo>
        <Position>(0.0, 0.0, 0.0)</Position>
            <Axis rotation="(0.0, 1.0, 0.0)" angle="0.0"/>
    </Placement>
    <Placement name="FrontWall">
        <RelativeTo>Center</RelativeTo>
        <Position>(0.0, 0.0, -4.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="LeftWall">
        <RelativeTo>Center</RelativeTo>
        <Position>(-4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="RightWall">
        <RelativeTo>Center</RelativeTo>
        <Position>(4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="FloorWall">
        <RelativeTo>Center</RelativeTo>
        <Position>(0.0, -4.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 0.0, -1.0)"/>
    </Placement>
</PlacementRoot>
```

### Placement

- `RelativeTo`: Which Placement inside `PlacementRoot` the object is a child of
- `Position`: Origin of the object
- [Axis || LookAt || Normal]
  - `Axis`: Optional, the objects rotation around an axis
    - `rotation`: The x/y/z rotation of the object
    - `angle`: The rotation angle of the object, in degrees
    - **unity = Vec(rotation) * angle**
  - `LookAt`: Optional, applies rotation to the object
    - `target`: The direction the Placement is rotated to look at. (World Position)
    - `up`: Which direction in world space is considered up
  - `Normal`: Optional, same as LookAt but with a normalized vector.
    - `normal`: A normalized vector
    - `angle`: The rotation angle of the object, in degrees

#### Conversions

- I believe we need to flip all of the z axis to match. (?)
- We need to convert `LookAt` and `Normal` from world space to local rotation - essentially making everything an `Axis` object.


Example:

```xml
<PlacementRoot>
    <Placement name="Center">
        <RelativeTo>Center</RelativeTo>
        <Position>(0.0, 0.0, 0.0)</Position>
        <!-- Rotate 0 degrees around the y axis -->
        <Axis rotation="(0.0, 1.0, 0.0)" angle="0.0" />
    </Placement>
    <Placement name="FrontWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the y axis pointed upwards -->
        <!-- The object is in front of the origin so it must rotate to do so -->
        <!-- <Axis rotation="(1.0, 0.0, 0.0)" angle="90.0" /> -->
        <Position>(0.0, 0.0, -4.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)" />
    </Placement>
            <Placement name="LeftWall">
            <RelativeTo>Center</RelativeTo>
            <!-- Look at the origin with the y axis pointed upwards -->
            <!-- The object is to the left of the origin so it must rotate to do so -->
            <!-- <Axis rotation="(1.0, 0.0, 0.0)" angle="90.0" /> -->
            <Position>(-4.0, 0.0, 0.0)</Position>
            <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)" />
        </Placement>
</PlacementRoot>
```

## SoundRoot

- "Play on Wake" should be turned off for all sounds


## Globals

Background color will be controlled by the lighting (Skybox Material)

## Camera and XRRig

The XRRig is what instantiates the player in VR. It is the basis for `CaveCamera`.

- The "Requested Tracking Mode" of the CameraOffset script should be set to "Floor"
- 
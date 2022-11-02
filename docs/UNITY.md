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
- An `EventSystem` object must be added to the scene - use `XR -> UI EventSystem`
  - This will add `XR UI Input Module` script, make sure it's present
  - The object can be left in the root of the hierarchy, preferably at the bottom of the list

### VR Settings

The Unity project settings and XRRig must be adjusted for VR to work:

- The "XR Plugin Management" package should be installed by virtue of the "VR Project" template. **Version 4.2.1**. In the "XR Plug-In Management" section of the Project Settings:
  - Add the "Oculus Touch Controller Profile" to the `OpenXR -> Interaction Profiles` list
    - _HTC, Microsoft, Valve, etc support can also be enabled here_
- The "XR Interaction toolkit" package must be added by name - `com.unity.xr.interaction.toolkit`. **Version 2.0.2**
  - Download the "Starter Assets" from the samples download. This downloads the needed presets for VR interaction.
    - I moved the starter assets to the `ExampleAssets/XR InteractionToolkit` folder
- Add the "XR Origin" script to the `XRRig` component
  - Set the base GameObject, floor offset, and Camera GameObject from the XRRig hierarchy
  - Set the "Camera Y Offset" of the tracking to 1.36144
  - Set the Requested Tracking Mode to "Floor"
  - _This may be added by default but be sure the settings are adjusted correctly_
- Add the "Input Action Manager" script to the `XRRig` component
  - Add the "XRI Default Input Actions" preset to the "Action Assets" list
    - Note that this is what maps the software actions to the different hardware buttons
- Add the "XR Interaction Manager" script to the `XRRig` component
- Add the "XR Controller (Action Based)" script to each controller
  - "XRI Default Left Controller" preset for the `LeftController` object
  - "XRI Default Right Controller" preset for the `RightController` object
  - Add the "XR Ray Interactor" script to `RightController`
    - This will automatically add the "LineRenderer" component and "XR Interactor Line Visual" script to `RightController`
    - The color/style of the ray can be changed here

Check out [this tutorial](https://www.youtube.com/watch?v=5ZBkEYUyBWQ) for more information on VR with Unity and the XR Interaction Toolkit.

### MiddleVR Settings

In addition to the Unity XRRig, a root MiddleVR package needs to be added in order for the project to work with MiddleVR and the CAVE.

_More info to come._

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
  - `<CameraPos><Placement>...</CameraPos>` sets the transform of the XRRig directly.
    - Everything that updates XRRig must convert the xml (feet) to Unity (meters) because it's not inside the `Story`.
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

## Placement

Each `<Placement>` inside `PlacementRoot` is a reference point for the `<RelativeTo>` child. They are empty GameObjects in Unity, nested under story and moved to the correct position/rotation. PlacementRoot is the same for all projects (see [minimuim.xml](examples/cweditor/minimum.xml)):

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
        <!-- The object is in front of the origin (z axis flipped) -->
        <Position>(0.0, 0.0, -4.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="LeftWall">
        <RelativeTo>Center</RelativeTo>
          <!-- Look at the origin with the y axis pointed upwards -->
          <!-- The object is to the left of the origin so it must rotate to do so -->
        <Position>(-4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="RightWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the y axis pointed upwards -->
        <!-- The object is to the right of the origin so it must rotate to do so -->
        <Position>(4.0, 0.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
    </Placement>
    <Placement name="FloorWall">
        <RelativeTo>Center</RelativeTo>
        <!-- Look at the origin with the z axis pointed upwards -->
        <!-- The object is below the origin so it must rotate to do so. Note that the Z axis points downward as a result of the rotation. -->
        <Position>(0.0, -4.0, 0.0)</Position>
        <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 0.0, -1.0)"/>
    </Placement>
</PlacementRoot>
```

- `RelativeTo`: Which wall inside `PlacementRoot` the object is a child of in the hierarchy
  - Objects that are `<RelativeTo>Center</RelativeTo>` are children of `Story`.
- `<Position>`: The local position of the object
- Rotation is an `<xs:choice>` (Axis, LookAt, Normal)
  - `<Axis>`: The objects rotation around a specified axis
    - `rotation`: The axis around which the rotation takes place
    - `angle`: The rotation angle of the object, in degrees
  - `<LookAt>`: Object is rotated to look at a specified point (in `Story` space)
    - `target`: The position the object is looking at
    - `up`: Which direction (world space) is considered up (+y)
  - `<Normal>`: **(TODO [#63](https://github.com/brown-ccv/w3d-translator/issues/63))**: _Same as LookAt but with a normalized vector?_
    - `normal`: A normalized vector
    - `angle`: The rotation angle of the object, in degrees
  - Every rotation in Unity can be thought of as an `<Axis>` type

### Changes and Conversions (Placement)

- `<Axis>` is calculated by creating a Eular angle (`rotation * axis`)
- `<LookAt>` is calculated by generating a direction vector (`<Position> - target`)
  - Note that `target` must be converted to world space before calculating the direction vector
  - Unity has a built in `LookRotation()` function that takes the direction vector and `up`
- `Normal` is calculated by **TODO: [63](https://github.com/brown-ccv/w3d-translator/issues/63)**

## Object

Each `<Object>` inside `<ObjectRoot>` corresponds to a single GameObject in Unity. The `<Placement>` is set using `Placement.SetTransform`, see [above](#placement).

- `name`: gameObject.name
- `<Color>`: gameObject.[content].color
  - Exactly how the color is applied will change (e.g. this is DisabledColor for a link object)
- `<Visible>`: gameObject.active
- `<Lighting>`: TODO [(76)](https://github.com/brown-ccv/w3d-translator/issues/76)
- `<ClickThrough>`: gameObject[BoxCollider] (enable/disable attached component)
  - These are opposites - the component is disabled if ClickThrough is false
- `<AroundSelfAxis>`: TODO [(76)](https://github.com/brown-ccv/w3d-translator/issues/76)
- `<Scale>`: gameObject.localScale
  - `scale * Vector3(1, 1, 1)`
- `<Content>`: An `<xs:choice>` between several content types, [see below](#content)
- `<LinkRoot>`: Adds a `LinkManager` script to the gameObject [see below](#link)

### Content

`<Content>` always contains exactly one child, a choice between several different types of content. Each type corresponds (roughly) to a different GameObject type in Unity and is translated as such. Note that `<Content>` does NOT create a child object in Unity, it is attached to the GameObject created by `<Object>` directly.

#### None

`<Object>` is an empty GameObject. This is the default cause in the switch statement (`CLI.TranslateGameObjects`).

#### Text

Text in Unity is defined by `TextMeshPro`. Some properties are set for all `TextMeshPro` objects to closer match the text defined in the original project (font size, word wrapping and overflow settings, etc.)

- `<text>`: The string physically displayed on screen
- `horiz-align`: The horizontal alignment of `<text>` (TMPro.HorizontalAlignmentOptions)
- `vert-align`: The vertical alignment of `<text>` (TMPro.VerticalAlignmentOptions)
- `font`: A path to a font asset
  - Several "default" font materials have already been created in `Assets/Resources/Materials/Fonts`
  - `font` is a .ttf file, if the material hasn't been created the script attempts to create it
  - LiberationSans SDF (The default TextMeshPro font) is used as a fallback
- `depth`: The size of the text along the z axis

The vertex and material color (`.color` and `.faceColor`) of the TextMeshPro object are set using the parent `<Color>` tag.

#### Image

TODO [65](https://github.com/brown-ccv/w3d-translator/issues/65)

- `filename`: Path to the image file

#### StereoImage

TODO [66](https://github.com/brown-ccv/w3d-translator/issues/66)

- `left-image`: Path to the image file on the left side
- `right-image`: Path to the image file on the right side

#### Model

TODO [67](https://github.com/brown-ccv/w3d-translator/issues/67)

- `filename`: Path to the 3d object file
- `check-collisions`: Whether or not other objects can pass through
  - A Unity mesh is added over the object

#### Light

TODO [68](https://github.com/brown-ccv/w3d-translator/issues/68)

- The kind of light is an `<xs:choice>` (Point, Directional, Spot)
  - `Point`:
  - `Directional`:
  - `Spot`:
    - `angle`: What angle the spotlight is pointed at (based on the objects transform)
- `diffuse`:
- `specular`:
- `const_atten`:
- `lin_atten`:
- `quad_atten`:

#### ParticleSystem

TODO [69](https://github.com/brown-ccv/w3d-translator/issues/69)

- `max-particles`: The maximum number of particles that can be created
- `actions-name`:
- `particle-group`: Reference to a `ParticleActionList`
- `look-at-camera`: Whether or not the particles are pointed at the camera
- `sequential`: Whether or not the particles are created sequentially
- `speed`: How fast the particles move

### Link

`<LinkRoot>` contains exactly one child, `Link`. Adding the `<LinkRoot>` child to an object makes it interactable with the controller's raycast. This is done inside [LinkManager.cs](unity\CAVE\Assets\Resources\Scripts\LinkManager.cs) - the class inherits from `XRBaseInteractable` which handles the interaction with the controller.

- `<Enabled>`: LinkManager.Enabled, use EnabledColor or the object's original color
- `<RemainEnabled>`: If false, adds `DisableLink` action to the script
- `<EnabledColor>`: LinkManager.EnabledColor
- `<SelectedColor>`: LinkManager.ActiveColor
- `<Actions>`: An action to complete once triggered, see [below](#link-actions)

_Note that there can be multiple `<Actions>` per `<Link>`_

#### Other Methods

In addition to the available action types, there are a few methods in `LinkManager.cs` that provide runtime functionality:

- `EnableLink` sets the color to EnabledColor and enables LinkManger
- `DisableLink` sets the color to DisabledColor and disabled LinkManager
- `Activate` sets the color to ActiveColor and updates the script's click counter
- `Deactivate` sets the color back to `ActiveColor`

These functions are added to the Activate event (enable link, activate) or Deactivate event (deactivate), more information about the setup can be found in the [UnityEvents and UnityActions](#unityevents-and-unityactions) section.

## Actions

### UnityEvents and UnityActions

A [Unity Event](https://docs.unity3d.com/ScriptReference/Events.UnityEvent.html) and [Unity Action](https://docs.unity3d.com/ScriptReference/Events.UnityAction.html) are a common way to cause change during runtime in Unity. This is especially true for our purposes - clicking on and interacting with objects using a mouse or controller.

An event can be thought of as "a thing that occurs" and an action as "the things to do when an event occurs". A given event (a button is clicked, a scene is loaded, etc) can have _many_ actions that are executed when that event occurs. For example, the LinkManager script (see [Link](#link)) keeps track of many events, two of which we care about.

- `Activated`: Called when hovering over the object and the trigger is pressed (think "on trigger down")
- `Deactivated`: Called when the trigger is released after activation (think "on trigger up")

Each action added to these events consists of three parts - the referenced GameObject, the function to be called, and the parameter to that function. These listeners can be done in code but are added as persistent listeners so appear in the GUI for future users to see.

![Unity Actions](./Unity%20Action.png)

In this example the action is calling the `ObjectManager.VisibleTransition` function on the `frontlink` object with the parameter `(Visible)`. Because we are adding persistent listeners the parameters must be sent as a [Scriptable Object](https://docs.unity3d.com/Manual/class-ScriptableObject.html).

### Link Actions

Every [Link](#link) contains one or more Link Actions. Every `<LinkAction>` is translated into a scriptable object of the same name in Unity. These are added to the `Deactivated` event of the LinkManager script - this way pressing and holding the trigger just changes the objects color.

- The kind of Action is an `<xs:choice>` (See [Action Types](#action-types))
- `<Clicks>`: How the link is activated
  - Any: The button is activated every time it's clicked (`NumClicks = 1`)
  - Number: The button is activated based on `<NumClicks>`
  - `<NumClicks>`: `LinkAction.NumClicks`
    - `num_clicks`: `NumClicks`
    - `reset`: `Reset`

Every `LinkAction` consists of an `ActionEvent` onto which the Action is added. `LinkAction` is essentially a wrapper to make sure the inner action is only clicked after `NumClicks` has been reached.

![Link Action](./Link%20Action.png)

### Action Types

`ActionsType` is a `<xs:complexType>` used to change properties of the scene during runtime. Each different type is a different function in [Actions/](unity/CAVE/Assets/Resources/Scripts/Actions/) and every `<Action>` is one of the following types:

- `<ObjectChange>` changes a given `<Object>`
- `<GroupRef>` changes a given `<Group>`
- `<TimerChange>` changes a given `<Timeline>`
- `<SoundRef>` changes a given `<Sound>`
- `<Event>` changes a given `<EventTrigger>`
- `<MoveCave>` moves the entire `<Story>` to a new position
- `<Restart>` changes a given `<Object>`

### ObjectChange

`ObjectChange` will always reference a given `ObjectManager` script attached to an `<Object>`. The underlying transition is attached to the `LinkAction`'s `ActionEvent` directly.

- `<Transition>`: The underlying [Transition](#transitions) action to be applied
- `name`: The name of the referenced GameObject onto which the transition is applied

### GroupRef

TODO [87](https://github.com/brown-ccv/w3d-translator/issues/87)

### TimerChange

TODO [88](https://github.com/brown-ccv/w3d-translator/issues/88)

### SoundRef

TODO [89](https://github.com/brown-ccv/w3d-translator/issues/89)

### Event

TODO [90](https://github.com/brown-ccv/w3d-translator/issues/90)

### MoveCave

TODO [91](https://github.com/brown-ccv/w3d-translator/issues/91)

### Restart

TODO [92](https://github.com/brown-ccv/w3d-translator/issues/92)

### Transitions

Each transition is a Unity Action as described [above](#unityevents-and-unityactions). They are scriptable objects that alter a GameObject in some way.

- The kind of Action is an `<xs:choice>`
  - `<Visible>`: Fades the object int/out and sets `gameObject[Renderer].enabled`
  - `<Movement>`: Moves the object to a new [placement](#placement)
  - `<MoveRel>`: Moves the object by a [placement](#placement), relative to its current position
  - `<Color>`: Changes the color of the object
  - `<Scale>`: Changes the scale of the object
  - `<Sound>`: Plays or stops the sound attached to the object
    - `Play`
    - `Stop`
  - `<LinkChange>`: Manipulates the LinkManager script attached to the GameObject
    - `<link_on>`: `LinkManager.enabled = true`
    - `<link_off>`: `LinkManager.enabled = false`
    - `<activate>`: `LinkManager.enabled = true` and execute `Deactivated` event
    - `<activate_if_on>`: execute `Deactivated` event
- `duration`: How long it takes for the action to complete

# Unity Setup for VR Deployment

## Settings

The Unity project packages and settings must be adjusted for VR to work:

- `XR Plugin Management` package version **4.2.1**
- `XR Interaction Toolkit` package version **2.2.0**

1. Add the profile of your specific device in the "XR Plug-In Management" section of the Project Settings:
   - _Oculus Touch Controller Profile_
   - See [build settings](#build-settings) for Windows vs Android deployment. You must add the profile(s) for each deployment
2. Download the starter assets from the package manager
   - `Samples/XR Interaction Toolkit/2.2.0/Starter Assets`
   - `Samples/XR Interaction Toolkit/2.2.0/XR Device Simulator`
   - `Samples/XR Interaction Toolkit/2.2.0/Tunneling Vignette`
   - Sample Assets for `XR Plugin Management`, `OpenXR Plugin`, etc. can also be downloaded, but are not required.

### Build Settings

- The Windows build settings are used to build for connected deployment (e.g. SteamVR)
- The Android build settings are used for deployment directly on the headset

## Starter Assets

XR Interaction Toolkit comes with several starter assets and prefabs that can be used to build out the VR player used in the given scene.

1. Add the `Complete XR Origin Set Up` prefab to the root of the scene. _It's recommended to create a prefab variant so you can make changes to the origin without breaking the sample asset._
   - The `Input Action Manager` component should use the `XRI Default Input Actions` by default, but can be changed to map different software actions to the hardware input
   - The `Line Renderer` of the `Ray Interactor` component (`XR Origin -> [Left/Right]Hand ->`) can be adjusted to change the color/style of the ray can be changed here
2. `XR Device Simulator` can be used to simulate playing the game in VR with a keyboard and mouse. This is useful during development.

### Other assets

- `UI Sample`: Prefab of an example 2D menu in VR
- `Interactables Sample`: Prefab containing interactable objects in VR
- `Complete Teleport Area Set Up`: Prefab containing the teleport area components needed for teleport movement in VR
- The subfolders contain prefabs for the individual GameObjects used in the above prefabs
- `Models/XRControllerLeft` and `Models/XRControllerRight` contain the 3D models for the controllers used in the XR Origin
- `TunnelingVignette` creates a small vignette around the player's camera which can help with motion sickness in some applications.

The sample assets of the other XR packages (e.g. XR Plugin Management, OpenXR Plugin) can be used to create custom XR controllers and devices. The knowledge is out of scope for most VR projects but, for example, are used to create the controllers in the CAVE.

## Our Assets

TODO: Information about various starter assets we have created for VR use.

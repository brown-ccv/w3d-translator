# Unity Setup for VR Deployment

## Starter Assets

- The starter `XRRig` stays as a root object of the project. Keep defaults.

## Settings

The Unity project settings and XRRig must be adjusted for VR to work:

- The "XR Plugin Management" package should be installed by virtue of the "VR Project" template. **Version 4.2.1**. In the "XR Plug-In Management" section of the Project Settings:
  - Add the "Oculus Touch Controller Profile" to the `OpenXR -> Interaction Profiles` list
    - *HTC, Microsoft, Valve, etc support can also be enabled here*
- The "XR Interaction toolkit" package must be added by name - `com.unity.xr.interaction.toolkit`. **Version 2.0.2**
  - Download the "Starter Assets" from the samples download. This downloads the needed presets for VR interaction.
    - I moved the starter assets to the `ExampleAssets/XR InteractionToolkit` folder
- Add the "XR Origin" script to the `XRRig` component
  - Set the base GameObject, floor offset, and Camera GameObject from the XRRig hierarchy
  - Set the "Camera Y Offset" of the tracking to 1.36144
  - Set the Requested Tracking Mode to "Floor"
  - *This may be added by default but be sure the settings are adjusted correctly*
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

from generateDS.classes import Story


def clean_xml(story: Story) -> Story:
    # TODO: Loop over all over story instead of path then color then vector
    # TODO: Manage choice first? Utility function

    # Convert each path type to a Path
    # TODO: Object.Content.Image
    # TODO: Object.Content.StereoImage.left_image
    # TODO: Object.Content.StereoImage.right_image
    # TODO: Object.Content.Model
    # TODO: Sound.filename

    # Convert each color type to a tuple of integers, assert 0 <= [int] <= 255
    # TODO: Object.Color
    # TODO: Object.Link.EnabledColor
    # TODO: Object.Link.SelectedColor
    # TODO: ParticleAction.TargetColor.color
    # TODO: Global.Background.color
    # TODO: Timeline.TimedActions.GroupRef.Transition.Color
    # TODO: Timeline.TimedActions.ObjectChange.Transition.Color
    # TODO: EventTrigger.Actions.GroupRef.Transition.Color
    # TODO: EventTrigger.Actions.ObjectChange.Transition.Color
    # TODO: Object.LinkRoot.Link.Actions.ObjectChange.Transition.Color
        # I think LinkRoot will be an array?

    # Convert each vector type to a tuple of floats
    # TODO: EventTrigger.HeadTrack.Direction.PointTarget.point
    # TODO: EventTrigger.HeadTrack.Direction.DirectionTarget.direction
    # TODO: EventTrigger.HeadTrack.Position.Box.corner1
    # TODO: EventTrigger.HeadTrack.Position.Box.corner2
    # TODO: EventTrigger.MoveTrack.Box.corner1
    # TODO: EventTrigger.MoveTrack.Box.corner2
    # TODO: ParticleAction.Gravity.direction
    # TODO: ParticleAction.Damping.direction
    # TODO: ParticleAction.OrbitPoint.center
    # TODO: ParticleDomain.Point.point
    # TODO: ParticleDomain.Line.p1
    # TODO: ParticleDomain.Line.p2
    # TODO: ParticleDomain.Triangle.p1
    # TODO: ParticleDomain.Triangle.p2
    # TODO: ParticleDomain.Triangle.p3
    # TODO: ParticleDomain.Plane.point
    # TODO: ParticleDomain.Plane.normal
    # TODO: ParticleDomain.Rect.point
    # TODO: ParticleDomain.Rect.u-dir
    # TODO: ParticleDomain.Rect.v-dir
    # TODO: ParticleDomain.Box.p1
    # TODO: ParticleDomain.Box.p2
    # TODO: ParticleDomain.Sphere.center
    # TODO: ParticleDomain.Cylinder.p1
    # TODO: ParticleDomain.Cylinder.p2
    # TODO: ParticleDomain.Cone.base_center
    # TODO: ParticleDomain.Cone.apex
    # TODO: ParticleDomain.Blob.center
    # TODO: ParticleDomain.Disc.center
    # TODO: ParticleDomain.Disc.normal

    # Placement is used in PlacementRoot
    # Placement is used in Object
    # Placement is used in ActionsType.MoveCave (Note: multiple ActionsType)
    # Placement is used in Camera
    # Placement is used in Transition.Movement (note: multiple Transition)
        # ActionsType.ObjectChange
        # ActionsType.GroupRef
    # Placement is used in Transition.MoveRel (note: multiple Transition)
    # TODO: Placement.Position
    # TODO: Placement.Axis.rotation
    # TODO: Placement.LookAt.target
    # TODO: Placement.LookAt.up
    # TODO: Placement.Normal.normal

    # Convert each _Root property to a dictionary of that type
    if story.ObjectRoot is not None:
        story.ObjectRoot = name_dictionary(story.ObjectRoot.Object)
    if story.GroupRoot is not None:
        story.GroupRoot = name_dictionary(story.GroupRoot.Group)
    if story.TimelineRoot is not None:
        story.TimelineRoot = name_dictionary(story.TimelineRoot.Timeline)
    if story.PlacementRoot is not None:
        story.PlacementRoot = name_dictionary(story.PlacementRoot.Placement)
    if story.SoundRoot is not None:
        story.SoundRoot = name_dictionary(story.SoundRoot.Sound)
    if story.EventRoot is not None:
        story.EventRoot = name_dictionary(story.EventRoot.EventTrigger)
    if story.ParticleActionRoot is not None:
        story.ParticleActionRoot = name_dictionary(
            story.ParticleActionRoot.ParticleActionList
        )


def name_dictionary(container: list) -> dict:
    """Converts a list of classes into a dictionary
    { key: [class.name], val: [class] }
    """
    if container is not None:
        return dict((item.name, item) for item in container)

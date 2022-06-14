from generateDS.classes import Story


def clean_xml(Story: Story) -> Story:
    # Convert each _Root property to a dictionary of that type
    if Story.ObjectRoot is not None:
        Story.ObjectRoot = name_dictionary(Story.ObjectRoot.Object)
    if Story.GroupRoot is not None:
        Story.GroupRoot = name_dictionary(Story.GroupRoot.Group)
    if Story.TimelineRoot is not None:
        Story.TimelineRoot = name_dictionary(Story.TimelineRoot.Timeline)
    if Story.PlacementRoot is not None:
        Story.PlacementRoot = name_dictionary(Story.PlacementRoot.Placement)
    if Story.SoundRoot is not None:
        Story.SoundRoot = name_dictionary(Story.SoundRoot.Sound)
    if Story.EventRoot is not None:
        Story.EventRoot = name_dictionary(Story.EventRoot.EventTrigger)
    if Story.ParticleActionRoot is not None:
        Story.ParticleActionRoot = name_dictionary(
            Story.ParticleActionRoot.ParticleActionList
        )

    return Story


def name_dictionary(container: list) -> dict:
    """Converts a list of classes into a dictionary
    key: class.name
    val: class
    """
    if container is not None:
        return dict((item.name, item) for item in container)

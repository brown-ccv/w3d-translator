from generateDS.classes import Story


def clean_xml(story: Story) -> Story:
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

    # Convert each color type to a tuple of integers and assert 0 <= [int] <= 255
    # TODO:
    # Convert each vector type to a tuple of floats

    # Convert each path type to a Path


def name_dictionary(container: list) -> dict:
    """Converts a list of classes into a dictionary
    key: class.name
    val: class
    """
    if container is not None:
        return dict((item.name, item) for item in container)

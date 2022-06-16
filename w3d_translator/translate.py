import generateDS.classes as classes


def clean_xml(story: classes.Story) -> classes.Story:
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


def get_choice(obj, options=None):
    """Loop over options, returning the class property that is not None"""

    # Use all members if custom list isn't given
    if options is None:
        options = obj.member_data_items_
    for member in options:
        temp = getattr(obj, member.get_name())
        if temp is not None:
            return temp


def set_choice(obj, value, options=None):
    """Loop over options, updating the property that is not None"""

    # Use all members if custom list isn't given
    if options is None:
        options = obj.member_data_items_
    for member in options:
        if getattr(obj, member.get_name()) is not None:
            setattr(obj, member.get_name(), value)


def print_member_names(obj):
    """Helper function to print xml class properties"""
    names = list(map(lambda x: x.get_name(), obj.member_data_items_))
    print(names)

import re
from pathlib import Path
from typing import Union

from generateDS.classes import Story


def clean_xml(Story: Story):
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
    print(Story.TimelineRoot)

    return Story


def name_dictionary(container: list) -> dict:
    """ Converts a list of classes into a dictionary
        key: class.name
        val: class
    """
    if container is not None:
        return dict((item.name, item) for item in container)


# TODO: Regex validation should be done in the schema directly
def parse_string(string: str) -> Union[tuple, Path]:
    """Parses the variable type of a given string

    Args:
        string (str): Input string

    Returns:
        Union[bool, int, float, tuple, Path, str]: Data parsed as correct type

    # Test tuple of integers
    >>> parse_string('(1, 2, 3)')
    (1, 2, 3)
    >>> parse_string('(12, 2, -1)')
    (12, 2, -1)

    # Test tuple of floats
    >>> parse_string('(1.1, 2.2, 3.3)')
    (1.1, 2.2, 3.3)
    >>> parse_string('(13.5, 2.5, -1.5)')
    (13.5, 2.5, -1.5)

    # Test Paths
    >>> isinstance(parse_string('/folder/file.xml'), Path)
    True
    >>> isinstance(parse_string('./folder/file.xml'), Path)
    True
    >>> isinstance(parse_string('../folder/file.xml'), Path)
    True
    >>> isinstance(parse_string('/folder/.'), Path)
    True
    >>> isinstance(parse_string('/folder/'), Path)
    True
    >>> isinstance(parse_string('/folder'), Path)
    True

    # TODO 27, 28
    # >>> parse_string('(cat, dog, pigeon)') # Tuple of strings
    # '(cat, dog, pigeon)'
    # >>> parse_string('(13.0, 2., -1.)') # Floats without trailing 0
    # (13.0, 2.0, -1.0)
    # >>> p7 = parse_string('folder/file.xml')
    # >>> isinstance(p7, Path), p7.parts
    # (True, ('folder', 'file.xml'))
    """
    string = string.strip()

    # Check if string is a tuple (of integers or floats)
    if re.match(
        r"\(?\s*-?(\d+)\s*,\s*-?(\d+)\s*,\s*-?(\d+)?\)?",
        string,
    ):
        # Match "[int], [int], [int]" or "[int],[int],[int]"
        # or "([int], [int], [int])"  or "([int],[int],[int])"
        string = string.strip("()").split(",")
        return tuple(int(x) for x in string)
    elif re.match(
        r"\(?\s*-?(\d+(\.\d+))\s*,\s*-?(\d+(\.\d+))\s*,\s*-?(\d+(\.\d+))?\)?",
        string,
    ):
        # Match "[float], [float], [float]" or "[float],[float],[float]"
        # or "([float], [float], [float])" or "([float],[float],[float])"
        string = string.strip("()").split(",")
        return tuple(float(x) for x in string)

    # Check if string is a path
    if re.match(r"^(.+)?\/([^\/]+)", string):
        # Match "/" or "./" or "../" at the beginning of the string
        return Path(string)

    # Plain text
    return string

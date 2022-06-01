import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union

import generateDS.classes as generateDS


def read_xml(file):
    Story = generateDS.parse(file, silence=True)

    # Bring each list child up a level in the class
    # TODO: Dictionary of class referenced by name, not list
    if Story.Objects is not None:
        Story.Objects = Story.Objects.Object
    if Story.Groups is not None:
        Story.Groups = Story.Groups.Group
    if Story.Timelines is not None:
        Story.Timelines = Story.Timelines.Timeline
    if Story.Placements is not None:
        Story.Placements = Story.Placements.Placement
    if Story.Sounds is not None:
        Story.Sounds = Story.Sounds.Sound

    if Story.Events is not None:
        Story.Events = Story.Events.Event
    if Story.ParticleActions is not None:
        Story.ParticleActions = Story.ParticleActions.ParticleActionList

    #! OLD
    # # Parse each <PlacementRoot>, each <Placement> is referenced by name
    # story["walls"] = dict(
    #     (tag.attrib.pop("name"), parse_recursive(tag))
    #     for tag in root.find("PlacementRoot")
    # )
    return Story


def parse_string(string: str) -> Union[bool, int, float, tuple, Path, str]:
    """Parses the variable type of a given string

    Args:
        string (str): Input string

    Returns:
        Union[bool, int, float, tuple, Path, str]: Data parsed as correct type

    # Test boolean
    >>> parse_string('True')
    True
    >>> parse_string('TRUE')
    True
    >>> parse_string('false')
    False
    >>> parse_string('FaLSe') # Bad capitalization passes
    False

    # Test integer
    >>> parse_string('123')
    123
    >>> parse_string('-123')
    -123

    # Test float
    >>> parse_string('123.4')
    123.4
    >>> parse_string('-123.4')
    -123.4
    >>> parse_string('b123.4') # Invalid, return string
    'b123.4'

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

    # Test strings
    # >> parse_string('Center') # String
    # 'Center'
    # >>> parse_string('12a3') # String with numbers
    # '12a3'
    # >>> parse_string('(12, 2.0, 1)') # Tuple of mixed types
    # '(12, 2.0, 1)'
    # >>> parse_string('(1,)') # Tuple with one element
    # '(1,)'

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

    # Check if string is a boolean
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False

    # Check if string is an integer
    try:
        return int(string)
    except Exception:
        pass

    # Check if string is a float
    try:
        return float(string)
    except Exception:
        pass

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


def parse_attributes(xml: ET.Element) -> dict:
    return dict(
        # Use snake_case when val is not a dict
        (key.replace("-", "_"), parse_string(value))
        for key, value in xml.attrib.items()
    )


def parse_recursive(xml: ET.Element) -> dict:
    key = xml.tag
    val = parse_attributes(xml)
    title_to_snake = re.compile(r"(?<!^)(?=[A-Z])")

    if val or xml.find("*") is not None:
        for child in xml:
            val = val | parse_recursive(child)

        # Only add text property if it isn't empty
        text = parse_string(xml.text) if xml.text is not None else None
        if text:
            val["text"] = text
    else:
        # Use snake_case when val is not a dict
        return {title_to_snake.sub("_", key).lower(): parse_string(xml.text)}
    return {key: val}

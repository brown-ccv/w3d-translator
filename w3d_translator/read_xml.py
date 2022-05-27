import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()
    story = parse_attributes(root)

    # Parse <Globals>
    g = root.find("Global")
    story["Camera"] = parse_recursive(g.find("CameraPos"))
    story["CaveCamera"] = parse_recursive(g.find("CaveCameraPos"))
    story["background_color"] = parse_attributes(g.find("Background"))["color"]
    story["WandNavigation"] = parse_recursive(g.find("WandNavigation"))

    # Parse <PlacementRoot>
    story["walls"] = dict(
        (tag.attrib.pop("name"), parse_recursive(tag))
        for tag in root.find("PlacementRoot")
    )

    # TODO: Build each <Sound> in <SoundRoot> (10)
    # Parse <SoundRoot>
    story["sounds"] = dict(
        (tag.attrib.pop("name"), parse_sound(tag))
        for tag in root.find("SoundRoot")
    )

    # TODO: Build each <Object> in <ObjectRoot> (6)
    # TODO: Build each <Group> in <GroupRoot> (7)

    # TODO: Build each <ParticleActionList> in <ParticleActionRoot> (11)
    # TODO: Build each <Timeline> in <TimelineRoot> (8)
    return story


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


def parse_child_one_of_type(xml: ET.Element, options: dict):
    try:
        return options[xml.find("*").tag]
    except KeyError:
        return None


def parse_sound(xml: ET.Element) -> dict:
    sound = parse_attributes(xml)

    # Bring <Settings> up a level
    sound = sound | parse_attributes(xml.find("Settings"))

    # Parse <Mode> types
    modes = {"Fixed": True, "Positional": False}
    mode = xml.find("Mode")
    if mode is not None:
        sound["fixed"] = parse_child_one_of_type(mode, modes)

    # Parse <Repeat> types
    mapping = {"Repeat": True, "NoRepeat": False}
    repeat = xml.find("Repeat")
    if repeat is not None:
        sound["repeat"] = parse_child_one_of_type(repeat, mapping)

    return sound

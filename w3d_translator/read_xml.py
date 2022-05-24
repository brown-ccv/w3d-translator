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

    # Parse each <PlacementRoot>, each <Placement> is referenced by name
    story["walls"] = dict(
        (tag.attrib.pop("name"), parse_recursive(tag))
        for tag in root.find("PlacementRoot")
    )

    # TODO: Build each <Object> in <ObjectRoot> (6)
    # TODO: Build each <Group> in <GroupRoot> (7)

    # TODO: Build each <Sound> in <SoundRoot> (10)
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
    >>> p1 = parse_string('/folder/file.xml')
    >>> isinstance(p1, Path), p1.parts
    (True, ('/', 'folder', 'file.xml'))
    >>> p2 = parse_string('./folder/file.xml')
    >>> isinstance(p2, Path), p2.parts
    (True, ('folder', 'file.xml'))
    >>> p3 = parse_string('../folder/file.xml')
    >>> isinstance(p3, Path), p3.parts
    (True, ('..', 'folder', 'file.xml'))
    >>> p4 = parse_string('/folder/.')
    >>> isinstance(p4, Path), p4.parts
    (True, ('/', 'folder'))
    >>> p5 = parse_string('/folder/') # TODO: This is failing
    >>> isinstance(p5, Path), p5.parts
    (True, ('/', 'folder'))
    >>> p6 = parse_string('/folder')
    >>> isinstance(p6, Path), p6.parts
    (True, ('/', 'folder'))
    >>> p7 = parse_string('folder/file.xml') #TODO: 28
    >>> isinstance(p7, Path), p7.parts
    (True, ('folder', 'file.xml'))

    >>> parse_string('/folder/file.xml')
    WindowsPath('/folder/file.xml')
    >>> parse_string('./folder/file.xml')
    WindowsPath('folder/file.xml')
    >>> parse_string('../folder/file.xml')
    WindowsPath('../folder/file.xml')
    >>> parse_string('/folder/.')
    WindowsPath('/folder')
    >>> parse_string('/folder/')
    WindowsPath('/folder')
    >>> parse_string('/folder')
    WindowsPath('/folder')

    # Test invalid strings
    # >> parse_string('Center')
    # 'Center'
    # >>> parse_string('12a3')
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
    # >>> parse_string('folder/file.xml') # Path without starting /
    # WindowsPath('folder/file.xml')
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

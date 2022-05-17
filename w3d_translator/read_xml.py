import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()

    story = parse_attributes(root)

    # Parse <Globals>
    story = story | parse_recursive(root.find("Global"))

    # Parse each Placement in PlacementRoot by name
    story["walls"] = dict(
        (tag.attrib["name"], parse_recursive(tag))
        for tag in root.find("PlacementRoot")
    )

    # TODO: Build each <Object> in <ObjectRoot> (6)
    # TODO: Build each <Group> in <GroupRoot> (7)
    # TODO: Build each <Timeline> in <TimelineRoot> (8)
    # TODO: Build each <Sound> in <SoundRoot> (10)
    # TODO: Build each <ParticleActionList> in <ParticleActionRoot> (11)

    # Rename and/or re-arrange select properties
    story["camera"] = story.pop("CameraPos")
    story["cave_camera"] = story.pop("CaveCameraPos")
    story["background_color"] = story.pop("Background")["color"]

    # TODO: pop all text keys with value of '' or None

    return story


def parse_string(string: str) -> Union[bool, int, float, tuple, Path, str]:
    string = string.strip()

    # Check if string is a boolean
    if re.match(r"^\s*(?i)(true)\s*$", string):
        return True
    elif re.match(r"^\s*(?i)(false)\s*$", string):
        return False

    # Check if string is an integer
    if re.match(r"^\s*-?(\d+)\s*$", string):
        return int(string)

    # Check if string is a float
    if re.match(r"^\s*-?(\d+(\.\d+))\s*$", string):
        return float(string)

    # Check if string is a tuple (of integers or floats)
    if re.match(
        r"\(?\s*-?(\d)\s*,\s*-?(\d)\s*,\s*-?(\d)?\)?",
        string,
    ):
        string = string.strip("()").split(",")
        return tuple(int(x) for x in string)
    elif re.match(
        r"\(?\s*-?(\d+(\.\d+))\s*,\s*-?(\d+(\.\d+))\s*,\s*-?(\d+(\.\d+))?\)?",
        string,
    ):
        string = string.strip("()").split(",")
        return tuple(float(x) for x in string)

    # Check if string is a path
    if re.match(r"^[.\/]", string):
        return Path(string)

    # Plain text
    return string


def parse_attributes(xml: ET.Element) -> dict:
    attributes = xml.attrib
    for key, value in attributes.items():
        attributes[key] = parse_string(value)
    return attributes


def parse_recursive(xml: ET.Element) -> dict:
    out = parse_attributes(xml)
    if out or xml.find("*") is not None:
        out["text"] = parse_string(xml.text) if xml.text is not None else None
        out = out | dict((child.tag, parse_recursive(child)) for child in xml)
    else:
        return parse_string(xml.text)

    return out

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
        if text != "" and text is not None:
            val["text"] = text
    else:
        # Use snake_case when val is not a dict
        return {title_to_snake.sub("_", key).lower(): parse_string(xml.text)}
    return {key: val}

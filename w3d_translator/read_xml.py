import xml.etree.ElementTree as ET
from typing import Union


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()

    story = parse_attributes(root)

    # Parse <Globals>
    g = root.find("Global")
    story["Camera"] = parse_camera(g.find("CameraPos"))
    story["CaveCamera"] = parse_camera(g.find("CaveCameraPos"))
    story["background_color"] = parse_attributes(g.find("Background"))["color"]
    story["WandNavigation"] = parse_attributes(g.find("WandNavigation"))

    # Parse each Placement in PlacementRoot by name
    story["walls"] = dict(
        (parse_attributes(tag)["name"], parse_placement(tag))
        for tag in root.find("PlacementRoot")
    )

    # TODO: Build each <Object> in <ObjectRoot> (6)
    # object_root = {}
    for tag in root.find("ObjectRoot") or []:
        pass  # Dict of objects by name

    # TODO: Build each <Group> in <GroupRoot> (7)
    # group_root = {}
    for tag in root.find("GroupRoot") or []:
        pass  # Dict of groups by name (group -> array of object names)

    # TODO: Build each <Timeline> in <TimelineRoot> (8)
    # timeline_root = {}
    for tag in root.find("TimelineRoot") or []:
        pass  # Dict of Timeline by name

    # TODO: Build each <Sound> in <SoundRoot> (10)
    # sound_root = {}
    for tag in root.find("SoundRoot") or []:
        pass  # Dict of Sound by name

    # TODO: Build each <ParticleActionList> in <ParticleActionRoot> (11)
    # particle_action_root = {}
    for tag in root.find("ParticleActionRoot") or []:
        pass  # Dict of ParticleActionList by name

    return story


def parse_string(string: str) -> Union[bool, int, float, tuple, str]:
    # Check if string is a boolean
    try:
        test = string.lower()
        if test == "true":
            return True
        elif test == "false":
            return False
    except AttributeError:
        pass

    # Check if string is an integer
    try:
        return int(string)
    except ValueError:
        pass

    # Check if string is a float
    try:
        return float(string)
    except ValueError:
        pass

    # Check if string is a tuple (of integers or floats)
    test = string.replace("(", "").replace(")", "").split(",")
    try:
        return tuple([int(x) for x in test])
    except ValueError:
        pass
    try:
        return tuple([float(x) for x in test])
    except ValueError:
        pass

    # Plain text
    return string


def parse_attributes(xml: ET.Element) -> dict:
    attributes = xml.attrib
    for key, value in attributes.items():
        attributes[key] = parse_string(value)
    return attributes


def parse_text(xml: ET.Element) -> Union[bool, int, float, tuple, str]:
    return parse_string(xml.text)


def parse_camera(xml: ET.Element) -> dict:
    return {
        **parse_attributes(xml),
        "Placement": parse_placement(xml.find("Placement")),
    }


def parse_placement(xml: ET.Element) -> dict:
    return {
        "RelativeTo": parse_text(xml.find("RelativeTo")),
        "Position": parse_text(xml.find("Position")),
        "Axis": (
            parse_attributes(xml.find("Axis"))
            if xml.find("Axis") is not None
            else None
        ),
        "LookAt": (
            parse_attributes(xml.find("LookAt"))
            if xml.find("LookAt") is not None
            else None
        ),
    }

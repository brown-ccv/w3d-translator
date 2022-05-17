from typing import Union
import xml.etree.ElementTree as ET
from pathlib import Path

from utils import str_to_tuple, tf_to_bool


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()
    story = {
        "version": int(root.attrib["version"]),
        "last_xpath": Path(root.attrib["last_xpath"]),
    }

    # Globals
    g = root.find("Global")
    story["Camera"] = parse_camera(g.find("CameraPos"))
    # story["CaveCamera"] = parse_camera(g.find("CaveCameraPos"))
    # story["background"] = str_to_tuple(g.find("Background").attrib["color"])
    # story["wand_navigation"] = parse_wand_navigation(g.find("WandNavigation"))

    story["walls"] = parse_placements(root.find("PlacementRoot"))
    # print(story)

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


def parse_attribs(atrtibutes: dict) -> dict:
    pass


def parse_string(string: str) -> Union[str, float, tuple, dict]:
    pass


def parse_camera(xml: ET.Element) -> dict:
    ET.dump(xml)
    return {
        "far_clip": float(xml.attrib["far-clip"]),
        "placement": parse_placement(xml.find("Placement")),
    }


def parse_placement(xml: ET.Element) -> dict:
    placement = {
        "relative_to": xml.find("RelativeTo").text,
        "position": str_to_tuple(xml.find("Position").text),
        "axis": None,
        "look_at": None,
    }

    axis_xml = xml.find("Axis")
    if axis_xml is not None:
        placement["axis"] = {
            "rotation": str_to_tuple(axis_xml.attrib["rotation"]),
            "angle": float(axis_xml.attrib["angle"]),
        }

    look_at_xml = xml.find("LookAt")
    if look_at_xml is not None:
        placement["look_at"] = {
            "target": str_to_tuple(look_at_xml.attrib["target"]),
            "up": str_to_tuple(look_at_xml.attrib["up"]),
        }

    return placement


def parse_wand_navigation(xml: ET.Element) -> dict:
    return {
        "allow_rotation": tf_to_bool(xml.attrib["allow-rotation"]),
        "allow_movement": tf_to_bool(xml.attrib["allow-movement"]),
    }


def parse_placements(xml: ET.Element) -> dict:
    walls = {}
    # TODO: Build each <Placement> in <PlacementRoot> (9)
    for tag in xml:
        walls[tag.attrib["name"]] = parse_placement(tag)
    return walls

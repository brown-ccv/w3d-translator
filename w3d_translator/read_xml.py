import xml.etree.ElementTree as ET
from pathlib import Path

from classes import Color, WandNavigation, Camera, Story


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()

    # Get attributes
    version = root.attrib["version"]
    last_xpath = Path(root.attrib["last_xpath"])

    # TODO: Build each <Object> in <ObjectRoot> (6)
    object_root = {}
    for tag in root.find("ObjectRoot") or []:
        pass  # dict of objects by name

    # TODO: Build each <Group> in <GroupRoot> (7)
    group_root = {}
    for tag in root.find("GroupRoot") or []:
        pass  # dict of groups by name (group -> array of object names)

    # TODO: Build each <Timeline> in <TimelineRoot> (8)
    timeline_root = {}
    for tag in root.find("TimelineRoot") or []:
        pass  # dict of Timeline by name

    # TODO: Build each <Placement> in <PlacementRoot> (9)
    placement_root = {}
    for tag in root.find("PlacementRoot") or []:
        pass  # dict of Placement by name

    # TODO: Build each <Sound> in <SoundRoot> (10)
    sound_root = {}
    for tag in root.find("SoundRoot") or []:
        pass  # dict of Sound by name

    # TODO: Build each <ParticleActionList> in <ParticleActionRoot> (11)
    particle_action_root = {}
    for tag in root.find("ParticleActionRoot") or []:
        pass  # dict of ParticleActionList by name

    # Get Globals
    g = root.find("Global")
    camera_pos = Camera(g.find("CameraPos"))
    cave_camera_pos = Camera(g.find("CaveCameraPos"))
    background = Color(g.find("Background"))
    wand_navigation = WandNavigation(g.find("WandNavigation"))

    story = Story(
        version,
        last_xpath,
        object_root,
        group_root,
        timeline_root,
        placement_root,
        sound_root,
        particle_action_root,
        camera_pos,
        cave_camera_pos,
        background,
        wand_navigation,
    )
    print(story)
    return story

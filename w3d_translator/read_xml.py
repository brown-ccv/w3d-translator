import xml.etree.ElementTree as ET

from utils import str_to_tuple


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()
    story = {}

    # Globals
    g = root.find("Global")
    # story["camera_pos"] = parse_camera_pos(g.find("CameraPos"))
    # story["cave_camera_pos"] = parse_cave_camera_pos(g.find("CaveCameraPos"))
    story["background"] = read_background(g.find("Background"))
    # story["wand_navigation"] = WandNavigation(g.find("WandNavigation"))

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

    # TODO: Build each <Placement> in <PlacementRoot> (9)
    # placement_root = {}
    for tag in root.find("PlacementRoot") or []:
        pass  # Dict of Placement by name

    # TODO: Build each <Sound> in <SoundRoot> (10)
    # sound_root = {}
    for tag in root.find("SoundRoot") or []:
        pass  # Dict of Sound by name

    # TODO: Build each <ParticleActionList> in <ParticleActionRoot> (11)
    # particle_action_root = {}
    for tag in root.find("ParticleActionRoot") or []:
        pass  # Dict of ParticleActionList by name

    return story


def read_background(xml):
    print(xml, str_to_tuple(xml.attrib["color"]))
    return str_to_tuple(xml.attrib["color"])

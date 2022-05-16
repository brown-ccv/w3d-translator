import xml.etree.ElementTree as ET

from utils import str_to_tuple, tf_to_bool


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()
    story = {}

    # Globals
    g = root.find("Global")
    # story["camera_pos"] = parse_camera_pos(g.find("CameraPos"))
    # story["cave_camera_pos"] = parse_cave_camera_pos(g.find("CaveCameraPos"))
    story["background"] = str_to_tuple(g.find("Background").attrib["color"])
    story["wand_navigation"] = read_wand_navigation(g.find("WandNavigation"))
    print(story)

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


def read_wand_navigation(xml: ET.Element):
    return {
        "allow_rotation": tf_to_bool(xml.attrib["allow-rotation"]),
        "allow_movement": tf_to_bool(xml.attrib["allow-movement"]),
    }

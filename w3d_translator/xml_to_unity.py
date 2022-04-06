import xml.etree.ElementTree as ET

from classes.Color import Color
from classes.WandNavigation import WandNavigation


def xml_to_unity(file):
    xml = ET.parse(file)
    root = xml.getroot()

    story = {}  # TODO: Make story its own class

    # object_root = {}
    for tag in root.find("ObjectRoot"):
        pass  # Dict of objects by name

    # group_root = {}
    for tag in root.find("GroupRoot"):
        pass  # Dict of groups by name (group -> array of object names)

    # timeline_root = {}
    for tag in root.find("TimelineRoot"):
        pass  # Dict of Timeline by name

    # placement_root = {}
    for tag in root.find("PlacementRoot"):
        pass  # Dict of Placement by name

    # sound_root = {}
    for tag in root.find("SoundRoot"):
        pass  # Dict of Sound by name

    # particle_action_root = {}
    for tag in root.find("ParticleActionRoot"):
        pass  # Dict of ParticleActionList by name

    # Globals
    g = root.find("Global")
    # story["camera_pos"] = parse_camera_pos(g.find("CameraPos"))
    # story["cave_camera_pos"] = parse_cave_camera_pos(g.find("CaveCameraPos"))
    story["background"] = Color(g.find("Background"))
    story["wand_navigation"] = WandNavigation(g.find("WandNavigation"))

    print(story)
    return story

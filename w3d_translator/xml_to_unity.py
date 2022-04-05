import xml.etree.ElementTree as ET

from classes.Color import Color
from classes.WandNavigation import WandNavigation


def xml_to_unity(file):
    xml = ET.parse(file)
    root = xml.getroot()

    story = {}

    # object_root = {}
    for tag in root.find("ObjectRoot"):
        pass

    # group_root = {}
    for tag in root.find("GroupRoot"):
        # Each group is an array of names
        pass

    # timeline_root = {}
    for tag in root.find("TimelineRoot"):
        pass

    # placement_root = {}
    for tag in root.find("PlacementRoot"):
        pass

    # sound_root = {}
    for tag in root.find("SoundRoot"):
        pass

    # particle_action_root = {}
    for tag in root.find("ParticleActionRoot"):
        pass

    # Globals
    g = root.find("Global")
    # story["camera_pos"] = parse_camera_pos(g.find("CameraPos"))
    # story["cave_camera_pos"] = parse_cave_camera_pos(g.find("CaveCameraPos"))
    story["background"] = Color(g.find("Background"))
    story["wand_navigation"] = WandNavigation(g.find("WandNavigation"))

    print(story)

    return story

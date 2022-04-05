import xml.etree.ElementTree as ET

from classes.WandNavigation import WandNavigation


def parse_object(xml):
    pass


def parse_group(xml):
    pass


def parse_timeline(xml):
    pass


def parse_placement(xml):
    pass


def parse_sound(xml):
    pass


def parse_particle_action_list(xml):
    pass


def parse_camera_pos(xml):
    pass


def parse_cave_camera_pos(xml):
    pass


def parse_background(xml):
    pass


def xml_to_unity(file):
    xml = ET.parse(file)
    root = xml.getroot()

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
    # camera_pos = parse_camera_pos(g.find("CameraPos"))
    # cave_camera_pos = parse_cave_camera_pos(g.find("CaveCameraPos"))
    # background = parse_background(g.find("Background"))
    wand_navigation = WandNavigation(g.find("WandNavigation"))

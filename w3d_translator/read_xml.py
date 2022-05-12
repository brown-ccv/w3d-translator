import xml.etree.ElementTree as ET

from classes import Color, WandNavigation, Camera


def read_xml(file):
    xml = ET.parse(file)
    root = xml.getroot()

    story = {}  # TODO: Make story its own class (5)

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

    # Globals
    g = root.find("Global")
    # TODO: Build <CameraPos> and <CaveCameraPos> (12)
    story["camera_pos"] = Camera(g.find("CameraPos"))
    story["cave_camera_pos"] = Camera(g.find("CaveCameraPos"))
    story["background"] = Color(g.find("Background"))
    story["wand_navigation"] = WandNavigation(g.find("WandNavigation"))

    # print(story)
    return story

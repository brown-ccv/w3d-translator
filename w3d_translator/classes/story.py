from dataclasses import dataclass
from pathlib import Path

from classes import XmlDataClass, Camera, Color, WandNavigation


@dataclass
class Story(XmlDataClass):
    version: int
    last_xpath: Path
    objects: dict
    groups: dict
    timelines: dict
    placements: dict
    sounds: dict
    particle_actions: dict
    camera: Camera
    cave_camera: Camera
    background: Color
    wand_navigation: WandNavigation

    def __init__(
        self,
        version,
        last_xpath,
        objects,
        groups,
        timelines,
        placements,
        sounds,
        particle_actions,
        camera,
        cave_camera,
        background,
        wand_navigation,
    ):
        super().__init__()
        self.version = version
        self.last_xpath = last_xpath
        self.objects = objects
        self.groups = groups
        self.timelines = timelines
        self.placements = placements
        self.sounds = sounds
        self.particle_actions = particle_actions
        self.camera = camera
        self.cave_camera = cave_camera
        self.background = background
        self.wand_navigation = wand_navigation

    def to_yaml():
        pass

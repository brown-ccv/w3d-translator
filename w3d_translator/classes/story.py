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

    def to_yaml():
        pass

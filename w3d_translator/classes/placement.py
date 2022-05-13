import xml.etree.ElementTree as ET
from enum import Enum
from dataclasses import dataclass, field

from classes import XmlDataClass, Vec3

# TODO: Placements in PlacementRoot include "Axis" and "LookAt" (15)


class Reference(Enum):
    CENTER = "Center"
    FRONT_WALL = "FrontWall"
    LEFT_WALL = "LeftWall"
    RIGHT_WALL = "RightWall"
    FLOOR_WALL = "CenterWall"


@dataclass
class Placement(XmlDataClass):
    xml: ET.Element = field(repr=False)
    relative_to: Reference = field(init=False)
    position: Vec3 = field(init=False)

    def __post_init__(self):
        super().__init__()
        self.relative_to = Reference(self.xml.find("RelativeTo").text)
        self.position = Vec3(self.xml.find("Position").text)

    def to_yaml():
        pass

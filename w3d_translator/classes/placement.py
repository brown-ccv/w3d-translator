import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from classes import XmlDataClass, Vec3

# TODO: Wall enum for relative_to


@dataclass
class Placement(XmlDataClass):
    xml: ET.Element
    relative_to: str = field(init=False)
    position: Vec3 = field(init=False)

    def __post_init__(self):
        super().__init__()
        self.relative_to = self.xml.find("RelativeTo").text  # TEMP
        self.position = Vec3(self.xml.find("Position").text)

    def to_yaml():
        pass

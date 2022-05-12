import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from classes import XmlDataClass, Placement


@dataclass
class Camera(XmlDataClass):
    xml: ET.Element
    far_clip: float = field(init=False)
    placement: Placement = field(init=False)

    def __post_init__(self):
        super().__init__()
        self.far_clip = float(self.xml.attrib["far-clip"])
        self.placement = Placement(self.xml.find("Placement"))

    def to_yaml():
        pass

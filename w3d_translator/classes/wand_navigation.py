import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from classes import XmlDataClass
from utils import tf_to_bool


@dataclass
class WandNavigation(XmlDataClass):
    xml: ET.Element = field(repr=False)
    allow_rotation: bool = field(init=False)
    allow_movement: bool = field(init=False)

    def __post_init__(self):
        super().__init__()
        self.allow_rotation = tf_to_bool(self.xml.attrib["allow-rotation"])
        self.allow_movement = tf_to_bool(self.xml.attrib["allow-movement"])

    def to_yaml():
        pass

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from utils import tf_to_bool


@dataclass
class WandNavigation:
    xml: ET.Element
    allow_rotation: bool = field(init=False)
    allow_movement: bool = field(init=False)

    def __post_init__(self):
        self.allow_rotation = tf_to_bool(self.xml.attrib["allow-rotation"])
        self.allow_movement = tf_to_bool(self.xml.attrib["allow-movement"])

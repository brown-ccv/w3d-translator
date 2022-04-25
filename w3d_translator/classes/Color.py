import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from utils import str_to_rgba


@dataclass
class Color:
    xml: ET.Element
    rgba: dict = field(init=False)
    r: float = field(init=False)
    g: float = field(init=False)
    b: float = field(init=False)
    a: float = field(init=False)

    def __post_init__(self):
        self.rgba = str_to_rgba(self.xml.attrib["color"])
        self.r = self.rgba["r"]
        self.g = self.rgba["g"]
        self.b = self.rgba["b"]
        self.a = self.rgba["a"]

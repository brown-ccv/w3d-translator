import xml.etree.ElementTree as ET
from utils import str_to_rgba


class Color:
    def __init__(self, xml: ET.Element):
        self.xml = xml
        self.rgba = str_to_rgba(xml.attrib["color"])
        self.r = self.rgba["r"]
        self.g = self.rgba["g"]
        self.b = self.rgba["b"]
        self.a = self.rgba["a"]

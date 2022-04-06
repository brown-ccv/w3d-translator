import xml.etree.ElementTree as ET
from utils import tf_to_bool


class WandNavigation:
    def __init__(self, xml: ET.Element):
        self.xml = xml
        self.allow_rotation = tf_to_bool(xml.attrib["allow-rotation"])
        self.allow_movement = tf_to_bool(xml.attrib["allow-movement"])

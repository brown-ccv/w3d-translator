import xml.etree.ElementTree as ET


# TODO: Better error handling (all classes)
# TODO: Define functions somewhere else?
def get_tf(string):
    if string == "false":
        return False
    elif string == "true":
        return True
    else:
        print("Error reading attribute", string)
        return None


class WandNavigation:
    def __init__(self, xml: ET.Element):
        self.xml = xml
        self.allow_rotation = get_tf(xml.attrib["allow-rotation"])
        self.allow_movement = get_tf(xml.attrib["allow-movement"])

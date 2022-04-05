import xml.etree.ElementTree as ET


class WandNavigation:
    def __init__(self, xml: ET.Element):
        self.xml = xml,
        self.allow_rotation = self.get_tf(xml.attrib["allow-rotation"])
        self.allow_movement = self.get_tf(xml.attrib["allow-movement"])

    def __repr__(self):
        return "WandNavigation:\n" + \
                "\tAllow Rotation: %s\n" % (self.allow_rotation) + \
                "\tAllow Rotation: %s" % (self.allow_movement)

    # TODO: Better error handling (all classes)
    # TODO: Define functions somewhere else?
    def get_tf(self, string):
        if string == "false":
            return False
        elif string == "true":
            return True
        else:
            print("Error reading attribute", self.xml)
            return None

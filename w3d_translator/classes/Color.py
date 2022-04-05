import xml.etree.ElementTree as ET


# TODO: Better error handling (all classes)
# TODO: Define functions somewhere else?
def get_color(string):
    arr = string.split(", ")
    return {
        "r": int(arr[0]),
        "g": int(arr[1]),
        "b": int(arr[2]),
        "a": 1
    }


class Color:
    def __init__(self, xml: ET.Element):
        self.xml = xml
        self.color = get_color(xml.attrib["color"])
        self.r = self.color["r"]
        self.g = self.color["g"]
        self.b = self.color["b"]
        self.a = self.color["a"]

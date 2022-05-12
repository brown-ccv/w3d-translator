from dataclasses import dataclass, field

from classes import XmlDataClass
from utils import str_to_xy, str_to_xyz


@dataclass
class Vec2(XmlDataClass):
    xy: dict = field(init=False)
    x: float = field(init=False)
    y: float = field(init=False)

    def __init__(self, text):
        super().__init__()
        self.xy = str_to_xy(text)
        self.x = self.xy["x"]
        self.y = self.xy["y"]

    def to_yaml():
        pass


@dataclass
class Vec3(XmlDataClass):
    xyz: dict = field(init=False)
    x: float = field(init=False)
    y: float = field(init=False)
    z: float = field(init=False)

    def __init__(self, text):
        super().__init__()
        self.xyz = str_to_xyz(text)
        self.x = self.xyz["x"]
        self.y = self.xyz["y"]
        self.z = self.xyz["z"]

    def to_yaml():
        pass

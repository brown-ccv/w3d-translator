import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from classes import XmlDataClass
from classes import Color

# Each TODO is a part of issue 6


@dataclass
class GameObject(XmlDataClass):
    xml: ET.Element = field(repr=False)
    name: str = field(init=False)
    visible: bool = field(init=False)
    color: Color = field(init=False)
    lighting: float = field(init=False)  # TODO: Variable type
    clickthrough: bool = field(init=False)  # TODO: Variable type
    around_self_axis: bool = field(init=False)  # TODO: Variable type
    scale: float = field(init=False)  # TODO: Variable type
    placement: float = field(init=False)  # TODO: Variable type (Placement)
    content: float = field(init=False)  # TODO: Variable type (Content)
    links: float = field(init=False)  # TODO: Variable type (list of Link)
    text: str = field(init=False)
    sound_ref: str = field(init=False)  # name of a sound

    # TODO: Use self.xml.find to get each sub-object
    def __post_init__(self):
        super().__init__()
        pass

    def to_yaml():
        pass

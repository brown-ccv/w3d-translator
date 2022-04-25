import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from classes.Color import Color

@dataclass
class GameObject:
    xml: ET.Element
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
        pass
        # self.name = name
        # self.visible = visible
        # self.color = color
        # self.lighting = lighting
        # self.clickthrough = clickthrough
        # self.around_self_axis = around_self_axis
        # self.scale = scale
        # self.placement = placement 
        # self.content = content
        # self.links = links
        # self.text = text
        # self.sound_ref = sound_ref

from msilib.schema import Class


class Object:
    def __init__(self, name, visible, color, lighting, clickthrough, around_self_axis, scale, placement, content, links, text, sound):
        self.name = name
        self.visible = visible
        self.color = color
        self.lighting = lighting
        self.clickthrough = clickthrough
        self.around_self_axis = around_self_axis
        self.scale = scale
        self.placement = placement
        self.content = content
        self.links = links
        self.text = text
        self.sound = sound
        
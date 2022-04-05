class Object:
    def __init__(
        self,
        name: str,
        visible: bool,
        color,
        lighting: bool,
        clickthrough: bool,
        around_self_axis: bool,
        scale: float,
        placement,
        content,
        links: list,
        text: str,
        sound_ref: str,
    ):
        self.name = name
        self.visible = visible
        self.color = color  # TODO: Custom Unity color type
        self.lighting = lighting
        self.clickthrough = clickthrough
        self.around_self_axis = around_self_axis
        self.scale = scale
        self.placement = placement  # TODO: Placement object type
        self.content = content  # TODO: Content object type
        self.links = links  # TODO: Array of link type
        self.text = text
        self.sound_ref = sound_ref

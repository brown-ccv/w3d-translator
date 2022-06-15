from pathlib import Path
from typing import Union

import generateDS.classes as classes
import generateDS.subclasses as sub


def clean_xml(story: classes.Story) -> classes.Story:
    # TODO: Convert <xs:simpleType>s (45)

    # Convert each <xs:simpleType name="file" type to a Path
    convert_paths(story)

    """Convert each <xs:simpleType name="color"> type to a vector of integers

    Object.color
    Object.Link.EnabledColor
    Object.Link.SelectedColor
    """
    # TODO: Convert 
    object: classes.Object
    for object in story.ObjectRoot.Object:
        color = str_to_color(object.Color)
        object.set_Color(color)

        if object.LinkRoot is not None:
            link: classes.Link = object.LinkRoot.Link
            enabled_color = str_to_color(link.EnabledColor)
            link.set_EnabledColor(enabled_color)

            selected_color = str_to_color(link.SelectedColor)
            link.set_SelectedColor(selected_color)

    # TODO: Object.LinkRoot.Link.Actions.ObjectChange.Transition.Color
    # TODO: ParticleAction.TargetColor.color
    # TODO: Global.Background.color
    # TODO: Timeline.TimedActions.GroupRef.Transition.Color
    # TODO: Timeline.TimedActions.ObjectChange.Transition.Color
    # TODO: EventTrigger.Actions.GroupRef.Transition.Color
    # TODO: EventTrigger.Actions.ObjectChange.Transition.Color

    # Convert each vector type to a tuple of floats
    # TODO: EventTrigger.HeadTrack.Direction.PointTarget.point
    # TODO: EventTrigger.HeadTrack.Direction.DirectionTarget.direction
    # TODO: EventTrigger.HeadTrack.Position.Box.corner1
    # TODO: EventTrigger.HeadTrack.Position.Box.corner2
    # TODO: EventTrigger.MoveTrack.Box.corner1
    # TODO: EventTrigger.MoveTrack.Box.corner2
    # TODO: ParticleAction.Gravity.direction
    # TODO: ParticleAction.Damping.direction
    # TODO: ParticleAction.OrbitPoint.center
    # TODO: ParticleDomain.Point.point
    # TODO: ParticleDomain.Line.p1
    # TODO: ParticleDomain.Line.p2
    # TODO: ParticleDomain.Triangle.p1
    # TODO: ParticleDomain.Triangle.p2
    # TODO: ParticleDomain.Triangle.p3
    # TODO: ParticleDomain.Plane.point
    # TODO: ParticleDomain.Plane.normal
    # TODO: ParticleDomain.Rect.point
    # TODO: ParticleDomain.Rect.u-dir
    # TODO: ParticleDomain.Rect.v-dir
    # TODO: ParticleDomain.Box.p1
    # TODO: ParticleDomain.Box.p2
    # TODO: ParticleDomain.Sphere.center
    # TODO: ParticleDomain.Cylinder.p1
    # TODO: ParticleDomain.Cylinder.p2
    # TODO: ParticleDomain.Cone.base_center
    # TODO: ParticleDomain.Cone.apex
    # TODO: ParticleDomain.Blob.center
    # TODO: ParticleDomain.Disc.center
    # TODO: ParticleDomain.Disc.normal

    # ! Repeat everywhere Placement is used
    # Placement is used in PlacementRoot
    # Placement is used in Object
    # Placement is used in ActionsType.MoveCave (Note: multiple ActionsType)
    # Placement is used in Camera
    # Placement is used in Transition.Movement (note: multiple Transition)
    # ActionsType.ObjectChange
    # ActionsType.GroupRef
    # Placement is used in Transition.MoveRel (note: multiple Transition)
    # TODO: Placement.Position
    # TODO: Placement.Axis.rotation
    # TODO: Placement.LookAt.target
    # TODO: Placement.LookAt.up
    # TODO: Placement.Normal.normal

    # Convert each _Root property to a dictionary of that type
    if story.ObjectRoot is not None:
        story.ObjectRoot = name_dictionary(story.ObjectRoot.Object)
    if story.GroupRoot is not None:
        story.GroupRoot = name_dictionary(story.GroupRoot.Group)
    if story.TimelineRoot is not None:
        story.TimelineRoot = name_dictionary(story.TimelineRoot.Timeline)
    if story.PlacementRoot is not None:
        story.PlacementRoot = name_dictionary(story.PlacementRoot.Placement)
    if story.SoundRoot is not None:
        story.SoundRoot = name_dictionary(story.SoundRoot.Sound)
    if story.EventRoot is not None:
        story.EventRoot = name_dictionary(story.EventRoot.EventTrigger)
    if story.ParticleActionRoot is not None:
        story.ParticleActionRoot = name_dictionary(
            story.ParticleActionRoot.ParticleActionList
        )


def convert_paths(story: classes.Story) -> classes.Story:
    """Type convert each <xs:simpleType name="path"> type to a Path

    Object.Content.Image.filename
    Object.Content.StereoImage.left_image
    Object.Content.StereoImage.right_image
    Object.Content.Model.filename
    Sound.filename
    """

    object: classes.Object
    choice: Union[sub.ImageTypeSub, sub.StereoImageTypeSub, sub.ModelTypeSub]
    for object in story.ObjectRoot.Object:
        choice = object.Content.get_choice()
        match type(choice):
            case sub.ImageTypeSub:
                choice.set_filename(Path(choice.get_filename()))
                object.Content.set_choice(choice)
            case sub.StereoImageTypeSub:
                choice.set_left_image(Path(choice.get_left_image()))
                choice.set_right_image(Path(choice.get_right_image()))
                object.Content.set_choice(choice)
            case sub.ModelTypeSub:
                choice.set_filename(Path(choice.get_filename()))
                object.Content.set_choice(choice)
            case _:
                pass

    sound: classes.Sound
    for sound in story.SoundRoot.Sound:
        sound.set_filename(Path(sound.get_filename()))

    return story


def name_dictionary(container: list) -> dict:
    """Converts a list of classes into a dictionary

    { key: [class.name], val: [class] }
    """
    if container is not None:
        return dict((item.name, item) for item in container)


# TODO: Add to each color tag?
def str_to_color(string: str) -> tuple:
    string = string.split(",")
    return tuple(int(x) for x in string)

#!/usr/bin/env python

#
# Generated Thu Jun  2 10:23:57 2022 by generateDS.py version 2.40.13.
# Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'w3d_translator/generateDS/classes.py')
#   ('-s', 'w3d_translator/generateDS/subclasses.py')
#   ('--super', 'generateDS.classes')
#   ('--use-getter-setter', 'none')
#   ('--member-specs', 'dict')
#   ('--cleanup-name-list', "[('[-:.]', '_'), ('Root$', 's'), ('Pos$', '')]")
#
# Command line arguments:
#   .\schema\caveschema.xsd
#
# Command line:
#   .\generateDS\generateDS.py -o "w3d_translator/generateDS/classes.py" -s "w3d_translator/generateDS/subclasses.py" --super="generateDS.classes" --use-getter-setter="none" --member-specs="dict" --cleanup-name-list="[('[-:.]', '_'), ('Root$', 's'), ('Pos$', '')]" .\schema\caveschema.xsd
#
# Current working directory (os.getcwd()):
#   W3D Translator
#

# flake8: noqa

import os
import sys
from lxml import etree as etree_

import generateDS.classes as supermod


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc


def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element


#
# Globals
#

ExternalEncoding = ""
SaveElementTreeNode = True

#
# Data representation classes
#


class StorySub(supermod.Story):
    def __init__(
        self,
        version=8,
        last_xpath=None,
        Objects=None,
        Groups=None,
        Timelines=None,
        Placements=None,
        Sounds=None,
        Events=None,
        ParticleActions=None,
        Global=None,
        About=None,
        **kwargs_
    ):
        super(StorySub, self).__init__(
            version,
            last_xpath,
            Objects,
            Groups,
            Timelines,
            Placements,
            Sounds,
            Events,
            ParticleActions,
            Global,
            About,
            **kwargs_
        )


supermod.Story.subclass = StorySub
# end class StorySub


class ObjectSub(supermod.Object):
    def __init__(
        self,
        name=None,
        Visible=True,
        Color="255,255,255",
        Lighting=False,
        ClickThrough=False,
        AroundSelfAxis=False,
        Scale=1.0,
        SoundRef=None,
        Placement=None,
        Content=None,
        Links=None,
        **kwargs_
    ):
        super(ObjectSub, self).__init__(
            name,
            Visible,
            Color,
            Lighting,
            ClickThrough,
            AroundSelfAxis,
            Scale,
            SoundRef,
            Placement,
            Content,
            Links,
            **kwargs_
        )


supermod.Object.subclass = ObjectSub
# end class ObjectSub


class ContentSub(supermod.Content):
    def __init__(
        self,
        None_=None,
        Text=None,
        Image=None,
        StereoImage=None,
        Model=None,
        Light=None,
        ParticleSystem=None,
        **kwargs_
    ):
        super(ContentSub, self).__init__(
            None_,
            Text,
            Image,
            StereoImage,
            Model,
            Light,
            ParticleSystem,
            **kwargs_
        )


supermod.Content.subclass = ContentSub
# end class ContentSub


class LinkSub(supermod.Link):
    def __init__(
        self,
        Enabled=True,
        RemainEnabled=True,
        EnabledColor="0,128,255",
        SelectedColor="255,0,0",
        Actions=None,
        **kwargs_
    ):
        super(LinkSub, self).__init__(
            Enabled,
            RemainEnabled,
            EnabledColor,
            SelectedColor,
            Actions,
            **kwargs_
        )


supermod.Link.subclass = LinkSub
# end class LinkSub


class GroupSub(supermod.Group):
    def __init__(self, name=None, Objects=None, Groups=None, **kwargs_):
        super(GroupSub, self).__init__(name, Objects, Groups, **kwargs_)


supermod.Group.subclass = GroupSub
# end class GroupSub


class ObjectsSub(supermod.Objects):
    def __init__(self, name=None, **kwargs_):
        super(ObjectsSub, self).__init__(name, **kwargs_)


supermod.Objects.subclass = ObjectsSub
# end class ObjectsSub


class GroupsSub(supermod.Groups):
    def __init__(self, name=None, **kwargs_):
        super(GroupsSub, self).__init__(name, **kwargs_)


supermod.Groups.subclass = GroupsSub
# end class GroupsSub


class TimelineSub(supermod.Timeline):
    def __init__(
        self, name=None, start_immediately=True, TimedActions=None, **kwargs_
    ):
        super(TimelineSub, self).__init__(
            name, start_immediately, TimedActions, **kwargs_
        )


supermod.Timeline.subclass = TimelineSub
# end class TimelineSub


class GroupRefSub(supermod.GroupRef):
    def __init__(self, name=None, random=None, Transition=None, **kwargs_):
        super(GroupRefSub, self).__init__(name, random, Transition, **kwargs_)


supermod.GroupRef.subclass = GroupRefSub
# end class GroupRefSub


class ActionsTypeSub(supermod.ActionsType):
    def __init__(
        self,
        ObjectChange=None,
        GroupRef=None,
        TimerChange=None,
        SoundRef=None,
        Event=None,
        MoveCave=None,
        Restart=None,
        extensiontype_=None,
        **kwargs_
    ):
        super(ActionsTypeSub, self).__init__(
            ObjectChange,
            GroupRef,
            TimerChange,
            SoundRef,
            Event,
            MoveCave,
            Restart,
            extensiontype_,
            **kwargs_
        )


supermod.ActionsType.subclass = ActionsTypeSub
# end class ActionsTypeSub


class TimerChangeSub(supermod.TimerChange):
    def __init__(
        self,
        name=None,
        start=None,
        stop=None,
        continue_=None,
        start_if_not_started=None,
        **kwargs_
    ):
        super(TimerChangeSub, self).__init__(
            name, start, stop, continue_, start_if_not_started, **kwargs_
        )


supermod.TimerChange.subclass = TimerChangeSub
# end class TimerChangeSub


class ObjectChangeSub(supermod.ObjectChange):
    def __init__(self, name=None, Transition=None, **kwargs_):
        super(ObjectChangeSub, self).__init__(name, Transition, **kwargs_)


supermod.ObjectChange.subclass = ObjectChangeSub
# end class ObjectChangeSub


class SoundRefSub(supermod.SoundRef):
    def __init__(self, name=None, **kwargs_):
        super(SoundRefSub, self).__init__(name, **kwargs_)


supermod.SoundRef.subclass = SoundRefSub
# end class SoundRefSub


class SoundSub(supermod.Sound):
    def __init__(
        self,
        name=None,
        filename=None,
        autostart=False,
        Mode=None,
        Repeat=None,
        Settings=None,
        **kwargs_
    ):
        super(SoundSub, self).__init__(
            name, filename, autostart, Mode, Repeat, Settings, **kwargs_
        )


supermod.Sound.subclass = SoundSub
# end class SoundSub


class EventTriggerSub(supermod.EventTrigger):
    def __init__(
        self,
        enabled=True,
        name=None,
        duration=0.0,
        remain_enabled=True,
        HeadTrack=None,
        MoveTrack=None,
        Actions=None,
        **kwargs_
    ):
        super(EventTriggerSub, self).__init__(
            enabled,
            name,
            duration,
            remain_enabled,
            HeadTrack,
            MoveTrack,
            Actions,
            **kwargs_
        )


supermod.EventTrigger.subclass = EventTriggerSub
# end class EventTriggerSub


class BoxSub(supermod.Box):
    def __init__(
        self,
        ignore_Y=True,
        corner1=None,
        corner2=None,
        Movement=None,
        **kwargs_
    ):
        super(BoxSub, self).__init__(
            ignore_Y, corner1, corner2, Movement, **kwargs_
        )


supermod.Box.subclass = BoxSub
# end class BoxSub


class EventSub(supermod.Event):
    def __init__(self, enable=None, name=None, **kwargs_):
        super(EventSub, self).__init__(enable, name, **kwargs_)


supermod.Event.subclass = EventSub
# end class EventSub


class ParticleActionListSub(supermod.ParticleActionList):
    def __init__(
        self,
        name=None,
        Source=None,
        Vel=None,
        ParticleAction=None,
        RemoveCondition=None,
        **kwargs_
    ):
        super(ParticleActionListSub, self).__init__(
            name, Source, Vel, ParticleAction, RemoveCondition, **kwargs_
        )


supermod.ParticleActionList.subclass = ParticleActionListSub
# end class ParticleActionListSub


class ParticleActionSub(supermod.ParticleAction):
    def __init__(
        self,
        Avoid=None,
        Bounce=None,
        Gravity=None,
        Damping=None,
        Gravitate=None,
        Follow=None,
        MatchVel=None,
        OrbitPoint=None,
        Jet=None,
        RandomVel=None,
        RandomAccel=None,
        RandomDisplace=None,
        TargetColor=None,
        TargetSize=None,
        TargetVel=None,
        **kwargs_
    ):
        super(ParticleActionSub, self).__init__(
            Avoid,
            Bounce,
            Gravity,
            Damping,
            Gravitate,
            Follow,
            MatchVel,
            OrbitPoint,
            Jet,
            RandomVel,
            RandomAccel,
            RandomDisplace,
            TargetColor,
            TargetSize,
            TargetVel,
            **kwargs_
        )


supermod.ParticleAction.subclass = ParticleActionSub
# end class ParticleActionSub


class ParticleDomainTypeSub(supermod.ParticleDomainType):
    def __init__(
        self,
        Point=None,
        Line=None,
        Triangle=None,
        Plane=None,
        Rect=None,
        Box=None,
        Sphere=None,
        Cylinder=None,
        Cone=None,
        Blob=None,
        Disc=None,
        **kwargs_
    ):
        super(ParticleDomainTypeSub, self).__init__(
            Point,
            Line,
            Triangle,
            Plane,
            Rect,
            Box,
            Sphere,
            Cylinder,
            Cone,
            Blob,
            Disc,
            **kwargs_
        )


supermod.ParticleDomainType.subclass = ParticleDomainTypeSub
# end class ParticleDomainTypeSub


class GlobalSub(supermod.Global):
    def __init__(
        self,
        Camera=None,
        CaveCamera=None,
        Background=None,
        WandNavigation=None,
        **kwargs_
    ):
        super(GlobalSub, self).__init__(
            Camera, CaveCamera, Background, WandNavigation, **kwargs_
        )


supermod.Global.subclass = GlobalSub
# end class GlobalSub


class CameraSub(supermod.Camera):
    def __init__(self, far_clip=100, Placement=None, **kwargs_):
        super(CameraSub, self).__init__(far_clip, Placement, **kwargs_)


supermod.Camera.subclass = CameraSub
# end class CameraSub


class PlacementSub(supermod.Placement):
    def __init__(
        self,
        name=None,
        RelativeTo="Center",
        Position="(0.0, 0.0, 0.0)",
        Axis=None,
        LookAt=None,
        Normal=None,
        **kwargs_
    ):
        super(PlacementSub, self).__init__(
            name, RelativeTo, Position, Axis, LookAt, Normal, **kwargs_
        )


supermod.Placement.subclass = PlacementSub
# end class PlacementSub


class TransitionSub(supermod.Transition):
    def __init__(
        self,
        duration=1.0,
        Visible=None,
        Movement=None,
        MoveRel=None,
        Color="255,255,255",
        Scale=1.0,
        Sound=None,
        LinkChange=None,
        **kwargs_
    ):
        super(TransitionSub, self).__init__(
            duration,
            Visible,
            Movement,
            MoveRel,
            Color,
            Scale,
            Sound,
            LinkChange,
            **kwargs_
        )


supermod.Transition.subclass = TransitionSub
# end class TransitionSub


class ObjectRootTypeSub(supermod.ObjectRootType):
    def __init__(self, Object=None, **kwargs_):
        super(ObjectRootTypeSub, self).__init__(Object, **kwargs_)


supermod.ObjectRootType.subclass = ObjectRootTypeSub
# end class ObjectRootTypeSub


class GroupRootTypeSub(supermod.GroupRootType):
    def __init__(self, Group=None, **kwargs_):
        super(GroupRootTypeSub, self).__init__(Group, **kwargs_)


supermod.GroupRootType.subclass = GroupRootTypeSub
# end class GroupRootTypeSub


class TimelineRootTypeSub(supermod.TimelineRootType):
    def __init__(self, Timeline=None, **kwargs_):
        super(TimelineRootTypeSub, self).__init__(Timeline, **kwargs_)


supermod.TimelineRootType.subclass = TimelineRootTypeSub
# end class TimelineRootTypeSub


class PlacementRootTypeSub(supermod.PlacementRootType):
    def __init__(self, Placement=None, **kwargs_):
        super(PlacementRootTypeSub, self).__init__(Placement, **kwargs_)


supermod.PlacementRootType.subclass = PlacementRootTypeSub
# end class PlacementRootTypeSub


class SoundRootTypeSub(supermod.SoundRootType):
    def __init__(self, Sound=None, **kwargs_):
        super(SoundRootTypeSub, self).__init__(Sound, **kwargs_)


supermod.SoundRootType.subclass = SoundRootTypeSub
# end class SoundRootTypeSub


class EventRootTypeSub(supermod.EventRootType):
    def __init__(self, EventTrigger=None, **kwargs_):
        super(EventRootTypeSub, self).__init__(EventTrigger, **kwargs_)


supermod.EventRootType.subclass = EventRootTypeSub
# end class EventRootTypeSub


class ParticleActionRootTypeSub(supermod.ParticleActionRootType):
    def __init__(self, ParticleActionList=None, **kwargs_):
        super(ParticleActionRootTypeSub, self).__init__(
            ParticleActionList, **kwargs_
        )


supermod.ParticleActionRootType.subclass = ParticleActionRootTypeSub
# end class ParticleActionRootTypeSub


class AboutTypeSub(supermod.AboutType):
    def __init__(self, news=None, **kwargs_):
        super(AboutTypeSub, self).__init__(news, **kwargs_)


supermod.AboutType.subclass = AboutTypeSub
# end class AboutTypeSub


class LinkRootTypeSub(supermod.LinkRootType):
    def __init__(self, Link=None, **kwargs_):
        super(LinkRootTypeSub, self).__init__(Link, **kwargs_)


supermod.LinkRootType.subclass = LinkRootTypeSub
# end class LinkRootTypeSub


class NoneTypeSub(supermod.NoneType):
    def __init__(self, **kwargs_):
        super(NoneTypeSub, self).__init__(**kwargs_)


supermod.NoneType.subclass = NoneTypeSub
# end class NoneTypeSub


class TextTypeSub(supermod.TextType):
    def __init__(
        self,
        horiz_align="center",
        vert_align="center",
        font=None,
        depth=0.0,
        text=None,
        **kwargs_
    ):
        super(TextTypeSub, self).__init__(
            horiz_align, vert_align, font, depth, text, **kwargs_
        )


supermod.TextType.subclass = TextTypeSub
# end class TextTypeSub


class ImageTypeSub(supermod.ImageType):
    def __init__(self, filename=None, **kwargs_):
        super(ImageTypeSub, self).__init__(filename, **kwargs_)


supermod.ImageType.subclass = ImageTypeSub
# end class ImageTypeSub


class StereoImageTypeSub(supermod.StereoImageType):
    def __init__(self, left_image=None, right_image=None, **kwargs_):
        super(StereoImageTypeSub, self).__init__(
            left_image, right_image, **kwargs_
        )


supermod.StereoImageType.subclass = StereoImageTypeSub
# end class StereoImageTypeSub


class ModelTypeSub(supermod.ModelType):
    def __init__(self, filename=None, check_collisions=False, **kwargs_):
        super(ModelTypeSub, self).__init__(
            filename, check_collisions, **kwargs_
        )


supermod.ModelType.subclass = ModelTypeSub
# end class ModelTypeSub


class LightTypeSub(supermod.LightType):
    def __init__(
        self,
        diffuse=True,
        specular=True,
        const_atten=1.0,
        lin_atten=0.0,
        quad_atten=0.0,
        Point=None,
        Directional=None,
        Spot=None,
        **kwargs_
    ):
        super(LightTypeSub, self).__init__(
            diffuse,
            specular,
            const_atten,
            lin_atten,
            quad_atten,
            Point,
            Directional,
            Spot,
            **kwargs_
        )


supermod.LightType.subclass = LightTypeSub
# end class LightTypeSub


class PointTypeSub(supermod.PointType):
    def __init__(self, **kwargs_):
        super(PointTypeSub, self).__init__(**kwargs_)


supermod.PointType.subclass = PointTypeSub
# end class PointTypeSub


class DirectionalTypeSub(supermod.DirectionalType):
    def __init__(self, **kwargs_):
        super(DirectionalTypeSub, self).__init__(**kwargs_)


supermod.DirectionalType.subclass = DirectionalTypeSub
# end class DirectionalTypeSub


class SpotTypeSub(supermod.SpotType):
    def __init__(self, angle=30.0, **kwargs_):
        super(SpotTypeSub, self).__init__(angle, **kwargs_)


supermod.SpotType.subclass = SpotTypeSub
# end class SpotTypeSub


class ParticleSystemTypeSub(supermod.ParticleSystemType):
    def __init__(
        self,
        max_particles=1000,
        actions_name=None,
        particle_group=None,
        look_at_camera=False,
        sequential=False,
        speed=1.0,
        **kwargs_
    ):
        super(ParticleSystemTypeSub, self).__init__(
            max_particles,
            actions_name,
            particle_group,
            look_at_camera,
            sequential,
            speed,
            **kwargs_
        )


supermod.ParticleSystemType.subclass = ParticleSystemTypeSub
# end class ParticleSystemTypeSub


class ActionsType1Sub(supermod.ActionsType1):
    def __init__(
        self,
        ObjectChange=None,
        GroupRef=None,
        TimerChange=None,
        SoundRef=None,
        Event=None,
        MoveCave=None,
        Restart=None,
        Clicks=None,
        **kwargs_
    ):
        super(ActionsType1Sub, self).__init__(
            ObjectChange,
            GroupRef,
            TimerChange,
            SoundRef,
            Event,
            MoveCave,
            Restart,
            Clicks,
            **kwargs_
        )


supermod.ActionsType1.subclass = ActionsType1Sub
# end class ActionsType1Sub


class ClicksTypeSub(supermod.ClicksType):
    def __init__(self, Any=None, NumClicks=None, **kwargs_):
        super(ClicksTypeSub, self).__init__(Any, NumClicks, **kwargs_)


supermod.ClicksType.subclass = ClicksTypeSub
# end class ClicksTypeSub


class AnyTypeSub(supermod.AnyType):
    def __init__(self, **kwargs_):
        super(AnyTypeSub, self).__init__(**kwargs_)


supermod.AnyType.subclass = AnyTypeSub
# end class AnyTypeSub


class NumClicksTypeSub(supermod.NumClicksType):
    def __init__(self, num_clicks=1, reset=False, **kwargs_):
        super(NumClicksTypeSub, self).__init__(num_clicks, reset, **kwargs_)


supermod.NumClicksType.subclass = NumClicksTypeSub
# end class NumClicksTypeSub


class TimedActionsTypeSub(supermod.TimedActionsType):
    def __init__(
        self,
        ObjectChange=None,
        GroupRef=None,
        TimerChange=None,
        SoundRef=None,
        Event=None,
        MoveCave=None,
        Restart=None,
        seconds_time=None,
        **kwargs_
    ):
        super(TimedActionsTypeSub, self).__init__(
            ObjectChange,
            GroupRef,
            TimerChange,
            SoundRef,
            Event,
            MoveCave,
            Restart,
            seconds_time,
            **kwargs_
        )


supermod.TimedActionsType.subclass = TimedActionsTypeSub
# end class TimedActionsTypeSub


class MoveCaveTypeSub(supermod.MoveCaveType):
    def __init__(
        self,
        duration=0.0,
        Relative=None,
        Absolute=None,
        Placement=None,
        **kwargs_
    ):
        super(MoveCaveTypeSub, self).__init__(
            duration, Relative, Absolute, Placement, **kwargs_
        )


supermod.MoveCaveType.subclass = MoveCaveTypeSub
# end class MoveCaveTypeSub


class RelativeTypeSub(supermod.RelativeType):
    def __init__(self, **kwargs_):
        super(RelativeTypeSub, self).__init__(**kwargs_)


supermod.RelativeType.subclass = RelativeTypeSub
# end class RelativeTypeSub


class AbsoluteTypeSub(supermod.AbsoluteType):
    def __init__(self, **kwargs_):
        super(AbsoluteTypeSub, self).__init__(**kwargs_)


supermod.AbsoluteType.subclass = AbsoluteTypeSub
# end class AbsoluteTypeSub


class RestartTypeSub(supermod.RestartType):
    def __init__(self, **kwargs_):
        super(RestartTypeSub, self).__init__(**kwargs_)


supermod.RestartType.subclass = RestartTypeSub
# end class RestartTypeSub


class startTypeSub(supermod.startType):
    def __init__(self, **kwargs_):
        super(startTypeSub, self).__init__(**kwargs_)


supermod.startType.subclass = startTypeSub
# end class startTypeSub


class stopTypeSub(supermod.stopType):
    def __init__(self, **kwargs_):
        super(stopTypeSub, self).__init__(**kwargs_)


supermod.stopType.subclass = stopTypeSub
# end class stopTypeSub


class continueTypeSub(supermod.continueType):
    def __init__(self, **kwargs_):
        super(continueTypeSub, self).__init__(**kwargs_)


supermod.continueType.subclass = continueTypeSub
# end class continueTypeSub


class start_if_not_startedTypeSub(supermod.start_if_not_startedType):
    def __init__(self, **kwargs_):
        super(start_if_not_startedTypeSub, self).__init__(**kwargs_)


supermod.start_if_not_startedType.subclass = start_if_not_startedTypeSub
# end class start_if_not_startedTypeSub


class ModeTypeSub(supermod.ModeType):
    def __init__(self, Positional=None, Fixed=None, **kwargs_):
        super(ModeTypeSub, self).__init__(Positional, Fixed, **kwargs_)


supermod.ModeType.subclass = ModeTypeSub
# end class ModeTypeSub


class PositionalTypeSub(supermod.PositionalType):
    def __init__(self, **kwargs_):
        super(PositionalTypeSub, self).__init__(**kwargs_)


supermod.PositionalType.subclass = PositionalTypeSub
# end class PositionalTypeSub


class FixedTypeSub(supermod.FixedType):
    def __init__(self, **kwargs_):
        super(FixedTypeSub, self).__init__(**kwargs_)


supermod.FixedType.subclass = FixedTypeSub
# end class FixedTypeSub


class RepeatTypeSub(supermod.RepeatType):
    def __init__(
        self, NoRepeat=None, RepeatForever=None, RepeatNum=None, **kwargs_
    ):
        super(RepeatTypeSub, self).__init__(
            NoRepeat, RepeatForever, RepeatNum, **kwargs_
        )


supermod.RepeatType.subclass = RepeatTypeSub
# end class RepeatTypeSub


class NoRepeatTypeSub(supermod.NoRepeatType):
    def __init__(self, **kwargs_):
        super(NoRepeatTypeSub, self).__init__(**kwargs_)


supermod.NoRepeatType.subclass = NoRepeatTypeSub
# end class NoRepeatTypeSub


class RepeatForeverTypeSub(supermod.RepeatForeverType):
    def __init__(self, **kwargs_):
        super(RepeatForeverTypeSub, self).__init__(**kwargs_)


supermod.RepeatForeverType.subclass = RepeatForeverTypeSub
# end class RepeatForeverTypeSub


class SettingsTypeSub(supermod.SettingsType):
    def __init__(self, freq="1.0", volume="1.0", pan="0.0", **kwargs_):
        super(SettingsTypeSub, self).__init__(freq, volume, pan, **kwargs_)


supermod.SettingsType.subclass = SettingsTypeSub
# end class SettingsTypeSub


class HeadTrackTypeSub(supermod.HeadTrackType):
    def __init__(self, Position=None, Direction=None, **kwargs_):
        super(HeadTrackTypeSub, self).__init__(Position, Direction, **kwargs_)


supermod.HeadTrackType.subclass = HeadTrackTypeSub
# end class HeadTrackTypeSub


class PositionTypeSub(supermod.PositionType):
    def __init__(self, Anywhere=None, Box=None, **kwargs_):
        super(PositionTypeSub, self).__init__(Anywhere, Box, **kwargs_)


supermod.PositionType.subclass = PositionTypeSub
# end class PositionTypeSub


class AnywhereTypeSub(supermod.AnywhereType):
    def __init__(self, **kwargs_):
        super(AnywhereTypeSub, self).__init__(**kwargs_)


supermod.AnywhereType.subclass = AnywhereTypeSub
# end class AnywhereTypeSub


class DirectionTypeSub(supermod.DirectionType):
    def __init__(
        self,
        PointTarget=None,
        DirectionTarget=None,
        ObjectTarget=None,
        None_=None,
        **kwargs_
    ):
        super(DirectionTypeSub, self).__init__(
            PointTarget, DirectionTarget, ObjectTarget, None_, **kwargs_
        )


supermod.DirectionType.subclass = DirectionTypeSub
# end class DirectionTypeSub


class PointTargetTypeSub(supermod.PointTargetType):
    def __init__(self, point=None, angle=30, **kwargs_):
        super(PointTargetTypeSub, self).__init__(point, angle, **kwargs_)


supermod.PointTargetType.subclass = PointTargetTypeSub
# end class PointTargetTypeSub


class DirectionTargetTypeSub(supermod.DirectionTargetType):
    def __init__(self, direction=None, angle=30, **kwargs_):
        super(DirectionTargetTypeSub, self).__init__(
            direction, angle, **kwargs_
        )


supermod.DirectionTargetType.subclass = DirectionTargetTypeSub
# end class DirectionTargetTypeSub


class ObjectTargetTypeSub(supermod.ObjectTargetType):
    def __init__(self, name=None, **kwargs_):
        super(ObjectTargetTypeSub, self).__init__(name, **kwargs_)


supermod.ObjectTargetType.subclass = ObjectTargetTypeSub
# end class ObjectTargetTypeSub


class NoneType2Sub(supermod.NoneType2):
    def __init__(self, **kwargs_):
        super(NoneType2Sub, self).__init__(**kwargs_)


supermod.NoneType2.subclass = NoneType2Sub
# end class NoneType2Sub


class MoveTrackTypeSub(supermod.MoveTrackType):
    def __init__(self, Source=None, Box=None, **kwargs_):
        super(MoveTrackTypeSub, self).__init__(Source, Box, **kwargs_)


supermod.MoveTrackType.subclass = MoveTrackTypeSub
# end class MoveTrackTypeSub


class SourceTypeSub(supermod.SourceType):
    def __init__(self, ObjectRef=None, GroupObj=None, **kwargs_):
        super(SourceTypeSub, self).__init__(ObjectRef, GroupObj, **kwargs_)


supermod.SourceType.subclass = SourceTypeSub
# end class SourceTypeSub


class ObjectRefTypeSub(supermod.ObjectRefType):
    def __init__(self, name=None, **kwargs_):
        super(ObjectRefTypeSub, self).__init__(name, **kwargs_)


supermod.ObjectRefType.subclass = ObjectRefTypeSub
# end class ObjectRefTypeSub


class GroupObjTypeSub(supermod.GroupObjType):
    def __init__(self, name=None, objects=None, **kwargs_):
        super(GroupObjTypeSub, self).__init__(name, objects, **kwargs_)


supermod.GroupObjType.subclass = GroupObjTypeSub
# end class GroupObjTypeSub


class MovementTypeSub(supermod.MovementType):
    def __init__(self, Inside=None, Outside=None, **kwargs_):
        super(MovementTypeSub, self).__init__(Inside, Outside, **kwargs_)


supermod.MovementType.subclass = MovementTypeSub
# end class MovementTypeSub


class InsideTypeSub(supermod.InsideType):
    def __init__(self, **kwargs_):
        super(InsideTypeSub, self).__init__(**kwargs_)


supermod.InsideType.subclass = InsideTypeSub
# end class InsideTypeSub


class OutsideTypeSub(supermod.OutsideType):
    def __init__(self, **kwargs_):
        super(OutsideTypeSub, self).__init__(**kwargs_)


supermod.OutsideType.subclass = OutsideTypeSub
# end class OutsideTypeSub


class SourceType3Sub(supermod.SourceType3):
    def __init__(self, rate=None, ParticleDomain=None, **kwargs_):
        super(SourceType3Sub, self).__init__(rate, ParticleDomain, **kwargs_)


supermod.SourceType3.subclass = SourceType3Sub
# end class SourceType3Sub


class VelTypeSub(supermod.VelType):
    def __init__(self, ParticleDomain=None, **kwargs_):
        super(VelTypeSub, self).__init__(ParticleDomain, **kwargs_)


supermod.VelType.subclass = VelTypeSub
# end class VelTypeSub


class RemoveConditionTypeSub(supermod.RemoveConditionType):
    def __init__(self, Age=None, Position=None, Velocity=None, **kwargs_):
        super(RemoveConditionTypeSub, self).__init__(
            Age, Position, Velocity, **kwargs_
        )


supermod.RemoveConditionType.subclass = RemoveConditionTypeSub
# end class RemoveConditionTypeSub


class AgeTypeSub(supermod.AgeType):
    def __init__(self, age=None, younger_than=False, **kwargs_):
        super(AgeTypeSub, self).__init__(age, younger_than, **kwargs_)


supermod.AgeType.subclass = AgeTypeSub
# end class AgeTypeSub


class PositionType4Sub(supermod.PositionType4):
    def __init__(self, inside=False, ParticleDomain=None, **kwargs_):
        super(PositionType4Sub, self).__init__(
            inside, ParticleDomain, **kwargs_
        )


supermod.PositionType4.subclass = PositionType4Sub
# end class PositionType4Sub


class VelocityTypeSub(supermod.VelocityType):
    def __init__(self, inside=False, ParticleDomain=None, **kwargs_):
        super(VelocityTypeSub, self).__init__(
            inside, ParticleDomain, **kwargs_
        )


supermod.VelocityType.subclass = VelocityTypeSub
# end class VelocityTypeSub


class AvoidTypeSub(supermod.AvoidType):
    def __init__(
        self,
        magnitude=None,
        epsilon=0.001,
        lookahead=None,
        ParticleDomain=None,
        **kwargs_
    ):
        super(AvoidTypeSub, self).__init__(
            magnitude, epsilon, lookahead, ParticleDomain, **kwargs_
        )


supermod.AvoidType.subclass = AvoidTypeSub
# end class AvoidTypeSub


class BounceTypeSub(supermod.BounceType):
    def __init__(
        self,
        friction=None,
        resilience=None,
        cutoff=None,
        ParticleDomain=None,
        **kwargs_
    ):
        super(BounceTypeSub, self).__init__(
            friction, resilience, cutoff, ParticleDomain, **kwargs_
        )


supermod.BounceType.subclass = BounceTypeSub
# end class BounceTypeSub


class GravityTypeSub(supermod.GravityType):
    def __init__(self, direction=None, **kwargs_):
        super(GravityTypeSub, self).__init__(direction, **kwargs_)


supermod.GravityType.subclass = GravityTypeSub
# end class GravityTypeSub


class DampingTypeSub(supermod.DampingType):
    def __init__(self, direction=None, vel_low=0.0, vel_high=0.0, **kwargs_):
        super(DampingTypeSub, self).__init__(
            direction, vel_low, vel_high, **kwargs_
        )


supermod.DampingType.subclass = DampingTypeSub
# end class DampingTypeSub


class GravitateTypeSub(supermod.GravitateType):
    def __init__(
        self, magnitude=1.0, epsilon=0.001, max_radius=0.0, **kwargs_
    ):
        super(GravitateTypeSub, self).__init__(
            magnitude, epsilon, max_radius, **kwargs_
        )


supermod.GravitateType.subclass = GravitateTypeSub
# end class GravitateTypeSub


class FollowTypeSub(supermod.FollowType):
    def __init__(
        self, magnitude=1.0, epsilon=0.001, max_radius=0.0, **kwargs_
    ):
        super(FollowTypeSub, self).__init__(
            magnitude, epsilon, max_radius, **kwargs_
        )


supermod.FollowType.subclass = FollowTypeSub
# end class FollowTypeSub


class MatchVelTypeSub(supermod.MatchVelType):
    def __init__(
        self, magnitude=1.0, epsilon=0.001, max_radius=0.0, **kwargs_
    ):
        super(MatchVelTypeSub, self).__init__(
            magnitude, epsilon, max_radius, **kwargs_
        )


supermod.MatchVelType.subclass = MatchVelTypeSub
# end class MatchVelTypeSub


class OrbitPointTypeSub(supermod.OrbitPointType):
    def __init__(
        self,
        center=None,
        magnitude=1.0,
        epsilon=0.001,
        max_radius=0.0,
        **kwargs_
    ):
        super(OrbitPointTypeSub, self).__init__(
            center, magnitude, epsilon, max_radius, **kwargs_
        )


supermod.OrbitPointType.subclass = OrbitPointTypeSub
# end class OrbitPointTypeSub


class JetTypeSub(supermod.JetType):
    def __init__(self, ParticleDomain=None, AccelDomain=None, **kwargs_):
        super(JetTypeSub, self).__init__(
            ParticleDomain, AccelDomain, **kwargs_
        )


supermod.JetType.subclass = JetTypeSub
# end class JetTypeSub


class TargetColorTypeSub(supermod.TargetColorType):
    def __init__(self, color=None, alpha=1.0, scale=None, **kwargs_):
        super(TargetColorTypeSub, self).__init__(
            color, alpha, scale, **kwargs_
        )


supermod.TargetColorType.subclass = TargetColorTypeSub
# end class TargetColorTypeSub


class PointType5Sub(supermod.PointType5):
    def __init__(self, point=None, **kwargs_):
        super(PointType5Sub, self).__init__(point, **kwargs_)


supermod.PointType5.subclass = PointType5Sub
# end class PointType5Sub


class LineTypeSub(supermod.LineType):
    def __init__(self, p1=None, p2=None, **kwargs_):
        super(LineTypeSub, self).__init__(p1, p2, **kwargs_)


supermod.LineType.subclass = LineTypeSub
# end class LineTypeSub


class TriangleTypeSub(supermod.TriangleType):
    def __init__(self, p1=None, p2=None, p3=None, **kwargs_):
        super(TriangleTypeSub, self).__init__(p1, p2, p3, **kwargs_)


supermod.TriangleType.subclass = TriangleTypeSub
# end class TriangleTypeSub


class PlaneTypeSub(supermod.PlaneType):
    def __init__(self, point=None, normal=None, **kwargs_):
        super(PlaneTypeSub, self).__init__(point, normal, **kwargs_)


supermod.PlaneType.subclass = PlaneTypeSub
# end class PlaneTypeSub


class RectTypeSub(supermod.RectType):
    def __init__(self, point=None, u_dir=None, v_dir=None, **kwargs_):
        super(RectTypeSub, self).__init__(point, u_dir, v_dir, **kwargs_)


supermod.RectType.subclass = RectTypeSub
# end class RectTypeSub


class BoxTypeSub(supermod.BoxType):
    def __init__(self, p1=None, p2=None, **kwargs_):
        super(BoxTypeSub, self).__init__(p1, p2, **kwargs_)


supermod.BoxType.subclass = BoxTypeSub
# end class BoxTypeSub


class SphereTypeSub(supermod.SphereType):
    def __init__(self, center=None, radius=None, radius_inner=0.0, **kwargs_):
        super(SphereTypeSub, self).__init__(
            center, radius, radius_inner, **kwargs_
        )


supermod.SphereType.subclass = SphereTypeSub
# end class SphereTypeSub


class CylinderTypeSub(supermod.CylinderType):
    def __init__(
        self, p1=None, p2=None, radius=None, radius_inner=0.0, **kwargs_
    ):
        super(CylinderTypeSub, self).__init__(
            p1, p2, radius, radius_inner, **kwargs_
        )


supermod.CylinderType.subclass = CylinderTypeSub
# end class CylinderTypeSub


class ConeTypeSub(supermod.ConeType):
    def __init__(
        self,
        base_center=None,
        apex=None,
        radius=None,
        radius_inner=0.0,
        **kwargs_
    ):
        super(ConeTypeSub, self).__init__(
            base_center, apex, radius, radius_inner, **kwargs_
        )


supermod.ConeType.subclass = ConeTypeSub
# end class ConeTypeSub


class BlobTypeSub(supermod.BlobType):
    def __init__(self, center=None, stdev=1.0, **kwargs_):
        super(BlobTypeSub, self).__init__(center, stdev, **kwargs_)


supermod.BlobType.subclass = BlobTypeSub
# end class BlobTypeSub


class DiscTypeSub(supermod.DiscType):
    def __init__(
        self,
        center=None,
        normal=None,
        radius=None,
        radius_inner=0.0,
        **kwargs_
    ):
        super(DiscTypeSub, self).__init__(
            center, normal, radius, radius_inner, **kwargs_
        )


supermod.DiscType.subclass = DiscTypeSub
# end class DiscTypeSub


class BackgroundTypeSub(supermod.BackgroundType):
    def __init__(self, color="0, 0, 0", **kwargs_):
        super(BackgroundTypeSub, self).__init__(color, **kwargs_)


supermod.BackgroundType.subclass = BackgroundTypeSub
# end class BackgroundTypeSub


class WandNavigationTypeSub(supermod.WandNavigationType):
    def __init__(self, allow_rotation=False, allow_movement=False, **kwargs_):
        super(WandNavigationTypeSub, self).__init__(
            allow_rotation, allow_movement, **kwargs_
        )


supermod.WandNavigationType.subclass = WandNavigationTypeSub
# end class WandNavigationTypeSub


class AxisTypeSub(supermod.AxisType):
    def __init__(self, rotation="(0.0, 1.0, 0.0)", angle=0.0, **kwargs_):
        super(AxisTypeSub, self).__init__(rotation, angle, **kwargs_)


supermod.AxisType.subclass = AxisTypeSub
# end class AxisTypeSub


class LookAtTypeSub(supermod.LookAtType):
    def __init__(
        self, target="(0.0, 0.0, 0.0)", up="(0.0, 1.0, 0.0)", **kwargs_
    ):
        super(LookAtTypeSub, self).__init__(target, up, **kwargs_)


supermod.LookAtType.subclass = LookAtTypeSub
# end class LookAtTypeSub


class NormalTypeSub(supermod.NormalType):
    def __init__(self, normal="(0.0, 0.0, 1.0)", angle=0.0, **kwargs_):
        super(NormalTypeSub, self).__init__(normal, angle, **kwargs_)


supermod.NormalType.subclass = NormalTypeSub
# end class NormalTypeSub


class MovementType6Sub(supermod.MovementType6):
    def __init__(self, Placement=None, **kwargs_):
        super(MovementType6Sub, self).__init__(Placement, **kwargs_)


supermod.MovementType6.subclass = MovementType6Sub
# end class MovementType6Sub


class MoveRelTypeSub(supermod.MoveRelType):
    def __init__(self, Placement=None, **kwargs_):
        super(MoveRelTypeSub, self).__init__(Placement, **kwargs_)


supermod.MoveRelType.subclass = MoveRelTypeSub
# end class MoveRelTypeSub


class SoundTypeSub(supermod.SoundType):
    def __init__(self, action=None, **kwargs_):
        super(SoundTypeSub, self).__init__(action, **kwargs_)


supermod.SoundType.subclass = SoundTypeSub
# end class SoundTypeSub


class LinkChangeTypeSub(supermod.LinkChangeType):
    def __init__(
        self,
        link_on=None,
        link_off=None,
        activate=None,
        activate_if_on=None,
        **kwargs_
    ):
        super(LinkChangeTypeSub, self).__init__(
            link_on, link_off, activate, activate_if_on, **kwargs_
        )


supermod.LinkChangeType.subclass = LinkChangeTypeSub
# end class LinkChangeTypeSub


class link_onTypeSub(supermod.link_onType):
    def __init__(self, **kwargs_):
        super(link_onTypeSub, self).__init__(**kwargs_)


supermod.link_onType.subclass = link_onTypeSub
# end class link_onTypeSub


class link_offTypeSub(supermod.link_offType):
    def __init__(self, **kwargs_):
        super(link_offTypeSub, self).__init__(**kwargs_)


supermod.link_offType.subclass = link_offTypeSub
# end class link_offTypeSub


class activateTypeSub(supermod.activateType):
    def __init__(self, **kwargs_):
        super(activateTypeSub, self).__init__(**kwargs_)


supermod.activateType.subclass = activateTypeSub
# end class activateTypeSub


class activate_if_onTypeSub(supermod.activate_if_onType):
    def __init__(self, **kwargs_):
        super(activate_if_onTypeSub, self).__init__(**kwargs_)


supermod.activate_if_onType.subclass = activate_if_onTypeSub
# end class activate_if_onTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "Story"
        rootClass = supermod.Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag, namespacedef_="", pretty_print=True
        )
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "Story"
        rootClass = supermod.Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement,
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8",
        )
        sys.stdout.write(content)
        sys.stdout.write("\n")
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode = parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "Story"
        rootClass = supermod.Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(sys.stdout, 0, name_=rootTag, namespacedef_="")
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "Story"
        rootClass = supermod.Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write("#from generateDS.classes import *\n\n")
        sys.stdout.write("import generateDS.classes as model_\n\n")
        sys.stdout.write("rootObj = model_.rootClass(\n")
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(")\n")
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    main()

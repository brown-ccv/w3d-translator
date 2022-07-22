using System;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

namespace W3D
{

// TODO: Make name attribute part of W3D - don't need it anywhere else?

    /********** STORY            ***********/


    [Serializable]
    [XmlRoot(ElementName="Story")]
    public class Story : W3D
    {
        [XmlArray(ElementName="ObjectRoot")]
        [XmlArrayItem(ElementName="Object")] 
        public List<Object> ObjectRoot;
    
        [XmlArray(ElementName="GroupRoot")]
        [XmlArrayItem(ElementName="Group")] 
        public List<Group> GroupRoot;

    	[XmlArray(ElementName="TimelineRoot")]
        [XmlArrayItem(ElementName="Timeline")]
        public List<Timeline> TimelineRoot;
    
        [XmlArray(ElementName="PlacementRoot")]
        [XmlArrayItem(ElementName="Placement")] 
        public List<Placement> PlacementRoot;
    
        [XmlArray(ElementName="SoundRoot")]
        [XmlArrayItem(ElementName="Sound")] 
        public List<Sound> SoundRoot;

        [XmlArray(ElementName="EventRoot")]
        [XmlArrayItem(ElementName="EventTrigger")]
        public List<EventTrigger> EventRoot;
	    
        [XmlArray(ElementName="ParticleActionRoot")]
	    [XmlArrayItem(ElementName="ParticleActionList")] 
	    public List<ParticleAction> ParticleActionRoot;

        [XmlElement(ElementName="Global")]
        public Global Global;

        [XmlElement(ElementName="About")]
        public About About;

        [XmlAttribute(AttributeName="version")]
        public int version;

        [XmlAttribute(AttributeName="last_xpath")]
        public string lastXpath;

        [XmlText]
        public string text;

    }


    [Serializable]
    [XmlRoot(ElementName="About")]
    public class About : W3D
    {
        [XmlAttribute(AttributeName="news")]
        public string news;
    }


    /********** OBJECT            ***********/


    [Serializable]
    [XmlRoot(ElementName="Object")]
    public class Object : W3D
    {
        [XmlElement(ElementName="Visible")]
        public bool visible;

        [XmlElement(ElementName="Color")]
        public string colorString;

        [XmlElement(ElementName="Lighting")]
        public bool lighting;

        [XmlElement(ElementName="ClickThrough")]
        public bool clickThrough;

        [XmlElement(ElementName="AroundSelfAxis")]
        public bool aroundSelfAxis;

        [XmlElement(ElementName="Scale")]
        public double scale;

        [XmlElement(ElementName="SoundRef")]
        public string soundRef;

        [XmlElement(ElementName="Placement")]
        public Placement Placement;

        [XmlElement(ElementName="Content")]
        public Content Content;

        [XmlElement(ElementName="LinkRoot")]
        public LinkRoot LinkRoot;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    [XmlRoot(ElementName = "LinkRoot")]
    public class LinkRoot
    {
        [XmlElement(ElementName = "Link")]
        public Link Link;
    }


    // CONTENT


    [Serializable]
    [XmlRoot(ElementName="Content")]
    public class Content : W3D
    {
        [XmlChoiceIdentifier("contentType")]
        [XmlElement(ElementName="None", Type=null)]
        [XmlElement(ElementName="Text", Type=typeof(Text))]
        [XmlElement(ElementName="Image", Type=typeof(Image))]
        [XmlElement(ElementName="StereoImage", Type=typeof(StereoImage))]
        [XmlElement(ElementName="Model", Type=typeof(Model))]
        [XmlElement(ElementName="Light", Type=typeof(Light))]
        [XmlElement(ElementName="ParticleSystem", Type=typeof(ParticleSystem))]
        public object content;
        public ContentType contentType; 

        public enum ContentType {
            [XmlEnum("None")] None,
            [XmlEnum("Text")] Text,
            [XmlEnum("Image")] Image,
            [XmlEnum("StereoImage")] StereoImage,
            [XmlEnum("Model")] Model,
            [XmlEnum("Light")] Light,
            [XmlEnum("ParticleSystem")] ParticleSystem,
        }   
    }   


    [Serializable]
    [XmlRoot(ElementName="Text")]
    public class Text : W3D
    {

        [XmlElement(ElementName="text")]
        public List<string> text;

        [XmlAttribute(AttributeName="horiz-align")]
        public horizAlign horizontalAlign;
        public enum horizAlign { 
            None,
            [XmlEnum(Name="left")] Left,
            [XmlEnum(Name="center")] Center,
            [XmlEnum(Name="right")] Right,
        }

        [XmlAttribute(AttributeName="vert-align")]
        public vertAlign verticalAlign;
        public enum vertAlign { 
            None,
            [XmlEnum(Name="top")] Top,
            [XmlEnum(Name="center")] Center,
            [XmlEnum(Name="bottom")] Bottom,
        }

        [XmlAttribute(AttributeName="font")]
        public string font;

        [XmlAttribute(AttributeName="depth")]
        public double depth;
    }


    [Serializable]
    [XmlRoot(ElementName="Image")]
    public class Image : W3D
    {
        [XmlAttribute(AttributeName="filename")]
        public string filename;

    }


    [Serializable]
    [XmlRoot(ElementName="StereoImage")]
    public class StereoImage : W3D
    {
        [XmlAttribute(AttributeName="left-image")]
        public string leftImage;

        [XmlAttribute(AttributeName="right-image")]
        public string rightImage;

    }


    [Serializable]
    [XmlRoot(ElementName="Model")]
    public class Model : W3D
    {
        [XmlAttribute(AttributeName="filename")]
        public string filename;

        [XmlAttribute(AttributeName="check-collisions")]
        public string checkCollisions;
    }


    [Serializable]
    [XmlRoot(ElementName="ParticleSystem")]
    // TODO: Unity has a ParticleSystem class
    public class ParticleSystem : W3D
    {
        [XmlAttribute(AttributeName="max-particles")]
        public int maxParticles;

        [XmlAttribute(AttributeName="actions-name")]
        public string actionsName;

        [XmlAttribute(AttributeName="particle-group")]
        public string particleGroup;

        [XmlAttribute(AttributeName="look-at-camera")]
        public bool lookAtCamera;

        [XmlAttribute(AttributeName="sequential")]
        public bool sequential;

        [XmlAttribute(AttributeName="speed")]
        public double speed;
    }


    // Content.Light


    [Serializable]
    [XmlRoot(ElementName="Light")]
    // TODO: Unity has a Light class
    public class Light : W3D
    {
        [XmlChoiceIdentifier("lightType")]
        [XmlElement(ElementName="Point")]
        [XmlElement(ElementName="Directional")]
        [XmlElement(ElementName="Spot", Type=typeof(Spot))]
        public object light;
        public LightType lightType;

        [XmlAttribute(AttributeName="diffuse")]
        public bool diffuse;

        [XmlAttribute(AttributeName="specular")]
        public bool specular;

        [XmlAttribute(AttributeName="const_atten")]
        public double constAtten;

        [XmlAttribute(AttributeName="lin_atten")]
        public double linAtten;

        [XmlAttribute(AttributeName="quad_atten")]
        public double quadAtten;

        public enum LightType {
            [XmlEnum("Point")] Point,
            [XmlEnum("Directional")] Directional,
            [XmlEnum("Spot")] Spot,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Spot")]
    public class Spot : W3D
    {
        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // LINK


    [Serializable]
    [XmlRoot(ElementName="Link")]
    public class Link : W3D
    {
        [XmlElement(ElementName="Enabled")]
        public bool enabled;

        [XmlElement(ElementName="RemainEnabled")]
        public bool remainEnabled;

        [XmlElement(ElementName="EnabledColor")]
        public string enabledColorString;

        [XmlElement(ElementName="SelectedColor")]
        public string selectedColorString;

        [XmlElement(ElementName="Actions")]
        public List<LinkActions> Actions;
    }


    // Link.Actions


    [Serializable]
    [XmlRoot(ElementName="Actions")]
    public class LinkActions : Actions
    {
        [XmlElement(ElementName="Clicks")]
        public Clicks Clicks;
    }


    [Serializable]
    [XmlRoot(ElementName="Clicks")]
    public class Clicks : W3D
    {
        [XmlChoiceIdentifier("clicksType")]
        [XmlElement(ElementName="Any")]
        [XmlElement(ElementName="NumClicks", Type=typeof(NumClicks))]
        public object clicks;
        public ClicksType clicksType;

        public enum ClicksType {
            [XmlEnum("Any")] Any,
            [XmlEnum("NumClicks")] Number,
        }
    }



    [Serializable]
    [XmlRoot(ElementName="NumClicks")]
    public class NumClicks : W3D
    {
        [XmlAttribute(AttributeName="num_clicks")]
        public uint numClicks;

        [XmlAttribute(AttributeName="reset")]
        public bool reset;
    }


    /********** GROUP            ***********/


    [Serializable]
    [XmlRoot(ElementName="Group")]
    public class Group : W3D
    {
        [XmlChoiceIdentifier("referenceTypes")]
        [XmlElement(ElementName="Objects", Type=typeof(Reference))]
        [XmlElement(ElementName="Groups", Type=typeof(Reference))]
        public Reference[] references;
        public ReferenceType[] referenceTypes;

        [XmlAttribute(AttributeName="name")]
        public string name;

        public enum ReferenceType {
            [XmlEnum("Objects")] Object,
            [XmlEnum("Groups")] Group
        }
    }



    /********** TIMELINE        ***********/


    [Serializable]
    [XmlRoot(ElementName="Timeline")]
    public class Timeline : W3D
    {
        [XmlElement(ElementName="TimedActions")]
        public List<TimedActions> TimedActions;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlAttribute(AttributeName="start-immediately")]
        public bool startImmediately;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="TimedActions")]
    public class TimedActions : Actions
    {
        [XmlAttribute(AttributeName="seconds-time")]
        public double secondsTime;

        [XmlText]
        public string text;
    }


    /********** SOUND            ***********/


    [Serializable]
    [XmlRoot(ElementName="Sound")]
    public class Sound : W3D
    {
        [XmlElement(ElementName="Mode")]
        public Mode Mode;

        [XmlElement(ElementName="Repeat")]
        public Repeat Repeat;

        [XmlElement(ElementName="Settings")]
        public Settings Settings;

        [XmlAttribute(AttributeName="action")]
        public string action;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlAttribute(AttributeName="filename")]
        public string filename;

        [XmlAttribute(AttributeName="autostart")]
        public bool autostart;
    }


    [Serializable]
    [XmlRoot(ElementName="Mode")]
    public class Mode : W3D
    {
        [XmlChoiceIdentifier("modeType")]
        [XmlElement(ElementName="Positional")]
        [XmlElement(ElementName="Fixed")]
        public object mode;
        public ModeType modeType;

        public enum ModeType {
            [XmlEnum("Positional")] Positional,
            [XmlEnum("Fixed")] Fixed
        }
    }



    [Serializable]
    [XmlRoot(ElementName="Repeat")]
    public class Repeat : W3D
    {
        [XmlChoiceIdentifier("repeatType")]
        [XmlElement(ElementName="NoRepeat")]
        [XmlElement(ElementName="RepeatForever")]
        [XmlElement(ElementName="RepeatNum", Type=typeof(uint))]
        public object repeat;
        public RepeatType repeatType;
            
        public enum RepeatType {
            [XmlEnum("NoRepeat")] No,
            [XmlEnum("RepeatForever")] Forever,
            [XmlEnum("RepeatNum")] Number,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Settings")]
    public class Settings : W3D
    {
        [XmlAttribute(AttributeName="freq")]
        public double frequency;

        [XmlAttribute(AttributeName="volume")]
        public double volume;

        [XmlAttribute(AttributeName="pan")]
        public double pan;
    }


    /********** EVENT TRIGGER       ***********/


    [Serializable]
    [XmlRoot(ElementName="EventTrigger")]
    public class EventTrigger : W3D
    {
        [XmlChoiceIdentifier("trackType")]
        [XmlElement(ElementName="HeadTrack", Type=typeof(HeadTrack))]
        [XmlElement(ElementName="MoveTrack", Type=typeof(MoveTrack))]
        public object Track;
        public TrackType trackType;

        [XmlElement(ElementName="Actions")]
        public List<Actions> Actions;

        [XmlAttribute(AttributeName="enabled")]
        public bool enabled;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlAttribute(AttributeName="remain-enabled")]
        public bool remainEnabled;

        public enum TrackType {
            [XmlEnum("HeadTrack")] Head,
            [XmlEnum("MoveTrack")] Move,
        }
    }


    // HEAD TRACK


    [Serializable]
    [XmlRoot(ElementName="HeadTrack")]
    public class HeadTrack : W3D
    {
        [XmlElement(ElementName="Position")]
        public TrackPosition Position;

        [XmlElement(ElementName="Direction")]
        public Direction Direction;
    }


    [Serializable]
    [XmlRoot(ElementName="Position")]
    public class TrackPosition : W3D
    {
        [XmlChoiceIdentifier("positionType")]
        [XmlElement(ElementName="Anywhere")]
        [XmlElement(ElementName="Box", Type=typeof(Box))]
        public object position;
        public PositionType positionType;

        public enum PositionType {
            [XmlEnum("Anywhere")] Anywhere,
            [XmlEnum("Box")] Box
        }
    }


    // HeadTrack.Direction


    [Serializable]
    [XmlRoot(ElementName="Direction")]
    public class Direction : W3D
    {
        [XmlChoiceIdentifier("directionType")]
        [XmlElement(ElementName="None")]
        [XmlElement(ElementName="PointTarget", Type=typeof(PointTarget))]
        [XmlElement(ElementName="DirectionTarget", Type=typeof(DirectionTarget))]
        [XmlElement(ElementName="ObjectTarget", Type=typeof(Reference))]
        public object direction;
        public DirectionType directionType;

        public enum DirectionType {
            [XmlEnum("None")] None,
            [XmlEnum("PointTarget")] PointTarget,
            [XmlEnum("DirectionTarget")] DirectionTarget,
            [XmlEnum("ObjectTarget")] ObjectTarget
        }
    }


    [Serializable]
    [XmlRoot(ElementName="PointTarget")]
    public class PointTarget : W3D
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;

    }


    [Serializable]
    [XmlRoot(ElementName="DirectionTarget")]
    public class DirectionTarget : W3D
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // MOVE TRACK


    [Serializable]
    [XmlRoot(ElementName="MoveTrack")]
    public class MoveTrack : W3D
    {
        [XmlElement(ElementName="Source")]
        public Source Source;

        [XmlElement(ElementName="Box")]
        public Box Box;

    }


    [Serializable]
    [XmlRoot(ElementName="Source")]
    public class Source : W3D
    {
        [XmlChoiceIdentifier("sourceType")]
        [XmlElement(ElementName="ObjectRef", Type=typeof(Reference))]
        [XmlElement(ElementName="GroupObj", Type=typeof(GroupSource))]
        public object source;
        public SourceType sourceType;

        public enum SourceType {
            [XmlEnum("ObjectRef")] Object,
            [XmlEnum("GroupObj")] Group,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="GroupObj")]
    public class GroupSource : Reference
    {
        [XmlAttribute(AttributeName="objects")]
        public Selection objectSelection;
        public enum Selection { 
            None,
            [XmlEnum(Name="Any Object")] Any,
            [XmlEnum(Name="All Objects")] All
        }
    }


    // BOX


    [Serializable]
    [XmlRoot(ElementName="Box")]
    public class Box : W3D
    {
        [XmlElement(ElementName="Movement")]
        public Movement Movement;

        [XmlAttribute(AttributeName="ignore-Y")]
        public bool ignoreY;

        [XmlAttribute(AttributeName="corner1")]
        public string corner1String;

        [XmlAttribute(AttributeName="corner2")]
        public string corner2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Movement")]
    public class Movement : W3D
    {
        [XmlChoiceIdentifier("movementType")]
        [XmlElement(ElementName="Outside")]
        [XmlElement(ElementName="Inside")]
        public object movement;
        public MovementType movementType;

        public enum MovementType {
            [XmlEnum("Outside")] Outside,
            [XmlEnum("Inside")] Inside
        }
    }


    /********** PARTICLE ACTION     ***********/


    [Serializable]
    [XmlRoot(ElementName="ParticleActionList")]
    public class ParticleActionList : W3D
    {

        [XmlElement(ElementName="Source")]
        public ParticleSource Source;

        [XmlElement(ElementName="Vel")]
        public Vel Vel;

        [XmlElement(ElementName="ParticleAction")]
        public List<ParticleAction> ParticleAction;

        [XmlElement(ElementName="RemoveCondition")]
        public RemoveCondition RemoveCondition;

        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [Serializable]
    [XmlRoot(ElementName="Source")]
    public class ParticleSource : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="rate")]
        public double rate;
    }


    [Serializable]
    [XmlRoot(ElementName="Vel")]
    public class Vel : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;
    }


    // PARTICLE ACTION


    [Serializable]
    [XmlRoot(ElementName="ParticleAction")]
    public class ParticleAction : W3D
    {
        [XmlChoiceIdentifier("particleType")]
        [XmlElement(ElementName="Avoid", Type=typeof(Avoid))]
        [XmlElement(ElementName="Bounce", Type=typeof(Bounce))]
        [XmlElement(ElementName="Gravity", Type=typeof(Gravity))]
        [XmlElement(ElementName="Damping", Type=typeof(Damping))]
        [XmlElement(ElementName="Gravitate", Type=typeof(Gravitate))]
        [XmlElement(ElementName="Follow", Type=typeof(Follow))]
        [XmlElement(ElementName="MatchVel", Type=typeof(MatchVel))]
        [XmlElement(ElementName="OrbitPoint", Type=typeof(OrbitPoint))]
        [XmlElement(ElementName="Jet", Type=typeof(Jet))]
        [XmlElement(ElementName="RandomVel")]
        [XmlElement(ElementName="RandomAccel")]
        [XmlElement(ElementName="RandomDisplace")]
        [XmlElement(ElementName="TargetColor", Type=typeof(TargetColor))]
        [XmlElement(ElementName="TargetSize")]
        [XmlElement(ElementName="TargetVel")]
        public object particle;
        public ParticleActionType particleType;

        public enum ParticleActionType {
            [XmlEnum("Avoid")] Avoid,
            [XmlEnum("Bounce")] Bounce,
            [XmlEnum("Gravity")] Gravity,
            [XmlEnum("Damping")] Damping,
            [XmlEnum("Gravitate")] Gravitate,
            [XmlEnum("Follow")] Follow,
            [XmlEnum("MatchVel")] MatchVelocity,
            [XmlEnum("OrbitPoint")] OrbitPoint,
            [XmlEnum("Jet")] Jet,
            [XmlEnum("RandomVel")] RandomVelocity,
            [XmlEnum("RandomAccel")] RandomAcceleration,
            [XmlEnum("RandomDisplace")] RandomDisplace,
            [XmlEnum("TargetColor")] TargetColor,
            [XmlEnum("TargetSize")] TargetSize,
            [XmlEnum("TargetVel")] TargetVelocity,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Avoid")]
    public class Avoid : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="lookahead")]
        public double lookAhead;
    }


    [Serializable]
    [XmlRoot(ElementName="Bounce")]
    public class Bounce : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="friction")]
        public double friction;

        [XmlAttribute(AttributeName="resilience")]
        public double resilience;

        [XmlAttribute(AttributeName="cutoff")]
        public double cutoff;
    }


    [Serializable]
    [XmlRoot(ElementName="Gravity")]
    public class Gravity : W3D
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString;
    }


    [Serializable]
    [XmlRoot(ElementName="Damping")]
    public class Damping : W3D
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString;

        [XmlAttribute(AttributeName="vel_low")]
        public double velocityLow;

        [XmlAttribute(AttributeName="vel_high")]
        public double velocityHigh;
    }


    [Serializable]
    [XmlRoot(ElementName="Gravitate")]
    public class Gravitate : W3D
    {
        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double maxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Follow")]
    public class Follow : W3D
    {

        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double maxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="MatchVel")]
    public class MatchVel : W3D
    {
        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double maxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="OrbitPoint")]
    public class OrbitPoint : W3D
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString;

        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double maxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Jet")]
    public class Jet : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlElement(ElementName="AccelDomain")]
        public Particle AccelDomain;
    }


    [Serializable]
    [XmlRoot(ElementName="TargetColor")]
    public class TargetColor : W3D
    {
        [XmlAttribute(AttributeName="color")]
        public string colorString;

        [XmlAttribute(AttributeName="alpha")]
        public double alpha;

        [XmlAttribute(AttributeName="scale")]
        public double scale;
    }


    // REMOVE CONDITION


    [Serializable]
    [XmlRoot(ElementName="RemoveCondition")]
    public class RemoveCondition : W3D
    {
        [XmlChoiceIdentifier("removeType")]
        [XmlElement(ElementName="Age", Type=typeof(Age))]
        [XmlElement(ElementName="Position", Type=typeof(Remove))]
        [XmlElement(ElementName="Velocity", Type=typeof(Remove))]
        public object remove;
        public RemoveType removeType;

        public enum RemoveType {
            [XmlEnum("Age")] Age,
            [XmlEnum("Position")] Position,
            [XmlEnum("Velocity")] Velocity
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Age")]
    public class Age : W3D
    {
        [XmlAttribute(AttributeName="age")]
        public double age;

        [XmlAttribute(AttributeName="younger-than")]
        public bool youngerThan;
    }


    [Serializable]
    public class Remove : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="inside")]
        public bool inside;
    }


    /********** GLOBAL              ***********/


    [Serializable]
    [XmlRoot(ElementName="Global")]
    public class Global : W3D
    {
        [XmlElement(ElementName="CameraPos")]
        public Camera Camera;

        [XmlElement(ElementName="CaveCameraPos")]
        public Camera CaveCamera;

        [XmlElement(ElementName="Background")]
        public Background Background;

        [XmlElement(ElementName="WandNavigation")]

        public WandNavigation WandNavigation;
    }


    [Serializable]
    public class Camera : W3D
    {
        [XmlElement(ElementName="Placement")]
        public Placement Placement;

        [XmlAttribute(AttributeName="far-clip")]
        public float farClip;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="Background")]
    public class Background : W3D
    {
        [XmlAttribute(AttributeName="color")]
        public string colorString;
    }


    [Serializable]
    [XmlRoot(ElementName="WandNavigation")]
    public class WandNavigation : W3D
    {
        [XmlAttribute(AttributeName="allow-rotation")]
        public bool allowRotation;

        [XmlAttribute(AttributeName="allow-movement")]
        public bool allowMovement;
    }


    /********** COMPLEX TYPES    ***********/


    // PLACEMENT TYPE


    [Serializable]
    [XmlRoot(ElementName="Placement")]
    public class Placement : W3D
    {
        [XmlElement(ElementName="RelativeTo")]
        public string relativeTo;

        [XmlElement(ElementName="Position")]
        public string positionString;

        [XmlElement(ElementName="Axis")]
        public Axis Axis;

        [XmlElement(ElementName="LookAt")]
        public LookAt LookAt;

        [XmlElement(ElementName="Normal")]
        public Normal Normal;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="Axis")]
    public class Axis : W3D
    {
        [XmlAttribute(AttributeName="rotation")]
        public string rotationString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    [Serializable]
    [XmlRoot(ElementName="LookAt")]
    public class LookAt : W3D
    {
        [XmlAttribute(AttributeName="target")]
        public string targetString;

        [XmlAttribute(AttributeName="up")]
        public string upString;
    }


    [Serializable]
    [XmlRoot(ElementName="Normal")]
    public class Normal : W3D
    {
        [XmlAttribute(AttributeName="normal")]
        public string normalString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // ACTIONS TYPE


    [Serializable]
    public class Actions : W3D
    {
        [XmlChoiceIdentifier("actionType")]
        [XmlElement(ElementName="ObjectChange", Type=typeof(ObjectChange))]
        [XmlElement(ElementName="GroupRef", Type=typeof(GroupRef))]
        [XmlElement(ElementName="TimerChange", Type=typeof(TimerChange))]
        [XmlElement(ElementName="SoundRef", Type=typeof(Reference))]
        [XmlElement(ElementName="Event", Type=typeof(Event))]
        [XmlElement(ElementName="MoveCave", Type=typeof(MoveCave))]
        [XmlElement(ElementName="Restart")]
        public object action;
        public ActionType actionType;

        public enum ActionType {
            [XmlEnum("ObjectChange")] ObjectChange,
            [XmlEnum("GroupRef")] GroupReference,
            [XmlEnum("TimerChange")] TimerChange,
            [XmlEnum("SoundRef")] SoundReference,
            [XmlEnum("Event")] EventReference,
            [XmlEnum("MoveCave")] MoveCave,
            [XmlEnum("Restart")] Restart,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="ObjectChange")]
    public class ObjectChange : Reference
    {
        [XmlElement(ElementName="Transition")]
        public Transition Transition;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="GroupRef")]
    public class GroupRef : Reference
    {
        [XmlElement(ElementName="Transition")]
        public Transition Transition;

        [XmlAttribute(AttributeName="random")]
        public Random random;
        public enum Random { 
            None,
            [XmlEnum(Name="Select One Randomly")] OneRandom,
        }

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="TimerChange")]
    public class TimerChange : Reference
    {        
        [XmlChoiceIdentifier("changeType")]
        [XmlElement(ElementName="start")]
        [XmlElement(ElementName="stop")]
        [XmlElement(ElementName="continue")]
        [XmlElement(ElementName="start_if_not_started")]
        public object change;
        public ChangeType changeType;

        public enum ChangeType {
            [XmlEnum("start")] Start,
            [XmlEnum("stop")] Stop,
            [XmlEnum("continue")] Continue,
            [XmlEnum("start_if_not_started")] StartIfNotStarted,
        }
    }

    [Serializable]
    [XmlRoot(ElementName="Event")]
    public class Event : Reference
    {
        [XmlAttribute(AttributeName="enable")]
        public bool enable;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveCave")]
    public class MoveCave : W3D
    {
        [XmlChoiceIdentifier("moveType")]
        [XmlElement(ElementName="Relative")]
        [XmlElement(ElementName="Absolute")]
        public object move;
        public MoveType moveType;

        [XmlElement(ElementName="Placement")]
        public Placement Placement;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlText]
        public string text;

        public enum MoveType {
            [XmlEnum("Relative")] Relative,
            [XmlEnum("Absolute")] Absolute,
        }
    }


    // TRANSITION TYPE

 
    [Serializable]
    public class Transition : W3D
    {
        [XmlChoiceIdentifier("transitionType")]
        [XmlElement(ElementName="Visible", Type=typeof(bool))]
        [XmlElement(ElementName="Movement", Type=typeof(MovementTransition))]
        [XmlElement(ElementName="MoveRel", Type=typeof(MoveRel))]
        [XmlElement(ElementName="Color", Type=typeof(string))]
        [XmlElement(ElementName="Scale", Type=typeof(double))]
        [XmlElement(ElementName="Sound", Type=typeof(SoundTransition))]
        [XmlElement(ElementName="LinkTransition", Type=typeof(LinkTransition))]
        public object transition;
        public TransitionType transitionType;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlText]
        public string text;

        public enum TransitionType {
            [XmlEnum("Visible")] Visible,
            [XmlEnum("Movement")] Movement,
            [XmlEnum("MoveRel")] MoveRelative,
            [XmlEnum("Color")] Color,
            [XmlEnum("Scale")] Scale,
            [XmlEnum("Sound")] Sound,
            [XmlEnum("LinkTransition")] Link,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Movement")]
    public class MovementTransition : W3D
    {
        [XmlElement(ElementName="Placement")]
        public Placement Placement;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveRel")]
    public class MoveRel : W3D
    {
        [XmlElement(ElementName="Placement")]
        public Placement Placement;

    }


    [Serializable]
    [XmlRoot(ElementName="Sound")]
    public class SoundTransition : W3D
    {
        [XmlAttribute(AttributeName="action")]
        public Action action;
        public enum Action { 
            None,
            [XmlEnum(Name="Play Sound")] Play,
            [XmlEnum(Name="Stop Sound")] Stop,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="LinkChange")]
    public class LinkTransition : W3D
    {
        [XmlChoiceIdentifier("transitionType")]
        [XmlElement(ElementName="link_on")]
        [XmlElement(ElementName="link_off")]
        [XmlElement(ElementName="activate")]
        [XmlElement(ElementName="activate_if_on")]
        public object transition;
        public LinkTransitionType transitionType;

        public enum LinkTransitionType {
            [XmlEnum("link_on")] On,
            [XmlEnum("link_off")] Off,
            [XmlEnum("activate")] Activate,
            [XmlEnum("activate_if_on")] ActivateIfOn,
        }

    }


    // PARTICLE DOMAIN TYPE


    [Serializable]
    [XmlRoot(ElementName="ParticleDomain")]
    public class Particle : W3D
    {
        [XmlChoiceIdentifier("particleType")]
        [XmlElement(ElementName="Point", Type=typeof(Point))]
        [XmlElement(ElementName="Line", Type=typeof(Line))]
        [XmlElement(ElementName="Triangle", Type=typeof(Triangle))]
        [XmlElement(ElementName="Plane", Type=typeof(Plane))]
        [XmlElement(ElementName="Rect", Type=typeof(Rectangle))]
        [XmlElement(ElementName="Box", Type=typeof(BoxBoxParticle))]
        [XmlElement(ElementName="Sphere", Type=typeof(Sphere))]
        [XmlElement(ElementName="Cylinder", Type=typeof(Cylinder))]
        [XmlElement(ElementName="Cone", Type=typeof(Cone))]
        [XmlElement(ElementName="Blob", Type=typeof(Blob))]
        [XmlElement(ElementName="Disc", Type=typeof(Disc))]
        public object particle;
        public ParticleType particleType;

        public enum ParticleType {
            [XmlEnum("Point")] Point,
            [XmlEnum("Line")] Line,
            [XmlEnum("Triangle")] Triangle,
            [XmlEnum("Plane")] Plane,
            [XmlEnum("Rect")] Rectangle,
            [XmlEnum("Box")] BoxBoxParticle,
            [XmlEnum("Sphere")] Sphere,
            [XmlEnum("Cylinder")] Cylinder,
            [XmlEnum("Cone")] Cone,
            [XmlEnum("Blob")] Blob,
            [XmlEnum("Disc")] Disc,
        }
   }


    [Serializable]
    [XmlRoot(ElementName="Point")]
    public class Point : W3D
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;
    }


    [Serializable]
    [XmlRoot(ElementName="Line")]
    public class Line : W3D
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Triangle")]
    public class Triangle : W3D
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;

        [XmlAttribute(AttributeName="p3")]
        public string p3String;
    }


    [Serializable]
    [XmlRoot(ElementName="Plane")]
    public class Plane : W3D
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;

        [XmlAttribute(AttributeName="normal")]
        public string normalString;
    }


    [Serializable]
    [XmlRoot(ElementName="Rectangle")]
    public class Rectangle : W3D
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="u-dir")]
        public string uString;

        [XmlAttribute(AttributeName="v-dir")]
        public string vStringl;
    }


    [Serializable]
    [XmlRoot(ElementName="Box")]
    public class BoxBoxParticle : W3D
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Sphere")]
    public class Sphere : W3D
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString;

        [XmlAttribute(AttributeName="radius")]
        public string radiusString;

        [XmlAttribute(AttributeName="radius-inner")]
        public string innerRadiusString;
    }


    [Serializable]
    [XmlRoot(ElementName="Cylinder")]
    public class Cylinder : W3D
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;

        [XmlAttribute(AttributeName="radius")]
        public double radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Cone")]
    public class Cone : W3D
    {
        [XmlAttribute(AttributeName="base-center")]
        public string baseCenterString;

        [XmlAttribute(AttributeName="apex")]
        public string apexString;

        [XmlAttribute(AttributeName="radius")]
        public double radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Blob")]
    public class Blob : W3D
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString;

        [XmlAttribute(AttributeName="stdev")]
        public double deviation;
    }


    [Serializable]
    [XmlRoot(ElementName="Disc")]
    public class Disc : W3D
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString;

        [XmlAttribute(AttributeName="normal")]
        public string normal;

        [XmlAttribute(AttributeName="radius")]
        public float radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    /********** BASE CLASS              ***********/


    [Serializable]
    public class W3D
    {
        public string pprint()
        {
            return JsonUtility.ToJson(this, true);
        }

        static public Color ConvertColor(string colorString)
        {
            string[] strings=colorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Color(
                float.Parse(strings[0]) / 255,
                float.Parse(strings[1]) / 255,
                float.Parse(strings[2]) / 255
            );
        }

        static public Vector3 ConvertVector3(string vectorString)
        {
            string[] strings=vectorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Vector3(
                float.Parse(strings[0]),
                float.Parse(strings[1]),
                float.Parse(strings[2])
            );
        }
    }


    // Reference another class/object by name
    public class Reference : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }
}
using System;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using UnityEngine;


namespace W3D
{


    /********** STORY            ***********/


    [Serializable]
    [XmlRoot(ElementName="Story")]
    public class Story : Xml
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
    public class About : Xml
    {
        [XmlAttribute(AttributeName="news")]
        public string news;
    }


    /********** OBJECT            ***********/


    [Serializable]
    [XmlRoot(ElementName="Object")]
    public class Object : Xml
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
        public float scale;

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
    public class Content : Xml
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
    public class Text : Xml
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
    public class Image : Xml
    {
        [XmlAttribute(AttributeName="filename")]
        public string filename;

    }


    [Serializable]
    [XmlRoot(ElementName="StereoImage")]
    public class StereoImage : Xml
    {
        [XmlAttribute(AttributeName="left-image")]
        public string leftImage;

        [XmlAttribute(AttributeName="right-image")]
        public string rightImage;

    }


    [Serializable]
    [XmlRoot(ElementName="Model")]
    public class Model : Xml
    {
        [XmlAttribute(AttributeName="filename")]
        public string filename;

        [XmlAttribute(AttributeName="check-collisions")]
        public string checkCollisions;
    }


    [Serializable]
    [XmlRoot(ElementName="ParticleSystem")]
    // TODO: Unity has a ParticleSystem class
    public class ParticleSystem : Xml
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
    public class Light : Xml
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
    public class Spot : Xml
    {
        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // LINK


    [Serializable]
    [XmlRoot(ElementName="Link")]
    public class Link : Xml
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
    public class Clicks : Xml
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
    public class NumClicks : Xml
    {
        [XmlAttribute(AttributeName="num_clicks")]
        public uint numClicks;

        [XmlAttribute(AttributeName="reset")]
        public bool reset;
    }


    /********** GROUP            ***********/


    [Serializable]
    [XmlRoot(ElementName="Group")]
    public class Group : Xml
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
    public class Timeline : Xml
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
    public class Sound : Xml
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
    public class Mode : Xml
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
    public class Repeat : Xml
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
    public class Settings : Xml
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
    public class EventTrigger : Xml
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
    public class HeadTrack : Xml
    {
        [XmlElement(ElementName="Position")]
        public TrackPosition Position;

        [XmlElement(ElementName="Direction")]
        public Direction Direction;
    }


    [Serializable]
    [XmlRoot(ElementName="Position")]
    public class TrackPosition : Xml
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
    public class Direction : Xml
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
    public class PointTarget : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;

    }


    [Serializable]
    [XmlRoot(ElementName="DirectionTarget")]
    public class DirectionTarget : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // MOVE TRACK


    [Serializable]
    [XmlRoot(ElementName="MoveTrack")]
    public class MoveTrack : Xml
    {
        [XmlElement(ElementName="Source")]
        public Source Source;

        [XmlElement(ElementName="Box")]
        public Box Box;

    }


    [Serializable]
    [XmlRoot(ElementName="Source")]
    public class Source : Xml
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
    public class Box : Xml
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
    public class Movement : Xml
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
    public class ParticleActionList : Xml
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
    public class ParticleSource : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="rate")]
        public double rate;
    }


    [Serializable]
    [XmlRoot(ElementName="Vel")]
    public class Vel : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;
    }


    // PARTICLE ACTION


    [Serializable]
    [XmlRoot(ElementName="ParticleAction")]
    public class ParticleAction : Xml
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
    public class Avoid : Xml
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
    public class Bounce : Xml
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
    public class Gravity : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString;
    }


    [Serializable]
    [XmlRoot(ElementName="Damping")]
    public class Damping : Xml
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
    public class Gravitate : Xml
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
    public class Follow : Xml
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
    public class MatchVel : Xml
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
    public class OrbitPoint : Xml
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
    public class Jet : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlElement(ElementName="AccelDomain")]
        public Particle AccelDomain;
    }


    [Serializable]
    [XmlRoot(ElementName="TargetColor")]
    public class TargetColor : Xml
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
    public class RemoveCondition : Xml
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
    public class Age : Xml
    {
        [XmlAttribute(AttributeName="age")]
        public double age;

        [XmlAttribute(AttributeName="younger-than")]
        public bool youngerThan;
    }


    [Serializable]
    public class Remove : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="inside")]
        public bool inside;
    }


    /********** GLOBAL              ***********/


    [Serializable]
    [XmlRoot(ElementName="Global")]
    public class Global : Xml
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
    public class Camera : Xml
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
    public class Background : Xml
    {
        [XmlAttribute(AttributeName="color")]
        public string colorString;
    }


    [Serializable]
    [XmlRoot(ElementName="WandNavigation")]
    public class WandNavigation : Xml
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
    public class Placement : Xml
    {
        [XmlElement(ElementName="RelativeTo")]
        public RelativeTo relativeTo;

        [XmlElement(ElementName="Position")]
        public string positionString;

        [XmlChoiceIdentifier("rotationType")]
        [XmlElement(ElementName="Axis", Type=typeof(Axis))]
        [XmlElement(ElementName="LookAt", Type=typeof(LookAt))]
        [XmlElement(ElementName="Normal", Type=typeof(Normal))]
        public object rotation;
        public RotationType rotationType;
        public enum RotationType {
            Null,
            [XmlEnum("Axis")] Axis,
            [XmlEnum("LookAt")] LookAt,
            [XmlEnum("Normal")] Normal,
        }

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;

        public enum RelativeTo {
            Center,
            FrontWall,
            LeftWall,
            RightWall,
            FloorWall
        }

        /** Set parent GameObject and local transforms of gameObjectT
            relativeTo: [GameObject].transform.parent
            position: [GameObject].transform.localPosition
            Axis: Local rotation around Axis 
            LookAt: Rotate to look at target vector
            Normal: Local rotation around a normalized vector
        */
        public void SetTransform(Transform gameObjectT, float scale, Transform rootT) {
            // Set parent, position, and scale
            gameObjectT.parent = 
                this.relativeTo == Placement.RelativeTo.Center
                    ? rootT // There's no "center wall" - just make relative to Story
                    : rootT.Find(this.relativeTo.ToString());
            gameObjectT.localScale = Vector3.one * scale;
            gameObjectT.localPosition = Xml.ConvertVector3(this.positionString);

            // TODO: Set localRotation based off Axis, LookAt, and Normal are a choice (?)
            switch(this.rotationType) {
                case(Placement.RotationType.Null): {
                    // No rotation
                    gameObjectT.localRotation = Quaternion.identity;
                    break;
                }
                case(Placement.RotationType.Axis): {
                    // Set local rotation directly
                    Axis axis = (Axis)this.rotation;
                    gameObjectT.localEulerAngles = axis.GetEuler();
                    break;
                }
                case(Placement.RotationType.LookAt): {
                    // Rotate to look at the target in world space
                    LookAt lookAt = (LookAt)this.rotation;
                    gameObjectT.LookAt(
                        rootT.TransformPoint(Xml.ConvertVector3(lookAt.targetString)),
                        Xml.ConvertVector3(lookAt.upString)
                    );
                    break;
                }
                case(Placement.RotationType.Normal): {
                    // TODO
                    break;
                }
                default: break;
            }
            return;
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Axis")]
    public class Axis : Xml
    {
        [XmlAttribute(AttributeName="rotation")]
        public string rotationString;

        [XmlAttribute(AttributeName="angle")]
        public float angle;

        public Vector3 GetEuler() {
            return Xml.ConvertVector3(this.rotationString) * this.angle;
        }
    }


    [Serializable]
    [XmlRoot(ElementName="LookAt")]
    public class LookAt : Xml
    {
        [XmlAttribute(AttributeName="target")]
        public string targetString;

        [XmlAttribute(AttributeName="up")]
        public string upString;
    }


    [Serializable]
    [XmlRoot(ElementName="Normal")]
    public class Normal : Xml
    {
        [XmlAttribute(AttributeName="normal")]
        public string normalString;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // ACTIONS TYPE


    [Serializable]
    public class Actions : Xml
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
    public class MoveCave : Xml
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
    public class Transition : Xml
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
    public class MovementTransition : Xml
    {
        [XmlElement(ElementName="Placement")]
        public Placement Placement;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveRel")]
    public class MoveRel : Xml
    {
        [XmlElement(ElementName="Placement")]
        public Placement Placement;

    }


    [Serializable]
    [XmlRoot(ElementName="Sound")]
    public class SoundTransition : Xml
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
    public class LinkTransition : Xml
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
    public class Particle : Xml
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
    public class Point : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;
    }


    [Serializable]
    [XmlRoot(ElementName="Line")]
    public class Line : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Triangle")]
    public class Triangle : Xml
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
    public class Plane : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString;

        [XmlAttribute(AttributeName="normal")]
        public string normalString;
    }


    [Serializable]
    [XmlRoot(ElementName="Rectangle")]
    public class Rectangle : Xml
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
    public class BoxBoxParticle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String;

        [XmlAttribute(AttributeName="p2")]
        public string p2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Sphere")]
    public class Sphere : Xml
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
    public class Cylinder : Xml
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
    public class Cone : Xml
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
    public class Blob : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString;

        [XmlAttribute(AttributeName="stdev")]
        public double deviation;
    }


    [Serializable]
    [XmlRoot(ElementName="Disc")]
    public class Disc : Xml
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
    public class Xml
    {
        public string pprint()
        {
            return JsonUtility.ToJson(this, true);
        }

        // Converts "[int], [int], [int]" to a UnityEngine.Color object
        static public Color ConvertColor(string colorString)
        {
            string[] strings=colorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Color(
                float.Parse(strings[0]) / 255,
                float.Parse(strings[1]) / 255,
                float.Parse(strings[2]) / 255
            );
        }

        // Converts a "([float], [float], [float])" string to a UnityEngine.Vector3 object
        static public Vector3 ConvertVector3(string vectorString)
        {
            string[] strings=vectorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Vector3(
                float.Parse(strings[0]),
                float.Parse(strings[1]),
                float.Parse(strings[2]) * -1 // The z axis is inverted in Unity 
            );
        }
    }


    // Reference another class/object by name
    public class Reference : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }
}
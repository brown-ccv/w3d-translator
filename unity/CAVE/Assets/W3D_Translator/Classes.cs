using System;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;
using System.Collections.Generic;
using System.IO;
using UnityEngine;


namespace W3D
{
    [Serializable]
    public class Xml
    {
        public string pprint() { return JsonUtility.ToJson(this, true); }

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
        public List<PlacementType> PlacementRoot;
    
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
        public string colorString
        {
            get { return color.ToString(); }
            set { color = ConvertColor(value); }
        }
        public Color color;

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
        public PlacementType Placement;

        [XmlElement(ElementName="Content")]
        public Content Content;

        [XmlArray(ElementName="LinkRoot")]
        [XmlArrayItem(ElementName="Link")]
        public List<Link> LinkRoot;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    // CONTENT


    [Serializable]
    [XmlRoot(ElementName="Content")]
    public class Content : Xml
    {
        [XmlElement(ElementName="None")]
        public object None;

        [XmlElement(ElementName="Text")]
        public Text Text;

        [XmlElement(ElementName="Image")]
        public Image Image;

        [XmlElement(ElementName="StereoImage")]
        public StereoImage StereoImage;

        [XmlElement(ElementName="Model")]
        public Model Model;

        [XmlElement(ElementName="Light")]
        public Light Light;

        [XmlElement(ElementName="ParticleSystem")]
        public ParticleSystem ParticleSystem;
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
    public class Light : Xml
    {
        [XmlElement(ElementName="Point")]
        public object Point;

        [XmlElement(ElementName="Directional")]
        public object Directional;

        [XmlElement(ElementName="Spot")]
        public object Spot;

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
        public string enabledColorString
        {
            get { return enabledColor.ToString(); }
            set { enabledColor= ConvertColor(value); }
        }
        public Color enabledColor;

        [XmlElement(ElementName="SelectedColor")]
        public string selectedColorString
        {
            get { return selectedColor.ToString(); }
            set { selectedColor= ConvertColor(value); }
        }
        public Color selectedColor;

        [XmlElement(ElementName="Actions")]
        public List<Actions> Actions;
    }


    // Link.Actions


    [Serializable]
    [XmlRoot(ElementName="Actions")]
    public class Actions : ActionsType
    {
        [XmlElement(ElementName="Clicks")]
        public Clicks Clicks;
    }


    [Serializable]
    [XmlRoot(ElementName="Clicks")]
    public class Clicks : Xml
    {
        [XmlElement(ElementName="Any")]
        public object Any;

        [XmlElement(ElementName="NumClicks")]
        public NumClicks NumClicks;


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
        [XmlElement(ElementName="Objects")]
        public List<Objects> Objects;

        [XmlElement(ElementName="Groups")]
        public List<Groups> Groups;

        [XmlAttribute(AttributeName="name")]
        public string name;

    }


    [Serializable]
    [XmlRoot(ElementName="Objects")]
    public class Objects : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [Serializable]
    [XmlRoot(ElementName="Groups")]
    public class Groups : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
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
    public class TimedActions : ActionsType
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
        [XmlElement(ElementName="Positional")]
        public object Positional;

        [XmlElement(ElementName="Fixed")]
        public object Fixed;
    }


    [Serializable]
    [XmlRoot(ElementName="Repeat")]
    public class Repeat : Xml
    {
        [XmlElement(ElementName="NoRepeat")]
        public object NoRepeat;

        [XmlElement(ElementName="RepeatForever")]
        public object RepeatForever;

        [XmlElement(ElementName="RepeatNum")]
        public uint repeatNum;
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

        [XmlElement(ElementName="HeadTrack")]
        public HeadTrack HeadTrack;

        [XmlElement(ElementName="MoveTrack")]
        public MoveTrack MoveTrack;

        [XmlElement(ElementName="Actions")]
        public List<ActionsType> Actions;

        [XmlAttribute(AttributeName="enabled")]
        public bool enabled;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlAttribute(AttributeName="remain-enabled")]
        public bool remainEnabled;
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
        [XmlElement(ElementName="Anywhere")]
        public object Anywhere;

        [XmlElement(ElementName="Box")]
        public Box Box;
    }


    // HeadTrack.Direction


    [Serializable]
    [XmlRoot(ElementName="Direction")]
    public class Direction : Xml
    {
        [XmlElement(ElementName="None")]
        public object None;

        [XmlElement(ElementName="PointTarget")]
        public PointTarget PointTarget;

        [XmlElement(ElementName="DirectionTarget")]
        public DirectionTarget DirectionTarget;

        [XmlElement(ElementName="ObjectTarget")]
        public ObjectTarget ObjectTarget;
    }


    [Serializable]
    [XmlRoot(ElementName="PointTarget")]
    public class PointTarget : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString
        {
            get { return point.ToString(); }
            set { point= ConvertVector3(value); }
        }
        public Vector3 point;

        [XmlAttribute(AttributeName="angle")]
        public double angle;

    }
    [Serializable]
    [XmlRoot(ElementName="DirectionTarget")]
    public class DirectionTarget : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString
        {
            get { return direction.ToString(); }
            set { direction= ConvertVector3(value); }
        }
        public Vector3 direction;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    [Serializable]
    [XmlRoot(ElementName="ObjectTarget")]
    public class ObjectTarget : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
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
        [XmlElement(ElementName="ObjectRef")]
        public ObjectRef ObjectRef;

        [XmlElement(ElementName="GroupObj")]
        public GroupObj GroupObj;
    }


    [Serializable]
    [XmlRoot(ElementName="ObjectRef")]
    public class ObjectRef : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;

    }


    [Serializable]
    [XmlRoot(ElementName="GroupObj")]
    public class GroupObj : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;

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
        public string corner1String
        {
            get { return corner1.ToString(); }
            set { corner1= ConvertVector3(value); }
        }
        public Vector3 corner1;

        [XmlAttribute(AttributeName="corner2")]
        public string corner2String
        {
            get { return corner2.ToString(); }
            set { corner2= ConvertVector3(value); }
        }
        public Vector3 corner2;
    }


    [Serializable]
    [XmlRoot(ElementName="Movement")]
    public class Movement : Xml
    {

        [XmlElement(ElementName="Outside")]
        public object Outside;

        [XmlElement(ElementName="Inside")]
        public object Inside;
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
        public ParticleDomainType ParticleDomain;

        [XmlAttribute(AttributeName="rate")]
        public double rate;
    }


    [Serializable]
    [XmlRoot(ElementName="Vel")]
    public class Vel : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;
    }


    // PARTICLE ACTION


    [Serializable]
    [XmlRoot(ElementName="ParticleAction")]
    public class ParticleAction : Xml
    {
        [XmlElement(ElementName="Avoid")]
        public Avoid Avoid;

        [XmlElement(ElementName="Bounce")]
        public Bounce Bounce;

        [XmlElement(ElementName="Gravity")]
        public Gravity Gravity;

        [XmlElement(ElementName="Damping")]
        public Damping Damping;

        [XmlElement(ElementName="Gravitate")]
        public Gravitate Gravitate;

        [XmlElement(ElementName="Follow")]
        public Follow Follow;

        [XmlElement(ElementName="MatchVel")]
        public MatchVel MatchVel;

        [XmlElement(ElementName="OrbitPoint")]
        public OrbitPoint OrbitPoint;

        [XmlElement(ElementName="Jet")]
        public Jet Jet;

        [XmlElement(ElementName="RandomVel")]
        public object randomVelocity;

        [XmlElement(ElementName="RandomAccel")]
        public object randomAcceleration;

        [XmlElement(ElementName="RandomDisplace")]
        public object randomDisplacement;

        [XmlElement(ElementName="TargetColor")]
        public TargetColor TargetColor;

        [XmlElement(ElementName="TargetSize")]
        public object targetSize;

        [XmlElement(ElementName="TargetVel")]
        public object targetVelocity;
    }


    [Serializable]
    [XmlRoot(ElementName="Avoid")]
    public class Avoid : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

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
        public ParticleDomainType ParticleDomain;

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
        public string directionString
        {
            get { return direction.ToString(); }
            set { direction= ConvertVector3(value); }
        }
        public Vector3 direction;
    }


    [Serializable]
    [XmlRoot(ElementName="Damping")]
    public class Damping : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string directionString
        {
            get { return direction.ToString(); }
            set { direction= ConvertVector3(value); }
        }
        public Vector3 direction;

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
        public string centerString
        {
            get { return center.ToString(); }
            set { center= ConvertVector3(value); }
        }
        public Vector3 center;
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
        public ParticleDomainType ParticleDomain;

        [XmlElement(ElementName="AccelDomain")]
        public ParticleDomainType AccelDomain;
    }


    [Serializable]
    [XmlRoot(ElementName="TargetColor")]
    public class TargetColor : Xml
    {
        [XmlAttribute(AttributeName="color")]
        public string colorString
        {
            get { return color.ToString(); }
            set { color= ConvertColor(value); }
        }
        public Color color;

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

        [XmlElement(ElementName="Age")]
        public Age Age;

        [XmlElement(ElementName="Position")]
        public Position Position;

        [XmlElement(ElementName="Velocity")]
        public Velocity Velocity;
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
    [XmlRoot(ElementName="Position")]
    public class Position : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

        [XmlAttribute(AttributeName="inside")]
        public bool inside;
    }


    [Serializable]
    [XmlRoot(ElementName="Velocity")]
    public class Velocity : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

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
        public PlacementType Placement;

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
        public string colorString
        {
            get { return color.ToString(); }
            set { color= ConvertColor(value); }
        }
        public Color color;

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
    public class PlacementType : Xml
    {
        [XmlElement(ElementName="RelativeTo")]
        public string relativeTo;

        [XmlElement(ElementName="Position")]
        public string positionString
        {
            get { return position.ToString(); }
            set { position= ConvertVector3(value); }
        }
        public Vector3 position;

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
    public class Axis : Xml
    {
        [XmlAttribute(AttributeName="rotation")]
        public string rotationString
        {
            get { return rotation.ToString(); }
            set { rotation= ConvertVector3(value); }
        }
        public Vector3 rotation;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    [Serializable]
    [XmlRoot(ElementName="LookAt")]
    public class LookAt : Xml
    {
        [XmlAttribute(AttributeName="target")]
        public string targetString
        {
            get { return target.ToString(); }
            set { target= ConvertVector3(value); }
        }
        public Vector3 target;

        [XmlAttribute(AttributeName="up")]
        public string upString
        {
            get { return up.ToString(); }
            set { up= ConvertVector3(value); }
        }
        public Vector3 up;
    }


    [Serializable]
    [XmlRoot(ElementName="Normal")]
    public class Normal : Xml
    {
        [XmlAttribute(AttributeName="normal")]
        public string normalString
        {
            get { return normal.ToString(); }
            set { normal= ConvertVector3(value); }
        }
        public Vector3 normal;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // ACTIONS TYPE


    [Serializable]
    // TODO: Enum?
    public class ActionsType : Xml
    {
        [XmlElement(ElementName="ObjectChange")]
        public ObjectChange ObjectChange;

        [XmlElement(ElementName="GroupRef")]
        public GroupRef GroupRef;

        [XmlElement(ElementName="TimerChange")]
        public TimerChange TimerChange;

        [XmlElement(ElementName="SoundRef")]
        public SoundRef SoundRef;

        [XmlElement(ElementName="Event")]
        public Event Event;

        [XmlElement(ElementName="MoveCave")]
        public MoveCave MoveCave;

        [XmlElement(ElementName="Restart")]
        public object Restart;
    }


    [Serializable]
    [XmlRoot(ElementName="ObjectChange")]
    public class ObjectChange : Xml
    {
        [XmlElement(ElementName="Transition")]
        public TransitionType Transition;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="GroupRef")]
    public class GroupRef : Xml
    {
        [XmlElement(ElementName="Transition")]
        public TransitionType Transition;

        [XmlAttribute(AttributeName="name")]
        public string name;

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
    public class TimerChange : Xml
    {
        [XmlElement(ElementName="start")]
        public object start;

        [XmlElement(ElementName="stop")]
        public object stop;

        [XmlElement(ElementName="continue")]
        public object continueTimer;

        [XmlElement(ElementName="start_if_not_started")]
        public object startIfNotStarted;

        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [Serializable]
    [XmlRoot(ElementName="SoundRef")]
    public class SoundRef : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [Serializable]
    [XmlRoot(ElementName="Event")]
    public class Event : Xml
    {
        [XmlAttribute(AttributeName="enable")]
        public bool enable;

        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveCave")]
    public class MoveCave : Xml
    {
        [XmlElement(ElementName="Relative")]
        public object Relative;

        [XmlElement(ElementName="Absolute")]
        public object Absolute;

        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlText]
        public string text;
    }


    // TRANSITION TYPE

 
    [Serializable]
    public class TransitionType : Xml
    {
        [XmlElement(ElementName="Visible")]
        public bool visible;

        [XmlElement(ElementName="Movement")]
        public MovementTransition Movement;

        [XmlElement(ElementName="MoveRel")]
        public MoveRel MoveRel;

        [XmlElement(ElementName="Color")]
        public string colorString
        {
            get { return color.ToString(); }
            set { color= ConvertColor(value); }
        }
        public Color color;

        [XmlElement(ElementName="Scale")]
        public double scale;

        [XmlElement(ElementName="Sound")]
        public SoundTransition Sound;

        [XmlElement(ElementName="LinkChange")]
        public LinkChange LinkChange;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="Movement")]
    public class MovementTransition : Xml
    {
        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveRel")]
    public class MoveRel : Xml
    {
        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;

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
    public class LinkChange : Xml
    {
        [XmlElement(ElementName="link_on")]
        public object on;

        [XmlElement(ElementName="link_off")]
        public object off;

        [XmlElement(ElementName="activate")]
        public object activate;

        [XmlElement(ElementName="activate_if_on")]
        public object activateIfOn;
    }


    // PARTICLE DOMAIN TYPE


    [Serializable]
    [XmlRoot(ElementName="ParticleDomain")]
    public class ParticleDomainType : Xml
    {
        [XmlElement(ElementName="Point")]
        public Point Point;

        [XmlElement(ElementName="Line")]
        public Line Line;

        [XmlElement(ElementName="Triangle")]
        public Triangle Triangle;

        [XmlElement(ElementName="Plane")]
        public Plane Plane;

        [XmlElement(ElementName="Rect")]
        public Rectangle Rectangle;

        [XmlElement(ElementName="Box")]
        public Box Box;

        [XmlElement(ElementName="Sphere")]
        public Sphere Sphere;

        [XmlElement(ElementName="Cylinder")]
        public Cylinder Cylinder;

        [XmlElement(ElementName="Cone")]
        public Cone Cone;

        [XmlElement(ElementName="Blob")]
        public Blob Blob;

        [XmlElement(ElementName="Disc")]
        public Disc Disc;
    }


    [Serializable]
    [XmlRoot(ElementName="Point")]
    public class Point : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString
        {
            get { return point.ToString(); }
            set { point= ConvertVector3(value); }
        }
        public Vector3 point;

    }


    [Serializable]
    [XmlRoot(ElementName="Line")]
    public class Line : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String
        {
            get { return p1.ToString(); }
            set { p1= ConvertVector3(value); }
        }
        public Vector3 p1;

        [XmlAttribute(AttributeName="p2")]
        public string p2String
        {
            get { return p2.ToString(); }
            set { p2= ConvertVector3(value); }
        }
        public Vector3 p2;
    }


    [Serializable]
    [XmlRoot(ElementName="Triangle")]
    public class Triangle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String
        {
            get { return p1.ToString(); }
            set { p1= ConvertVector3(value); }
        }
        public Vector3 p1;

        [XmlAttribute(AttributeName="p2")]
        public string p2String
        {
            get { return p2.ToString(); }
            set { p2= ConvertVector3(value); }
        }
        public Vector3 p2;

        [XmlAttribute(AttributeName="p3")]
        public string p3String
        {
            get { return p3.ToString(); }
            set { p3= ConvertVector3(value); }
        }
        public Vector3 p3;
    }


    [Serializable]
    [XmlRoot(ElementName="Plane")]
    public class Plane : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string pointString
        {
            get { return point.ToString(); }
            set { point= ConvertVector3(value); }
        }
        public Vector3 point;

        [XmlAttribute(AttributeName="normal")]
        public string normalString
        {
            get { return normal.ToString(); }
            set { normal= ConvertVector3(value); }
        }
        public Vector3 normal;
    }


    [Serializable]
    [XmlRoot(ElementName="Rectangle")]
    public class Rectangle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String
        {
            get { return p1.ToString(); }
            set { p1= ConvertVector3(value); }
        }
        public Vector3 p1;

        [XmlAttribute(AttributeName="u-dir")]
        public string uString
        {
            get { return u.ToString(); }
            set { u= ConvertVector3(value); }
        }
        public Vector3 u;

        [XmlAttribute(AttributeName="v-dir")]
        public string vString
        {
            get { return v.ToString(); }
            set { v= ConvertVector3(value); }
        }
        public Vector3 v;
    }


    [Serializable]
    [XmlRoot(ElementName="Box")]
    public class BoxParticle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String
        {
            get { return p1.ToString(); }
            set { p1= ConvertVector3(value); }
        }
        public Vector3 p1;

        [XmlAttribute(AttributeName="p2")]
        public string p2String
        {
            get { return p2.ToString(); }
            set { p2= ConvertVector3(value); }
        }
        public Vector3 p2;
    }


    [Serializable]
    [XmlRoot(ElementName="Sphere")]
    public class Sphere : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString
        {
            get { return center.ToString(); }
            set { center= ConvertVector3(value); }
        }
        public Vector3 center;

        [XmlAttribute(AttributeName="radius")]
        public string radiusString
        {
            get { return radius.ToString(); }
            set { radius= ConvertVector3(value); }
        }
        public Vector3 radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public string innerRadiusString
        {
            get { return innerRadius.ToString(); }
            set { innerRadius= ConvertVector3(value); }
        }
        public Vector3 innerRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Cylinder")]
    public class Cylinder : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string p1String
        {
            get { return p1.ToString(); }
            set { p1= ConvertVector3(value); }
        }
        public Vector3 p1;

        [XmlAttribute(AttributeName="p2")]
        public string p2String
        {
            get { return p2.ToString(); }
            set { p2= ConvertVector3(value); }
        }
        public Vector3 p2;

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
        public string baseCenterString
        {
            get { return baseCenter.ToString(); }
            set { baseCenter= ConvertVector3(value); }
        }
        public Vector3 baseCenter;

        [XmlAttribute(AttributeName="apex")]
        public string apexString
        {
            get { return apex.ToString(); }
            set { apex= ConvertVector3(value); }
        }
        public Vector3 apex;

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
        public string centerString
        {
            get { return center.ToString(); }
            set { center= ConvertVector3(value); }
        }
        public Vector3 center;

        [XmlAttribute(AttributeName="stdev")]
        public double deviation;
    }


    [Serializable]
    [XmlRoot(ElementName="Disc")]
    public class Disc : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string centerString
        {
            get { return center.ToString(); }
            set { center= ConvertVector3(value); }
        }
        public Vector3 center;

        [XmlAttribute(AttributeName="normal")]
        public string normal;

        [XmlAttribute(AttributeName="radius")]
        public float radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }
}

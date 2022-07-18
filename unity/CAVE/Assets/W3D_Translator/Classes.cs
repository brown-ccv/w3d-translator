using System.Xml.Serialization;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

// TODO: Convert vector types to Unity Vector3
// TODO: Add color, vector, and file class types (custom string translation)

namespace W3D
{
    using Newtonsoft.Json;

    /********** STORY            ***********/


    [XmlRoot(ElementName="Story")]
    public class Story : W3D
    {
        [XmlElement(ElementName="ObjectRoot")]
        public ObjectRoot ObjectRoot;

        [XmlElement(ElementName="GroupRoot")]
        public GroupRoot GroupRoot;

        [XmlElement(ElementName="TimelineRoot")]
        public TimelineRoot TimelineRoot;

        [XmlElement(ElementName="PlacementRoot")]
        public PlacementRoot PlacementRoot;

        [XmlElement(ElementName="SoundRoot")]
        public SoundRoot SoundRoot;

        [XmlElement(ElementName="EventRoot")]
        public EventRoot EventRoot;

        [XmlElement(ElementName="ParticleActionRoot")]
        public ParticleActionRoot ParticleActionRoot;

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

    [XmlRoot(ElementName="ObjectRoot")]
    public class ObjectRoot : W3D
    {
        [XmlElement(ElementName="Object")]
        public List<Object> Object;
    }


    [XmlRoot(ElementName="GroupRoot")]
    public class GroupRoot : W3D
    {
        [XmlElement(ElementName="Group")]
        public List<Group> Group;
    }


    [XmlRoot(ElementName="TimelineRoot")]
    public class TimelineRoot : W3D
    {

        [XmlElement(ElementName="Timeline")]
        public List<Timeline> Timeline;
    }


    [XmlRoot(ElementName="PlacementRoot")]
    public class PlacementRoot : W3D
    {
        [XmlElement(ElementName="Placement")]
        public List<PlacementType> Placement;
    }


    [XmlRoot(ElementName="SoundRoot")]
    public class SoundRoot : W3D
    {
        [XmlElement(ElementName="Sound")]
        public List<Sound> Sound;
    }


    [XmlRoot(ElementName="EventRoot")]
    public class EventRoot : W3D
    {
        [XmlElement(ElementName="EventTrigger")]
        public List<EventTrigger> EventTrigger;
    }


    [XmlRoot(ElementName="ParticleActionRoot")]
    public class ParticleActionRoot : W3D
    {
        [XmlElement(ElementName="ParticleActionList")]
        public List<ParticleActionList> ParticleActionList;
    }


    [XmlRoot(ElementName="About")]
    public class About : W3D
    {
        [XmlAttribute(AttributeName="About")]
        public string news;
    }


    /********** OBJECT            ***********/


    [XmlRoot(ElementName="Object")]
    public class Object : W3D
    {
        [XmlElement(ElementName="Visible")]
        public bool visible;

        [XmlElement(ElementName="Color")]
        public string Color;

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

        [XmlElement(ElementName="LinkRoot")]
        public LinkRoot LinkRoot;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    // CONTENT


    // TODO: Enum?
    [XmlRoot(ElementName="Content")]
    public class Content : W3D
    {
        // TODO: Just make content null
        [XmlElement(ElementName="None")]
        public object None;

        [XmlElement(ElementName="Text")]
        public Text Text;

        [XmlElement(ElementName="Image")]
        public Image Image;

        [XmlElement(ElementName="StereoImage")]
        public StereoImage StereoImage;

        // TODO: Model
        [XmlElement(ElementName="Model")]
        public Model Model;

        [XmlElement(ElementName="Light")]
        public Light Light;

        [XmlElement(ElementName="ParticleSystem")]
        public ParticleSystem ParticleSystem;
    }


    [XmlRoot(ElementName="Text")]
    public class Text : W3D
    {

        [XmlElement(ElementName="text")]
        public List<string> text;

        // TODO: Enum
        [XmlAttribute(AttributeName="horiz-align")]
        public string horizontalAlign;

        // TODO: Enum
        [XmlAttribute(AttributeName="vert-align")]
        public string verticalAlign;

        [XmlAttribute(AttributeName="font")]
        public string font;

        [XmlAttribute(AttributeName="depth")]
        public double depth;
    }


    [XmlRoot(ElementName="Image")]
    public class Image : W3D
    {
        // TODO: file simple type
        [XmlAttribute(AttributeName="filename")]
        public string filename;
    }

    [XmlRoot(ElementName="StereoImage")]
    public class StereoImage : W3D
    {
        // TODO: file simple type
        [XmlAttribute(AttributeName="left-image")]
        public string leftImage;

        // TODO: file simple type
        [XmlAttribute(AttributeName="right-image")]
        public string rightImage;
    }

    [XmlRoot(ElementName="Model")]
    public class Model : W3D
    {
        // TODO: file simple type
        [XmlAttribute(AttributeName="filename")]
        public string filename;

        [XmlAttribute(AttributeName="check-collisions")]
        public string checkCollisions;
    }


    [XmlRoot(ElementName="ParticleSystem")]
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


    [XmlRoot(ElementName="Light")]
    public class Light : W3D
    {
        // TODO: Enum (Point, Directional, Spot)
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

    [XmlRoot(ElementName="Spot")]
    public class Spot : W3D
    {
        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // LINK


    [XmlRoot(ElementName="LinkRoot")]
    public class LinkRoot : W3D
    {
        [XmlElement(ElementName="Link")]
        public List<Link> Link;
    }


    [XmlRoot(ElementName="Link")]
    public class Link : W3D
    {
        [XmlElement(ElementName="Enabled")]
        public bool enabled;

        [XmlElement(ElementName="RemainEnabled")]
        public bool remainEnabled;

        // TODO: color simple type
        [XmlElement(ElementName="EnabledColor")]
        public string enabledColor;

        // TODO: color simple type
        [XmlElement(ElementName="SelectedColor")]
        public string selectedColor;

        [XmlElement(ElementName="Actions")]
        public Actions Actions;
    }


    // Link.Actions


    [XmlRoot(ElementName="Actions")]
    public class Actions : ActionsType
    {
        // TODO: Enum
        [XmlElement(ElementName="Clicks")]
        public Clicks Clicks;
    }


    [XmlRoot(ElementName="Clicks")]
    public class Clicks : W3D
    {
        [XmlElement(ElementName="Any")]
        public object Any;

        [XmlElement(ElementName="NumClicks")]
        public NumClicks NumClicks;


    }


    [XmlRoot(ElementName="NumClicks")]
    public class NumClicks : W3D
    {
        [XmlAttribute(AttributeName="num_clicks")]
        public uint numClicks;

        [XmlAttribute(AttributeName="reset")]
        public bool reset;
    }


    /********** GROUP            ***********/


    [XmlRoot(ElementName="Group")]
    public class Group : W3D
    {
        [XmlElement(ElementName="Objects")]
        public List<Objects> Objects;

        [XmlElement(ElementName="Groups")]
        public List<Groups> Groups;

        [XmlAttribute(AttributeName="name")]
        public string name;
    }

    [XmlRoot(ElementName="Objects")]
    public class Objects : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [XmlRoot(ElementName="Groups")]
    public class Groups : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    /********** TIMELINE        ***********/


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


    [XmlRoot(ElementName="TimedActions")]
    public class TimedActions : ActionsType
    {
        [XmlAttribute(AttributeName="seconds-time")]
        public double secondsTime;

        [XmlText]
        public string text;
    }


    /********** SOUND            ***********/


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

        // TODO: file simple type
        [XmlAttribute(AttributeName="filename")]
        public string filename;

        [XmlAttribute(AttributeName="autostart")]
        public bool autostart;
    }


    // TODO Make an enum
    [XmlRoot(ElementName="Mode")]
    public class Mode : W3D
    {
        [XmlElement(ElementName="Positional")]
        public object Positional;

        [XmlElement(ElementName="Fixed")]
        public object Fixed;
    }


    [XmlRoot(ElementName="Repeat")]
    public class Repeat : W3D
    {
        [XmlElement(ElementName="NoRepeat")]
        public object NoRepeat;

        [XmlElement(ElementName="RepeatForever")]
        public object RepeatForever;

        [XmlElement(ElementName="RepeatNum")]
        public uint repeatNum;
    }


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


    [XmlRoot(ElementName="EventTrigger")]
    public class EventTrigger : W3D
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


    [XmlRoot(ElementName="HeadTrack")]
    public class HeadTrack : W3D
    {
        [XmlElement(ElementName="Position")]
        public TrackPosition Position;

        [XmlElement(ElementName="Direction")]
        public Direction Direction;
    }


    [XmlRoot(ElementName="Position")]
    public class TrackPosition : W3D
    {
        [XmlElement(ElementName="Anywhere")]
        public object Anywhere;

        [XmlElement(ElementName="Box")]
        public Box Box;
    }


    // HeadTrack.Direction


    [XmlRoot(ElementName="Direction")]
    public class Direction : W3D
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


    [XmlRoot(ElementName="PointTarget")]
    public class PointTarget : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="point")]
        public string point;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }

    [XmlRoot(ElementName="DirectionTarget")]
    public class DirectionTarget : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="direction")]
        public string direction;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    [XmlRoot(ElementName="ObjectTarget")]
    public class ObjectTarget : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    // MOVE TRACK


    [XmlRoot(ElementName="MoveTrack")]
    public class MoveTrack : W3D
    {
        [XmlElement(ElementName="Source")]
        public Source Source;

        [XmlElement(ElementName="Box")]
        public Box Box;
    }

    [XmlRoot(ElementName="Source")]
    public class Source : W3D
    {
        [XmlElement(ElementName="ObjectRef")]
        public ObjectRef ObjectRef;

        [XmlElement(ElementName="GroupObj")]
        public GroupObj GroupObj;
    }


    [XmlRoot(ElementName="ObjectRef")]
    public class ObjectRef : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }

    [XmlRoot(ElementName="GroupObj")]
    public class GroupObj : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;

        // TODO: Enum ("any Object" or "All Objects")
        [XmlAttribute(AttributeName="objects")]
        public string objects;
    }


    // BOX

    [XmlRoot(ElementName="Box")]
    public class Box : W3D
    {
        [XmlElement(ElementName="Movement")]
        public Movement Movement;

        [XmlAttribute(AttributeName="ignore-Y")]
        public bool ignoreY;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="corner1")]
        public string corner1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="corner2")]
        public string corner2;
    }


    // TODO: Enum
    [XmlRoot(ElementName="Movement")]
    public class Movement : W3D
    {

        [XmlElement(ElementName="Outside")]
        public object Outside;

        [XmlElement(ElementName="Inside")]
        public object Inside;
    }

    /********** PARTICLE ACTION     ***********/


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


    [XmlRoot(ElementName="Source")]
    public class ParticleSource : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

        [XmlAttribute(AttributeName="rate")]
        public double rate;
    }


    [XmlRoot(ElementName="Vel")]
    public class Vel : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;
    }


    // PARTICLE ACTION


    // TODO: enum?
    [XmlRoot(ElementName="ParticleAction")]
    public class ParticleAction : W3D
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


    [XmlRoot(ElementName="Avoid")]
    public class Avoid : W3D
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


    [XmlRoot(ElementName="Bounce")]
    public class Bounce : W3D
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


    [XmlRoot(ElementName="Gravity")]
    public class Gravity : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="direction")]
        public string direction;
    }


    [XmlRoot(ElementName="Damping")]
    public class Damping : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="direction")]
        public string direction;

        [XmlAttribute(AttributeName="vel_low")]
        public double velocityLow;

        [XmlAttribute(AttributeName="vel_high")]
        public double velocityHigh;
    }


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


    [XmlRoot(ElementName="OrbitPoint")]
    public class OrbitPoint : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="center")]
        public string center;

        [XmlAttribute(AttributeName="magnitude")]
        public double magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double maxRadius;
    }


    [XmlRoot(ElementName="Jet")]
    public class Jet : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

        [XmlElement(ElementName="AccelDomain")]
        public ParticleDomainType AccelDomain;
    }


    [XmlRoot(ElementName="TargetColor")]
    public class TargetColor : W3D
    {
        // TODO: color simple type
        [XmlAttribute(AttributeName="color")]
        public string color;

        [XmlAttribute(AttributeName="alpha")]
        public double alpha;

        [XmlAttribute(AttributeName="scale")]
        public double scale;
    }

    // REMOVE CONDITION


    // TODO: Enum?
    [XmlRoot(ElementName="RemoveCondition")]
    public class RemoveCondition : W3D
    {

        [XmlElement(ElementName="Age")]
        public Age Age;

        [XmlElement(ElementName="Position")]
        public Position Position;

        [XmlElement(ElementName="Velocity")]
        public Velocity Velocity;
    }


    [XmlRoot(ElementName="Age")]
    public class Age : W3D
    {
        [XmlAttribute(AttributeName="age")]
        public double age;

        [XmlAttribute(AttributeName="younger-than")]
        public bool youngerThan;
    }


    [XmlRoot(ElementName="Position")]
    public class Position : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

        [XmlAttribute(AttributeName="inside")]
        public bool inside;
    }


    [XmlRoot(ElementName="Velocity")]
    public class Velocity : W3D
    {
        [XmlElement(ElementName="ParticleDomain")]
        public ParticleDomainType ParticleDomain;

        [XmlAttribute(AttributeName="inside")]
        public bool inside;
    }


    /********** GLOBAL              ***********/


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


    public class Camera : W3D
    {
        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;

        [XmlAttribute(AttributeName="far-clip")]
        public float farClip;

        [XmlText]
        public string text;
    }


    [XmlRoot(ElementName="Background")]
    public class Background : W3D
    {
        [XmlAttribute(AttributeName="color")]
        public string color;
    }


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


    [XmlRoot(ElementName="Placement")]
    public class PlacementType : W3D
    {
        [XmlElement(ElementName="RelativeTo")]
        public string relativeTo;

        // TODO: vector enum
        [XmlElement(ElementName="Position")]
        public string Position;

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


    [XmlRoot(ElementName="Axis")]
    public class Axis : W3D
    {
        // TODO: Vector simple type
        [XmlAttribute(AttributeName="rotation")]
        public string rotation;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    [XmlRoot(ElementName="LookAt")]
    public class LookAt : W3D
    {
        // TODO: Vector simple type
        [XmlAttribute(AttributeName="target")]
        public string target;

        // TODO: Vector simple type
        [XmlAttribute(AttributeName="up")]
        public string up;
    }


    [XmlRoot(ElementName="Normal")]
    public class Normal : W3D
    {
        // TODO: Vector simple type
        [XmlAttribute(AttributeName="normal")]
        public string normal;

        [XmlAttribute(AttributeName="angle")]
        public double angle;
    }


    // ACTIONS TYPE


    // TODO: Enum?
    public class ActionsType : W3D
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


    [XmlRoot(ElementName="ObjectChange")]
    public class ObjectChange : W3D
    {
        [XmlElement(ElementName="Transition")]
        public TransitionType Transition;

        [XmlAttribute(AttributeName="name")]
        public string name;

        [XmlText]
        public string text;
    }


    [XmlRoot(ElementName="GroupRef")]
    public class GroupRef : W3D
    {
        [XmlElement(ElementName="Transition")]
        public TransitionType Transition;

        [XmlAttribute(AttributeName="name")]
        public string name;

        // TODO: Enum ("Select One Randomly")
        [XmlAttribute(AttributeName="random")]
        public string random;

        [XmlText]
        public string text;
    }


    // TODO: Enum
    [XmlRoot(ElementName="TimerChange")]
    public class TimerChange : W3D
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


    [XmlRoot(ElementName="SoundRef")]
    public class SoundRef : W3D
    {
        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [XmlRoot(ElementName="Event")]
    public class Event : W3D
    {
        [XmlAttribute(AttributeName="enable")]
        public bool enable;

        [XmlAttribute(AttributeName="name")]
        public string name;
    }


    [XmlRoot(ElementName="MoveCave")]
    public class MoveCave : W3D
    {
        // TODO: Enum (relative or Absolute)
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


    // TODO: Enum?
    // [XmlRoot(ElementName="Transition")]
    public class TransitionType : W3D
    {
        [XmlElement(ElementName="Visible")]
        public bool visible;

        [XmlElement(ElementName="Movement")]
        public MovementTransition Movement;

        [XmlElement(ElementName="MoveRel")]
        public MoveRel MoveRel;

        // TODO: Color simple type
        [XmlElement(ElementName="Color")]
        public string Color;

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


    [XmlRoot(ElementName="Movement")]
    public class MovementTransition : W3D
    {
        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;
    }


    [XmlRoot(ElementName="MoveRel")]
    public class MoveRel : W3D
    {
        [XmlElement(ElementName="Placement")]
        public PlacementType Placement;
    }

    [XmlRoot(ElementName="Sound")]
    public class SoundTransition : W3D
    {
        // TODO: Enum ("Play Sound", "Stop Sound")
        [XmlAttribute(AttributeName="action")]
        public string action;
    }


    // TODO: Enum
    [XmlRoot(ElementName="LinkChange")]
    public class LinkChange : W3D
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


    // TODO: Enum?
    [XmlRoot(ElementName="ParticleDomain")]
    public class ParticleDomainType : W3D
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


    [XmlRoot(ElementName="Point")]
    public class Point : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="point")]
        public string point;
    }

    [XmlRoot(ElementName="Line")]
    public class Line : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="p1")]
        public string p1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="p2")]
        public string p2;
    }


    [XmlRoot(ElementName="Triangle")]
    public class Triangle : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="p1")]
        public string p1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="p2")]
        public string p2;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="p3")]
        public string p3;
    }


    [XmlRoot(ElementName="Plane")]
    public class Plane : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="point")]
        public string point;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="normal")]
        public string normal;
    }


    [XmlRoot(ElementName="Rectangle")]
    public class Rectangle : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="p1")]
        public string p1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="u-dir")]
        public string u;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="v-dir")]
        public string v;
    }


    [XmlRoot(ElementName="Box")]
    public class BoxParticle : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="p1")]
        public string p1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="p2")]
        public string p2;
    }


    [XmlRoot(ElementName="Sphere")]
    public class Sphere : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="center")]
        public string center;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="radius")]
        public double radius;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    [XmlRoot(ElementName="Cylinder")]
    public class Cylinder : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="p1")]
        public string p1;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="p2")]
        public string p2;

        [XmlAttribute(AttributeName="radius")]
        public double radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    [XmlRoot(ElementName="Cone")]
    public class Cone : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="base-center")]
        public string baseCenter;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="apex")]
        public string apex;

        [XmlAttribute(AttributeName="radius")]
        public double radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }

    [XmlRoot(ElementName="Blob")]
    public class Blob : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="center")]
        public string center;

        [XmlAttribute(AttributeName="stdev")]
        public double deviation;
    }


    [XmlRoot(ElementName="Disc")]
    public class Disc : W3D
    {
        // TODO: vector simple type
        [XmlAttribute(AttributeName="center")]
        public string center;

        // TODO: vector simple type
        [XmlAttribute(AttributeName="normal")]
        public string normal;

        [XmlAttribute(AttributeName="radius")]
        public float radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double innerRadius;
    }


    /********** BASE CLASS          ***********/

    public class W3D
    {
        public string serialize()
        {
            return JsonConvert.SerializeObject(
                this,
                Formatting.Indented,
                new JsonSerializerSettings() { ReferenceLoopHandling=ReferenceLoopHandling.Ignore }
            );
        }
    }
}
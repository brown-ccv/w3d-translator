using System.Xml.Serialization;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

// TODO: Convert vector types to Unity Vector3
// TODO: Add color, vector, and file class types (custom string translation)

/********** STORY            ***********/


[XmlRoot(ElementName="Story")]
public class Story { 
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
public class ObjectRoot { 
    [XmlElement(ElementName="Object")] 
    public List<Object> Object; 
}


[XmlRoot(ElementName="GroupRoot")]
public class GroupRoot { 
    [XmlElement(ElementName="Group")] 
    public List<Group> Group; 
}


[XmlRoot(ElementName="TimelineRoot")]
public class TimelineRoot { 

    [XmlElement(ElementName="Timeline")] 
    public List<Timeline> Timeline; 
}


[XmlRoot(ElementName="PlacementRoot")]
public class PlacementRoot { 
    [XmlElement(ElementName="Placement")] 
    public List<Placement> Placement; 
}


[XmlRoot(ElementName="SoundRoot")]
public class SoundRoot { 
    [XmlElement(ElementName="Sound")] 
    public List<Sound> Sound; 
}


[XmlRoot(ElementName="EventRoot")]
public class EventRoot { 
    [XmlElement(ElementName="EventTrigger")] 
    public List<EventTrigger> EventTrigger; 
}


[XmlRoot(ElementName="ParticleActionRoot")]
public class ParticleActionRoot { 
    [XmlElement(ElementName="ParticleActionList")] 
    public List<ParticleActionList> ParticleActionList; 
}


[XmlRoot(ElementName="About")]
public class About { 
    [XmlAttribute(AttributeName="About")] 
    public string news;
}


/********** OBJECT            ***********/


[XmlRoot(ElementName="Object")]
public class Object { 
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


// CONTENT


[XmlRoot(ElementName="Content")]
public class Content { 
    // TODO: Just make content null?
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
public class Text { 

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
public class Image { 
    // TODO: file simple type
    [XmlAttribute(AttributeName="filename")] 
    public string filename; 
}

[XmlRoot(ElementName="StereoImage")]
public class StereoImage { 
    // TODO: file simple type
    [XmlAttribute(AttributeName="left-image")] 
    public string leftImage;

    // TODO: file simple type
    [XmlAttribute(AttributeName="right-image")] 
    public string rightImage;
}

[XmlRoot(ElementName="Model")]
public class Model { 
    // TODO: file simple type
    [XmlAttribute(AttributeName="filename")] 
    public string filename; 

    [XmlAttribute(AttributeName="check-collisions")] 
    public string checkCollisions;
}


[XmlRoot(ElementName="ParticleSystem")]
public class ParticleSystem { 
    [XmlAttribute(AttributeName="max-particles")] 
    public uint maxParticles; 

    [XmlAttribute(AttributeName="actions-name")] 
    public int actionsName; 

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
public class Light { 
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
public class Spot {
    [XmlAttribute(AttributeName="angle")] 
    public double angle; 
}


// LINK


[XmlRoot(ElementName="LinkRoot")]
public class LinkRoot { 
    [XmlElement(ElementName="Link")] 
    public List<Link> Link; 
}


[XmlRoot(ElementName="Link")]
public class Link { 
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
public class Actions : ActionsType { 
    // TODO: Enum
    [XmlElement(ElementName="Clicks")] 
    public Clicks Clicks; 
}


[XmlRoot(ElementName="Clicks")]
public class Clicks { 
    [XmlElement(ElementName="Any")] 
    public object Any;

    [XmlElement(ElementName="NumClicks")] 
    public NumClicks NumClicks; 

 
}


[XmlRoot(ElementName="NumClicks")]
public class NumClicks { 
    [XmlAttribute(AttributeName="num_clicks")] 
    public uint numClicks; 

    [XmlAttribute(AttributeName="reset")] 
    public bool reset; 
}


/********** GROUP            ***********/


[XmlRoot(ElementName="Group")]
public class Group { 
    [XmlElement(ElementName="Objects")] 
    public List<Objects> Objects; 

    [XmlElement(ElementName="Groups")] 
    public List<Groups> Groups; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 
}

[XmlRoot(ElementName="Objects")]
public class Objects { 
    [XmlAttribute(AttributeName="name")] 
    public string name; 
}


[XmlRoot(ElementName="Groups")]
public class Groups { 
    [XmlAttribute(AttributeName="name")] 
    public string name; 
}


/********** TIMELINE        ***********/


[XmlRoot(ElementName="Timeline")]
public class Timeline { 
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
public class TimedActions : ActionsType { 
    [XmlAttribute(AttributeName="seconds-time")] 
    public double secondsTime; 

    [XmlText] 
    public string text; 
}


/********** SOUND            ***********/


[XmlRoot(ElementName="Sound")]
public class Sound { 
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
public class Mode { 
    [XmlElement(ElementName="Positional")] 
    public object Positional;

    [XmlElement(ElementName="Fixed")] 
    public object Fixed; 
}


[XmlRoot(ElementName="Repeat")]
public class Repeat { 
    [XmlElement(ElementName="NoRepeat")] 
    public object NoRepeat;

    [XmlElement(ElementName="RepeatForever")] 
    public object RepeatForever; 

    [XmlElement(ElementName="RepeatNum")] 
    public uint repeatNum; 
}


[XmlRoot(ElementName="Settings")]
public class Settings { 
    [XmlAttribute(AttributeName="freq")] 
    public double frequency; 

    [XmlAttribute(AttributeName="volume")] 
    public double volume; 

    [XmlAttribute(AttributeName="pan")] 
    public double pan; 
}


/********** EVENT TRIGGER       ***********/


[XmlRoot(ElementName="EventTrigger")]
public class EventTrigger { 

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
public class HeadTrack { 
    [XmlElement(ElementName="Position")] 
    public TrackPosition Position; 

    [XmlElement(ElementName="Direction")] 
    public Direction Direction; 
}


[XmlRoot(ElementName="Position")]
public class TrackPosition { 
	[XmlElement(ElementName="Anywhere")] 
	public object Anywhere; 

	[XmlElement(ElementName="Box")] 
	public Box Box;
}


// TODO: Enum
[XmlRoot(ElementName="Movement")]
public class Movement { 
    
    [XmlElement(ElementName="Outside")] 
    public object Outside; 

    [XmlElement(ElementName="Inside")] 
    public object Inside; 
}



// HeadTrack.Direction


[XmlRoot(ElementName="Direction")]
public class Direction { 
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
public class PointTarget { 
    // TODO: vector simple type
	[XmlAttribute(AttributeName="point")] 
	public string point; 

	[XmlAttribute(AttributeName="angle")] 
	public double angle; 
}

[XmlRoot(ElementName="DirectionTarget")]
public class DirectionTarget { 
    // TODO: vector simple type
	[XmlAttribute(AttributeName="direction")] 
	public string direction; 

	[XmlAttribute(AttributeName="angle")] 
	public double angle; 
}


[XmlRoot(ElementName="ObjectTarget")]
public class ObjectTarget { 
	[XmlAttribute(AttributeName="name")] 
	public string name; 
}


// MOVE TRACK


[XmlRoot(ElementName="MoveTrack")]
public class MoveTrack { 

	[XmlElement(ElementName="Source")] 
	public Source Source; 

	[XmlElement(ElementName="Box")] 
	public Box Box; 
}

[XmlRoot(ElementName="Source")]
public class Source { 

	[XmlElement(ElementName="ObjectRef")] 
	public ObjectRef ObjectRef; 

	[XmlElement(ElementName="GroupObj")] 
	public GroupObj GroupObj; 
}


[XmlRoot(ElementName="ObjectRef")]
public class ObjectRef { 
	[XmlAttribute(AttributeName="name")] 
	public string name; 
}

[XmlRoot(ElementName="GroupObj")]
public class GroupObj { 

	[XmlAttribute(AttributeName="name")] 
	public string name; 

    // TODO: Enum ("any Object" or "All Objects")
	[XmlAttribute(AttributeName="objects")] 
	public string objects; 
}



// BOX

[XmlRoot(ElementName="Box")]
public class Box { 
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


/********** PARTICLE ACTION     ***********/


/********** GLOBAL              ***********/


[XmlRoot(ElementName="Global")]
public class Global { 
    [XmlElement(ElementName="CameraPos")] 
    public Camera Camera; 

    [XmlElement(ElementName="CaveCameraPos")] 
    public Camera CaveCamera; 

    [XmlElement(ElementName="Background")] 
    public Background Background; 

    [XmlElement(ElementName="WandNavigation")] 
    public WandNavigation WandNavigation; 
}

public class Camera { 
    [XmlElement(ElementName="Placement")] 
    public Placement Placement; 

    [XmlAttribute(AttributeName="far-clip")] 
    public float farClip; 

    [XmlText]
    public string text; 
}


[XmlRoot(ElementName="Background")] 
public class Background {
    [XmlAttribute(AttributeName="color")] 
    public string color;
}

[XmlRoot(ElementName="WandNavigation")]
public class WandNavigation { 
    [XmlAttribute(AttributeName="allow-rotation")] 
    public bool allowRotation; 

    [XmlAttribute(AttributeName="allow-movement")] 
    public bool allowMovement; 
}


/********** COMPLEX TYPES    ***********/


// PLACEMENT TYPE

// ACTIONS TYPE


public class ActionsType {
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
public class ObjectChange { 

    [XmlElement(ElementName="Transition")] 
    public TransitionType Transition; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 

    [XmlText] 
    public string text; 
}

[XmlRoot(ElementName="TimerChange")]
public class TimerChange { 

    [XmlElement(ElementName="start_if_not_started")] 
    public object start_if_not_started; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 

    [XmlElement(ElementName="start")] 
    public object start; 

    [XmlElement(ElementName="stop")] 
    public object stop; 
}


[XmlRoot(ElementName="MoveCave")]
public class MoveCave { 

    [XmlElement(ElementName="Relative")] 
    public object Relative; 

    [XmlElement(ElementName="Placement")] 
    public Placement Placement; 

    [XmlAttribute(AttributeName="duration")] 
    public double duration; 

    [XmlText] 
    public string text; 
}

// TRANSITION TYPE

// [XmlRoot(ElementName="Transition")]
public class TransitionType { 
    [XmlElement(ElementName="Visible")] 
    public bool visible; 

    [XmlElement(ElementName="Movement")] 
    public Movement Movement; 

    [XmlElement(ElementName="MoveRel")] 
    public MoveRel MoveRel; 

    // TODO: Color simple type
    [XmlElement(ElementName="Color")] 
    public string Color; 

    [XmlElement(ElementName="Scale")] 
    public double scale; 

    [XmlElement(ElementName="Sound")] 
    public Sound Sound; 

    [XmlElement(ElementName="LinkChange")] 
    public LinkChange LinkChange;


    [XmlAttribute(AttributeName="duration")] 
    public double duration;

    [XmlText] 
    public string text; 
}

/********** UNORGANIZED **********/



[XmlRoot(ElementName="Age")]
public class Age { 

    [XmlAttribute(AttributeName="age")] 
    public int age; 

    [XmlAttribute(AttributeName="younger-than")] 
    public bool youngerThan; 
}


[XmlRoot(ElementName="Axis")]
public class Axis { 

    [XmlAttribute(AttributeName="rotation")] 
    public string rotation; 

    [XmlAttribute(AttributeName="angle")] 
    public double angle; 
}


[XmlRoot(ElementName="Bounce")]
public class Bounce { 

    [XmlElement(ElementName="ParticleDomain")] 
    public ParticleDomain ParticleDomain; 

    [XmlAttribute(AttributeName="friction")] 
    public double friction; 

    [XmlAttribute(AttributeName="resilience")] 
    public double resilience; 

    [XmlAttribute(AttributeName="cutoff")] 
    public int cutoff; 
}


[XmlRoot(ElementName="Box")]
public class BoxParticle { 
    [XmlAttribute(AttributeName="p1")] 
    public string p1; 

    [XmlAttribute(AttributeName="p2")] 
    public string p2; 
}

[XmlRoot(ElementName="Cylinder")]
public class Cylinder { 

    [XmlAttribute(AttributeName="p1")] 
    public string p1; 

    [XmlAttribute(AttributeName="p2")] 
    public string p2; 

    [XmlAttribute(AttributeName="radius")] 
    public double radius; 

    [XmlAttribute(AttributeName="radius-inner")] 
    public double radiusInner; 
}


[XmlRoot(ElementName="Disc")]
public class Disc { 

    [XmlAttribute(AttributeName="center")] 
    public string center; 

    [XmlAttribute(AttributeName="normal")] 
    public string normal; 

    [XmlAttribute(AttributeName="radius")] 
    public int radius; 

    [XmlAttribute(AttributeName="radius-inner")] 
    public double radiusInner; 
}


[XmlRoot(ElementName="Event")]
public class Event { 

    [XmlAttribute(AttributeName="enable")] 
    public bool enable; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 
}


[XmlRoot(ElementName="Gravity")]
public class Gravity { 

    [XmlAttribute(AttributeName="direction")] 
    public string direction; 
}


[XmlRoot(ElementName="GroupRef")]
public class GroupRef { 

    [XmlElement(ElementName="Transition")] 
    public TransitionType Transition; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 

    [XmlText] 
    public string text; 
}


[XmlRoot(ElementName="Line")]
public class Line { 

    [XmlAttribute(AttributeName="p1")] 
    public string p1; 

    [XmlAttribute(AttributeName="p2")] 
    public string p2; 
}


[XmlRoot(ElementName="LinkChange")]
public class LinkChange { 

    [XmlElement(ElementName="link_on")] 
    public object link_on; 

    [XmlElement(ElementName="link_off")] 
    public object link_off; 
}


[XmlRoot(ElementName="LookAt")]
public class LookAt { 

    [XmlAttribute(AttributeName="target")] 
    public string target; 

    [XmlAttribute(AttributeName="up")] 
    public string up; 
}


[XmlRoot(ElementName="MoveRel")]
public class MoveRel { 

    [XmlElement(ElementName="Placement")] 
    public Placement Placement; 
}


[XmlRoot(ElementName="OrbitPoint")]
public class OrbitPoint { 

    [XmlAttribute(AttributeName="center")] 
    public string center; 

    [XmlAttribute(AttributeName="magnitude")] 
    public double magnitude; 

    [XmlAttribute(AttributeName="epsilon")] 
    public double epsilon; 

    [XmlAttribute(AttributeName="max_radius")] 
    public double max_radius; 
}


[XmlRoot(ElementName="ParticleAction")]
public class ParticleAction { 

    [XmlElement(ElementName="Gravity")] 
    public Gravity Gravity; 

    [XmlElement(ElementName="Bounce")] 
    public Bounce Bounce; 

    [XmlElement(ElementName="OrbitPoint")] 
    public OrbitPoint OrbitPoint; 
}


[XmlRoot(ElementName="ParticleActionList")]
public class ParticleActionList { 

    [XmlElement(ElementName="Source")] 
    public Source Source; 

    [XmlElement(ElementName="Vel")] 
    public Vel Vel; 

    [XmlElement(ElementName="ParticleAction")] 
    public List<ParticleAction> ParticleAction; 

    [XmlElement(ElementName="RemoveCondition")] 
    public RemoveCondition RemoveCondition; 

    [XmlAttribute(AttributeName="name")] 
    public int name; 
}


[XmlRoot(ElementName="ParticleDomain")]
public class ParticleDomain { 

    [XmlElement(ElementName="Line")] 
    public Line Line; 

    [XmlElement(ElementName="Cylinder")] 
    public Cylinder Cylinder; 

    [XmlElement(ElementName="Disc")] 
    public Disc Disc; 

    [XmlElement(ElementName="Plane")] 
    public Plane Plane; 

    [XmlElement(ElementName="Sphere")] 
    public Sphere Sphere; 

    [XmlElement(ElementName="Box")] 
    public Box Box; 
}


[XmlRoot(ElementName="Placement")]
public class Placement { 

    [XmlElement(ElementName="RelativeTo")] 
    public string RelativeTo; 

    [XmlElement(ElementName="Position")] 
    public string Position; 

    [XmlElement(ElementName="Axis")] 
    public Axis Axis; 

    [XmlAttribute(AttributeName="name")] 
    public string name; 

    [XmlText] 
    public string text; 

    [XmlElement(ElementName="LookAt")] 
    public LookAt LookAt; 
}


[XmlRoot(ElementName="Plane")]
public class Plane { 

    [XmlAttribute(AttributeName="point")] 
    public string point; 

    [XmlAttribute(AttributeName="normal")] 
    public string normal; 
}


[XmlRoot(ElementName="RemoveCondition")]
public class RemoveCondition { 

    [XmlElement(ElementName="Position")] 
    public Position Position; 

    [XmlElement(ElementName="Age")] 
    public Age Age; 
}


[XmlRoot(ElementName="SoundRef")]
public class SoundRef { 

    [XmlAttribute(AttributeName="name")] 
    public string name; 
}


[XmlRoot(ElementName="Source")]
public class ParticleSource { 
	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="rate")] 
	public double rate; 
}


[XmlRoot(ElementName="Sphere")]
public class Sphere { 

    [XmlAttribute(AttributeName="center")] 
    public string center; 

    [XmlAttribute(AttributeName="radius")] 
    public int radius; 

    [XmlAttribute(AttributeName="radius-inner")] 
    public double radiusInner; 
}


[XmlRoot(ElementName="Vel")]
public class Vel { 
    [XmlElement(ElementName="ParticleDomain")] 
    public ParticleDomain ParticleDomain; 
}


[XmlRoot(ElementName="Position")]
public class Position { 
	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="inside")] 
	public bool inside; 
}


[XmlRoot(ElementName="Movement")]
public class MovementTransition { 
    [XmlElement(ElementName="Placement")] 
    public Placement Placement; 
}
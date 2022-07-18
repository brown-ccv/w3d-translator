using System.Xml.Serialization;
using System.Collections.Generic;
using UnityEngine;

// TODO: Convert vector types to Unity Vector3
// TODO: Add color, vector, and file class types (custom string translation)

/********** STORY			***********/


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

[XmlRoot(ElementName="PlacementRoot")]
public class PlacementRoot { 

	[XmlElement(ElementName="Placement")] 
	public List<Placement> Placement; 
}


[XmlRoot(ElementName="Global")]
public class Global { 

	[XmlElement(ElementName="CameraPos")] 
	public Camera Camera; 

	[XmlElement(ElementName="CaveCameraPos")] 
	public Camera CaveCamera; 

	[XmlElement(ElementName="Background")] 
	public string backgroundColor; 

	[XmlElement(ElementName="WandNavigation")] 
	public WandNavigation WandNavigation; 
}


[XmlRoot(ElementName="About")]
public class About { 

    [XmlAttribute(AttributeName="About")] 
    public string news;
}


public class Camera { 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 

	[XmlAttribute(AttributeName="far-clip")] 
	public float farClip; 

	[XmlText]
	public string text; 
}


[XmlRoot(ElementName="WandNavigation")]
public class WandNavigation { 

	[XmlAttribute(AttributeName="allow-rotation")] 
	public bool allowRotation; 

	[XmlAttribute(AttributeName="allow-movement")] 
	public bool allowMovement; 
}


/********** OBJECT			***********/


[XmlRoot(ElementName="ObjectRoot")]
public class ObjectRoot { 

	[XmlElement(ElementName="Object")] 
	public List<Object> Object; 
}


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

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 

	[XmlElement(ElementName="Content")] 
	public Content Content; 

	[XmlAttribute(AttributeName="name")] 
	public string name; 

	[XmlText] 
	public string text;

	[XmlElement(ElementName="LinkRoot")] 
	public LinkRoot LinkRoot; 

	[XmlElement(ElementName="SoundRef")] 
	public string soundRef; 
}



/********** GROUP			***********/
/********** TIMELINE		***********/
/********** SOUND			***********/
/********** EVENT			***********/
/********** PARTICLE ACTION	***********/
/********** GLOBAL			***********/
/********** OBJECT			***********/
/********** COMPLEX TYPES	***********/


/********** UNORGANIZED **********/

[XmlRoot(ElementName="Actions")]
public class Actions { 

	[XmlElement(ElementName="Event")] 
	public Event Event; 

	[XmlElement(ElementName="TimerChange")] 
	public TimerChange TimerChange; 

	[XmlElement(ElementName="Clicks")] 
	public Clicks Clicks; 
}


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
public class Box { 

	[XmlElement(ElementName="Movement")] 
	public Movement Movement; 

	[XmlAttribute(AttributeName="ignore-Y")] 
	public bool ignoreY; 

	[XmlAttribute(AttributeName="corner1")] 
	public string corner1; 

	[XmlAttribute(AttributeName="corner2")] 
	public string corner2; 

	[XmlAttribute(AttributeName="p1")] 
	public string p1; 

	[XmlAttribute(AttributeName="p2")] 
	public string p2; 
}

[XmlRoot(ElementName="Clicks")]
public class Clicks { 

	[XmlElement(ElementName="NumClicks")] 
	public NumClicks NumClicks; 

	[XmlElement(ElementName="Any")] 
	public object Any; 
}


[XmlRoot(ElementName="Content")]
public class Content { 

	[XmlElement(ElementName="Light")] 
	public Light Light; 

	[XmlElement(ElementName="Text")] 
	public Text Text; 

	[XmlElement(ElementName="Image")] 
	public Image Image; 

	[XmlElement(ElementName="None")] 
	public object None; 

	[XmlElement(ElementName="ParticleSystem")] 
	public ParticleSystem ParticleSystem; 
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


[XmlRoot(ElementName="Direction")]
public class Direction { 

	[XmlElement(ElementName="None")] 
	public object None; 
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


[XmlRoot(ElementName="EventRoot")]
public class EventRoot { 

	[XmlElement(ElementName="EventTrigger")] 
	public List<EventTrigger> EventTrigger; 
}


[XmlRoot(ElementName="EventTrigger")]
public class EventTrigger { 

	[XmlElement(ElementName="HeadTrack")] 
	public HeadTrack HeadTrack; 

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
}


[XmlRoot(ElementName="Gravity")]
public class Gravity { 

	[XmlAttribute(AttributeName="direction")] 
	public string direction; 
}


[XmlRoot(ElementName="Group")]
public class Group { 

	[XmlElement(ElementName="Objects")] 
	public List<Objects> Objects; 

	[XmlAttribute(AttributeName="name")] 
	public string name; 
}


[XmlRoot(ElementName="GroupRef")]
public class GroupRef { 

	[XmlElement(ElementName="Transition")] 
	public Transition Transition; 

	[XmlAttribute(AttributeName="name")] 
	public string name; 

	[XmlText] 
	public string text; 
}


[XmlRoot(ElementName="GroupRoot")]
public class GroupRoot { 

	[XmlElement(ElementName="Group")] 
	public List<Group> Group; 
}


[XmlRoot(ElementName="HeadTrack")]
public class HeadTrack { 

	[XmlElement(ElementName="Position")] 
	public Position Position; 

	[XmlElement(ElementName="Direction")] 
	public Direction Direction; 
}


[XmlRoot(ElementName="Image")]
public class Image { 

	[XmlAttribute(AttributeName="filename")] 
	public string filename; 
}


[XmlRoot(ElementName="Light")]
public class Light { 

	[XmlElement(ElementName="Point")] 
	public object Point; 

	[XmlAttribute(AttributeName="diffuse")] 
	public bool diffuse; 

	[XmlAttribute(AttributeName="specular")] 
	public bool specular; 

	[XmlAttribute(AttributeName="const_atten")] 
	public double const_atten; 

	[XmlAttribute(AttributeName="lin_atten")] 
	public double lin_atten; 

	[XmlAttribute(AttributeName="quad_atten")] 
	public double quad_atten; 
}


[XmlRoot(ElementName="Line")]
public class Line { 

	[XmlAttribute(AttributeName="p1")] 
	public string p1; 

	[XmlAttribute(AttributeName="p2")] 
	public string p2; 
}


[XmlRoot(ElementName="Link")]
public class Link { 

	[XmlElement(ElementName="Enabled")] 
	public bool Enabled; 

	[XmlElement(ElementName="RemainEnabled")] 
	public bool RemainEnabled; 

	[XmlElement(ElementName="EnabledColor")] 
	public string EnabledColor; 

	[XmlElement(ElementName="SelectedColor")] 
	public string SelectedColor; 

	[XmlElement(ElementName="Actions")] 
	public Actions Actions; 
}


[XmlRoot(ElementName="LinkChange")]
public class LinkChange { 

	[XmlElement(ElementName="link_on")] 
	public object link_on; 

	[XmlElement(ElementName="link_off")] 
	public object link_off; 
}


[XmlRoot(ElementName="LinkRoot")]
public class LinkRoot { 

	[XmlElement(ElementName="Link")] 
	public Link Link; 
}


[XmlRoot(ElementName="LookAt")]
public class LookAt { 

	[XmlAttribute(AttributeName="target")] 
	public string target; 

	[XmlAttribute(AttributeName="up")] 
	public string up; 
}


[XmlRoot(ElementName="Mode")]
public class Mode { 

	[XmlElement(ElementName="Fixed")] 
	public object Fixed; 
}


[XmlRoot(ElementName="Movement")]
public class Movement { 

	[XmlElement(ElementName="Outside")] 
	public object Outside; 

	[XmlElement(ElementName="Inside")] 
	public object Inside; 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 
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


[XmlRoot(ElementName="MoveRel")]
public class MoveRel { 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 
}


[XmlRoot(ElementName="NumClicks")]
public class NumClicks { 

	[XmlAttribute(AttributeName="num_clicks")] 
	public int num_clicks; 

	[XmlAttribute(AttributeName="reset")] 
	public bool reset; 
}


[XmlRoot(ElementName="ObjectChange")]
public class ObjectChange { 

	[XmlElement(ElementName="Transition")] 
	public Transition Transition; 

	[XmlAttribute(AttributeName="name")] 
	public string name; 

	[XmlText] 
	public string text; 
}


[XmlRoot(ElementName="Objects")]
public class Objects { 

	[XmlAttribute(AttributeName="name")] 
	public string name; 
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


[XmlRoot(ElementName="ParticleActionRoot")]
public class ParticleActionRoot { 

	[XmlElement(ElementName="ParticleActionList")] 
	public List<ParticleActionList> ParticleActionList; 
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


[XmlRoot(ElementName="ParticleSystem")]
public class ParticleSystem { 

	[XmlAttribute(AttributeName="max-particles")] 
	public int maxParticles; 

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


[XmlRoot(ElementName="Position")]
public class Position { 

	[XmlElement(ElementName="Box")] 
	public Box Box; 

	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="inside")] 
	public bool inside; 
}


[XmlRoot(ElementName="RemoveCondition")]
public class RemoveCondition { 

	[XmlElement(ElementName="Position")] 
	public Position Position; 

	[XmlElement(ElementName="Age")] 
	public Age Age; 
}


[XmlRoot(ElementName="Repeat")]
public class Repeat { 

	[XmlElement(ElementName="NoRepeat")] 
	public object NoRepeat; 
}


[XmlRoot(ElementName="Settings")]
public class Settings { 

	[XmlAttribute(AttributeName="freq")] 
	public double freq; 

	[XmlAttribute(AttributeName="volume")] 
	public double volume; 

	[XmlAttribute(AttributeName="pan")] 
	public double pan; 
}


[XmlRoot(ElementName="Sound")]
public class Sound { 

	[XmlAttribute(AttributeName="action")] 
	public string action; 

	[XmlElement(ElementName="Mode")] 
	public Mode Mode; 

	[XmlElement(ElementName="Repeat")] 
	public Repeat Repeat; 

	[XmlElement(ElementName="Settings")] 
	public Settings Settings; 

	[XmlAttribute(AttributeName="name")] 
	public string name; 

	[XmlAttribute(AttributeName="filename")] 
	public string filename; 

	[XmlAttribute(AttributeName="autostart")] 
	public bool autostart; 
}


[XmlRoot(ElementName="SoundRef")]
public class SoundRef { 

	[XmlAttribute(AttributeName="name")] 
	public string name; 
}


[XmlRoot(ElementName="SoundRoot")]
public class SoundRoot { 

	[XmlElement(ElementName="Sound")] 
	public List<Sound> Sound; 
}


[XmlRoot(ElementName="Source")]
public class Source { 

	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="rate")] 
	public int rate; 
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


[XmlRoot(ElementName="Text")]
public class Text { 

	[XmlElement(ElementName="text")] 
	public List<string> text;

	[XmlAttribute(AttributeName="horiz-align")]
	public string horizAlign; 

	[XmlAttribute(AttributeName="vert-align")] 
	public string vertAlign; 

	[XmlAttribute(AttributeName="font")] 
	public string font; 

	[XmlAttribute(AttributeName="depth")] 
	public double depth; 
}


[XmlRoot(ElementName="TimedActions")]
public class TimedActions { 

	[XmlElement(ElementName="GroupRef")] 
	public GroupRef GroupRef; 

	[XmlAttribute(AttributeName="seconds-time")] 
	public double secondsTime; 

	[XmlText] 
	public string text; 

	[XmlElement(ElementName="TimerChange")] 
	public TimerChange TimerChange; 

	[XmlElement(ElementName="SoundRef")] 
	public SoundRef SoundRef; 

	[XmlElement(ElementName="ObjectChange")] 
	public ObjectChange ObjectChange; 

	[XmlElement(ElementName="MoveCave")] 
	public MoveCave MoveCave; 
}


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


[XmlRoot(ElementName="TimelineRoot")]
public class TimelineRoot { 

	[XmlElement(ElementName="Timeline")] 
	public List<Timeline> Timeline; 
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


[XmlRoot(ElementName="Transition")]
public class Transition { 

	[XmlElement(ElementName="MoveRel")] 
	public MoveRel MoveRel; 

	[XmlAttribute(AttributeName="duration")] 
	public double duration; 

	[XmlText] 
	public string text; 

	[XmlElement(ElementName="Visible")] 
	public bool Visible; 

	[XmlElement(ElementName="LinkChange")] 
	public LinkChange LinkChange; 

	[XmlElement(ElementName="Scale")] 
	public double Scale; 

	[XmlElement(ElementName="Movement")] 
	public Movement Movement; 

	[XmlElement(ElementName="Sound")] 
	public Sound Sound; 

	[XmlElement(ElementName="Color")] 
	public string Color; 
}


[XmlRoot(ElementName="Vel")]
public class Vel { 

	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 
}
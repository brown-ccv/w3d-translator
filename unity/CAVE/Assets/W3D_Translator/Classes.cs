using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Collections.Generic;
using Unity;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using TMPro;


namespace W3D
{
    [Serializable]
    public class Xml
    {
        // Print the class as a Json object
        public string pprint() { return JsonUtility.ToJson(this, true); }

        // Converts "[int], [int], [int]" to a UnityEngine.Color object
        static public Color ConvertColor(string colorString)
        {
            string[] strings = colorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Color(
                float.Parse(strings[0]) / 255,
                float.Parse(strings[1]) / 255,
                float.Parse(strings[2]) / 255
            );
        }

        // Converts a "([float], [float], [float])" string to a UnityEngine.Vector3 object
        static public Vector3 ConvertVector3(string vectorString)
        {
            string[] strings = vectorString.Trim(new Char[] { ' ', '(', ')' }).Split(",");
            return new Vector3(
                float.Parse(strings[0]),
                float.Parse(strings[1]),
                float.Parse(strings[2]) * -1
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
        public int Version;

        [XmlAttribute(AttributeName="last_xpath")]
        public string LastXpath;

        [XmlText]
        public string text;

    }


    [Serializable]
    [XmlRoot(ElementName="About")]
    public class About : Xml
    {
        [XmlAttribute(AttributeName="news")]
        public string News;
    }


    /********** OBJECT            ***********/


    [Serializable]
    [XmlRoot(ElementName="Object")]
    public class Object : Xml
    {
        [XmlElement(ElementName="Visible")]
        public bool Visible;

        [XmlElement(ElementName="Color")]
        public string ColorString;

        [XmlElement(ElementName="Lighting")]
        public bool Lighting;

        [XmlElement(ElementName="ClickThrough")]
        public bool ClickThrough;

        [XmlElement(ElementName="AroundSelfAxis")]
        public bool AroundSelfAxis;

        [XmlElement(ElementName="Scale")]
        public float Scale;

        [XmlElement(ElementName="SoundRef")]
        public string SoundRef;

        [XmlElement(ElementName="Placement")]
        public Placement Placement;

        [XmlElement(ElementName="Content")]
        public Content Content;

        [XmlElement(ElementName="LinkRoot")]
        public LinkRoot LinkRoot;

        [XmlAttribute(AttributeName="name")]
        public string Name;

        [XmlText]
        public string text;
    }


    [XmlRoot(ElementName = "LinkRoot")]
    public class LinkRoot
    {
        [XmlElement(ElementName = "Link")]
        public Link Link;
    }


    // OBJECT.CONTENT


    [Serializable]
    [XmlRoot(ElementName="Content")]
    public class Content : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="None", Type=null)]
        [XmlElement(ElementName="Text", Type=typeof(Text))]
        [XmlElement(ElementName="Image", Type=typeof(Image))]
        [XmlElement(ElementName="StereoImage", Type=typeof(StereoImage))]
        [XmlElement(ElementName="Model", Type=typeof(Model))]
        [XmlElement(ElementName="Light", Type=typeof(Light))]
        [XmlElement(ElementName="ParticleSystem", Type=typeof(ParticleSystem))]
        public object ContentData;
        public ContentTypes Type; 

        public enum ContentTypes {
            [XmlEnum("None")] None,
            [XmlEnum("Text")] Text,
            [XmlEnum("Image")] Image,
            [XmlEnum("StereoImage")] StereoImage,
            [XmlEnum("Model")] Model,
            [XmlEnum("Light")] Light,
            [XmlEnum("ParticleSystem")] ParticleSystem,
        }

        public GameObject Create(Object parent) {
            GameObject gameObject = this.ContentData switch
            {
                Text text => text.GenerateTMP(
                    parent.LinkRoot is not null, 
                    Xml.ConvertColor(parent.ColorString)
                ),
                Image image => new GameObject(), // TODO (65)
                StereoImage stereoImage => new GameObject(), // TODO (66)
                Model model => new GameObject(), // TODO (67)
                Light light => new GameObject(), // TODO (68)
                ParticleSystem particleSystem => new GameObject(), // TODO (69)
                _ => new GameObject(), // TODO: - Shouldn't occur, throw error
            };
            gameObject.name = parent.Name;
            return gameObject;
        }   
    }   


    [Serializable]
    [XmlRoot(ElementName="Text")]
    public class Text : Xml
    {
        [XmlElement(ElementName="text")]
        public string String;

        // Match TMPro.HorizontalAlignmentOptions
        [XmlAttribute(AttributeName="horiz-align")]
        public HorizontalAlignments HorizontalAlignment;
        public enum HorizontalAlignments {
            [XmlEnum(Name="left")] Left = 1,
            [XmlEnum(Name="center")] Center = 2,
            [XmlEnum(Name="right")] Right = 4,
        }

        // Match TMPro.VerticalAlignmentOptions
        [XmlAttribute(AttributeName="vert-align")]
        public VerticalAlignments VerticalAlignment;
        public enum VerticalAlignments { 
            [XmlEnum(Name="top")] Top = 256,
            [XmlEnum(Name="center")] Middle = 512,
            [XmlEnum(Name="bottom")] Bottom = 1024,
        }

        [XmlAttribute(AttributeName="font")]
        public string Font;

        [XmlAttribute(AttributeName="depth")]
        public float Depth;

        public GameObject GenerateTMP(bool isLink, Color color) {
            // Instantiate TextMeshPro or TextMeshProUGUI prefab
            // TODO (64): Validate prefab settings
            GameObject gameObject = UnityEngine.Object.Instantiate(
                Resources.Load<GameObject>("Prefabs/tmp" + (isLink ? "GUI" : ""))
            );
            TMP_Text tmp = gameObject.GetComponent<TMP_Text>();

            // Load font material
            TMP_FontAsset tmpFont = Resources.Load<TMP_FontAsset>(
                "Materials/Fonts/" + 
                Path.GetFileNameWithoutExtension(this.Font) + 
                " SDF"
            );
            // Font material hasn't been created, attempt to load from ttf file
            // TODO (72): More robust path checking
            if(tmpFont == null) {
                try {
                    Font font = AssetDatabase.LoadAssetAtPath<Font>(this.Font);
                    tmpFont = TMP_FontAsset.CreateFontAsset(font);
                    tmpFont.name = Path.GetFileNameWithoutExtension(this.Font);
                } catch(NullReferenceException e) {
                    Debug.LogError($"Error loading font: {this.Font}");
                    Debug.LogException(e);
                }
            }
            // Add font to the TextMeshPro object
            try {tmp.font = tmpFont; }
            catch(NullReferenceException e) {
                Debug.LogWarning($"{gameObject.name} {tmpFont.ToString()} {tmp.font.ToString()}");
                Debug.LogError($"Error creating font asset {this.Font} for {gameObject.name}");
                Debug.Log("Defaulting to fallback font LiberationSans SDF");
                Debug.LogException(e);
            }
            
            // Set object properties defined in the xml
            tmp.SetText(this.String);
            tmp.horizontalAlignment = (HorizontalAlignmentOptions)this.HorizontalAlignment;
            tmp.verticalAlignment = (VerticalAlignmentOptions)this.VerticalAlignment;
            tmp.color = color; // Vertex Color
            tmp.faceColor = color; // Material color
            return gameObject;
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Image")]
    public class Image : Xml
    {
        [XmlAttribute(AttributeName="filename")]
        public string Filename;
    }


    [Serializable]
    [XmlRoot(ElementName="StereoImage")]
    public class StereoImage : Xml
    {
        [XmlAttribute(AttributeName="left-image")]
        public string LeftImage;

        [XmlAttribute(AttributeName="right-image")]
        public string RightImage;

    }


    [Serializable]
    [XmlRoot(ElementName="Model")]
    public class Model : Xml
    {
        [XmlAttribute(AttributeName="filename")]
        public string Filename;

        [XmlAttribute(AttributeName="check-collisions")]
        public string CheckCollisions;
    }


    [Serializable]
    [XmlRoot(ElementName="ParticleSystem")]
    // TODO (69): Unity has a ParticleSystem class
    public class ParticleSystem : Xml
    {
        [XmlAttribute(AttributeName="max-particles")]
        public int MaxParticles;

        [XmlAttribute(AttributeName="actions-name")]
        public string ActionsName;

        [XmlAttribute(AttributeName="particle-group")]
        public string ParticleGroup;

        [XmlAttribute(AttributeName="look-at-camera")]
        public bool LookAtCamera;

        [XmlAttribute(AttributeName="sequential")]
        public bool Sequential;

        [XmlAttribute(AttributeName="speed")]
        public double Speed;
    }


    [Serializable]
    [XmlRoot(ElementName="Light")]
    // TODO (68): Unity has a Light class 
    public class Light : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Point")]
        [XmlElement(ElementName="Directional")]
        [XmlElement(ElementName="Spot", Type=typeof(Spot))]
        public object Data;
        public LightTypes Type;

        [XmlAttribute(AttributeName="diffuse")]
        public bool Diffuse;

        [XmlAttribute(AttributeName="specular")]
        public bool Specular;

        [XmlAttribute(AttributeName="const_atten")]
        public double ConstAtten;

        [XmlAttribute(AttributeName="lin_atten")]
        public double LinAtten;

        [XmlAttribute(AttributeName="quad_atten")]
        public double QuadAtten;

        public enum LightTypes {
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
        public double Angle;
    }


    // LINK


    [Serializable]
    [XmlRoot(ElementName="Link")]
    public class Link : Xml
    {
        [XmlElement(ElementName="Enabled")]
        public bool Enabled;

        [XmlElement(ElementName="RemainEnabled")]
        public bool RemainEnabled;

        [XmlElement(ElementName="EnabledColor")]
        public string EnabledColorString;

        [XmlElement(ElementName="SelectedColor")]
        public string SelectedColorString;

        [XmlElement(ElementName="Actions")]
        public List<LinkActions> Actions;

        public ColorBlock SetColors(ColorBlock colors, string parentColorString) {
            colors.normalColor = colors.highlightedColor =
                Xml.ConvertColor(this.EnabledColorString);
            colors.pressedColor = colors.selectedColor = 
                Xml.ConvertColor(this.SelectedColorString);
            colors.disabledColor = Xml.ConvertColor(parentColorString);
            return colors;
        } 
    }


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
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Any")]
        [XmlElement(ElementName="NumClicks", Type=typeof(NumClicks))]
        public object Activation;
        public ActivationTypes Type;

        public enum ActivationTypes {
            [XmlEnum("Any")] Any,
            [XmlEnum("NumClicks")] Number,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="NumClicks")]
    public class NumClicks : Xml
    {
        [XmlAttribute(AttributeName="num_clicks")]
        public uint Clicks;

        [XmlAttribute(AttributeName="reset")]
        public bool Reset;
    }


    /********** GROUP            ***********/


    [Serializable]
    [XmlRoot(ElementName="Group")]
    public class Group : Xml
    {
        [XmlChoiceIdentifier("ReferenceTypes")]
        [XmlElement(ElementName="Objects", Type=typeof(Reference))]
        [XmlElement(ElementName="Groups", Type=typeof(Reference))]
        public Reference[] References;
        public ReferenceType[] ReferenceTypes;

        [XmlAttribute(AttributeName="name")]
        public string Name;

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
        public string Name;

        [XmlAttribute(AttributeName="start-immediately")]
        public bool StartImmediately;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="TimedActions")]
    public class TimedActions : Actions
    {
        [XmlAttribute(AttributeName="seconds-time")]
        public double SecondsTime;

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
        public string Action;

        [XmlAttribute(AttributeName="name")]
        public string Name;

        [XmlAttribute(AttributeName="filename")]
        public string Filename;

        [XmlAttribute(AttributeName="autostart")]
        public bool Autostart;
    }


    [Serializable]
    [XmlRoot(ElementName="Mode")]
    public class Mode : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Positional")]
        [XmlElement(ElementName="Fixed")]
        public object Data;
        public Modes Type;

        public enum Modes {
            [XmlEnum("Positional")] Positional,
            [XmlEnum("Fixed")] Fixed
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Repeat")]
    public class Repeat : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="NoRepeat")]
        [XmlElement(ElementName="RepeatForever")]
        [XmlElement(ElementName="RepeatNum", Type=typeof(uint))]
        public object Data;
        public RepeatTypes Type;
            
        public enum RepeatTypes {
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
        public double Frequency;

        [XmlAttribute(AttributeName="volume")]
        public double Volume;

        [XmlAttribute(AttributeName="pan")]
        public double Pan;
    }


    /********** EVENT TRIGGER       ***********/


    [Serializable]
    [XmlRoot(ElementName="EventTrigger")]
    public class EventTrigger : Xml
    {
        [XmlChoiceIdentifier("TrackType")]
        [XmlElement(ElementName="HeadTrack", Type=typeof(HeadTrack))]
        [XmlElement(ElementName="MoveTrack", Type=typeof(MoveTrack))]
        public object Tracking;
        public TrackTypes TrackType;

        [XmlElement(ElementName="Actions")]
        public List<Actions> Actions;

        [XmlAttribute(AttributeName="enabled")]
        public bool Enabled;

        [XmlAttribute(AttributeName="name")]
        public string Name;

        [XmlAttribute(AttributeName="duration")]
        public double Duration;

        [XmlAttribute(AttributeName="remain-enabled")]
        public bool RemainEnabled;

        public enum TrackTypes {
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
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Anywhere")]
        [XmlElement(ElementName="Box", Type=typeof(Box))]
        public object Position;
        public PositionTypes Type;

        public enum PositionTypes {
            [XmlEnum("Anywhere")] Anywhere,
            [XmlEnum("Box")] Box
        }
    }


    [Serializable]
    [XmlRoot(ElementName="Direction")]
    public class Direction : Xml
    {
        [XmlChoiceIdentifier("TargetType")]
        [XmlElement(ElementName="None")]
        [XmlElement(ElementName="PointTarget", Type=typeof(PointTarget))]
        [XmlElement(ElementName="DirectionTarget", Type=typeof(DirectionTarget))]
        [XmlElement(ElementName="ObjectTarget", Type=typeof(Reference))]
        public object Target;
        public Targets TargetType;

        public enum Targets {
            [XmlEnum("None")] None,
            [XmlEnum("PointTarget")] Point,
            [XmlEnum("DirectionTarget")] Direction,
            [XmlEnum("ObjectTarget")] Object
        }
    }


    [Serializable]
    [XmlRoot(ElementName="PointTarget")]
    public class PointTarget : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string PointString;

        [XmlAttribute(AttributeName="angle")]
        public double Angle;

    }


    [Serializable]
    [XmlRoot(ElementName="DirectionTarget")]
    public class DirectionTarget : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string DirectionString;

        [XmlAttribute(AttributeName="angle")]
        public double Angle;
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
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="ObjectRef", Type=typeof(Reference))]
        [XmlElement(ElementName="GroupObj", Type=typeof(GroupSource))]
        public object Data;
        public Sources Type;

        public enum Sources {
            [XmlEnum("ObjectRef")] Object,
            [XmlEnum("GroupObj")] Group,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="GroupObj")]
    public class GroupSource : Reference
    {
        [XmlAttribute(AttributeName="objects")]
        public Selections Selection;
        public enum Selections { 
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
        public bool IgnoreY;

        [XmlAttribute(AttributeName="corner1")]
        public string Corner1String;

        [XmlAttribute(AttributeName="corner2")]
        public string Corner2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Movement")]
    public class Movement : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Outside")]
        [XmlElement(ElementName="Inside")]
        public object Data;
        public MovementTypes Type;

        public enum MovementTypes {
            [XmlEnum("Outside")] Outside,
            [XmlEnum("Inside")] Inside
        }
    }


    /********** PARTICLE ACTION LIST     ***********/


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
        public string Name;
    }


    [Serializable]
    [XmlRoot(ElementName="Source")]
    public class ParticleSource : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="rate")]
        public double Rate;
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
        [XmlChoiceIdentifier("Type")]
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
        public object Action;
        public ParticleActionTypes Type;

        public enum ParticleActionTypes {
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
        public double Magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double Epsilon;

        [XmlAttribute(AttributeName="lookahead")]
        public double LookAhead;
    }


    [Serializable]
    [XmlRoot(ElementName="Bounce")]
    public class Bounce : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="friction")]
        public double Friction;

        [XmlAttribute(AttributeName="resilience")]
        public double Resilience;

        [XmlAttribute(AttributeName="cutoff")]
        public double Cutoff;
    }

    [Serializable]
    [XmlRoot(ElementName="Gravity")]
    public class Gravity : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string DirectionString;
    }


    [Serializable]
    [XmlRoot(ElementName="Damping")]
    public class Damping : Xml
    {
        [XmlAttribute(AttributeName="direction")]
        public string DirectionString;

        [XmlAttribute(AttributeName="vel_low")]
        public double VelocityLow;

        [XmlAttribute(AttributeName="vel_high")]
        public double VelocityHigh;
    }


    [Serializable]
    [XmlRoot(ElementName="Gravitate")]
    public class Gravitate : Xml
    {
        [XmlAttribute(AttributeName="magnitude")]
        public double Magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double Epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double MaxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Follow")]
    public class Follow : Xml
    {

        [XmlAttribute(AttributeName="magnitude")]
        public double Magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double Epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double MaxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="MatchVel")]
    public class MatchVel : Xml
    {
        [XmlAttribute(AttributeName="magnitude")]
        public double Magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double Epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double MaxRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="OrbitPoint")]
    public class OrbitPoint : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string CenterString;

        [XmlAttribute(AttributeName="magnitude")]
        public double Magnitude;

        [XmlAttribute(AttributeName="epsilon")]
        public double Epsilon;

        [XmlAttribute(AttributeName="max_radius")]
        public double MaxRadius;
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
        public string ColorString;

        [XmlAttribute(AttributeName="alpha")]
        public double Alpha;

        [XmlAttribute(AttributeName="scale")]
        public double Scale;
    }


    // REMOVE CONDITION


    [Serializable]
    [XmlRoot(ElementName="RemoveCondition")]
    public class RemoveCondition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Age", Type=typeof(Age))]
        [XmlElement(ElementName="Position", Type=typeof(Remove))]
        [XmlElement(ElementName="Velocity", Type=typeof(Remove))]
        public object Condition;
        public RemoveConditions Type;

        public enum RemoveConditions {
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
        public double Seconds;

        [XmlAttribute(AttributeName="younger-than")]
        public bool YoungerThan;
    }


    [Serializable]
    public class Remove : Xml
    {
        [XmlElement(ElementName="ParticleDomain")]
        public Particle Particle;

        [XmlAttribute(AttributeName="inside")]
        public bool Inside;
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
        public float FarClip;

        [XmlText]
        public string text;
    }


    [Serializable]
    [XmlRoot(ElementName="Background")]
    public class Background : Xml
    {
        [XmlAttribute(AttributeName="color")]
        public string ColorString;
    }


    [Serializable]
    [XmlRoot(ElementName="WandNavigation")]
    public class WandNavigation : Xml
    {
        [XmlAttribute(AttributeName="allow-rotation")]
        public bool AllowRotation;

        [XmlAttribute(AttributeName="allow-movement")]
        public bool AllowMovement;
    }


    /********** COMPLEX TYPES    ***********/


    // PLACEMENT


    [Serializable]
    [XmlRoot(ElementName="Placement")]
    public class Placement : Xml
    {
        [XmlElement(ElementName="RelativeTo")]
        public PlacementTypes RelativeTo;
        public enum PlacementTypes {
            Center,
            FrontWall,
            LeftWall,
            RightWall,
            FloorWall
        }


        [XmlElement(ElementName="Position")]
        public string PositionString;

        [XmlChoiceIdentifier("RotationType")]
        [XmlElement(ElementName="Axis", Type=typeof(Axis))]
        [XmlElement(ElementName="LookAt", Type=typeof(LookAt))]
        [XmlElement(ElementName="Normal", Type=typeof(Normal))]
        public object Rotation;
        public RotationTypes RotationType;
        public enum RotationTypes {
            Null,
            [XmlEnum("Axis")] Axis,
            [XmlEnum("LookAt")] LookAt,
            [XmlEnum("Normal")] Normal,
        }

        [XmlAttribute(AttributeName="name")]
        public string Name;

        [XmlText]
        public string text;
        
        /** Set parent GameObject and local transforms of gameObjectT
            relativeTo: [GameObject].transform.parent
            position: [GameObject].transform.localPosition
            rotationType.Axis: Rotation angle around an axis 
            rotationType.LookAt: Rotate to look at target vector (world space)
            rotationType.Normal: Local rotation around a normalized vector
        */
        // TODO (81): Split into separate functions that return their values
        public void SetTransform(Transform gameObjectT, float scale, Transform storyT) {
            gameObjectT.SetParent(
                this.RelativeTo == Placement.PlacementTypes.Center
                    ? storyT // Nest under Story directly
                    : storyT.Find(this.RelativeTo.ToString())
                , false
            );
            gameObjectT.localScale = Vector3.one * scale;
            gameObjectT.localPosition = Xml.ConvertVector3(this.PositionString);

            switch(this.Rotation) {
                case(Axis rotation):
                    gameObjectT.localEulerAngles = 
                        Xml.ConvertVector3(rotation.RotationString) * rotation.Angle;
                    break;
                case(LookAt rotation):
                    gameObjectT.rotation = Quaternion.LookRotation(
                        gameObjectT.position - 
                            storyT.TransformPoint(Xml.ConvertVector3(rotation.TargetString)),
                        Xml.ConvertVector3(rotation.UpString)
                    );
                    break;
                case(Normal rotation):
                    // TODO (63): Add logic
                    break;
                case(null):
                    gameObjectT.localRotation = Quaternion.identity;
                    break;
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
        public string RotationString;

        [XmlAttribute(AttributeName="angle")]
        public float Angle;
    }


    [Serializable]
    [XmlRoot(ElementName="LookAt")]
    public class LookAt : Xml
    {
        [XmlAttribute(AttributeName="target")]
        public string TargetString;

        [XmlAttribute(AttributeName="up")]
        public string UpString;
    }


    [Serializable]
    [XmlRoot(ElementName="Normal")]
    public class Normal : Xml
    {
        [XmlAttribute(AttributeName="normal")]
        public string NormalString;

        [XmlAttribute(AttributeName="angle")]
        public double Angle;
    }


    // ACTIONS


    [Serializable]
    public class Actions : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="ObjectChange", Type=typeof(ObjectChange))]
        [XmlElement(ElementName="GroupRef", Type=typeof(GroupRef))]
        [XmlElement(ElementName="TimerChange", Type=typeof(TimerChange))]
        [XmlElement(ElementName="SoundRef", Type=typeof(Reference))]
        [XmlElement(ElementName="Event", Type=typeof(Event))]
        [XmlElement(ElementName="MoveCave", Type=typeof(MoveCave))]
        [XmlElement(ElementName="Restart")]
        public object Action;
        public ActionTypes Type;

        public enum ActionTypes {
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
        public RandomTypes Random;
        public enum RandomTypes { 
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
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="start")]
        [XmlElement(ElementName="stop")]
        [XmlElement(ElementName="continue")]
        [XmlElement(ElementName="start_if_not_started")]
        public object Change;
        public ChangeTypes Type;

        public enum ChangeTypes {
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
        public bool Enable;
    }


    [Serializable]
    [XmlRoot(ElementName="MoveCave")]
    public class MoveCave : Xml
    {
        [XmlChoiceIdentifier("OriginType")]
        [XmlElement(ElementName="Relative")]
        [XmlElement(ElementName="Absolute")]
        public object Origin;
        public OriginTypes OriginType;

        [XmlElement(ElementName="Placement")]
        public Placement Placement;

        [XmlAttribute(AttributeName="duration")]
        public double duration;

        [XmlText]
        public string text;

        public enum OriginTypes {
            [XmlEnum("Relative")] Relative,
            [XmlEnum("Absolute")] Absolute,
        }
    }


    // TRANSITION

 
    [Serializable]
    public class Transition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Visible", Type=typeof(bool))]
        [XmlElement(ElementName="Movement", Type=typeof(MovementTransition))]
        [XmlElement(ElementName="MoveRel", Type=typeof(MoveRel))]
        [XmlElement(ElementName="Color", Type=typeof(string))]
        [XmlElement(ElementName="Scale", Type=typeof(double))]
        [XmlElement(ElementName="Sound", Type=typeof(SoundTransition))]
        [XmlElement(ElementName="LinkTransition", Type=typeof(LinkTransition))]
        public object Change;
        public TransitionType Type;

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
        public Controls Control;
        public enum Controls { 
            None,
            [XmlEnum(Name="Play Sound")] Play,
            [XmlEnum(Name="Stop Sound")] Stop,
        }
    }


    [Serializable]
    [XmlRoot(ElementName="LinkChange")]
    public class LinkTransition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="link_on")]
        [XmlElement(ElementName="link_off")]
        [XmlElement(ElementName="activate")]
        [XmlElement(ElementName="activate_if_on")]
        public object Transition;
        public LinkTransitionTypes Type;

        public enum LinkTransitionTypes {
            [XmlEnum("link_on")] On,
            [XmlEnum("link_off")] Off,
            [XmlEnum("activate")] Activate,
            [XmlEnum("activate_if_on")] ActivateIfOn,
        }
    }


    // PARTICLE DOMAIN


    [Serializable]
    [XmlRoot(ElementName="ParticleDomain")]
    public class Particle : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement(ElementName="Point", Type=typeof(Point))]
        [XmlElement(ElementName="Line", Type=typeof(Line))]
        [XmlElement(ElementName="Triangle", Type=typeof(Triangle))]
        [XmlElement(ElementName="Plane", Type=typeof(Plane))]
        [XmlElement(ElementName="Rect", Type=typeof(Rectangle))]
        [XmlElement(ElementName="Box", Type=typeof(BoxParticle))]
        [XmlElement(ElementName="Sphere", Type=typeof(Sphere))]
        [XmlElement(ElementName="Cylinder", Type=typeof(Cylinder))]
        [XmlElement(ElementName="Cone", Type=typeof(Cone))]
        [XmlElement(ElementName="Blob", Type=typeof(Blob))]
        [XmlElement(ElementName="Disc", Type=typeof(Disc))]
        public object Data;
        public ParticleTypes Type;

        public enum ParticleTypes {
            [XmlEnum("Point")] Point,
            [XmlEnum("Line")] Line,
            [XmlEnum("Triangle")] Triangle,
            [XmlEnum("Plane")] Plane,
            [XmlEnum("Rect")] Rectangle,
            [XmlEnum("Box")] BoxParticle,
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
        public string PointString;
    }


    [Serializable]
    [XmlRoot(ElementName="Line")]
    public class Line : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string P1String;

        [XmlAttribute(AttributeName="p2")]
        public string P2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Triangle")]
    public class Triangle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string P1String;

        [XmlAttribute(AttributeName="p2")]
        public string P2String;

        [XmlAttribute(AttributeName="p3")]
        public string P3String;
    }


    [Serializable]
    [XmlRoot(ElementName="Plane")]
    public class Plane : Xml
    {
        [XmlAttribute(AttributeName="point")]
        public string PointString;

        [XmlAttribute(AttributeName="normal")]
        public string NormalString;
    }


    [Serializable]
    [XmlRoot(ElementName="Rectangle")]
    public class Rectangle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string P1String;

        [XmlAttribute(AttributeName="u-dir")]
        public string UString;

        [XmlAttribute(AttributeName="v-dir")]
        public string VString;
    }


    [Serializable]
    [XmlRoot(ElementName="Box")]
    public class BoxParticle : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string P1String;

        [XmlAttribute(AttributeName="p2")]
        public string P2String;
    }


    [Serializable]
    [XmlRoot(ElementName="Sphere")]
    public class Sphere : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string CenterString;

        [XmlAttribute(AttributeName="radius")]
        public string RadiusString;

        [XmlAttribute(AttributeName="radius-inner")]
        public string InnerRadiusString;
    }


    [Serializable]
    [XmlRoot(ElementName="Cylinder")]
    public class Cylinder : Xml
    {
        [XmlAttribute(AttributeName="p1")]
        public string P1String;

        [XmlAttribute(AttributeName="p2")]
        public string P2String;

        [XmlAttribute(AttributeName="radius")]
        public double Radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double InnerRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Cone")]
    public class Cone : Xml
    {
        [XmlAttribute(AttributeName="base-center")]
        public string BaseCenterString;

        [XmlAttribute(AttributeName="apex")]
        public string ApexString;

        [XmlAttribute(AttributeName="radius")]
        public double Radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double InnerRadius;
    }


    [Serializable]
    [XmlRoot(ElementName="Blob")]
    public class Blob : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string CenterString;

        [XmlAttribute(AttributeName="stdev")]
        public double Deviation;
    }


    [Serializable]
    [XmlRoot(ElementName="Disc")]
    public class Disc : Xml
    {
        [XmlAttribute(AttributeName="center")]
        public string CenterString;

        [XmlAttribute(AttributeName="normal")]
        public string Normal;

        [XmlAttribute(AttributeName="radius")]
        public float Radius;

        [XmlAttribute(AttributeName="radius-inner")]
        public double InnerRadius;
    }


    // Reference another class/object by name
    [Serializable]
    public class Reference : Xml
    {
        [XmlAttribute(AttributeName="name")]
        public string Name;
    }
}

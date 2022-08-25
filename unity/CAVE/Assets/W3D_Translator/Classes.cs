using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Events;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using TMPro;

namespace XML
{
    [Serializable]
    public class Xml
    {
        // Print the class as a Json object
        public string Pprint() { return JsonUtility.ToJson(this, true); }

        // Converts "[int], [int], [int]" to a UnityEngine.Color object
        public static Color ConvertColor(string colorString)
        {
            string[] strings = colorString.Trim(new[] { ' ', '(', ')' }).Split(",");
            return new Color(
                float.Parse(strings[0]) / 255,
                float.Parse(strings[1]) / 255,
                float.Parse(strings[2]) / 255
            );
        }

        // Converts a "([float], [float], [float])" string to a UnityEngine.Vector3 object
        public static Vector3 ConvertVector3(string vectorString)
        {
            string[] strings = vectorString.Trim(new[] { ' ', '(', ')' }).Split(",");
            return new Vector3(
                float.Parse(strings[0]),
                float.Parse(strings[1]),
                float.Parse(strings[2]) * -1
            );
        }
    }

    /********** STORY            ***********/

    [Serializable]
    [XmlRoot("Story")]
    public class Story : Xml
    {
        [XmlArray("ObjectRoot")]
        [XmlArrayItem("Object")]
        public List<Object> ObjectRoot;

        [XmlArray("GroupRoot")]
        [XmlArrayItem("Group")]
        public List<Group> GroupRoot;

        [XmlArray("TimelineRoot")]
        [XmlArrayItem("Timeline")]
        public List<Timeline> TimelineRoot;

        [XmlArray("PlacementRoot")]
        [XmlArrayItem("Placement")]
        public List<Placement> PlacementRoot;

        [XmlArray("SoundRoot")]
        [XmlArrayItem("Sound")]
        public List<Sound> SoundRoot;

        [XmlArray("EventRoot")]
        [XmlArrayItem("EventTrigger")]
        public List<EventTrigger> EventRoot;

        [XmlArray("ParticleActionRoot")]
        [XmlArrayItem("ParticleActionList")]
        public List<ParticleAction> ParticleActionRoot;

        [XmlElement("Global")]
        public Global Global;

        [XmlElement("About")]
        public About About;

        [XmlAttribute("version")]
        public int Version;

        [XmlAttribute("last_xpath")]
        public string LastXpath;

        [XmlText]
        public string Text;
    }

    [Serializable]
    [XmlRoot("About")]
    public class About : Xml
    {
        [XmlAttribute("news")]
        public string News;
    }

    /********** OBJECT            ***********/

    [Serializable]
    [XmlRoot("Object")]
    public class Object : Xml
    {
        [XmlElement("Visible")]
        public bool Visible;

        [XmlElement("Color")]
        public string ColorString;

        [XmlElement("Lighting")]
        public bool Lighting;

        [XmlElement("ClickThrough")]
        public bool ClickThrough;

        [XmlElement("AroundSelfAxis")]
        public bool AroundSelfAxis;

        [XmlElement("Scale")]
        public float Scale;

        [XmlElement("SoundRef")]
        public string SoundRef;

        [XmlElement("Placement")]
        public Placement Placement;

        [XmlElement("Content")]
        public Content Content;

        [XmlElement("LinkRoot")]
        public LinkRoot LinkRoot;

        [XmlAttribute("name")]
        public string Name;

        [XmlText]
        public string Text;

        public Vector3 GetScale() { return Vector3.one * Scale; }
    }

    [XmlRoot("LinkRoot")]
    public class LinkRoot
    {
        [XmlElement("Link")]
        public Link Link;
    }

    // OBJECT.CONTENT

    [Serializable]
    [XmlRoot("Content")]
    public class Content : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("None", null)]
        [XmlElement("Text", typeof(Text))]
        [XmlElement("Image", typeof(Image))]
        [XmlElement("StereoImage", typeof(StereoImage))]
        [XmlElement("Model", typeof(Model))]
        [XmlElement("Light", typeof(Light))]
        [XmlElement("ParticleSystem", typeof(ParticleSystem))]
        public object ContentData;
        public ContentTypes Type;

        public enum ContentTypes
        {
            [XmlEnum("None")] None,
            [XmlEnum("Text")] Text,
            [XmlEnum("Image")] Image,
            [XmlEnum("StereoImage")] StereoImage,
            [XmlEnum("Model")] Model,
            [XmlEnum("Light")] Light,
            [XmlEnum("ParticleSystem")] ParticleSystem,
        }

        public GameObject Create(Object parent)
        {
            GameObject gameObject = ContentData switch
            {
                Text text => text.GenerateTMP(
                    parent.LinkRoot is not null,
                    ConvertColor(parent.ColorString)
                ),
                Image image => new GameObject(), // TODO (65)
                StereoImage stereoImage => new(), // TODO (66)
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
    [XmlRoot("Text")]
    public class Text : Xml
    {
        [XmlElement("text")]
        public string String;

        // Match TMPro.HorizontalAlignmentOptions
        [XmlAttribute("horiz-align")]
        public HorizontalAlignments HorizontalAlignment;
        public enum HorizontalAlignments
        {
            [XmlEnum(Name = "left")] Left = 1,
            [XmlEnum(Name = "center")] Center = 2,
            [XmlEnum(Name = "right")] Right = 4,
        }

        // Match TMPro.VerticalAlignmentOptions
        [XmlAttribute("vert-align")]
        public VerticalAlignments VerticalAlignment;
        public enum VerticalAlignments
        {
            [XmlEnum(Name = "top")] Top = 256,
            [XmlEnum(Name = "center")] Middle = 512,
            [XmlEnum(Name = "bottom")] Bottom = 1024,
        }

        [XmlAttribute("font")]
        public string Font;

        [XmlAttribute("depth")]
        public float Depth;

        public GameObject GenerateTMP(bool isLink, Color color)
        {
            // Instantiate TextMeshPro or TextMeshProUGUI prefab
            // TODO (64): Validate prefab settings
            GameObject gameObject = UnityEngine.Object.Instantiate(
                Resources.Load<GameObject>("Prefabs/TmpText" + (isLink ? "GUI" : ""))
            );
            TMP_Text tmpText = gameObject.GetComponent<TMP_Text>();

            // Set object properties defined in the xml
            tmpText.SetText(String);
            tmpText.horizontalAlignment = (HorizontalAlignmentOptions)HorizontalAlignment;
            tmpText.verticalAlignment = (VerticalAlignmentOptions)VerticalAlignment;
            tmpText.color = color; // Vertex Color
            tmpText.faceColor = color; // Material color

            // Load font material
            // TODO (72): More robust path checking
            TMP_FontAsset tmpFont = Resources.Load<TMP_FontAsset>(
                "Materials/Fonts/" +
                Path.GetFileNameWithoutExtension(Font) +
                " SDF"
            );
            if (tmpFont == null)
            {
                // Font material hasn't been created, attempt to load from ttf file
                try
                {
                    Font font = AssetDatabase.LoadAssetAtPath<Font>(Font);
                    tmpFont = TMP_FontAsset.CreateFontAsset(font);
                    tmpFont.name = Path.GetFileNameWithoutExtension(Font);
                }
                catch (NullReferenceException e)
                {
                    Debug.LogError($"Error loading font: {Font}");
                    Debug.LogException(e);
                }
            }

            // Add font to the TextMeshPro object
            try { tmpText.font = tmpFont; }
            catch (NullReferenceException e)
            {
                Debug.LogWarning($"{gameObject.name} {tmpFont} {tmpText.font}");
                Debug.LogError($"Error creating font asset {Font} for {gameObject.name}");
                Debug.Log("Defaulting to fallback font LiberationSans SDF");
                Debug.LogException(e);
            }

            return gameObject;
        }
    }

    [Serializable]
    [XmlRoot("Image")]
    public class Image : Xml
    {
        [XmlAttribute("filename")]
        public string Filename;
    }

    [Serializable]
    [XmlRoot("StereoImage")]
    public class StereoImage : Xml
    {
        [XmlAttribute("left-image")]
        public string LeftImage;

        [XmlAttribute("right-image")]
        public string RightImage;
    }

    [Serializable]
    [XmlRoot("Model")]
    public class Model : Xml
    {
        [XmlAttribute("filename")]
        public string Filename;

        [XmlAttribute("check-collisions")]
        public string CheckCollisions;
    }

    [Serializable]
    [XmlRoot("ParticleSystem")]
    // TODO (69): Unity has a ParticleSystem class
    public class ParticleSystem : Xml
    {
        [XmlAttribute("max-particles")]
        public int MaxParticles;

        [XmlAttribute("actions-name")]
        public string ActionsName;

        [XmlAttribute("particle-group")]
        public string ParticleGroup;

        [XmlAttribute("look-at-camera")]
        public bool LookAtCamera;

        [XmlAttribute("sequential")]
        public bool Sequential;

        [XmlAttribute(AttributeName = "speed")]
        public float Speed;
    }

    [Serializable]
    [XmlRoot("Light")]
    // TODO (68): Unity has a Light class
    public class Light : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Point")]
        [XmlElement("Directional")]
        [XmlElement("Spot", typeof(Spot))]
        public object Data;
        public LightTypes Type;

        [XmlAttribute("diffuse")]
        public bool Diffuse;

        [XmlAttribute("specular")]
        public bool Specular;

        [XmlAttribute(AttributeName = "const_atten")]
        public float ConstantAtten;

        [XmlAttribute(AttributeName = "lin_atten")]
        public float LinearAtten;

        [XmlAttribute(AttributeName = "quad_atten")]
        public float QuadraticAtten;

        public enum LightTypes
        {
            [XmlEnum("Point")] Point,
            [XmlEnum("Directional")] Directional,
            [XmlEnum("Spot")] Spot,
        }
    }

    [Serializable]
    [XmlRoot("Spot")]
    public class Spot : Xml
    {
        [XmlAttribute(AttributeName = "angle")]
        public float Angle;
    }

    // LINK

    [Serializable]
    [XmlRoot("Link")]
    public class Link : Xml
    {
        [XmlElement("Enabled")]
        public bool Enabled;

        [XmlElement("RemainEnabled")]
        public bool RemainEnabled;

        [XmlElement("EnabledColor")]
        public string EnabledColorString;

        [XmlElement("SelectedColor")]
        public string SelectedColorString;

        [XmlElement("Actions")]
        public List<LinkActions> Actions;

        public ColorBlock SetColors(ColorBlock colors, string parentColorString)
        {
            colors.normalColor = colors.highlightedColor =
                ConvertColor(EnabledColorString);
            colors.pressedColor = colors.selectedColor =
                ConvertColor(SelectedColorString);
            colors.disabledColor = ConvertColor(parentColorString);
            return colors;
        }
    }

    [Serializable]
    [XmlRoot("Actions")]
    public class LinkActions : Actions
    {
        [XmlElement("Clicks")]
        public Clicks Clicks;
    }

    [Serializable]
    [XmlRoot("Clicks")]
    public class Clicks : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Any")]
        [XmlElement("NumClicks", typeof(NumClicks))]
        public object Activation;
        public ActivationTypes Type;

        public enum ActivationTypes
        {
            [XmlEnum("Any")] Any,
            [XmlEnum("NumClicks")] Number,
        }

        // public static DefaultClicks
    }

    [Serializable]
    [XmlRoot("NumClicks")]
    public class NumClicks : Xml
    {
        [XmlAttribute("num_clicks")]
        public uint Clicks;

        [XmlAttribute("reset")]
        public bool Reset;
    }

    /********** GROUP            ***********/

    [Serializable]
    [XmlRoot("Group")]
    public class Group : Xml
    {
        [XmlChoiceIdentifier("ReferenceTypes")]
        [XmlElement("Objects", typeof(Reference))]
        [XmlElement("Groups", typeof(Reference))]
        public Reference[] References;
        public ReferenceType[] ReferenceTypes;

        [XmlAttribute("name")]
        public string Name;

        public enum ReferenceType
        {
            [XmlEnum("Objects")] Object,
            [XmlEnum("Groups")] Group
        }
    }

    /********** TIMELINE        ***********/

    [Serializable]
    [XmlRoot("Timeline")]
    public class Timeline : Xml
    {
        [XmlElement("TimedActions")]
        public List<TimedActions> TimedActions;

        [XmlAttribute("name")]
        public string Name;

        [XmlAttribute("start-immediately")]
        public bool StartImmediately;

        [XmlText]
        public string Text;
    }

    [Serializable]
    [XmlRoot("TimedActions")]
    public class TimedActions : Actions
    {
        [XmlAttribute("seconds-time")]
        public float SecondsTime;

        [XmlText]
        public string Text;
    }

    /********** SOUND            ***********/

    [Serializable]
    [XmlRoot("Sound")]
    public class Sound : Xml
    {
        [XmlElement("Mode")]
        public Mode Mode;

        [XmlElement("Repeat")]
        public Repeat Repeat;

        [XmlElement("Settings")]
        public Settings Settings;

        [XmlAttribute("action")]
        public string Action;

        [XmlAttribute("name")]
        public string Name;

        [XmlAttribute("filename")]
        public string Filename;

        [XmlAttribute("autostart")]
        public bool Autostart;
    }

    [Serializable]
    [XmlRoot("Mode")]
    public class Mode : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Positional")]
        [XmlElement("Fixed")]
        public object Data;
        public Modes Type;

        public enum Modes
        {
            [XmlEnum("Positional")] Positional,
            [XmlEnum("Fixed")] Fixed
        }
    }

    [Serializable]
    [XmlRoot("Repeat")]
    public class Repeat : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("NoRepeat")]
        [XmlElement("RepeatForever")]
        [XmlElement("RepeatNum", typeof(uint))]
        public object Data;
        public RepeatTypes Type;

        public enum RepeatTypes
        {
            [XmlEnum("NoRepeat")] No,
            [XmlEnum("RepeatForever")] Forever,
            [XmlEnum("RepeatNum")] Number,
        }
    }

    [Serializable]
    [XmlRoot("Settings")]
    public class Settings : Xml
    {
        [XmlAttribute("freq")]
        public float Frequency;

        [XmlAttribute("volume")]
        public float Volume;

        [XmlAttribute("pan")]
        public float Pan;
    }

    /********** EVENT TRIGGER       ***********/

    [Serializable]
    [XmlRoot("EventTrigger")]
    public class EventTrigger : Xml
    {
        [XmlChoiceIdentifier("TrackType")]
        [XmlElement("HeadTrack", typeof(HeadTrack))]
        [XmlElement("MoveTrack", typeof(MoveTrack))]
        public object Tracking;
        public TrackTypes TrackType;

        [XmlElement("Actions")]
        public List<Actions> Actions;

        [XmlAttribute("enabled")]
        public bool Enabled;

        [XmlAttribute("name")]
        public string Name;

        [XmlAttribute("duration")]
        public float Duration;

        [XmlAttribute("remain-enabled")]
        public bool RemainEnabled;

        public enum TrackTypes
        {
            [XmlEnum("HeadTrack")] Head,
            [XmlEnum("MoveTrack")] Move,
        }
    }

    // HEAD TRACK

    [Serializable]
    [XmlRoot("HeadTrack")]
    public class HeadTrack : Xml
    {
        [XmlElement("Position")]
        public TrackPosition Position;

        [XmlElement("Direction")]
        public Direction Direction;
    }

    [Serializable]
    [XmlRoot("Position")]
    public class TrackPosition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Anywhere")]
        [XmlElement("Box", typeof(Box))]
        public object Position;
        public PositionTypes Type;

        public enum PositionTypes
        {
            [XmlEnum("Anywhere")] Anywhere,
            [XmlEnum("Box")] Box
        }
    }

    [Serializable]
    [XmlRoot("Direction")]
    public class Direction : Xml
    {
        [XmlChoiceIdentifier("TargetType")]
        [XmlElement("None")]
        [XmlElement("PointTarget", typeof(PointTarget))]
        [XmlElement("DirectionTarget", typeof(DirectionTarget))]
        [XmlElement("ObjectTarget", typeof(Reference))]
        public object Target;
        public Targets TargetType;

        public enum Targets
        {
            [XmlEnum("None")] None,
            [XmlEnum("PointTarget")] Point,
            [XmlEnum("DirectionTarget")] Direction,
            [XmlEnum("ObjectTarget")] Object
        }
    }

    [Serializable]
    [XmlRoot("PointTarget")]
    public class PointTarget : Xml
    {
        [XmlAttribute("point")]
        public string PointString;

        [XmlAttribute("angle")]
        public float Angle;
    }

    [Serializable]
    [XmlRoot("DirectionTarget")]
    public class DirectionTarget : Xml
    {
        [XmlAttribute("direction")]
        public string DirectionString;

        [XmlAttribute("angle")]
        public float Angle;
    }

    // MOVE TRACK

    [Serializable]
    [XmlRoot("MoveTrack")]
    public class MoveTrack : Xml
    {
        [XmlElement("Source")]
        public Source Source;

        [XmlElement("Box")]
        public Box Box;
    }

    [Serializable]
    [XmlRoot("Source")]
    public class Source : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("ObjectRef", typeof(Reference))]
        [XmlElement("GroupObj", typeof(GroupSource))]
        public object Data;
        public Sources Type;

        public enum Sources
        {
            [XmlEnum("ObjectRef")] Object,
            [XmlEnum("GroupObj")] Group,
        }
    }

    [Serializable]
    [XmlRoot("GroupObj")]
    public class GroupSource : Reference
    {
        [XmlAttribute("objects")]
        public Selections Selection;
        public enum Selections
        {
            None,
            [XmlEnum(Name = "Any Object")] Any,
            [XmlEnum(Name = "All Objects")] All
        }
    }

    // BOX

    [Serializable]
    [XmlRoot("Box")]
    public class Box : Xml
    {
        [XmlElement("Movement")]
        public Movement Movement;

        [XmlAttribute("ignore-Y")]
        public bool IgnoreY;

        [XmlAttribute("corner1")]
        public string Corner1String;

        [XmlAttribute("corner2")]
        public string Corner2String;
    }

    [Serializable]
    [XmlRoot("Movement")]
    public class Movement : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Outside")]
        [XmlElement("Inside")]
        public object Data;
        public MovementTypes Type;

        public enum MovementTypes
        {
            [XmlEnum("Outside")] Outside,
            [XmlEnum("Inside")] Inside
        }
    }

    /********** PARTICLE ACTION LIST     ***********/

    [Serializable]
    [XmlRoot("ParticleActionList")]
    public class ParticleActionList : Xml
    {
        [XmlElement("Source")]
        public ParticleSource Source;

        [XmlElement("Vel")]
        public Vel Vel;

        [XmlElement("ParticleAction")]
        public List<ParticleAction> ParticleAction;

        [XmlElement("RemoveCondition")]
        public RemoveCondition RemoveCondition;

        [XmlAttribute("name")]
        public string Name;
    }

    [Serializable]
    [XmlRoot("Source")]
    public class ParticleSource : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;

        [XmlAttribute("rate")]
        public float Rate;
    }

    [Serializable]
    [XmlRoot("Vel")]
    public class Vel : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;
    }

    // PARTICLE ACTION

    [Serializable]
    [XmlRoot("ParticleAction")]
    public class ParticleAction : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Avoid", typeof(Avoid))]
        [XmlElement("Bounce", typeof(Bounce))]
        [XmlElement("Gravity", typeof(Gravity))]
        [XmlElement("Damping", typeof(Damping))]
        [XmlElement("Gravitate", typeof(Gravitate))]
        [XmlElement("Follow", typeof(Follow))]
        [XmlElement("MatchVel", typeof(MatchVel))]
        [XmlElement("OrbitPoint", typeof(OrbitPoint))]
        [XmlElement("Jet", typeof(Jet))]
        [XmlElement("RandomVel")]
        [XmlElement("RandomAccel")]
        [XmlElement("RandomDisplace")]
        [XmlElement("TargetColor", typeof(TargetColor))]
        [XmlElement("TargetSize")]
        [XmlElement("TargetVel")]
        public object Action;
        public ParticleActionTypes Type;

        public enum ParticleActionTypes
        {
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
    [XmlRoot("Avoid")]
    public class Avoid : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;

        [XmlAttribute("magnitude")]
        public float Magnitude;

        [XmlAttribute("epsilon")]
        public float Epsilon;

        [XmlAttribute("lookahead")]
        public float LookAhead;
    }

    [Serializable]
    [XmlRoot("Bounce")]
    public class Bounce : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;

        [XmlAttribute("friction")]
        public float Friction;

        [XmlAttribute("resilience")]
        public float Resilience;

        [XmlAttribute("cutoff")]
        public float Cutoff;
    }

    [Serializable]
    [XmlRoot("Gravity")]
    public class Gravity : Xml
    {
        [XmlAttribute("direction")]
        public string DirectionString;
    }

    [Serializable]
    [XmlRoot("Damping")]
    public class Damping : Xml
    {
        [XmlAttribute("direction")]
        public string DirectionString;

        [XmlAttribute("vel_low")]
        public float VelocityLow;

        [XmlAttribute("vel_high")]
        public float VelocityHigh;
    }

    [Serializable]
    [XmlRoot("Gravitate")]
    public class Gravitate : Xml
    {
        [XmlAttribute("magnitude")]
        public float Magnitude;

        [XmlAttribute("epsilon")]
        public float Epsilon;

        [XmlAttribute("max_radius")]
        public float MaxRadius;
    }

    [Serializable]
    [XmlRoot("Follow")]
    public class Follow : Xml
    {
        [XmlAttribute("magnitude")]
        public float Magnitude;

        [XmlAttribute("epsilon")]
        public float Epsilon;

        [XmlAttribute("max_radius")]
        public float MaxRadius;
    }

    [Serializable]
    [XmlRoot("MatchVel")]
    public class MatchVel : Xml
    {
        [XmlAttribute("magnitude")]
        public float Magnitude;

        [XmlAttribute("epsilon")]
        public float Epsilon;

        [XmlAttribute("max_radius")]
        public float MaxRadius;
    }

    [Serializable]
    [XmlRoot("OrbitPoint")]
    public class OrbitPoint : Xml
    {
        [XmlAttribute("center")]
        public string CenterString;

        [XmlAttribute("magnitude")]
        public float Magnitude;

        [XmlAttribute("epsilon")]
        public float Epsilon;

        [XmlAttribute("max_radius")]
        public float MaxRadius;
    }

    [Serializable]
    [XmlRoot("Jet")]
    public class Jet : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;

        [XmlElement("AccelDomain")]
        public Particle AccelDomain;
    }

    [Serializable]
    [XmlRoot("TargetColor")]
    public class TargetColor : Xml
    {
        [XmlAttribute("color")]
        public string ColorString;

        [XmlAttribute("alpha")]
        public float Alpha;

        [XmlAttribute("scale")]
        public float Scale;
    }

    // REMOVE CONDITION

    [Serializable]
    [XmlRoot("RemoveCondition")]
    public class RemoveCondition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Age", typeof(Age))]
        [XmlElement("Position", typeof(Remove))]
        [XmlElement("Velocity", typeof(Remove))]
        public object Condition;
        public RemoveConditions Type;

        public enum RemoveConditions
        {
            [XmlEnum("Age")] Age,
            [XmlEnum("Position")] Position,
            [XmlEnum("Velocity")] Velocity
        }
    }

    [Serializable]
    [XmlRoot("Age")]
    public class Age : Xml
    {
        [XmlAttribute("age")]
        public float Seconds;

        [XmlAttribute("younger-than")]
        public bool YoungerThan;
    }

    [Serializable]
    public class Remove : Xml
    {
        [XmlElement("ParticleDomain")]
        public Particle Particle;

        [XmlAttribute("inside")]
        public bool Inside;
    }

    /********** GLOBAL              ***********/

    [Serializable]
    [XmlRoot("Global")]
    public class Global : Xml
    {
        [XmlElement("CameraPos")]
        public Camera Camera;

        [XmlElement("CaveCameraPos")]
        public Camera CaveCamera;

        [XmlElement("Background")]
        public Background Background;

        [XmlElement("WandNavigation")]
        public WandNavigation WandNavigation;
    }

    [Serializable]
    public class Camera : Xml
    {
        [XmlElement("Placement")]
        public Placement Placement;

        [XmlAttribute("far-clip")]
        public float FarClip;

        [XmlText]
        public string Text;
    }

    [Serializable]
    [XmlRoot("Background")]
    public class Background : Xml
    {
        [XmlAttribute("color")]
        public string ColorString;
    }

    [Serializable]
    [XmlRoot("WandNavigation")]
    public class WandNavigation : Xml
    {
        [XmlAttribute("allow-rotation")]
        public bool AllowRotation;

        [XmlAttribute("allow-movement")]
        public bool AllowMovement;
    }

    /********** COMPLEX TYPES    ***********/

    // PLACEMENT

    [Serializable]
    [XmlRoot("Placement")]
    public class Placement : Xml
    {
        [XmlElement("RelativeTo")]
        public PlacementTypes RelativeTo;
        public enum PlacementTypes
        {
            Center,
            FrontWall,
            LeftWall,
            RightWall,
            FloorWall
        }

        [XmlElement("Position")]
        public string PositionString;

        [XmlChoiceIdentifier("RotationType")]
        [XmlElement("Axis", typeof(Axis))]
        [XmlElement("LookAt", typeof(LookAt))]
        [XmlElement("Normal", typeof(Normal))]
        public object Rotation;
        public RotationTypes RotationType;
        public enum RotationTypes
        {
            Null,
            [XmlEnum("Axis")] Axis,
            [XmlEnum("LookAt")] LookAt,
            [XmlEnum("Normal")] Normal,
        }

        [XmlAttribute("name")]
        public string Name;

        [XmlText]
        public string Text;

        /** Set parent GameObject and local transforms of gameObjectT
            relativeTo: [GameObject].transform.parent
            position: [GameObject].transform.localPosition
            rotationType.Axis: Rotation angle around an axis
            rotationType.LookAt: Rotate to look at target vector (world space)
            rotationType.Normal: Local rotation around a normalized vector
        */
        // TODO (81): Split into separate functions that return their values
        public void SetTransform(Transform gameObjectT, Vector3 scale, Transform storyT)
        {
            gameObjectT.SetParent(GetParent(storyT), false);
            gameObjectT.localPosition = GetPosition();
            gameObjectT.localScale = scale;

            switch (Rotation)
            {
                case Axis rotation:
                    gameObjectT.localEulerAngles = rotation.GetEuler();
                    break;
                case LookAt rotation:
                    gameObjectT.rotation = rotation.GetQuaternion(gameObjectT.position, storyT);
                    break;
                case Normal rotation:
                    gameObjectT.localEulerAngles = rotation.GetEuler();
                    break;
                case null:
                    gameObjectT.localRotation = Quaternion.identity;
                    break;
                default: break;
            }
            return;
        }

        public Vector3 GetPosition() { return ConvertVector3(PositionString); }

        public Transform GetParent(Transform storyT)
        {
            return RelativeTo == PlacementTypes.Center
                    ? storyT // Nest under Story directly
                    : storyT.Find(RelativeTo.ToString());
        }
    }

    [Serializable]
    [XmlRoot("Axis")]
    public class Axis : Xml
    {
        [XmlAttribute("rotation")]
        public string RotationString;

        [XmlAttribute("angle")]
        public float Angle;

        public Vector3 GetEuler()
        {
            return ConvertVector3(RotationString) * Angle;
        }
    }

    [Serializable]
    [XmlRoot("LookAt")]
    public class LookAt : Xml
    {
        [XmlAttribute("target")]
        public string TargetString;

        [XmlAttribute("up")]
        public string UpString;

        public Quaternion GetQuaternion(Vector3 position, Transform storyT)
        {
            return Quaternion.LookRotation(
                position -
                    storyT.TransformPoint(ConvertVector3(TargetString)),
                ConvertVector3(UpString)
            );
        }
    }

    [Serializable]
    [XmlRoot("Normal")]
    public class Normal : Xml
    {
        [XmlAttribute("normal")]
        public string NormalString;

        [XmlAttribute("angle")]
        public float Angle;

        public Vector3 GetEuler()
        {
            // TODO (63): Is this the correct logic?
            return ConvertVector3(NormalString) * Angle;
        }
    }

    // ACTIONS

    [Serializable]
    public class Actions : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("ObjectChange", typeof(ObjectChange))]
        [XmlElement("GroupRef", typeof(GroupRef))]
        [XmlElement("TimerChange", typeof(TimerChange))]
        [XmlElement("SoundRef", typeof(Reference))]
        [XmlElement("Event", typeof(Event))]
        [XmlElement("MoveCave", typeof(MoveCave))]
        [XmlElement("Restart")]
        public object Action;
        public ActionTypes Type;

        public enum ActionTypes
        {
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
    [XmlRoot("ObjectChange")]
    public class ObjectChange : Reference
    {
        [XmlElement("Transition")]
        public Transition Transition;

        [XmlText]
        public string Text;
    }

    [Serializable]
    [XmlRoot("GroupRef")]
    public class GroupRef : Reference
    {
        [XmlElement("Transition")]
        public Transition Transition;

        [XmlAttribute("random")]
        public RandomTypes Random;
        public enum RandomTypes
        {
            None,
            [XmlEnum(Name = "Select One Randomly")] OneRandom,
        }

        [XmlText]
        public string Text;
    }

    [Serializable]
    [XmlRoot("TimerChange")]
    public class TimerChange : Reference
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("start")]
        [XmlElement("stop")]
        [XmlElement("continue")]
        [XmlElement("start_if_not_started")]
        public object Change;
        public ChangeTypes Type;

        public enum ChangeTypes
        {
            [XmlEnum("start")] Start,
            [XmlEnum("stop")] Stop,
            [XmlEnum("continue")] Continue,
            [XmlEnum("start_if_not_started")] StartIfNotStarted,
        }
    }

    [Serializable]
    [XmlRoot("Event")]
    public class Event : Reference
    {
        [XmlAttribute("enable")]
        public bool Enable;
    }

    [Serializable]
    [XmlRoot("MoveCave")]
    public class MoveCave : Xml
    {
        [XmlChoiceIdentifier("OriginType")]
        [XmlElement("Relative")]
        [XmlElement("Absolute")]
        public object Origin;
        public OriginTypes OriginType;

        [XmlElement("Placement")]
        public Placement Placement;

        [XmlAttribute("duration")]
        public float Duration;

        [XmlText]
        public string Text;

        public enum OriginTypes
        {
            [XmlEnum("Relative")] Relative,
            [XmlEnum("Absolute")] Absolute,
        }
    }

    // TRANSITION

    [Serializable]
    public class Transition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Visible", typeof(bool))]
        [XmlElement("Movement", typeof(MovementTransition))]
        [XmlElement("MoveRel", typeof(MoveRel))]
        [XmlElement("Color", typeof(string))]
        [XmlElement("Scale", typeof(float))]
        [XmlElement("Sound", typeof(SoundTransition))]
        [XmlElement("LinkTransition", typeof(LinkTransition))]
        public object Change;
        public TransitionType Type;

        [XmlAttribute("duration")]
        public float Duration;

        [XmlText]
        public string Text;

        public enum TransitionType
        {
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
    [XmlRoot("Movement")]
    public class MovementTransition : Xml
    {
        [XmlElement("Placement")]
        public Placement Placement;
    }

    [Serializable]
    [XmlRoot("MoveRel")]
    public class MoveRel : Xml
    {
        [XmlElement("Placement")]
        public Placement Placement;
    }

    [Serializable]
    [XmlRoot("Sound")]
    public class SoundTransition : Xml
    {
        [XmlAttribute("action")]
        public Controls Control;
        public enum Controls
        {
            None,
            [XmlEnum(Name = "Play Sound")] Play,
            [XmlEnum(Name = "Stop Sound")] Stop,
        }
    }

    [Serializable]
    [XmlRoot("LinkChange")]
    public class LinkTransition : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("link_on")]
        [XmlElement("link_off")]
        [XmlElement("activate")]
        [XmlElement("activate_if_on")]
        public object Transition;
        public LinkTransitionTypes Type;

        public enum LinkTransitionTypes
        {
            [XmlEnum("link_on")] On,
            [XmlEnum("link_off")] Off,
            [XmlEnum("activate")] Activate,
            [XmlEnum("activate_if_on")] ActivateIfOn,
        }
    }

    // PARTICLE DOMAIN

    [Serializable]
    [XmlRoot("ParticleDomain")]
    public class Particle : Xml
    {
        [XmlChoiceIdentifier("Type")]
        [XmlElement("Point", typeof(Point))]
        [XmlElement("Line", typeof(Line))]
        [XmlElement("Triangle", typeof(Triangle))]
        [XmlElement("Plane", typeof(Plane))]
        [XmlElement("Rect", typeof(Rectangle))]
        [XmlElement("Box", typeof(BoxParticle))]
        [XmlElement("Sphere", typeof(Sphere))]
        [XmlElement("Cylinder", typeof(Cylinder))]
        [XmlElement("Cone", typeof(Cone))]
        [XmlElement("Blob", typeof(Blob))]
        [XmlElement("Disc", typeof(Disc))]
        public object Data;
        public ParticleTypes Type;

        public enum ParticleTypes
        {
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
    [XmlRoot("Point")]
    public class Point : Xml
    {
        [XmlAttribute("point")]
        public string PointString;
    }

    [Serializable]
    [XmlRoot("Line")]
    public class Line : Xml
    {
        [XmlAttribute("p1")]
        public string P1String;

        [XmlAttribute("p2")]
        public string P2String;
    }

    [Serializable]
    [XmlRoot("Triangle")]
    public class Triangle : Xml
    {
        [XmlAttribute("p1")]
        public string P1String;

        [XmlAttribute("p2")]
        public string P2String;

        [XmlAttribute("p3")]
        public string P3String;
    }

    [Serializable]
    [XmlRoot("Plane")]
    public class Plane : Xml
    {
        [XmlAttribute("point")]
        public string PointString;

        [XmlAttribute("normal")]
        public string NormalString;
    }

    [Serializable]
    [XmlRoot("Rectangle")]
    public class Rectangle : Xml
    {
        [XmlAttribute("p1")]
        public string P1String;

        [XmlAttribute("u-dir")]
        public string UString;

        [XmlAttribute("v-dir")]
        public string VString;
    }

    [Serializable]
    [XmlRoot("Box")]
    public class BoxParticle : Xml
    {
        [XmlAttribute("p1")]
        public string P1String;

        [XmlAttribute("p2")]
        public string P2String;
    }

    [Serializable]
    [XmlRoot("Sphere")]
    public class Sphere : Xml
    {
        [XmlAttribute("center")]
        public string CenterString;

        [XmlAttribute("radius")]
        public string RadiusString;

        [XmlAttribute("radius-inner")]
        public string InnerRadiusString;
    }

    [Serializable]
    [XmlRoot("Cylinder")]
    public class Cylinder : Xml
    {
        [XmlAttribute("p1")]
        public string P1String;

        [XmlAttribute("p2")]
        public string P2String;

        [XmlAttribute("radius")]
        public float Radius;

        [XmlAttribute("radius-inner")]
        public float InnerRadius;
    }

    [Serializable]
    [XmlRoot("Cone")]
    public class Cone : Xml
    {
        [XmlAttribute("base-center")]
        public string BaseCenterString;

        [XmlAttribute("apex")]
        public string ApexString;

        [XmlAttribute("radius")]
        public float Radius;

        [XmlAttribute("radius-inner")]
        public float InnerRadius;
    }

    [Serializable]
    [XmlRoot("Blob")]
    public class Blob : Xml
    {
        [XmlAttribute("center")]
        public string CenterString;

        [XmlAttribute("stdev")]
        public float Deviation;
    }

    [Serializable]
    [XmlRoot("Disc")]
    public class Disc : Xml
    {
        [XmlAttribute("center")]
        public string CenterString;

        [XmlAttribute("normal")]
        public string Normal;

        [XmlAttribute("radius")]
        public float Radius;

        [XmlAttribute("radius-inner")]
        public float InnerRadius;
    }

    // Reference another class/object by name
    [Serializable]
    public class Reference : Xml
    {
        [XmlAttribute("name")]
        public string Name;
    }
}
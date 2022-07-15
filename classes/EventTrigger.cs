[XmlRoot(ElementName="EventTrigger")]
public class EventTrigger { 

	[XmlElement(ElementName="HeadTrack")] 
	public HeadTrack HeadTrack; 

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
}

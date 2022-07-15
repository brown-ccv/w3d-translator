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

	[XmlElement(ElementName="EventRoot")] 
	public EventRoot EventRoot; 

	[XmlElement(ElementName="Global")] 
	public Global Global; 

	[XmlAttribute(AttributeName="version")] 
	public int Version; 

	[XmlAttribute(AttributeName="last_xpath")] 
	public string LastXpath; 

	[XmlText] 
	public string Text; 

	[XmlElement(ElementName="SoundRoot")] 
	public SoundRoot SoundRoot; 

	[XmlElement(ElementName="ParticleActionRoot")] 
	public ParticleActionRoot ParticleActionRoot; 
}

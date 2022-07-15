[XmlRoot(ElementName="Sound")]
public class Sound { 

	[XmlAttribute(AttributeName="action")] 
	public string Action; 

	[XmlElement(ElementName="Mode")] 
	public Mode Mode; 

	[XmlElement(ElementName="Repeat")] 
	public Repeat Repeat; 

	[XmlElement(ElementName="Settings")] 
	public Settings Settings; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 

	[XmlAttribute(AttributeName="filename")] 
	public string Filename; 

	[XmlAttribute(AttributeName="autostart")] 
	public bool Autostart; 
}

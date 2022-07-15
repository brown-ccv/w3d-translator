[XmlRoot(ElementName="Event")]
public class Event { 

	[XmlAttribute(AttributeName="enable")] 
	public bool Enable; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 
}

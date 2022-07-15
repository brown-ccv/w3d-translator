[XmlRoot(ElementName="Placement")]
public class Placement { 

	[XmlElement(ElementName="RelativeTo")] 
	public string RelativeTo; 

	[XmlElement(ElementName="Position")] 
	public string Position; 

	[XmlElement(ElementName="Axis")] 
	public Axis Axis; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 

	[XmlText] 
	public string Text; 

	[XmlElement(ElementName="LookAt")] 
	public LookAt LookAt; 
}

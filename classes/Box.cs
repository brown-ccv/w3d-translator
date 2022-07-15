[XmlRoot(ElementName="Box")]
public class Box { 

	[XmlElement(ElementName="Movement")] 
	public Movement Movement; 

	[XmlAttribute(AttributeName="ignore-Y")] 
	public bool IgnoreY; 

	[XmlAttribute(AttributeName="corner1")] 
	public string Corner1; 

	[XmlAttribute(AttributeName="corner2")] 
	public string Corner2; 

	[XmlAttribute(AttributeName="p1")] 
	public string P1; 

	[XmlAttribute(AttributeName="p2")] 
	public string P2; 
}

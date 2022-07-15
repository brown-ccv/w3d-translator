[XmlRoot(ElementName="Cylinder")]
public class Cylinder { 

	[XmlAttribute(AttributeName="p1")] 
	public string P1; 

	[XmlAttribute(AttributeName="p2")] 
	public string P2; 

	[XmlAttribute(AttributeName="radius")] 
	public double Radius; 

	[XmlAttribute(AttributeName="radius-inner")] 
	public double RadiusInner; 
}

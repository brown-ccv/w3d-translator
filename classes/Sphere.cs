[XmlRoot(ElementName="Sphere")]
public class Sphere { 

	[XmlAttribute(AttributeName="center")] 
	public string Center; 

	[XmlAttribute(AttributeName="radius")] 
	public int Radius; 

	[XmlAttribute(AttributeName="radius-inner")] 
	public double RadiusInner; 
}

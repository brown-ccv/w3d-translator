[XmlRoot(ElementName="Disc")]
public class Disc { 

	[XmlAttribute(AttributeName="center")] 
	public string Center; 

	[XmlAttribute(AttributeName="normal")] 
	public string Normal; 

	[XmlAttribute(AttributeName="radius")] 
	public int Radius; 

	[XmlAttribute(AttributeName="radius-inner")] 
	public double RadiusInner; 
}

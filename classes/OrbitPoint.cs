[XmlRoot(ElementName="OrbitPoint")]
public class OrbitPoint { 

	[XmlAttribute(AttributeName="center")] 
	public string Center; 

	[XmlAttribute(AttributeName="magnitude")] 
	public double Magnitude; 

	[XmlAttribute(AttributeName="epsilon")] 
	public double Epsilon; 

	[XmlAttribute(AttributeName="max_radius")] 
	public double MaxRadius; 
}

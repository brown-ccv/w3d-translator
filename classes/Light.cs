[XmlRoot(ElementName="Light")]
public class Light { 

	[XmlElement(ElementName="Point")] 
	public object Point; 

	[XmlAttribute(AttributeName="diffuse")] 
	public bool Diffuse; 

	[XmlAttribute(AttributeName="specular")] 
	public bool Specular; 

	[XmlAttribute(AttributeName="const_atten")] 
	public double ConstAtten; 

	[XmlAttribute(AttributeName="lin_atten")] 
	public double LinAtten; 

	[XmlAttribute(AttributeName="quad_atten")] 
	public double QuadAtten; 
}

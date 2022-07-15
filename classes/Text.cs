[XmlRoot(ElementName="Text")]
public class Text { 

	[XmlElement(ElementName="text")] 
	public List<string> Text; 

	[XmlAttribute(AttributeName="horiz-align")] 
	public string HorizAlign; 

	[XmlAttribute(AttributeName="vert-align")] 
	public string VertAlign; 

	[XmlAttribute(AttributeName="font")] 
	public string Font; 

	[XmlAttribute(AttributeName="depth")] 
	public double Depth; 
}

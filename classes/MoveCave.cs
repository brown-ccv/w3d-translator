[XmlRoot(ElementName="MoveCave")]
public class MoveCave { 

	[XmlElement(ElementName="Relative")] 
	public object Relative; 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 

	[XmlAttribute(AttributeName="duration")] 
	public double Duration; 

	[XmlText] 
	public string Text; 
}

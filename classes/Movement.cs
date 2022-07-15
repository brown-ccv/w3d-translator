[XmlRoot(ElementName="Movement")]
public class Movement { 

	[XmlElement(ElementName="Outside")] 
	public object Outside; 

	[XmlElement(ElementName="Inside")] 
	public object Inside; 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 
}

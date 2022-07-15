[XmlRoot(ElementName="Transition")]
public class Transition { 

	[XmlElement(ElementName="MoveRel")] 
	public MoveRel MoveRel; 

	[XmlAttribute(AttributeName="duration")] 
	public double Duration; 

	[XmlText] 
	public string Text; 

	[XmlElement(ElementName="Visible")] 
	public bool Visible; 

	[XmlElement(ElementName="LinkChange")] 
	public LinkChange LinkChange; 

	[XmlElement(ElementName="Scale")] 
	public double Scale; 

	[XmlElement(ElementName="Movement")] 
	public Movement Movement; 

	[XmlElement(ElementName="Sound")] 
	public Sound Sound; 

	[XmlElement(ElementName="Color")] 
	public double Color; 
}

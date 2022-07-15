[XmlRoot(ElementName="ObjectChange")]
public class ObjectChange { 

	[XmlElement(ElementName="Transition")] 
	public Transition Transition; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 

	[XmlText] 
	public bool Text; 
}

[XmlRoot(ElementName="GroupRef")]
public class GroupRef { 

	[XmlElement(ElementName="Transition")] 
	public Transition Transition; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 

	[XmlText] 
	public string Text; 
}

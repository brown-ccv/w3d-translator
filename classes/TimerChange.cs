[XmlRoot(ElementName="TimerChange")]
public class TimerChange { 

	[XmlElement(ElementName="start_if_not_started")] 
	public object StartIfNotStarted; 

	[XmlAttribute(AttributeName="name")] 
	public string Name; 

	[XmlElement(ElementName="start")] 
	public object Start; 

	[XmlElement(ElementName="stop")] 
	public object Stop; 
}

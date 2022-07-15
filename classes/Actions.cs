[XmlRoot(ElementName="Actions")]
public class Actions { 

	[XmlElement(ElementName="Event")] 
	public Event Event; 

	[XmlElement(ElementName="TimerChange")] 
	public TimerChange TimerChange; 

	[XmlElement(ElementName="Clicks")] 
	public Clicks Clicks; 
}

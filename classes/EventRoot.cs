[XmlRoot(ElementName="EventRoot")]
public class EventRoot { 

	[XmlElement(ElementName="EventTrigger")] 
	public List<EventTrigger> EventTrigger; 
}

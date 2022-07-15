[XmlRoot(ElementName="TimedActions")]
public class TimedActions { 

	[XmlElement(ElementName="GroupRef")] 
	public GroupRef GroupRef; 

	[XmlAttribute(AttributeName="seconds-time")] 
	public double SecondsTime; 

	[XmlText] 
	public string Text; 

	[XmlElement(ElementName="TimerChange")] 
	public TimerChange TimerChange; 

	[XmlElement(ElementName="SoundRef")] 
	public SoundRef SoundRef; 

	[XmlElement(ElementName="ObjectChange")] 
	public ObjectChange ObjectChange; 

	[XmlElement(ElementName="MoveCave")] 
	public MoveCave MoveCave; 
}

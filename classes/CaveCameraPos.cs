[XmlRoot(ElementName="CaveCameraPos")]
public class CaveCameraPos { 

	[XmlElement(ElementName="Placement")] 
	public Placement Placement; 

	[XmlAttribute(AttributeName="far-clip")] 
	public int FarClip; 

	[XmlText] 
	public string Text; 
}

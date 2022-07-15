[XmlRoot(ElementName="Global")]
public class Global { 

	[XmlElement(ElementName="CameraPos")] 
	public CameraPos CameraPos; 

	[XmlElement(ElementName="CaveCameraPos")] 
	public CaveCameraPos CaveCameraPos; 

	[XmlElement(ElementName="Background")] 
	public Background Background; 

	[XmlElement(ElementName="WandNavigation")] 
	public WandNavigation WandNavigation; 
}

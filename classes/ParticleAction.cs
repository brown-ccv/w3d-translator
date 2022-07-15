[XmlRoot(ElementName="ParticleAction")]
public class ParticleAction { 

	[XmlElement(ElementName="Gravity")] 
	public Gravity Gravity; 

	[XmlElement(ElementName="Bounce")] 
	public Bounce Bounce; 

	[XmlElement(ElementName="OrbitPoint")] 
	public OrbitPoint OrbitPoint; 
}

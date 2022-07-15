[XmlRoot(ElementName="ParticleSystem")]
public class ParticleSystem { 

	[XmlAttribute(AttributeName="max-particles")] 
	public int MaxParticles; 

	[XmlAttribute(AttributeName="actions-name")] 
	public int ActionsName; 

	[XmlAttribute(AttributeName="particle-group")] 
	public string ParticleGroup; 

	[XmlAttribute(AttributeName="look-at-camera")] 
	public bool LookAtCamera; 

	[XmlAttribute(AttributeName="sequential")] 
	public bool Sequential; 

	[XmlAttribute(AttributeName="speed")] 
	public double Speed; 
}

[XmlRoot(ElementName="Bounce")]
public class Bounce { 

	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="friction")] 
	public double Friction; 

	[XmlAttribute(AttributeName="resilience")] 
	public double Resilience; 

	[XmlAttribute(AttributeName="cutoff")] 
	public int Cutoff; 
}

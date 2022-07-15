[XmlRoot(ElementName="Position")]
public class Position { 

	[XmlElement(ElementName="Box")] 
	public Box Box; 

	[XmlElement(ElementName="ParticleDomain")] 
	public ParticleDomain ParticleDomain; 

	[XmlAttribute(AttributeName="inside")] 
	public bool Inside; 
}

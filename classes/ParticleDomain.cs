[XmlRoot(ElementName="ParticleDomain")]
public class ParticleDomain { 

	[XmlElement(ElementName="Line")] 
	public Line Line; 

	[XmlElement(ElementName="Cylinder")] 
	public Cylinder Cylinder; 

	[XmlElement(ElementName="Disc")] 
	public Disc Disc; 

	[XmlElement(ElementName="Plane")] 
	public Plane Plane; 

	[XmlElement(ElementName="Sphere")] 
	public Sphere Sphere; 

	[XmlElement(ElementName="Box")] 
	public Box Box; 
}

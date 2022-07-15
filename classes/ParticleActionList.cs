[XmlRoot(ElementName="ParticleActionList")]
public class ParticleActionList { 

	[XmlElement(ElementName="Source")] 
	public Source Source; 

	[XmlElement(ElementName="Vel")] 
	public Vel Vel; 

	[XmlElement(ElementName="ParticleAction")] 
	public List<ParticleAction> ParticleAction; 

	[XmlElement(ElementName="RemoveCondition")] 
	public RemoveCondition RemoveCondition; 

	[XmlAttribute(AttributeName="name")] 
	public int Name; 
}

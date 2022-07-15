[XmlRoot(ElementName="Age")]
public class Age { 

	[XmlAttribute(AttributeName="age")] 
	public int Age; 

	[XmlAttribute(AttributeName="younger-than")] 
	public bool YoungerThan; 
}

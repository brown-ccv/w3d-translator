[XmlRoot(ElementName="Link")]
public class Link { 

	[XmlElement(ElementName="Enabled")] 
	public bool Enabled; 

	[XmlElement(ElementName="RemainEnabled")] 
	public bool RemainEnabled; 

	[XmlElement(ElementName="EnabledColor")] 
	public double EnabledColor; 

	[XmlElement(ElementName="SelectedColor")] 
	public double SelectedColor; 

	[XmlElement(ElementName="Actions")] 
	public Actions Actions; 
}

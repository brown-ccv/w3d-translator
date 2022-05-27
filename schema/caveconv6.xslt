<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <!-- Copy Story, Set version -->
  <xsl:template match="Story">
  <Story>
  <xsl:attribute name="version">7</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </Story>
  </xsl:template>
  
  <!-- Convert Sound-->
  <xsl:template match="Sound">
  <Sound name="{Filename}" filename="{Filename}" autostart="false">
  <Repeat><NoRepeat/></Repeat>
  <Settings freq="1.0" volume="1.0" pan="0.0"></Settings>
  </Sound>
  </xsl:template>
  
  <!-- Convert Link-->
  <xsl:template match="Object">
  <Object>
  <xsl:apply-templates select="@*|node()"/>
  <LinkRoot><xsl:copy-of select="Content/descendant::Link"></xsl:copy-of></LinkRoot>
  </Object>
  </xsl:template>
  
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
</xsl:stylesheet>

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <!-- Copy Story, Set version -->
  <xsl:template match="Story">
  <Story>
  <xsl:attribute name="version">5</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </Story>
  </xsl:template>
  
  <!-- Filter Effects -->
  <xsl:template match="/Story/Placement/LookAt[@target='(0.0, 0.0, -1.0)']">
  <LookAt>
  <xsl:attribute name="up"><xsl:value-of select="@up"/></xsl:attribute>
  <xsl:attribute name="target">(0.0, 0.0, 0.0)</xsl:attribute>
  </LookAt>
  </xsl:template>
  
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
</xsl:stylesheet>

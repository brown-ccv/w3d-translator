<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <!-- Copy Story, Set version -->
  <xsl:template match="Story">
  <Story>
  <xsl:attribute name="version">8</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </Story>
  </xsl:template>
  
  
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
</xsl:stylesheet>

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <!-- Copy Story, Set version -->
  <xsl:template match="story">
  <story>
  <xsl:attribute name="version">3</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </story>
  </xsl:template>
  
  <!-- Filter Effects -->
  <xsl:template match="scene[@start-time=-1]">
  <scene>
   <xsl:copy-of select="@*"/>
  <xsl:attribute name="start-time">0</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </scene>
  </xsl:template>
  
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
</xsl:stylesheet>

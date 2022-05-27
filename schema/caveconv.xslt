<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <!-- Copy Story, Set version -->
  <xsl:template match="story">
  <story>
  <xsl:attribute name="version">2</xsl:attribute>
  <xsl:apply-templates select="child::*"/>
  </story>
  </xsl:template>
  
  <!-- Filter Effects -->
  <xsl:template match="effect[@effect-type='link']">
    <xsl:variable name="linkto" select="@link-to"/>
    <effect>
      <!--<xsl:copy-of select="@*[not(self::effect-type) and not(self::link-to)]"/>-->
      <xsl:attribute name="effect-type">none</xsl:attribute>
      <xsl:attribute name="start-time">0</xsl:attribute>
      <xsl:attribute name="duration">0</xsl:attribute>
        <xsl:for-each select="word">
        <word>
          <xsl:copy-of select="@*"/>
          <xsl:attribute name="link-to"><xsl:value-of select="$linkto"/></xsl:attribute>
          <xsl:attribute name="activate-once">0</xsl:attribute>
          <xsl:value-of select="text()"/>
        </word>
      </xsl:for-each>
    </effect>
  </xsl:template>
  
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
</xsl:stylesheet>

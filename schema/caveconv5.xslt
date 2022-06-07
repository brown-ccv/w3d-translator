<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  <!-- Copy Story, Set version -->
  <xsl:template match="Story">
    <Story version="6">
      <About/>
      <ObjectRoot>
        <xsl:for-each select="Object">
          <xsl:copy-of select="."/>
        </xsl:for-each>
      </ObjectRoot>
      <GroupRoot>
        <xsl:for-each select="Group">
          <xsl:copy-of select="."/>
        </xsl:for-each>
      </GroupRoot>
      <TimelineRoot>
        <xsl:for-each select="Timeline">
          <xsl:copy-of select="."/>
        </xsl:for-each>
      </TimelineRoot>
      <PlacementRoot>
        <xsl:for-each select="Placement">
          <xsl:copy-of select="."/>
        </xsl:for-each>
      </PlacementRoot>
      <SoundRoot>
        <xsl:for-each select="Sound">
          <xsl:copy-of select="."/>
        </xsl:for-each>
      </SoundRoot>
      <xsl:copy-of select="Global"/>
    </Story>
  </xsl:template>
</xsl:stylesheet>

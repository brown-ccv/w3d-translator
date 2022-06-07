<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  <!-- Story -->
  <xsl:template match="story">
    <Story>
      <xsl:attribute name="version">7</xsl:attribute>
      <ObjectRoot>
        <xsl:for-each select="section">
          <xsl:apply-templates select="."/>
        </xsl:for-each>
      </ObjectRoot>
      <GroupRoot>
        <xsl:for-each select="scene[section-name]">
          <xsl:call-template name="make-groups"/>
        </xsl:for-each>
      </GroupRoot>
      <TimelineRoot>
        <xsl:for-each select="scene">
          <xsl:call-template name="make-timelines"/>
        </xsl:for-each>
      </TimelineRoot>      
      <PlacementRoot>
        <Placement name="Center">
          <RelativeTo>Center</RelativeTo>
          <Position>(0.0, 0.0, 0.0)</Position>
          <Axis rotation="(0.0, 1.0, 0.0)" angle="0.0"/>
        </Placement>
        <Placement name="FrontWall">
          <RelativeTo>Center</RelativeTo>
          <Position>(0.0, 0.0, -4.0)</Position>
          <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
        </Placement>
        <Placement name="LeftWall">
          <RelativeTo>Center</RelativeTo>
          <Position>(-4.0, 0.0, 0.0)</Position>
          <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
        </Placement>
        <Placement name="RightWall">
          <RelativeTo>Center</RelativeTo>
          <Position>(4.0, 0.0, 0.0)</Position>
          <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 1.0, 0.0)"/>
        </Placement>
        <Placement name="FloorWall">
          <RelativeTo>Center</RelativeTo>
          <Position>(0.0, -4.0, 0.0)</Position>
          <LookAt target="(0.0, 0.0, 0.0)" up="(0.0, 0.0, -1.0)"/>
        </Placement>
      </PlacementRoot>
      <SoundRoot>
        <xsl:for-each select="scene[@sound-name]">
          <xsl:call-template name="make-sounds"/>
        </xsl:for-each>
      </SoundRoot>
      <EventRoot></EventRoot>
      <Global>
    <CameraPos>
      <Placement>
        <RelativeTo>Center</RelativeTo>
        <Position>(0.0, 0.0, 6.0)</Position>
      </Placement>
    </CameraPos>
  </Global>
      <About/>
    </Story>
  </xsl:template>
  <!--Section-->
  <xsl:template match="section">
    <xsl:apply-templates select="effect"/>
  </xsl:template>
  <!--Effect-->
  <xsl:template match="effect">
    <xsl:for-each select="word">
      <xsl:variable name="name">
        <xsl:choose>
          <xsl:when test="count(../word)=1">
            <xsl:value-of select="../../name"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="concat(../../name, position())"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <Object name="{$name}">
        <Visible>
          <xsl:value-of select="../../@visible"/>
        </Visible>
        <Color>
          <xsl:value-of select="@color"/>
        </Color>
        <Scale>
          <xsl:value-of select="@scale"/>
        </Scale>
        <Placement>
          <RelativeTo>Center</RelativeTo>
          <xsl:variable name="X" select="normalize-space(substring-after(substring-before(../../translation, ','), '('))"/>
          <xsl:variable name="Y" select="number(normalize-space(substring-before(substring-after(../../translation, ','), ',')))"/>
          <xsl:variable name="Z" select="normalize-space(substring-before(substring-after(substring-after(../../translation, ','), ','), ')')) "/>
          <Position>(<xsl:value-of select="$X"/>,  <xsl:value-of select="$Y - .5*count(preceding-sibling::word[@line-break='true'])"/>, <xsl:value-of select="$Z"/>)<!--<xsl:value-of select="../../translation"/>-->
          </Position>
          <Axis rotation="{../../rotation-axis}" angle="{../../rotation-angle}"/>
        </Placement>
        <Content>
          <xsl:choose>
            <xsl:when test="@type='Text'">
              <Text horiz-align="{../../@halign}" vert-align="{../../@valign}" font="Courier.ttf" depth="0">
                <text>
                  <xsl:value-of select="text()"/>
                </text>
              </Text>
            </xsl:when>
            <xsl:when test="@type='Image' ">
              <Image filename="./{@left-image}"/>
            </xsl:when>
            <xsl:when test="@type='Stereo Image' ">
              <StereoImage left-image="./{@left-image}" right-image="./{@right-image}"/>
            </xsl:when>
            <xsl:when test="@type='3D Model' ">
              <Model filename="./{@model}"/>
            </xsl:when>
          </xsl:choose>
        </Content>
        <LinkRoot>
          <xsl:if test="@link-to">
            <Link>
              <Enabled>1</Enabled>
              <RemainEnabled>
                <xsl:value-of select="@activate-once"/>
              </RemainEnabled>
              <EnabledColor>
                <xsl:value-of select="@link-color"/>
              </EnabledColor>
              <SelectedColor>
                <xsl:value-of select="@selected-link-color"/>
              </SelectedColor>
              <Actions>
                <TimerChange name="{@link-to}">
                  <start/>
                </TimerChange>
              </Actions>
            </Link>
          </xsl:if>
        </LinkRoot>
      </Object>
    </xsl:for-each>
  </xsl:template>
  <!--Groups-->
  <xsl:template name="make-groups">
    <Group name="{@name}">
      <xsl:for-each select="section-name">
        <Objects name="{text()}"/>
      </xsl:for-each>
    </Group>
  </xsl:template>
  <!--Sounds-->
  <xsl:template name="make-sounds">
    <Sound name="{@sound-name}" filename="./sound/{@sound-name}.wav" autostart="false">
      <Repeat>
        <NoRepeat/>
      </Repeat>
      <Settings freq="1.0" volume="1.0" pan="0.0"/>
    </Sound>
  </xsl:template>
  <!--Timelines-->
  <xsl:template name="make-timelines">
    <xsl:variable name="start" select="number(@start-time)"/>
    <Timeline name="{@name}" start-immediately="{link-only='false'}">
    <xsl:choose>
    
      <xsl:when test="@type='fade'">
        <xsl:if test="@fade-in-duration != '0'">
          <TimedActions seconds-time="{$start}">
            <GroupRef name="{@name}">
              <Transition duration="{@fade-in-duration}">
                <Visible>true</Visible>
              </Transition>
            </GroupRef>
          </TimedActions>
        </xsl:if>
        <xsl:if test="@fade-out-duration != '0'">
          <TimedActions seconds-time="{number($start) + number(@fade-in-duration) + number(@paused-duration)}">
            <GroupRef name="{@name}">
              <Transition duration="{@fade-out-duration}">
                <Visible>false</Visible>
              </Transition>
            </GroupRef>
          </TimedActions>
        </xsl:if>
      </xsl:when>
      
      <xsl:when test="@type='move_cave_relative'">
      <TimedActions seconds-time="{$start}">
      <MoveCave duration="{@duration}">
      <Relative/>
      <Placement>
      <RelativeTo>Center</RelativeTo>
      <Position><xsl:value-of select="@translation"/></Position>
      <Axis rotation="{@rotation-axis}" angle="{@rotation-angle}"></Axis>
      </Placement>
      </MoveCave>
      </TimedActions>
      </xsl:when>
      
      <xsl:when test="@type='move_cave_absolute'">
      <TimedActions seconds-time="{$start}">
      <MoveCave duration="{@duration}">
      <Relative/>
      <Placement>
      <RelativeTo>Center</RelativeTo>
      <Position><xsl:value-of select="@translation"/></Position>
      <Axis rotation="{@rotation-axis}" angle="{@rotation-angle}"></Axis>
      </Placement>
      </MoveCave>
      </TimedActions>
      </xsl:when>     
      
    </xsl:choose>
    
    <xsl:if test="@sound-name">
    <TimedActions seconds-time="{$start}">
    <SoundRef name="{@sound-name}"></SoundRef>
    </TimedActions>
    </xsl:if>    
    
    <xsl:if test="count(section-name) > 0 and @type!='fade'">
    <TimedActions seconds-time="{$start}">
    <GroupRef name="{@name}">
    <Transition duration="0">
    <Visible>true</Visible>
    </Transition>
    </GroupRef>
    </TimedActions>
    </xsl:if>    
    
      </Timeline>

  </xsl:template>
  
  <!--    unpaused work  -->
  
  <xsl:template name="unpause">
    <xsl:variable name="start" select="number(@start-time)"/>
    <Timeline name="@name-unpause" start-immediately="not(@link-only)">
      <!--activate paused-->
      <xsl:for-each select="section-name">
        <xsl:if test="../story[name=text()]/@paused=true">
          <xsl:variable name="section" select="../story[name=text()]"/>
          <xsl:for-each select="$section/effect[@effect-type='lerp']">
            <xsl:for-each select="word">
              <TimedActions seconds-time="number(../@start-time)">
          
          </TimedActions>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:if>
      </xsl:for-each>
      <!--<xsl:choose>
        <xsl:when test="@type='fade'">
          <xsl:for-each select="section-name">
            <TimedActions seconds-time="@start-time">
            </TimedActions>
          </xsl:for-each>
        </xsl:when>
      </xsl:choose>-->
    </Timeline>
  </xsl:template>
  <!-- Copy Rest -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Union


# TODO: Move to .clean() method of appropriate classes
# TODO: Should be Dictionary (name is key), not a list
def clean_xml(Story):
    if Story.Objects is not None:
        Story.Objects = Story.Objects.Object
    if Story.Groups is not None:
        Story.Groups = Story.Groups.Group
    if Story.Timelines is not None:
        Story.Timelines = Story.Timelines.Timeline
    if Story.Placements is not None:
        Story.Placements = Story.Placements.Placement
    if Story.Sounds is not None:
        Story.Sounds = Story.Sounds.Sound

    if Story.Events is not None:
        Story.Events = Story.Events.Event
    if Story.ParticleActions is not None:
        Story.ParticleActions = Story.ParticleActions.ParticleActionList

    # OLD
    # # Parse each <PlacementRoot>, each <Placement> is referenced by name
    # story["walls"] = dict(
    #     (tag.attrib.pop("name"), parse_recursive(tag))
    #     for tag in root.find("PlacementRoot")
    # )
    return Story

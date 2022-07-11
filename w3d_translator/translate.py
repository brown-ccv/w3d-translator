from typing import Tuple
from uuid import uuid4 as uuid

import generateDS.classes as classes


def translate_objects(objects: list):
    game_objects = {}

    object: classes.Object
    for object in objects:
        name = object.name

        id = uuid()
        game_objects[name] = object

    return game_objects


def translate_path(string: str):
    """Translate a <xs:simpleType name="path> type"""
    pass


def translate_color(string: str):
    """Translate a <xs:simpleType name="color> type"""
    pass


def translate_vector(string: str):
    """Translate a <xs:simpleType name="vector> type"""
    pass


def get_choice(obj, options=None):
    """Loop over options, returning the class property that is not None"""

    # Use all members if custom list isn't given
    if options is None:
        options = obj.member_data_items_
    for member in options:
        temp = getattr(obj, member.get_name())
        if temp is not None:
            return temp


def set_choice(obj, value, options=None):
    """Loop over options, updating the property that is not None"""

    # Use all members if custom list isn't given
    if options is None:
        options = obj.member_data_items_
    for member in options:
        if getattr(obj, member.get_name()) is not None:
            setattr(obj, member.get_name(), value)


def print_member_names(obj):
    """Helper function to print xml class properties"""
    names = list(map(lambda x: x.get_name(), obj.member_data_items_))
    print(names)

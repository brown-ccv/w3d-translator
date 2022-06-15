#!/usr/bin/env python
# -*- mode: pymode; coding: latin1; -*-

from __future__ import print_function
import re


class MethodSpec(object):
    def __init__(
        self, name="", source="", class_names="", class_names_compiled=None
    ):
        """MethodSpec -- A specification of a method.
        Member variables:
            name -- The method name
            source -- The source code for the method.  Must be
                indented to fit in a class definition.
            class_names -- A regular expression that must match the
                class names in which the method is to be inserted.
            class_names_compiled -- The compiled class names.
                generateDS.py will do this compile for you.
        """
        self.name = name
        self.source = source
        if class_names is None:
            self.class_names = (".*",)
        else:
            self.class_names = class_names
        if class_names_compiled is None:
            self.class_names_compiled = re.compile(self.class_names)
        else:
            self.class_names_compiled = class_names_compiled

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    def get_class_names(self):
        return self.class_names

    def set_class_names(self, class_names):
        self.class_names = class_names
        self.class_names_compiled = re.compile(class_names)

    def get_class_names_compiled(self):
        return self.class_names_compiled

    def set_class_names_compiled(self, class_names_compiled):
        self.class_names_compiled = class_names_compiled

    def match_name(self, class_name):
        """Match against the name of the class currently being generated.
        If this method returns True, the method will be inserted in
          the generated class.
        """
        if self.class_names_compiled.search(class_name):
            return True
        else:
            return False

    def get_interpolated_source(self, values_dict):
        """Get the method source code, interpolating values from values_dict
        into it.  The source returned by this method is inserted into
        the generated class.
        """
        source = self.source % values_dict
        return source

    def show(self):
        print("specification:")
        print("    name: %s" % (self.name,))
        print(self.source)
        print("    class_names: %s" % (self.class_names,))
        print("    names pat  : %s" % (self.class_names_compiled.pattern,))


choice_classes = (
    f"^{string}$"
    for string in [
        "Content",
        "LightType",
        "Group",
        "ModeType",
        "RepeatType",
        "ParticleAction",
        "RemoveConditionType",
        "ActionsType",
        "MoveCaveType",
        "TimerChange",
        "PositionType",
        "DirectionType",
        "SourceType",
        "MovementType",
        "RemoveConditionType",
        "ParticleDomainType",
        "Transition",
    ]
)

choice_names = "|".join(choice_classes)

get_choice = MethodSpec(
    name="get_choice",
    source="""
    # Loop over the members, returning the class property that is not None
    def get_choice(self):
        for member in self.member_data_items_:
            temp = getattr(self, member.get_name())
            if temp is not None:
                return temp
    """,
    class_names=choice_names,
)

set_choice = MethodSpec(
    name="set_choice",
    source="""
    # Loop over members, updating the property that is not None
    def set_choice(self, value):
        for member in self.member_data_items_:
            if getattr(self, member.get_name()) is not None:
                setattr(self, member.get_name(), value)
    """,
    class_names=choice_names,
)

# TODO Custom get_choice and set_choice (new name)
# EventTrigger (includes either HeadTrack or MoveTrack) (43)
# Placement (includes either Axis, LookAt, or Normal) (44)


METHOD_SPECS = (get_choice, set_choice)


def test():
    for spec in METHOD_SPECS:
        spec.show()


def main():
    test()
    # pass


if __name__ == "__main__":
    main()

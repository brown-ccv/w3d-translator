#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jun  1 13:58:44 2022 by generateDS.py version 2.40.13.
# Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'w3d_translator/generateDS/classes.py')
#   ('-s', 'w3d_translator/generateDS/subclasses.py')
#   ('--super', 'generateDS.classes')
#   ('--no-namespace-defs', '')
#
# Command line arguments:
#   .\schema\caveschema.xsd
#
# Command line:
#   ..\..\Apps\generateDS\generateDS.py -o "w3d_translator/generateDS/classes.py" -s "w3d_translator/generateDS/subclasses.py" --super="generateDS.classes" --no-namespace-defs .\schema\caveschema.xsd
#
# Current working directory (os.getcwd()):
#   W3D Translator
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class actionType(str, Enum):
    PLAY_SOUND='Play Sound'
    STOP_SOUND='Stop Sound'


class horiz_alignType(str, Enum):
    LEFT='left'
    CENTER='center'
    RIGHT='right'


class objectsType(str, Enum):
    ANY_OBJECT='Any Object'
    ALL_OBJECTS='All Objects'


class randomType(str, Enum):
    SELECT_ONE_RANDOMLY='Select One Randomly'


class vert_alignType(str, Enum):
    TOP='top'
    CENTER='center'
    BOTTOM='bottom'


class Story(GeneratedsSuper):
    """Story -- The root story element
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, version=8, last_xpath=None, ObjectRoot=None, GroupRoot=None, TimelineRoot=None, PlacementRoot=None, SoundRoot=None, EventRoot=None, ParticleActionRoot=None, Global=None, About=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.version = _cast(int, version)
        self.version_nsprefix_ = None
        self.last_xpath = _cast(None, last_xpath)
        self.last_xpath_nsprefix_ = None
        self.ObjectRoot = ObjectRoot
        self.ObjectRoot_nsprefix_ = None
        self.GroupRoot = GroupRoot
        self.GroupRoot_nsprefix_ = None
        self.TimelineRoot = TimelineRoot
        self.TimelineRoot_nsprefix_ = None
        self.PlacementRoot = PlacementRoot
        self.PlacementRoot_nsprefix_ = None
        self.SoundRoot = SoundRoot
        self.SoundRoot_nsprefix_ = None
        self.EventRoot = EventRoot
        self.EventRoot_nsprefix_ = None
        self.ParticleActionRoot = ParticleActionRoot
        self.ParticleActionRoot_nsprefix_ = None
        self.Global = Global
        self.Global_nsprefix_ = None
        self.About = About
        self.About_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Story)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Story.subclass:
            return Story.subclass(*args_, **kwargs_)
        else:
            return Story(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ObjectRoot(self):
        return self.ObjectRoot
    def set_ObjectRoot(self, ObjectRoot):
        self.ObjectRoot = ObjectRoot
    def get_GroupRoot(self):
        return self.GroupRoot
    def set_GroupRoot(self, GroupRoot):
        self.GroupRoot = GroupRoot
    def get_TimelineRoot(self):
        return self.TimelineRoot
    def set_TimelineRoot(self, TimelineRoot):
        self.TimelineRoot = TimelineRoot
    def get_PlacementRoot(self):
        return self.PlacementRoot
    def set_PlacementRoot(self, PlacementRoot):
        self.PlacementRoot = PlacementRoot
    def get_SoundRoot(self):
        return self.SoundRoot
    def set_SoundRoot(self, SoundRoot):
        self.SoundRoot = SoundRoot
    def get_EventRoot(self):
        return self.EventRoot
    def set_EventRoot(self, EventRoot):
        self.EventRoot = EventRoot
    def get_ParticleActionRoot(self):
        return self.ParticleActionRoot
    def set_ParticleActionRoot(self, ParticleActionRoot):
        self.ParticleActionRoot = ParticleActionRoot
    def get_Global(self):
        return self.Global
    def set_Global(self, Global):
        self.Global = Global
    def get_About(self):
        return self.About
    def set_About(self, About):
        self.About = About
    def get_version(self):
        return self.version
    def set_version(self, version):
        self.version = version
    def get_last_xpath(self):
        return self.last_xpath
    def set_last_xpath(self, last_xpath):
        self.last_xpath = last_xpath
    def _hasContent(self):
        if (
            self.ObjectRoot is not None or
            self.GroupRoot is not None or
            self.TimelineRoot is not None or
            self.PlacementRoot is not None or
            self.SoundRoot is not None or
            self.EventRoot is not None or
            self.ParticleActionRoot is not None or
            self.Global is not None or
            self.About is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Story', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Story')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Story':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Story')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Story', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Story'):
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version="%s"' % self.gds_format_integer(self.version, input_name='version'))
        if self.last_xpath is not None and 'last_xpath' not in already_processed:
            already_processed.add('last_xpath')
            outfile.write(' last_xpath=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.last_xpath), input_name='last_xpath')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Story', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ObjectRoot is not None:
            namespaceprefix_ = self.ObjectRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectRoot_nsprefix_) else ''
            self.ObjectRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectRoot', pretty_print=pretty_print)
        if self.GroupRoot is not None:
            namespaceprefix_ = self.GroupRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.GroupRoot_nsprefix_) else ''
            self.GroupRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GroupRoot', pretty_print=pretty_print)
        if self.TimelineRoot is not None:
            namespaceprefix_ = self.TimelineRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.TimelineRoot_nsprefix_) else ''
            self.TimelineRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TimelineRoot', pretty_print=pretty_print)
        if self.PlacementRoot is not None:
            namespaceprefix_ = self.PlacementRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.PlacementRoot_nsprefix_) else ''
            self.PlacementRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PlacementRoot', pretty_print=pretty_print)
        if self.SoundRoot is not None:
            namespaceprefix_ = self.SoundRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.SoundRoot_nsprefix_) else ''
            self.SoundRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SoundRoot', pretty_print=pretty_print)
        if self.EventRoot is not None:
            namespaceprefix_ = self.EventRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.EventRoot_nsprefix_) else ''
            self.EventRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EventRoot', pretty_print=pretty_print)
        if self.ParticleActionRoot is not None:
            namespaceprefix_ = self.ParticleActionRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleActionRoot_nsprefix_) else ''
            self.ParticleActionRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleActionRoot', pretty_print=pretty_print)
        if self.Global is not None:
            namespaceprefix_ = self.Global_nsprefix_ + ':' if (UseCapturedNS_ and self.Global_nsprefix_) else ''
            self.Global.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Global', pretty_print=pretty_print)
        if self.About is not None:
            namespaceprefix_ = self.About_nsprefix_ + ':' if (UseCapturedNS_ and self.About_nsprefix_) else ''
            self.About.export(outfile, level, namespaceprefix_, namespacedef_='', name_='About', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = self.gds_parse_integer(value, node, 'version')
        value = find_attr_value_('last_xpath', node)
        if value is not None and 'last_xpath' not in already_processed:
            already_processed.add('last_xpath')
            self.last_xpath = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ObjectRoot':
            obj_ = ObjectRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectRoot = obj_
            obj_.original_tagname_ = 'ObjectRoot'
        elif nodeName_ == 'GroupRoot':
            obj_ = GroupRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GroupRoot = obj_
            obj_.original_tagname_ = 'GroupRoot'
        elif nodeName_ == 'TimelineRoot':
            obj_ = TimelineRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimelineRoot = obj_
            obj_.original_tagname_ = 'TimelineRoot'
        elif nodeName_ == 'PlacementRoot':
            obj_ = PlacementRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PlacementRoot = obj_
            obj_.original_tagname_ = 'PlacementRoot'
        elif nodeName_ == 'SoundRoot':
            obj_ = SoundRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SoundRoot = obj_
            obj_.original_tagname_ = 'SoundRoot'
        elif nodeName_ == 'EventRoot':
            obj_ = EventRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EventRoot = obj_
            obj_.original_tagname_ = 'EventRoot'
        elif nodeName_ == 'ParticleActionRoot':
            obj_ = ParticleActionRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleActionRoot = obj_
            obj_.original_tagname_ = 'ParticleActionRoot'
        elif nodeName_ == 'Global':
            obj_ = GlobalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Global = obj_
            obj_.original_tagname_ = 'Global'
        elif nodeName_ == 'About':
            obj_ = AboutType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.About = obj_
            obj_.original_tagname_ = 'About'
# end class Story


class Object(GeneratedsSuper):
    """Object -- Entire Content obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, Visible=True, Color='255,255,255', Lighting=False, ClickThrough=False, AroundSelfAxis=False, Scale=1.0, SoundRef=None, Placement=None, Content=None, LinkRoot=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.Visible = Visible
        self.Visible_nsprefix_ = None
        self.Color = Color
        self.validate_color(self.Color)
        self.Color_nsprefix_ = None
        self.Lighting = Lighting
        self.Lighting_nsprefix_ = None
        self.ClickThrough = ClickThrough
        self.ClickThrough_nsprefix_ = None
        self.AroundSelfAxis = AroundSelfAxis
        self.AroundSelfAxis_nsprefix_ = None
        self.Scale = Scale
        self.Scale_nsprefix_ = None
        self.SoundRef = SoundRef
        self.SoundRef_nsprefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
        self.Content = Content
        self.Content_nsprefix_ = None
        self.LinkRoot = LinkRoot
        self.LinkRoot_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Object)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Object.subclass:
            return Object.subclass(*args_, **kwargs_)
        else:
            return Object(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Visible(self):
        return self.Visible
    def set_Visible(self, Visible):
        self.Visible = Visible
    def get_Color(self):
        return self.Color
    def set_Color(self, Color):
        self.Color = Color
    def get_Lighting(self):
        return self.Lighting
    def set_Lighting(self, Lighting):
        self.Lighting = Lighting
    def get_ClickThrough(self):
        return self.ClickThrough
    def set_ClickThrough(self, ClickThrough):
        self.ClickThrough = ClickThrough
    def get_AroundSelfAxis(self):
        return self.AroundSelfAxis
    def set_AroundSelfAxis(self, AroundSelfAxis):
        self.AroundSelfAxis = AroundSelfAxis
    def get_Scale(self):
        return self.Scale
    def set_Scale(self, Scale):
        self.Scale = Scale
    def get_SoundRef(self):
        return self.SoundRef
    def set_SoundRef(self, SoundRef):
        self.SoundRef = SoundRef
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def get_Content(self):
        return self.Content
    def set_Content(self, Content):
        self.Content = Content
    def get_LinkRoot(self):
        return self.LinkRoot
    def set_LinkRoot(self, LinkRoot):
        self.LinkRoot = LinkRoot
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def validate_color(self, value):
        result = True
        # Validate type color, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            not self.Visible or
            self.Color != "255,255,255" or
            self.Lighting or
            self.ClickThrough or
            self.AroundSelfAxis or
            self.Scale != 1.0 or
            self.SoundRef is not None or
            self.Placement is not None or
            self.Content is not None or
            self.LinkRoot is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Object', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Object')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Object':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Object')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Object', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Object'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Object', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Visible is not None:
            namespaceprefix_ = self.Visible_nsprefix_ + ':' if (UseCapturedNS_ and self.Visible_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVisible>%s</%sVisible>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Visible, input_name='Visible'), namespaceprefix_ , eol_))
        if self.Visible is None:
            namespaceprefix_ = self.Visible_nsprefix_ + ':' if (UseCapturedNS_ and self.Visible_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVisible>true</%sVisible/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Color is not None:
            namespaceprefix_ = self.Color_nsprefix_ + ':' if (UseCapturedNS_ and self.Color_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sColor>%s</%sColor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Color), input_name='Color')), namespaceprefix_ , eol_))
        if self.Color is None:
            namespaceprefix_ = self.Color_nsprefix_ + ':' if (UseCapturedNS_ and self.Color_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sColor>255,255,255</%sColor/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Lighting is not None:
            namespaceprefix_ = self.Lighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Lighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLighting>%s</%sLighting>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Lighting, input_name='Lighting'), namespaceprefix_ , eol_))
        if self.Lighting is None:
            namespaceprefix_ = self.Lighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Lighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLighting>false</%sLighting/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.ClickThrough is not None:
            namespaceprefix_ = self.ClickThrough_nsprefix_ + ':' if (UseCapturedNS_ and self.ClickThrough_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sClickThrough>%s</%sClickThrough>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ClickThrough, input_name='ClickThrough'), namespaceprefix_ , eol_))
        if self.ClickThrough is None:
            namespaceprefix_ = self.ClickThrough_nsprefix_ + ':' if (UseCapturedNS_ and self.ClickThrough_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sClickThrough>false</%sClickThrough/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.AroundSelfAxis is not None:
            namespaceprefix_ = self.AroundSelfAxis_nsprefix_ + ':' if (UseCapturedNS_ and self.AroundSelfAxis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAroundSelfAxis>%s</%sAroundSelfAxis>%s' % (namespaceprefix_ , self.gds_format_boolean(self.AroundSelfAxis, input_name='AroundSelfAxis'), namespaceprefix_ , eol_))
        if self.AroundSelfAxis is None:
            namespaceprefix_ = self.AroundSelfAxis_nsprefix_ + ':' if (UseCapturedNS_ and self.AroundSelfAxis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAroundSelfAxis>false</%sAroundSelfAxis/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Scale is not None:
            namespaceprefix_ = self.Scale_nsprefix_ + ':' if (UseCapturedNS_ and self.Scale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScale>%s</%sScale>%s' % (namespaceprefix_ , self.gds_format_double(self.Scale, input_name='Scale'), namespaceprefix_ , eol_))
        if self.Scale is None:
            namespaceprefix_ = self.Scale_nsprefix_ + ':' if (UseCapturedNS_ and self.Scale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScale>1.0</%sScale/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.SoundRef is not None:
            namespaceprefix_ = self.SoundRef_nsprefix_ + ':' if (UseCapturedNS_ and self.SoundRef_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSoundRef>%s</%sSoundRef>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SoundRef), input_name='SoundRef')), namespaceprefix_ , eol_))
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
        if self.Content is not None:
            namespaceprefix_ = self.Content_nsprefix_ + ':' if (UseCapturedNS_ and self.Content_nsprefix_) else ''
            self.Content.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Content', pretty_print=pretty_print)
        if self.LinkRoot is not None:
            namespaceprefix_ = self.LinkRoot_nsprefix_ + ':' if (UseCapturedNS_ and self.LinkRoot_nsprefix_) else ''
            self.LinkRoot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LinkRoot', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Visible':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Visible')
            ival_ = self.gds_validate_boolean(ival_, node, 'Visible')
            self.Visible = ival_
            self.Visible_nsprefix_ = child_.prefix
        elif nodeName_ == 'Color':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Color')
            value_ = self.gds_validate_string(value_, node, 'Color')
            self.Color = value_
            self.Color_nsprefix_ = child_.prefix
            # validate type color
            self.validate_color(self.Color)
        elif nodeName_ == 'Lighting':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Lighting')
            ival_ = self.gds_validate_boolean(ival_, node, 'Lighting')
            self.Lighting = ival_
            self.Lighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'ClickThrough':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ClickThrough')
            ival_ = self.gds_validate_boolean(ival_, node, 'ClickThrough')
            self.ClickThrough = ival_
            self.ClickThrough_nsprefix_ = child_.prefix
        elif nodeName_ == 'AroundSelfAxis':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'AroundSelfAxis')
            ival_ = self.gds_validate_boolean(ival_, node, 'AroundSelfAxis')
            self.AroundSelfAxis = ival_
            self.AroundSelfAxis_nsprefix_ = child_.prefix
        elif nodeName_ == 'Scale' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Scale')
            fval_ = self.gds_validate_double(fval_, node, 'Scale')
            self.Scale = fval_
            self.Scale_nsprefix_ = child_.prefix
        elif nodeName_ == 'SoundRef':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SoundRef')
            value_ = self.gds_validate_string(value_, node, 'SoundRef')
            self.SoundRef = value_
            self.SoundRef_nsprefix_ = child_.prefix
        elif nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
        elif nodeName_ == 'Content':
            obj_ = Content.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Content = obj_
            obj_.original_tagname_ = 'Content'
        elif nodeName_ == 'LinkRoot':
            obj_ = LinkRootType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LinkRoot = obj_
            obj_.original_tagname_ = 'LinkRoot'
# end class Object


class Content(GeneratedsSuper):
    """Content -- Content node
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, None_=None, Text=None, Image=None, StereoImage=None, Model=None, Light=None, ParticleSystem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.None_ = None_
        self.None__nsprefix_ = None
        self.Text = Text
        self.Text_nsprefix_ = None
        self.Image = Image
        self.Image_nsprefix_ = None
        self.StereoImage = StereoImage
        self.StereoImage_nsprefix_ = None
        self.Model = Model
        self.Model_nsprefix_ = None
        self.Light = Light
        self.Light_nsprefix_ = None
        self.ParticleSystem = ParticleSystem
        self.ParticleSystem_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Content)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Content.subclass:
            return Content.subclass(*args_, **kwargs_)
        else:
            return Content(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_None(self):
        return self.None_
    def set_None(self, None_):
        self.None_ = None_
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def get_Image(self):
        return self.Image
    def set_Image(self, Image):
        self.Image = Image
    def get_StereoImage(self):
        return self.StereoImage
    def set_StereoImage(self, StereoImage):
        self.StereoImage = StereoImage
    def get_Model(self):
        return self.Model
    def set_Model(self, Model):
        self.Model = Model
    def get_Light(self):
        return self.Light
    def set_Light(self, Light):
        self.Light = Light
    def get_ParticleSystem(self):
        return self.ParticleSystem
    def set_ParticleSystem(self, ParticleSystem):
        self.ParticleSystem = ParticleSystem
    def _hasContent(self):
        if (
            self.None_ is not None or
            self.Text is not None or
            self.Image is not None or
            self.StereoImage is not None or
            self.Model is not None or
            self.Light is not None or
            self.ParticleSystem is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Content', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Content')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Content':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Content')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Content', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Content'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Content', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.None_ is not None:
            namespaceprefix_ = self.None__nsprefix_ + ':' if (UseCapturedNS_ and self.None__nsprefix_) else ''
            self.None_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='None', pretty_print=pretty_print)
        if self.Text is not None:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            self.Text.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
        if self.Image is not None:
            namespaceprefix_ = self.Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Image_nsprefix_) else ''
            self.Image.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Image', pretty_print=pretty_print)
        if self.StereoImage is not None:
            namespaceprefix_ = self.StereoImage_nsprefix_ + ':' if (UseCapturedNS_ and self.StereoImage_nsprefix_) else ''
            self.StereoImage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='StereoImage', pretty_print=pretty_print)
        if self.Model is not None:
            namespaceprefix_ = self.Model_nsprefix_ + ':' if (UseCapturedNS_ and self.Model_nsprefix_) else ''
            self.Model.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Model', pretty_print=pretty_print)
        if self.Light is not None:
            namespaceprefix_ = self.Light_nsprefix_ + ':' if (UseCapturedNS_ and self.Light_nsprefix_) else ''
            self.Light.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Light', pretty_print=pretty_print)
        if self.ParticleSystem is not None:
            namespaceprefix_ = self.ParticleSystem_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleSystem_nsprefix_) else ''
            self.ParticleSystem.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleSystem', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'None':
            obj_ = NoneType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.None_ = obj_
            obj_.original_tagname_ = 'None'
        elif nodeName_ == 'Text':
            obj_ = TextType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text = obj_
            obj_.original_tagname_ = 'Text'
        elif nodeName_ == 'Image':
            obj_ = ImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Image = obj_
            obj_.original_tagname_ = 'Image'
        elif nodeName_ == 'StereoImage':
            obj_ = StereoImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.StereoImage = obj_
            obj_.original_tagname_ = 'StereoImage'
        elif nodeName_ == 'Model':
            obj_ = ModelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Model = obj_
            obj_.original_tagname_ = 'Model'
        elif nodeName_ == 'Light':
            obj_ = LightType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Light = obj_
            obj_.original_tagname_ = 'Light'
        elif nodeName_ == 'ParticleSystem':
            obj_ = ParticleSystemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleSystem = obj_
            obj_.original_tagname_ = 'ParticleSystem'
# end class Content


class Link(GeneratedsSuper):
    """Link -- Link Object
    Actions -- Link Actions Obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Enabled=True, RemainEnabled=True, EnabledColor='0,128,255', SelectedColor='255,0,0', Actions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Enabled = Enabled
        self.Enabled_nsprefix_ = None
        self.RemainEnabled = RemainEnabled
        self.RemainEnabled_nsprefix_ = None
        self.EnabledColor = EnabledColor
        self.validate_color(self.EnabledColor)
        self.EnabledColor_nsprefix_ = None
        self.SelectedColor = SelectedColor
        self.validate_color(self.SelectedColor)
        self.SelectedColor_nsprefix_ = None
        if Actions is None:
            self.Actions = []
        else:
            self.Actions = Actions
        self.Actions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Link)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Link.subclass:
            return Link.subclass(*args_, **kwargs_)
        else:
            return Link(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Enabled(self):
        return self.Enabled
    def set_Enabled(self, Enabled):
        self.Enabled = Enabled
    def get_RemainEnabled(self):
        return self.RemainEnabled
    def set_RemainEnabled(self, RemainEnabled):
        self.RemainEnabled = RemainEnabled
    def get_EnabledColor(self):
        return self.EnabledColor
    def set_EnabledColor(self, EnabledColor):
        self.EnabledColor = EnabledColor
    def get_SelectedColor(self):
        return self.SelectedColor
    def set_SelectedColor(self, SelectedColor):
        self.SelectedColor = SelectedColor
    def get_Actions(self):
        return self.Actions
    def set_Actions(self, Actions):
        self.Actions = Actions
    def add_Actions(self, value):
        self.Actions.append(value)
    def insert_Actions_at(self, index, value):
        self.Actions.insert(index, value)
    def replace_Actions_at(self, index, value):
        self.Actions[index] = value
    def validate_color(self, value):
        result = True
        # Validate type color, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            not self.Enabled or
            not self.RemainEnabled or
            self.EnabledColor != "0,128,255" or
            self.SelectedColor != "255,0,0" or
            self.Actions
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Link', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Link')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Link':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Link')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Link', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Link'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Link', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Enabled is not None:
            namespaceprefix_ = self.Enabled_nsprefix_ + ':' if (UseCapturedNS_ and self.Enabled_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEnabled>%s</%sEnabled>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Enabled, input_name='Enabled'), namespaceprefix_ , eol_))
        if self.Enabled is None:
            namespaceprefix_ = self.Enabled_nsprefix_ + ':' if (UseCapturedNS_ and self.Enabled_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEnabled>true</%sEnabled/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.RemainEnabled is not None:
            namespaceprefix_ = self.RemainEnabled_nsprefix_ + ':' if (UseCapturedNS_ and self.RemainEnabled_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRemainEnabled>%s</%sRemainEnabled>%s' % (namespaceprefix_ , self.gds_format_boolean(self.RemainEnabled, input_name='RemainEnabled'), namespaceprefix_ , eol_))
        if self.RemainEnabled is None:
            namespaceprefix_ = self.RemainEnabled_nsprefix_ + ':' if (UseCapturedNS_ and self.RemainEnabled_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRemainEnabled>true</%sRemainEnabled/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.EnabledColor is not None:
            namespaceprefix_ = self.EnabledColor_nsprefix_ + ':' if (UseCapturedNS_ and self.EnabledColor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEnabledColor>%s</%sEnabledColor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EnabledColor), input_name='EnabledColor')), namespaceprefix_ , eol_))
        if self.EnabledColor is None:
            namespaceprefix_ = self.EnabledColor_nsprefix_ + ':' if (UseCapturedNS_ and self.EnabledColor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEnabledColor>0,128,255</%sEnabledColor/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.SelectedColor is not None:
            namespaceprefix_ = self.SelectedColor_nsprefix_ + ':' if (UseCapturedNS_ and self.SelectedColor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSelectedColor>%s</%sSelectedColor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SelectedColor), input_name='SelectedColor')), namespaceprefix_ , eol_))
        if self.SelectedColor is None:
            namespaceprefix_ = self.SelectedColor_nsprefix_ + ':' if (UseCapturedNS_ and self.SelectedColor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSelectedColor>255,0,0</%sSelectedColor/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for Actions_ in self.Actions:
            namespaceprefix_ = self.Actions_nsprefix_ + ':' if (UseCapturedNS_ and self.Actions_nsprefix_) else ''
            Actions_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Actions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Enabled':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Enabled')
            ival_ = self.gds_validate_boolean(ival_, node, 'Enabled')
            self.Enabled = ival_
            self.Enabled_nsprefix_ = child_.prefix
        elif nodeName_ == 'RemainEnabled':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'RemainEnabled')
            ival_ = self.gds_validate_boolean(ival_, node, 'RemainEnabled')
            self.RemainEnabled = ival_
            self.RemainEnabled_nsprefix_ = child_.prefix
        elif nodeName_ == 'EnabledColor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EnabledColor')
            value_ = self.gds_validate_string(value_, node, 'EnabledColor')
            self.EnabledColor = value_
            self.EnabledColor_nsprefix_ = child_.prefix
            # validate type color
            self.validate_color(self.EnabledColor)
        elif nodeName_ == 'SelectedColor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SelectedColor')
            value_ = self.gds_validate_string(value_, node, 'SelectedColor')
            self.SelectedColor = value_
            self.SelectedColor_nsprefix_ = child_.prefix
            # validate type color
            self.validate_color(self.SelectedColor)
        elif nodeName_ == 'Actions':
            obj_ = ActionsType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Actions.append(obj_)
            obj_.original_tagname_ = 'Actions'
# end class Link


class Group(GeneratedsSuper):
    """Group -- Group obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, Objects=None, Groups=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        if Objects is None:
            self.Objects = []
        else:
            self.Objects = Objects
        self.Objects_nsprefix_ = None
        if Groups is None:
            self.Groups = []
        else:
            self.Groups = Groups
        self.Groups_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Group)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Group.subclass:
            return Group.subclass(*args_, **kwargs_)
        else:
            return Group(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Objects(self):
        return self.Objects
    def set_Objects(self, Objects):
        self.Objects = Objects
    def add_Objects(self, value):
        self.Objects.append(value)
    def insert_Objects_at(self, index, value):
        self.Objects.insert(index, value)
    def replace_Objects_at(self, index, value):
        self.Objects[index] = value
    def get_Groups(self):
        return self.Groups
    def set_Groups(self, Groups):
        self.Groups = Groups
    def add_Groups(self, value):
        self.Groups.append(value)
    def insert_Groups_at(self, index, value):
        self.Groups.insert(index, value)
    def replace_Groups_at(self, index, value):
        self.Groups[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.Objects or
            self.Groups
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Group', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Group')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Group':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Group')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Group', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Group'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Group', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Objects_ in self.Objects:
            namespaceprefix_ = self.Objects_nsprefix_ + ':' if (UseCapturedNS_ and self.Objects_nsprefix_) else ''
            Objects_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Objects', pretty_print=pretty_print)
        for Groups_ in self.Groups:
            namespaceprefix_ = self.Groups_nsprefix_ + ':' if (UseCapturedNS_ and self.Groups_nsprefix_) else ''
            Groups_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Groups', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Objects':
            obj_ = Objects.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Objects.append(obj_)
            obj_.original_tagname_ = 'Objects'
        elif nodeName_ == 'Groups':
            obj_ = Groups.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Groups.append(obj_)
            obj_.original_tagname_ = 'Groups'
# end class Group


class Objects(GeneratedsSuper):
    """Objects -- Reference group objects
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Objects)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Objects.subclass:
            return Objects.subclass(*args_, **kwargs_)
        else:
            return Objects(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Objects', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Objects')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Objects':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Objects')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Objects', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Objects'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Objects', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Objects


class Groups(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Groups)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Groups.subclass:
            return Groups.subclass(*args_, **kwargs_)
        else:
            return Groups(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Groups', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Groups')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Groups':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Groups')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Groups', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Groups'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Groups', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Groups


class Timeline(GeneratedsSuper):
    """Timeline -- Timer obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, start_immediately=True, TimedActions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.start_immediately = _cast(bool, start_immediately)
        self.start_immediately_nsprefix_ = None
        if TimedActions is None:
            self.TimedActions = []
        else:
            self.TimedActions = TimedActions
        self.TimedActions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Timeline)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Timeline.subclass:
            return Timeline.subclass(*args_, **kwargs_)
        else:
            return Timeline(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TimedActions(self):
        return self.TimedActions
    def set_TimedActions(self, TimedActions):
        self.TimedActions = TimedActions
    def add_TimedActions(self, value):
        self.TimedActions.append(value)
    def insert_TimedActions_at(self, index, value):
        self.TimedActions.insert(index, value)
    def replace_TimedActions_at(self, index, value):
        self.TimedActions[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_start_immediately(self):
        return self.start_immediately
    def set_start_immediately(self, start_immediately):
        self.start_immediately = start_immediately
    def _hasContent(self):
        if (
            self.TimedActions
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Timeline', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Timeline')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Timeline':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Timeline')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Timeline', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Timeline'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if not self.start_immediately and 'start_immediately' not in already_processed:
            already_processed.add('start_immediately')
            outfile.write(' start-immediately="%s"' % self.gds_format_boolean(self.start_immediately, input_name='start-immediately'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Timeline', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TimedActions_ in self.TimedActions:
            namespaceprefix_ = self.TimedActions_nsprefix_ + ':' if (UseCapturedNS_ and self.TimedActions_nsprefix_) else ''
            TimedActions_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TimedActions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('start-immediately', node)
        if value is not None and 'start-immediately' not in already_processed:
            already_processed.add('start-immediately')
            if value in ('true', '1'):
                self.start_immediately = True
            elif value in ('false', '0'):
                self.start_immediately = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TimedActions':
            obj_ = TimedActionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimedActions.append(obj_)
            obj_.original_tagname_ = 'TimedActions'
# end class Timeline


class GroupRef(GeneratedsSuper):
    """GroupRef --  Reference Group
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, random=None, Transition=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.random = _cast(None, random)
        self.random_nsprefix_ = None
        self.Transition = Transition
        self.Transition_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupRef.subclass:
            return GroupRef.subclass(*args_, **kwargs_)
        else:
            return GroupRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transition(self):
        return self.Transition
    def set_Transition(self, Transition):
        self.Transition = Transition
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_random(self):
        return self.random
    def set_random(self, random):
        self.random = random
    def validate_randomType(self, value):
        # Validate type randomType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Select One Randomly']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on randomType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Transition is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupRef', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupRef'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.random is not None and 'random' not in already_processed:
            already_processed.add('random')
            outfile.write(' random=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.random), input_name='random')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupRef', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transition is not None:
            namespaceprefix_ = self.Transition_nsprefix_ + ':' if (UseCapturedNS_ and self.Transition_nsprefix_) else ''
            self.Transition.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transition', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('random', node)
        if value is not None and 'random' not in already_processed:
            already_processed.add('random')
            self.random = value
            self.validate_randomType(self.random)    # validate type randomType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transition':
            obj_ = Transition.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transition = obj_
            obj_.original_tagname_ = 'Transition'
# end class GroupRef


class ActionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ObjectChange=None, GroupRef=None, TimerChange=None, SoundRef=None, Event=None, MoveCave=None, Restart=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ObjectChange = ObjectChange
        self.ObjectChange_nsprefix_ = None
        self.GroupRef = GroupRef
        self.GroupRef_nsprefix_ = None
        self.TimerChange = TimerChange
        self.TimerChange_nsprefix_ = None
        self.SoundRef = SoundRef
        self.SoundRef_nsprefix_ = None
        self.Event = Event
        self.Event_nsprefix_ = None
        self.MoveCave = MoveCave
        self.MoveCave_nsprefix_ = None
        self.Restart = Restart
        self.Restart_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ActionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ActionsType.subclass:
            return ActionsType.subclass(*args_, **kwargs_)
        else:
            return ActionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ObjectChange(self):
        return self.ObjectChange
    def set_ObjectChange(self, ObjectChange):
        self.ObjectChange = ObjectChange
    def get_GroupRef(self):
        return self.GroupRef
    def set_GroupRef(self, GroupRef):
        self.GroupRef = GroupRef
    def get_TimerChange(self):
        return self.TimerChange
    def set_TimerChange(self, TimerChange):
        self.TimerChange = TimerChange
    def get_SoundRef(self):
        return self.SoundRef
    def set_SoundRef(self, SoundRef):
        self.SoundRef = SoundRef
    def get_Event(self):
        return self.Event
    def set_Event(self, Event):
        self.Event = Event
    def get_MoveCave(self):
        return self.MoveCave
    def set_MoveCave(self, MoveCave):
        self.MoveCave = MoveCave
    def get_Restart(self):
        return self.Restart
    def set_Restart(self, Restart):
        self.Restart = Restart
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.ObjectChange is not None or
            self.GroupRef is not None or
            self.TimerChange is not None or
            self.SoundRef is not None or
            self.Event is not None or
            self.MoveCave is not None or
            self.Restart is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ActionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ActionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ActionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ActionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ActionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ActionsType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ActionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ObjectChange is not None:
            namespaceprefix_ = self.ObjectChange_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectChange_nsprefix_) else ''
            self.ObjectChange.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectChange', pretty_print=pretty_print)
        if self.GroupRef is not None:
            namespaceprefix_ = self.GroupRef_nsprefix_ + ':' if (UseCapturedNS_ and self.GroupRef_nsprefix_) else ''
            self.GroupRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GroupRef', pretty_print=pretty_print)
        if self.TimerChange is not None:
            namespaceprefix_ = self.TimerChange_nsprefix_ + ':' if (UseCapturedNS_ and self.TimerChange_nsprefix_) else ''
            self.TimerChange.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TimerChange', pretty_print=pretty_print)
        if self.SoundRef is not None:
            namespaceprefix_ = self.SoundRef_nsprefix_ + ':' if (UseCapturedNS_ and self.SoundRef_nsprefix_) else ''
            self.SoundRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SoundRef', pretty_print=pretty_print)
        if self.Event is not None:
            namespaceprefix_ = self.Event_nsprefix_ + ':' if (UseCapturedNS_ and self.Event_nsprefix_) else ''
            self.Event.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Event', pretty_print=pretty_print)
        if self.MoveCave is not None:
            namespaceprefix_ = self.MoveCave_nsprefix_ + ':' if (UseCapturedNS_ and self.MoveCave_nsprefix_) else ''
            self.MoveCave.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MoveCave', pretty_print=pretty_print)
        if self.Restart is not None:
            namespaceprefix_ = self.Restart_nsprefix_ + ':' if (UseCapturedNS_ and self.Restart_nsprefix_) else ''
            self.Restart.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Restart', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ObjectChange':
            obj_ = ObjectChange.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectChange = obj_
            obj_.original_tagname_ = 'ObjectChange'
        elif nodeName_ == 'GroupRef':
            obj_ = GroupRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GroupRef = obj_
            obj_.original_tagname_ = 'GroupRef'
        elif nodeName_ == 'TimerChange':
            obj_ = TimerChange.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimerChange = obj_
            obj_.original_tagname_ = 'TimerChange'
        elif nodeName_ == 'SoundRef':
            obj_ = SoundRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SoundRef = obj_
            obj_.original_tagname_ = 'SoundRef'
        elif nodeName_ == 'Event':
            obj_ = Event.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Event = obj_
            obj_.original_tagname_ = 'Event'
        elif nodeName_ == 'MoveCave':
            obj_ = MoveCaveType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MoveCave = obj_
            obj_.original_tagname_ = 'MoveCave'
        elif nodeName_ == 'Restart':
            obj_ = RestartType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Restart = obj_
            obj_.original_tagname_ = 'Restart'
# end class ActionsType


class TimerChange(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, start=None, stop=None, continue_=None, start_if_not_started=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.start = start
        self.start_nsprefix_ = None
        self.stop = stop
        self.stop_nsprefix_ = None
        self.continue_ = continue_
        self.continue__nsprefix_ = None
        self.start_if_not_started = start_if_not_started
        self.start_if_not_started_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimerChange)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimerChange.subclass:
            return TimerChange.subclass(*args_, **kwargs_)
        else:
            return TimerChange(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_start(self):
        return self.start
    def set_start(self, start):
        self.start = start
    def get_stop(self):
        return self.stop
    def set_stop(self, stop):
        self.stop = stop
    def get_continue(self):
        return self.continue_
    def set_continue(self, continue_):
        self.continue_ = continue_
    def get_start_if_not_started(self):
        return self.start_if_not_started
    def set_start_if_not_started(self, start_if_not_started):
        self.start_if_not_started = start_if_not_started
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.start is not None or
            self.stop is not None or
            self.continue_ is not None or
            self.start_if_not_started is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimerChange', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimerChange')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimerChange':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimerChange')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimerChange', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimerChange'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimerChange', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start is not None:
            namespaceprefix_ = self.start_nsprefix_ + ':' if (UseCapturedNS_ and self.start_nsprefix_) else ''
            self.start.export(outfile, level, namespaceprefix_, namespacedef_='', name_='start', pretty_print=pretty_print)
        if self.stop is not None:
            namespaceprefix_ = self.stop_nsprefix_ + ':' if (UseCapturedNS_ and self.stop_nsprefix_) else ''
            self.stop.export(outfile, level, namespaceprefix_, namespacedef_='', name_='stop', pretty_print=pretty_print)
        if self.continue_ is not None:
            namespaceprefix_ = self.continue__nsprefix_ + ':' if (UseCapturedNS_ and self.continue__nsprefix_) else ''
            self.continue_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='continue', pretty_print=pretty_print)
        if self.start_if_not_started is not None:
            namespaceprefix_ = self.start_if_not_started_nsprefix_ + ':' if (UseCapturedNS_ and self.start_if_not_started_nsprefix_) else ''
            self.start_if_not_started.export(outfile, level, namespaceprefix_, namespacedef_='', name_='start_if_not_started', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'start':
            obj_ = startType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.start = obj_
            obj_.original_tagname_ = 'start'
        elif nodeName_ == 'stop':
            obj_ = stopType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.stop = obj_
            obj_.original_tagname_ = 'stop'
        elif nodeName_ == 'continue':
            obj_ = continueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.continue_ = obj_
            obj_.original_tagname_ = 'continue'
        elif nodeName_ == 'start_if_not_started':
            obj_ = start_if_not_startedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.start_if_not_started = obj_
            obj_.original_tagname_ = 'start_if_not_started'
# end class TimerChange


class ObjectChange(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, Transition=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.Transition = Transition
        self.Transition_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectChange)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectChange.subclass:
            return ObjectChange.subclass(*args_, **kwargs_)
        else:
            return ObjectChange(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transition(self):
        return self.Transition
    def set_Transition(self, Transition):
        self.Transition = Transition
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.Transition is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectChange', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectChange')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectChange':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectChange')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectChange', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectChange'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectChange', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transition is not None:
            namespaceprefix_ = self.Transition_nsprefix_ + ':' if (UseCapturedNS_ and self.Transition_nsprefix_) else ''
            self.Transition.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transition', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transition':
            obj_ = Transition.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transition = obj_
            obj_.original_tagname_ = 'Transition'
# end class ObjectChange


class SoundRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SoundRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SoundRef.subclass:
            return SoundRef.subclass(*args_, **kwargs_)
        else:
            return SoundRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SoundRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SoundRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SoundRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SoundRef', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SoundRef'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundRef', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SoundRef


class Sound(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, filename=None, autostart=False, Mode=None, Repeat=None, Settings=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.filename = _cast(None, filename)
        self.filename_nsprefix_ = None
        self.autostart = _cast(bool, autostart)
        self.autostart_nsprefix_ = None
        self.Mode = Mode
        self.Mode_nsprefix_ = None
        self.Repeat = Repeat
        self.Repeat_nsprefix_ = None
        self.Settings = Settings
        self.Settings_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Sound)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Sound.subclass:
            return Sound.subclass(*args_, **kwargs_)
        else:
            return Sound(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mode(self):
        return self.Mode
    def set_Mode(self, Mode):
        self.Mode = Mode
    def get_Repeat(self):
        return self.Repeat
    def set_Repeat(self, Repeat):
        self.Repeat = Repeat
    def get_Settings(self):
        return self.Settings
    def set_Settings(self, Settings):
        self.Settings = Settings
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def get_autostart(self):
        return self.autostart
    def set_autostart(self, autostart):
        self.autostart = autostart
    def validate_file(self, value):
        # Validate type file, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (
            self.Mode is not None or
            self.Repeat is not None or
            self.Settings is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Sound', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Sound')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Sound':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Sound')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Sound', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Sound'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.filename is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            outfile.write(' filename=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.filename), input_name='filename')), ))
        if self.autostart and 'autostart' not in already_processed:
            already_processed.add('autostart')
            outfile.write(' autostart="%s"' % self.gds_format_boolean(self.autostart, input_name='autostart'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Sound', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mode is not None:
            namespaceprefix_ = self.Mode_nsprefix_ + ':' if (UseCapturedNS_ and self.Mode_nsprefix_) else ''
            self.Mode.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Mode', pretty_print=pretty_print)
        if self.Repeat is not None:
            namespaceprefix_ = self.Repeat_nsprefix_ + ':' if (UseCapturedNS_ and self.Repeat_nsprefix_) else ''
            self.Repeat.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Repeat', pretty_print=pretty_print)
        if self.Settings is not None:
            namespaceprefix_ = self.Settings_nsprefix_ + ':' if (UseCapturedNS_ and self.Settings_nsprefix_) else ''
            self.Settings.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Settings', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('filename', node)
        if value is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            self.filename = value
            self.validate_file(self.filename)    # validate type file
        value = find_attr_value_('autostart', node)
        if value is not None and 'autostart' not in already_processed:
            already_processed.add('autostart')
            if value in ('true', '1'):
                self.autostart = True
            elif value in ('false', '0'):
                self.autostart = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mode':
            obj_ = ModeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Mode = obj_
            obj_.original_tagname_ = 'Mode'
        elif nodeName_ == 'Repeat':
            obj_ = RepeatType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Repeat = obj_
            obj_.original_tagname_ = 'Repeat'
        elif nodeName_ == 'Settings':
            obj_ = SettingsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Settings = obj_
            obj_.original_tagname_ = 'Settings'
# end class Sound


class EventTrigger(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enabled=True, name=None, duration=0.0, remain_enabled=True, HeadTrack=None, MoveTrack=None, Actions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enabled = _cast(bool, enabled)
        self.enabled_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.duration = _cast(float, duration)
        self.duration_nsprefix_ = None
        self.remain_enabled = _cast(bool, remain_enabled)
        self.remain_enabled_nsprefix_ = None
        self.HeadTrack = HeadTrack
        self.HeadTrack_nsprefix_ = None
        self.MoveTrack = MoveTrack
        self.MoveTrack_nsprefix_ = None
        if Actions is None:
            self.Actions = []
        else:
            self.Actions = Actions
        self.Actions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EventTrigger)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EventTrigger.subclass:
            return EventTrigger.subclass(*args_, **kwargs_)
        else:
            return EventTrigger(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_HeadTrack(self):
        return self.HeadTrack
    def set_HeadTrack(self, HeadTrack):
        self.HeadTrack = HeadTrack
    def get_MoveTrack(self):
        return self.MoveTrack
    def set_MoveTrack(self, MoveTrack):
        self.MoveTrack = MoveTrack
    def get_Actions(self):
        return self.Actions
    def set_Actions(self, Actions):
        self.Actions = Actions
    def add_Actions(self, value):
        self.Actions.append(value)
    def insert_Actions_at(self, index, value):
        self.Actions.insert(index, value)
    def replace_Actions_at(self, index, value):
        self.Actions[index] = value
    def get_enabled(self):
        return self.enabled
    def set_enabled(self, enabled):
        self.enabled = enabled
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration
    def get_remain_enabled(self):
        return self.remain_enabled
    def set_remain_enabled(self, remain_enabled):
        self.remain_enabled = remain_enabled
    def _hasContent(self):
        if (
            self.HeadTrack is not None or
            self.MoveTrack is not None or
            self.Actions
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EventTrigger', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EventTrigger')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EventTrigger':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EventTrigger')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EventTrigger', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EventTrigger'):
        if not self.enabled and 'enabled' not in already_processed:
            already_processed.add('enabled')
            outfile.write(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.duration != 0.0 and 'duration' not in already_processed:
            already_processed.add('duration')
            outfile.write(' duration="%s"' % self.gds_format_double(self.duration, input_name='duration'))
        if not self.remain_enabled and 'remain_enabled' not in already_processed:
            already_processed.add('remain_enabled')
            outfile.write(' remain-enabled="%s"' % self.gds_format_boolean(self.remain_enabled, input_name='remain-enabled'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EventTrigger', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HeadTrack is not None:
            namespaceprefix_ = self.HeadTrack_nsprefix_ + ':' if (UseCapturedNS_ and self.HeadTrack_nsprefix_) else ''
            self.HeadTrack.export(outfile, level, namespaceprefix_, namespacedef_='', name_='HeadTrack', pretty_print=pretty_print)
        if self.MoveTrack is not None:
            namespaceprefix_ = self.MoveTrack_nsprefix_ + ':' if (UseCapturedNS_ and self.MoveTrack_nsprefix_) else ''
            self.MoveTrack.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MoveTrack', pretty_print=pretty_print)
        for Actions_ in self.Actions:
            namespaceprefix_ = self.Actions_nsprefix_ + ':' if (UseCapturedNS_ and self.Actions_nsprefix_) else ''
            Actions_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Actions', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('duration', node)
        if value is not None and 'duration' not in already_processed:
            already_processed.add('duration')
            value = self.gds_parse_double(value, node, 'duration')
            self.duration = value
        value = find_attr_value_('remain-enabled', node)
        if value is not None and 'remain-enabled' not in already_processed:
            already_processed.add('remain-enabled')
            if value in ('true', '1'):
                self.remain_enabled = True
            elif value in ('false', '0'):
                self.remain_enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'HeadTrack':
            obj_ = HeadTrackType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.HeadTrack = obj_
            obj_.original_tagname_ = 'HeadTrack'
        elif nodeName_ == 'MoveTrack':
            obj_ = MoveTrackType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MoveTrack = obj_
            obj_.original_tagname_ = 'MoveTrack'
        elif nodeName_ == 'Actions':
            class_obj_ = self.get_class_obj_(child_, ActionsType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Actions.append(obj_)
            obj_.original_tagname_ = 'Actions'
# end class EventTrigger


class Box(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ignore_Y=True, corner1=None, corner2=None, Movement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ignore_Y = _cast(bool, ignore_Y)
        self.ignore_Y_nsprefix_ = None
        self.corner1 = _cast(None, corner1)
        self.corner1_nsprefix_ = None
        self.corner2 = _cast(None, corner2)
        self.corner2_nsprefix_ = None
        self.Movement = Movement
        self.Movement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Box)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Box.subclass:
            return Box.subclass(*args_, **kwargs_)
        else:
            return Box(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Movement(self):
        return self.Movement
    def set_Movement(self, Movement):
        self.Movement = Movement
    def get_ignore_Y(self):
        return self.ignore_Y
    def set_ignore_Y(self, ignore_Y):
        self.ignore_Y = ignore_Y
    def get_corner1(self):
        return self.corner1
    def set_corner1(self, corner1):
        self.corner1 = corner1
    def get_corner2(self):
        return self.corner2
    def set_corner2(self, corner2):
        self.corner2 = corner2
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (
            self.Movement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Box', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Box')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Box':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Box')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Box', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Box'):
        if not self.ignore_Y and 'ignore_Y' not in already_processed:
            already_processed.add('ignore_Y')
            outfile.write(' ignore-Y="%s"' % self.gds_format_boolean(self.ignore_Y, input_name='ignore-Y'))
        if self.corner1 is not None and 'corner1' not in already_processed:
            already_processed.add('corner1')
            outfile.write(' corner1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.corner1), input_name='corner1')), ))
        if self.corner2 is not None and 'corner2' not in already_processed:
            already_processed.add('corner2')
            outfile.write(' corner2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.corner2), input_name='corner2')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Box', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Movement is not None:
            namespaceprefix_ = self.Movement_nsprefix_ + ':' if (UseCapturedNS_ and self.Movement_nsprefix_) else ''
            self.Movement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Movement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ignore-Y', node)
        if value is not None and 'ignore-Y' not in already_processed:
            already_processed.add('ignore-Y')
            if value in ('true', '1'):
                self.ignore_Y = True
            elif value in ('false', '0'):
                self.ignore_Y = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('corner1', node)
        if value is not None and 'corner1' not in already_processed:
            already_processed.add('corner1')
            self.corner1 = value
            self.validate_vector(self.corner1)    # validate type vector
        value = find_attr_value_('corner2', node)
        if value is not None and 'corner2' not in already_processed:
            already_processed.add('corner2')
            self.corner2 = value
            self.validate_vector(self.corner2)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Movement':
            obj_ = MovementType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Movement = obj_
            obj_.original_tagname_ = 'Movement'
# end class Box


class Event(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enable=None, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enable = _cast(bool, enable)
        self.enable_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Event)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Event.subclass:
            return Event.subclass(*args_, **kwargs_)
        else:
            return Event(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_enable(self):
        return self.enable
    def set_enable(self, enable):
        self.enable = enable
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Event', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Event')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Event':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Event')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Event', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Event'):
        if self.enable is not None and 'enable' not in already_processed:
            already_processed.add('enable')
            outfile.write(' enable="%s"' % self.gds_format_boolean(self.enable, input_name='enable'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Event', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enable', node)
        if value is not None and 'enable' not in already_processed:
            already_processed.add('enable')
            if value in ('true', '1'):
                self.enable = True
            elif value in ('false', '0'):
                self.enable = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Event


class ParticleActionList(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, Source=None, Vel=None, ParticleAction=None, RemoveCondition=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.Vel = Vel
        self.Vel_nsprefix_ = None
        if ParticleAction is None:
            self.ParticleAction = []
        else:
            self.ParticleAction = ParticleAction
        self.ParticleAction_nsprefix_ = None
        self.RemoveCondition = RemoveCondition
        self.RemoveCondition_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticleActionList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticleActionList.subclass:
            return ParticleActionList.subclass(*args_, **kwargs_)
        else:
            return ParticleActionList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def get_Vel(self):
        return self.Vel
    def set_Vel(self, Vel):
        self.Vel = Vel
    def get_ParticleAction(self):
        return self.ParticleAction
    def set_ParticleAction(self, ParticleAction):
        self.ParticleAction = ParticleAction
    def add_ParticleAction(self, value):
        self.ParticleAction.append(value)
    def insert_ParticleAction_at(self, index, value):
        self.ParticleAction.insert(index, value)
    def replace_ParticleAction_at(self, index, value):
        self.ParticleAction[index] = value
    def get_RemoveCondition(self):
        return self.RemoveCondition
    def set_RemoveCondition(self, RemoveCondition):
        self.RemoveCondition = RemoveCondition
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.Source is not None or
            self.Vel is not None or
            self.ParticleAction or
            self.RemoveCondition is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleActionList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticleActionList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticleActionList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticleActionList')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticleActionList', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticleActionList'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleActionList', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Source is not None:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            self.Source.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
        if self.Vel is not None:
            namespaceprefix_ = self.Vel_nsprefix_ + ':' if (UseCapturedNS_ and self.Vel_nsprefix_) else ''
            self.Vel.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Vel', pretty_print=pretty_print)
        for ParticleAction_ in self.ParticleAction:
            namespaceprefix_ = self.ParticleAction_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleAction_nsprefix_) else ''
            ParticleAction_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleAction', pretty_print=pretty_print)
        if self.RemoveCondition is not None:
            namespaceprefix_ = self.RemoveCondition_nsprefix_ + ':' if (UseCapturedNS_ and self.RemoveCondition_nsprefix_) else ''
            self.RemoveCondition.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RemoveCondition', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Source':
            obj_ = SourceType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source = obj_
            obj_.original_tagname_ = 'Source'
        elif nodeName_ == 'Vel':
            obj_ = VelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Vel = obj_
            obj_.original_tagname_ = 'Vel'
        elif nodeName_ == 'ParticleAction':
            obj_ = ParticleAction.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleAction.append(obj_)
            obj_.original_tagname_ = 'ParticleAction'
        elif nodeName_ == 'RemoveCondition':
            obj_ = RemoveConditionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RemoveCondition = obj_
            obj_.original_tagname_ = 'RemoveCondition'
# end class ParticleActionList


class ParticleAction(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Avoid=None, Bounce=None, Gravity=None, Damping=None, Gravitate=None, Follow=None, MatchVel=None, OrbitPoint=None, Jet=None, RandomVel=None, RandomAccel=None, RandomDisplace=None, TargetColor=None, TargetSize=None, TargetVel=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Avoid = Avoid
        self.Avoid_nsprefix_ = None
        self.Bounce = Bounce
        self.Bounce_nsprefix_ = None
        self.Gravity = Gravity
        self.Gravity_nsprefix_ = None
        self.Damping = Damping
        self.Damping_nsprefix_ = None
        self.Gravitate = Gravitate
        self.Gravitate_nsprefix_ = None
        self.Follow = Follow
        self.Follow_nsprefix_ = None
        self.MatchVel = MatchVel
        self.MatchVel_nsprefix_ = None
        self.OrbitPoint = OrbitPoint
        self.OrbitPoint_nsprefix_ = None
        self.Jet = Jet
        self.Jet_nsprefix_ = None
        self.RandomVel = RandomVel
        self.RandomVel_nsprefix_ = None
        self.RandomAccel = RandomAccel
        self.RandomAccel_nsprefix_ = None
        self.RandomDisplace = RandomDisplace
        self.RandomDisplace_nsprefix_ = None
        self.TargetColor = TargetColor
        self.TargetColor_nsprefix_ = None
        self.TargetSize = TargetSize
        self.TargetSize_nsprefix_ = None
        self.TargetVel = TargetVel
        self.TargetVel_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticleAction)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticleAction.subclass:
            return ParticleAction.subclass(*args_, **kwargs_)
        else:
            return ParticleAction(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Avoid(self):
        return self.Avoid
    def set_Avoid(self, Avoid):
        self.Avoid = Avoid
    def get_Bounce(self):
        return self.Bounce
    def set_Bounce(self, Bounce):
        self.Bounce = Bounce
    def get_Gravity(self):
        return self.Gravity
    def set_Gravity(self, Gravity):
        self.Gravity = Gravity
    def get_Damping(self):
        return self.Damping
    def set_Damping(self, Damping):
        self.Damping = Damping
    def get_Gravitate(self):
        return self.Gravitate
    def set_Gravitate(self, Gravitate):
        self.Gravitate = Gravitate
    def get_Follow(self):
        return self.Follow
    def set_Follow(self, Follow):
        self.Follow = Follow
    def get_MatchVel(self):
        return self.MatchVel
    def set_MatchVel(self, MatchVel):
        self.MatchVel = MatchVel
    def get_OrbitPoint(self):
        return self.OrbitPoint
    def set_OrbitPoint(self, OrbitPoint):
        self.OrbitPoint = OrbitPoint
    def get_Jet(self):
        return self.Jet
    def set_Jet(self, Jet):
        self.Jet = Jet
    def get_RandomVel(self):
        return self.RandomVel
    def set_RandomVel(self, RandomVel):
        self.RandomVel = RandomVel
    def get_RandomAccel(self):
        return self.RandomAccel
    def set_RandomAccel(self, RandomAccel):
        self.RandomAccel = RandomAccel
    def get_RandomDisplace(self):
        return self.RandomDisplace
    def set_RandomDisplace(self, RandomDisplace):
        self.RandomDisplace = RandomDisplace
    def get_TargetColor(self):
        return self.TargetColor
    def set_TargetColor(self, TargetColor):
        self.TargetColor = TargetColor
    def get_TargetSize(self):
        return self.TargetSize
    def set_TargetSize(self, TargetSize):
        self.TargetSize = TargetSize
    def get_TargetVel(self):
        return self.TargetVel
    def set_TargetVel(self, TargetVel):
        self.TargetVel = TargetVel
    def _hasContent(self):
        if (
            self.Avoid is not None or
            self.Bounce is not None or
            self.Gravity is not None or
            self.Damping is not None or
            self.Gravitate is not None or
            self.Follow is not None or
            self.MatchVel is not None or
            self.OrbitPoint is not None or
            self.Jet is not None or
            self.RandomVel is not None or
            self.RandomAccel is not None or
            self.RandomDisplace is not None or
            self.TargetColor is not None or
            self.TargetSize is not None or
            self.TargetVel is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleAction', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticleAction')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticleAction':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticleAction')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticleAction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticleAction'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleAction', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Avoid is not None:
            namespaceprefix_ = self.Avoid_nsprefix_ + ':' if (UseCapturedNS_ and self.Avoid_nsprefix_) else ''
            self.Avoid.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Avoid', pretty_print=pretty_print)
        if self.Bounce is not None:
            namespaceprefix_ = self.Bounce_nsprefix_ + ':' if (UseCapturedNS_ and self.Bounce_nsprefix_) else ''
            self.Bounce.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bounce', pretty_print=pretty_print)
        if self.Gravity is not None:
            namespaceprefix_ = self.Gravity_nsprefix_ + ':' if (UseCapturedNS_ and self.Gravity_nsprefix_) else ''
            self.Gravity.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Gravity', pretty_print=pretty_print)
        if self.Damping is not None:
            namespaceprefix_ = self.Damping_nsprefix_ + ':' if (UseCapturedNS_ and self.Damping_nsprefix_) else ''
            self.Damping.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Damping', pretty_print=pretty_print)
        if self.Gravitate is not None:
            namespaceprefix_ = self.Gravitate_nsprefix_ + ':' if (UseCapturedNS_ and self.Gravitate_nsprefix_) else ''
            self.Gravitate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Gravitate', pretty_print=pretty_print)
        if self.Follow is not None:
            namespaceprefix_ = self.Follow_nsprefix_ + ':' if (UseCapturedNS_ and self.Follow_nsprefix_) else ''
            self.Follow.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Follow', pretty_print=pretty_print)
        if self.MatchVel is not None:
            namespaceprefix_ = self.MatchVel_nsprefix_ + ':' if (UseCapturedNS_ and self.MatchVel_nsprefix_) else ''
            self.MatchVel.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MatchVel', pretty_print=pretty_print)
        if self.OrbitPoint is not None:
            namespaceprefix_ = self.OrbitPoint_nsprefix_ + ':' if (UseCapturedNS_ and self.OrbitPoint_nsprefix_) else ''
            self.OrbitPoint.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrbitPoint', pretty_print=pretty_print)
        if self.Jet is not None:
            namespaceprefix_ = self.Jet_nsprefix_ + ':' if (UseCapturedNS_ and self.Jet_nsprefix_) else ''
            self.Jet.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Jet', pretty_print=pretty_print)
        if self.RandomVel is not None:
            namespaceprefix_ = self.RandomVel_nsprefix_ + ':' if (UseCapturedNS_ and self.RandomVel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRandomVel>%s</%sRandomVel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RandomVel), input_name='RandomVel')), namespaceprefix_ , eol_))
        if self.RandomAccel is not None:
            namespaceprefix_ = self.RandomAccel_nsprefix_ + ':' if (UseCapturedNS_ and self.RandomAccel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRandomAccel>%s</%sRandomAccel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RandomAccel), input_name='RandomAccel')), namespaceprefix_ , eol_))
        if self.RandomDisplace is not None:
            namespaceprefix_ = self.RandomDisplace_nsprefix_ + ':' if (UseCapturedNS_ and self.RandomDisplace_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRandomDisplace>%s</%sRandomDisplace>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RandomDisplace), input_name='RandomDisplace')), namespaceprefix_ , eol_))
        if self.TargetColor is not None:
            namespaceprefix_ = self.TargetColor_nsprefix_ + ':' if (UseCapturedNS_ and self.TargetColor_nsprefix_) else ''
            self.TargetColor.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TargetColor', pretty_print=pretty_print)
        if self.TargetSize is not None:
            namespaceprefix_ = self.TargetSize_nsprefix_ + ':' if (UseCapturedNS_ and self.TargetSize_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTargetSize>%s</%sTargetSize>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TargetSize), input_name='TargetSize')), namespaceprefix_ , eol_))
        if self.TargetVel is not None:
            namespaceprefix_ = self.TargetVel_nsprefix_ + ':' if (UseCapturedNS_ and self.TargetVel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTargetVel>%s</%sTargetVel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TargetVel), input_name='TargetVel')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Avoid':
            obj_ = AvoidType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Avoid = obj_
            obj_.original_tagname_ = 'Avoid'
        elif nodeName_ == 'Bounce':
            obj_ = BounceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bounce = obj_
            obj_.original_tagname_ = 'Bounce'
        elif nodeName_ == 'Gravity':
            obj_ = GravityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Gravity = obj_
            obj_.original_tagname_ = 'Gravity'
        elif nodeName_ == 'Damping':
            obj_ = DampingType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Damping = obj_
            obj_.original_tagname_ = 'Damping'
        elif nodeName_ == 'Gravitate':
            obj_ = GravitateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Gravitate = obj_
            obj_.original_tagname_ = 'Gravitate'
        elif nodeName_ == 'Follow':
            obj_ = FollowType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Follow = obj_
            obj_.original_tagname_ = 'Follow'
        elif nodeName_ == 'MatchVel':
            obj_ = MatchVelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MatchVel = obj_
            obj_.original_tagname_ = 'MatchVel'
        elif nodeName_ == 'OrbitPoint':
            obj_ = OrbitPointType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrbitPoint = obj_
            obj_.original_tagname_ = 'OrbitPoint'
        elif nodeName_ == 'Jet':
            obj_ = JetType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Jet = obj_
            obj_.original_tagname_ = 'Jet'
        elif nodeName_ == 'RandomVel':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RandomVel')
            value_ = self.gds_validate_string(value_, node, 'RandomVel')
            self.RandomVel = value_
            self.RandomVel_nsprefix_ = child_.prefix
        elif nodeName_ == 'RandomAccel':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RandomAccel')
            value_ = self.gds_validate_string(value_, node, 'RandomAccel')
            self.RandomAccel = value_
            self.RandomAccel_nsprefix_ = child_.prefix
        elif nodeName_ == 'RandomDisplace':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RandomDisplace')
            value_ = self.gds_validate_string(value_, node, 'RandomDisplace')
            self.RandomDisplace = value_
            self.RandomDisplace_nsprefix_ = child_.prefix
        elif nodeName_ == 'TargetColor':
            obj_ = TargetColorType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TargetColor = obj_
            obj_.original_tagname_ = 'TargetColor'
        elif nodeName_ == 'TargetSize':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TargetSize')
            value_ = self.gds_validate_string(value_, node, 'TargetSize')
            self.TargetSize = value_
            self.TargetSize_nsprefix_ = child_.prefix
        elif nodeName_ == 'TargetVel':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TargetVel')
            value_ = self.gds_validate_string(value_, node, 'TargetVel')
            self.TargetVel = value_
            self.TargetVel_nsprefix_ = child_.prefix
# end class ParticleAction


class RandomVel(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RandomVel)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RandomVel.subclass:
            return RandomVel.subclass(*args_, **kwargs_)
        else:
            return RandomVel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomVel', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RandomVel')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RandomVel':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RandomVel')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RandomVel', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RandomVel'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomVel', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RandomVel


class RandomAccel(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RandomAccel)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RandomAccel.subclass:
            return RandomAccel.subclass(*args_, **kwargs_)
        else:
            return RandomAccel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomAccel', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RandomAccel')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RandomAccel':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RandomAccel')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RandomAccel', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RandomAccel'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomAccel', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RandomAccel


class RandomDisplace(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RandomDisplace)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RandomDisplace.subclass:
            return RandomDisplace.subclass(*args_, **kwargs_)
        else:
            return RandomDisplace(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomDisplace', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RandomDisplace')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RandomDisplace':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RandomDisplace')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RandomDisplace', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RandomDisplace'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RandomDisplace', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RandomDisplace


class TargetSize(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TargetSize)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TargetSize.subclass:
            return TargetSize.subclass(*args_, **kwargs_)
        else:
            return TargetSize(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetSize', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TargetSize')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TargetSize':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TargetSize')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TargetSize', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TargetSize'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetSize', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TargetSize


class TargetVel(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TargetVel)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TargetVel.subclass:
            return TargetVel.subclass(*args_, **kwargs_)
        else:
            return TargetVel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetVel', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TargetVel')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TargetVel':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TargetVel')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TargetVel', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TargetVel'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetVel', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TargetVel


class Placement(GeneratedsSuper):
    """Placement -- Placement Obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, RelativeTo='Center', Position='(0.0, 0.0, 0.0)', Axis=None, LookAt=None, Normal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.RelativeTo = RelativeTo
        self.RelativeTo_nsprefix_ = None
        self.Position = Position
        self.validate_vector(self.Position)
        self.Position_nsprefix_ = None
        self.Axis = Axis
        self.Axis_nsprefix_ = None
        self.LookAt = LookAt
        self.LookAt_nsprefix_ = None
        self.Normal = Normal
        self.Normal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Placement)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Placement.subclass:
            return Placement.subclass(*args_, **kwargs_)
        else:
            return Placement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RelativeTo(self):
        return self.RelativeTo
    def set_RelativeTo(self, RelativeTo):
        self.RelativeTo = RelativeTo
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_Axis(self):
        return self.Axis
    def set_Axis(self, Axis):
        self.Axis = Axis
    def get_LookAt(self):
        return self.LookAt
    def set_LookAt(self, LookAt):
        self.LookAt = LookAt
    def get_Normal(self):
        return self.Normal
    def set_Normal(self, Normal):
        self.Normal = Normal
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def validate_vector(self, value):
        result = True
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.RelativeTo != "Center" or
            self.Position != "(0.0, 0.0, 0.0)" or
            self.Axis is not None or
            self.LookAt is not None or
            self.Normal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Placement', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Placement')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Placement':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Placement')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Placement', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Placement'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Placement', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RelativeTo is not None:
            namespaceprefix_ = self.RelativeTo_nsprefix_ + ':' if (UseCapturedNS_ and self.RelativeTo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRelativeTo>%s</%sRelativeTo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RelativeTo), input_name='RelativeTo')), namespaceprefix_ , eol_))
        if self.RelativeTo is None:
            namespaceprefix_ = self.RelativeTo_nsprefix_ + ':' if (UseCapturedNS_ and self.RelativeTo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRelativeTo>Center</%sRelativeTo/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Position is not None:
            namespaceprefix_ = self.Position_nsprefix_ + ':' if (UseCapturedNS_ and self.Position_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPosition>%s</%sPosition>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Position), input_name='Position')), namespaceprefix_ , eol_))
        if self.Position is None:
            namespaceprefix_ = self.Position_nsprefix_ + ':' if (UseCapturedNS_ and self.Position_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPosition>(0.0, 0.0, 0.0)</%sPosition/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Axis is not None:
            namespaceprefix_ = self.Axis_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis_nsprefix_) else ''
            self.Axis.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Axis', pretty_print=pretty_print)
        if self.LookAt is not None:
            namespaceprefix_ = self.LookAt_nsprefix_ + ':' if (UseCapturedNS_ and self.LookAt_nsprefix_) else ''
            self.LookAt.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LookAt', pretty_print=pretty_print)
        if self.Normal is not None:
            namespaceprefix_ = self.Normal_nsprefix_ + ':' if (UseCapturedNS_ and self.Normal_nsprefix_) else ''
            self.Normal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Normal', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RelativeTo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RelativeTo')
            value_ = self.gds_validate_string(value_, node, 'RelativeTo')
            self.RelativeTo = value_
            self.RelativeTo_nsprefix_ = child_.prefix
        elif nodeName_ == 'Position':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Position')
            value_ = self.gds_validate_string(value_, node, 'Position')
            self.Position = value_
            self.Position_nsprefix_ = child_.prefix
            # validate type vector
            self.validate_vector(self.Position)
        elif nodeName_ == 'Axis':
            obj_ = AxisType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Axis = obj_
            obj_.original_tagname_ = 'Axis'
        elif nodeName_ == 'LookAt':
            obj_ = LookAtType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LookAt = obj_
            obj_.original_tagname_ = 'LookAt'
        elif nodeName_ == 'Normal':
            obj_ = NormalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Normal = obj_
            obj_.original_tagname_ = 'Normal'
# end class Placement


class Transition(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, duration=1.0, Visible=None, Movement=None, MoveRel=None, Color='255,255,255', Scale=1.0, Sound=None, LinkChange=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.duration = _cast(float, duration)
        self.duration_nsprefix_ = None
        self.Visible = Visible
        self.Visible_nsprefix_ = None
        self.Movement = Movement
        self.Movement_nsprefix_ = None
        self.MoveRel = MoveRel
        self.MoveRel_nsprefix_ = None
        self.Color = Color
        self.validate_color(self.Color)
        self.Color_nsprefix_ = None
        self.Scale = Scale
        self.Scale_nsprefix_ = None
        self.Sound = Sound
        self.Sound_nsprefix_ = None
        self.LinkChange = LinkChange
        self.LinkChange_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Transition)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Transition.subclass:
            return Transition.subclass(*args_, **kwargs_)
        else:
            return Transition(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Visible(self):
        return self.Visible
    def set_Visible(self, Visible):
        self.Visible = Visible
    def get_Movement(self):
        return self.Movement
    def set_Movement(self, Movement):
        self.Movement = Movement
    def get_MoveRel(self):
        return self.MoveRel
    def set_MoveRel(self, MoveRel):
        self.MoveRel = MoveRel
    def get_Color(self):
        return self.Color
    def set_Color(self, Color):
        self.Color = Color
    def get_Scale(self):
        return self.Scale
    def set_Scale(self, Scale):
        self.Scale = Scale
    def get_Sound(self):
        return self.Sound
    def set_Sound(self, Sound):
        self.Sound = Sound
    def get_LinkChange(self):
        return self.LinkChange
    def set_LinkChange(self, LinkChange):
        self.LinkChange = LinkChange
    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration
    def validate_color(self, value):
        result = True
        # Validate type color, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.Visible is not None or
            self.Movement is not None or
            self.MoveRel is not None or
            self.Color != "255,255,255" or
            self.Scale != 1.0 or
            self.Sound is not None or
            self.LinkChange is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Transition', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Transition')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Transition':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Transition')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Transition', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Transition'):
        if self.duration != 1.0 and 'duration' not in already_processed:
            already_processed.add('duration')
            outfile.write(' duration="%s"' % self.gds_format_double(self.duration, input_name='duration'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='Transition', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Visible is not None:
            namespaceprefix_ = self.Visible_nsprefix_ + ':' if (UseCapturedNS_ and self.Visible_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVisible>%s</%sVisible>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Visible, input_name='Visible'), namespaceprefix_ , eol_))
        if self.Movement is not None:
            namespaceprefix_ = self.Movement_nsprefix_ + ':' if (UseCapturedNS_ and self.Movement_nsprefix_) else ''
            self.Movement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Movement', pretty_print=pretty_print)
        if self.MoveRel is not None:
            namespaceprefix_ = self.MoveRel_nsprefix_ + ':' if (UseCapturedNS_ and self.MoveRel_nsprefix_) else ''
            self.MoveRel.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MoveRel', pretty_print=pretty_print)
        if self.Color is not None:
            namespaceprefix_ = self.Color_nsprefix_ + ':' if (UseCapturedNS_ and self.Color_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sColor>%s</%sColor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Color), input_name='Color')), namespaceprefix_ , eol_))
        if self.Color is None:
            namespaceprefix_ = self.Color_nsprefix_ + ':' if (UseCapturedNS_ and self.Color_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sColor>255,255,255</%sColor/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Scale is not None:
            namespaceprefix_ = self.Scale_nsprefix_ + ':' if (UseCapturedNS_ and self.Scale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScale>%s</%sScale>%s' % (namespaceprefix_ , self.gds_format_double(self.Scale, input_name='Scale'), namespaceprefix_ , eol_))
        if self.Scale is None:
            namespaceprefix_ = self.Scale_nsprefix_ + ':' if (UseCapturedNS_ and self.Scale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScale>1.0</%sScale/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.Sound is not None:
            namespaceprefix_ = self.Sound_nsprefix_ + ':' if (UseCapturedNS_ and self.Sound_nsprefix_) else ''
            self.Sound.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sound', pretty_print=pretty_print)
        if self.LinkChange is not None:
            namespaceprefix_ = self.LinkChange_nsprefix_ + ':' if (UseCapturedNS_ and self.LinkChange_nsprefix_) else ''
            self.LinkChange.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LinkChange', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('duration', node)
        if value is not None and 'duration' not in already_processed:
            already_processed.add('duration')
            value = self.gds_parse_double(value, node, 'duration')
            self.duration = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Visible':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Visible')
            ival_ = self.gds_validate_boolean(ival_, node, 'Visible')
            self.Visible = ival_
            self.Visible_nsprefix_ = child_.prefix
        elif nodeName_ == 'Movement':
            obj_ = MovementType5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Movement = obj_
            obj_.original_tagname_ = 'Movement'
        elif nodeName_ == 'MoveRel':
            obj_ = MoveRelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MoveRel = obj_
            obj_.original_tagname_ = 'MoveRel'
        elif nodeName_ == 'Color':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Color')
            value_ = self.gds_validate_string(value_, node, 'Color')
            self.Color = value_
            self.Color_nsprefix_ = child_.prefix
            # validate type color
            self.validate_color(self.Color)
        elif nodeName_ == 'Scale' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Scale')
            fval_ = self.gds_validate_double(fval_, node, 'Scale')
            self.Scale = fval_
            self.Scale_nsprefix_ = child_.prefix
        elif nodeName_ == 'Sound':
            obj_ = SoundType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sound = obj_
            obj_.original_tagname_ = 'Sound'
        elif nodeName_ == 'LinkChange':
            obj_ = LinkChangeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LinkChange = obj_
            obj_.original_tagname_ = 'LinkChange'
# end class Transition


class ParticleDomainType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Point=None, Line=None, Triangle=None, Plane=None, Rect=None, Box=None, Sphere=None, Cylinder=None, Cone=None, Blob=None, Disc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Point = Point
        self.Point_nsprefix_ = None
        self.Line = Line
        self.Line_nsprefix_ = None
        self.Triangle = Triangle
        self.Triangle_nsprefix_ = None
        self.Plane = Plane
        self.Plane_nsprefix_ = None
        self.Rect = Rect
        self.Rect_nsprefix_ = None
        self.Box = Box
        self.Box_nsprefix_ = None
        self.Sphere = Sphere
        self.Sphere_nsprefix_ = None
        self.Cylinder = Cylinder
        self.Cylinder_nsprefix_ = None
        self.Cone = Cone
        self.Cone_nsprefix_ = None
        self.Blob = Blob
        self.Blob_nsprefix_ = None
        self.Disc = Disc
        self.Disc_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticleDomainType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticleDomainType.subclass:
            return ParticleDomainType.subclass(*args_, **kwargs_)
        else:
            return ParticleDomainType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Point(self):
        return self.Point
    def set_Point(self, Point):
        self.Point = Point
    def get_Line(self):
        return self.Line
    def set_Line(self, Line):
        self.Line = Line
    def get_Triangle(self):
        return self.Triangle
    def set_Triangle(self, Triangle):
        self.Triangle = Triangle
    def get_Plane(self):
        return self.Plane
    def set_Plane(self, Plane):
        self.Plane = Plane
    def get_Rect(self):
        return self.Rect
    def set_Rect(self, Rect):
        self.Rect = Rect
    def get_Box(self):
        return self.Box
    def set_Box(self, Box):
        self.Box = Box
    def get_Sphere(self):
        return self.Sphere
    def set_Sphere(self, Sphere):
        self.Sphere = Sphere
    def get_Cylinder(self):
        return self.Cylinder
    def set_Cylinder(self, Cylinder):
        self.Cylinder = Cylinder
    def get_Cone(self):
        return self.Cone
    def set_Cone(self, Cone):
        self.Cone = Cone
    def get_Blob(self):
        return self.Blob
    def set_Blob(self, Blob):
        self.Blob = Blob
    def get_Disc(self):
        return self.Disc
    def set_Disc(self, Disc):
        self.Disc = Disc
    def _hasContent(self):
        if (
            self.Point is not None or
            self.Line is not None or
            self.Triangle is not None or
            self.Plane is not None or
            self.Rect is not None or
            self.Box is not None or
            self.Sphere is not None or
            self.Cylinder is not None or
            self.Cone is not None or
            self.Blob is not None or
            self.Disc is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleDomainType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticleDomainType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticleDomainType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticleDomainType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticleDomainType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticleDomainType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleDomainType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Point is not None:
            namespaceprefix_ = self.Point_nsprefix_ + ':' if (UseCapturedNS_ and self.Point_nsprefix_) else ''
            self.Point.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Point', pretty_print=pretty_print)
        if self.Line is not None:
            namespaceprefix_ = self.Line_nsprefix_ + ':' if (UseCapturedNS_ and self.Line_nsprefix_) else ''
            self.Line.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Line', pretty_print=pretty_print)
        if self.Triangle is not None:
            namespaceprefix_ = self.Triangle_nsprefix_ + ':' if (UseCapturedNS_ and self.Triangle_nsprefix_) else ''
            self.Triangle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Triangle', pretty_print=pretty_print)
        if self.Plane is not None:
            namespaceprefix_ = self.Plane_nsprefix_ + ':' if (UseCapturedNS_ and self.Plane_nsprefix_) else ''
            self.Plane.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Plane', pretty_print=pretty_print)
        if self.Rect is not None:
            namespaceprefix_ = self.Rect_nsprefix_ + ':' if (UseCapturedNS_ and self.Rect_nsprefix_) else ''
            self.Rect.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Rect', pretty_print=pretty_print)
        if self.Box is not None:
            namespaceprefix_ = self.Box_nsprefix_ + ':' if (UseCapturedNS_ and self.Box_nsprefix_) else ''
            self.Box.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Box', pretty_print=pretty_print)
        if self.Sphere is not None:
            namespaceprefix_ = self.Sphere_nsprefix_ + ':' if (UseCapturedNS_ and self.Sphere_nsprefix_) else ''
            self.Sphere.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sphere', pretty_print=pretty_print)
        if self.Cylinder is not None:
            namespaceprefix_ = self.Cylinder_nsprefix_ + ':' if (UseCapturedNS_ and self.Cylinder_nsprefix_) else ''
            self.Cylinder.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Cylinder', pretty_print=pretty_print)
        if self.Cone is not None:
            namespaceprefix_ = self.Cone_nsprefix_ + ':' if (UseCapturedNS_ and self.Cone_nsprefix_) else ''
            self.Cone.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Cone', pretty_print=pretty_print)
        if self.Blob is not None:
            namespaceprefix_ = self.Blob_nsprefix_ + ':' if (UseCapturedNS_ and self.Blob_nsprefix_) else ''
            self.Blob.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Blob', pretty_print=pretty_print)
        if self.Disc is not None:
            namespaceprefix_ = self.Disc_nsprefix_ + ':' if (UseCapturedNS_ and self.Disc_nsprefix_) else ''
            self.Disc.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Disc', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Point':
            obj_ = PointType6.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Point = obj_
            obj_.original_tagname_ = 'Point'
        elif nodeName_ == 'Line':
            obj_ = LineType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Line = obj_
            obj_.original_tagname_ = 'Line'
        elif nodeName_ == 'Triangle':
            obj_ = TriangleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Triangle = obj_
            obj_.original_tagname_ = 'Triangle'
        elif nodeName_ == 'Plane':
            obj_ = PlaneType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Plane = obj_
            obj_.original_tagname_ = 'Plane'
        elif nodeName_ == 'Rect':
            obj_ = RectType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Rect = obj_
            obj_.original_tagname_ = 'Rect'
        elif nodeName_ == 'Box':
            obj_ = BoxType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Box = obj_
            obj_.original_tagname_ = 'Box'
        elif nodeName_ == 'Sphere':
            obj_ = SphereType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sphere = obj_
            obj_.original_tagname_ = 'Sphere'
        elif nodeName_ == 'Cylinder':
            obj_ = CylinderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Cylinder = obj_
            obj_.original_tagname_ = 'Cylinder'
        elif nodeName_ == 'Cone':
            obj_ = ConeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Cone = obj_
            obj_.original_tagname_ = 'Cone'
        elif nodeName_ == 'Blob':
            obj_ = BlobType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Blob = obj_
            obj_.original_tagname_ = 'Blob'
        elif nodeName_ == 'Disc':
            obj_ = DiscType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Disc = obj_
            obj_.original_tagname_ = 'Disc'
# end class ParticleDomainType


class ObjectRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Object=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
        self.Object_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectRootType.subclass:
            return ObjectRootType.subclass(*args_, **kwargs_)
        else:
            return ObjectRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Object(self):
        return self.Object
    def set_Object(self, Object):
        self.Object = Object
    def add_Object(self, value):
        self.Object.append(value)
    def insert_Object_at(self, index, value):
        self.Object.insert(index, value)
    def replace_Object_at(self, index, value):
        self.Object[index] = value
    def _hasContent(self):
        if (
            self.Object
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Object_ in self.Object:
            namespaceprefix_ = self.Object_nsprefix_ + ':' if (UseCapturedNS_ and self.Object_nsprefix_) else ''
            Object_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Object', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Object':
            obj_ = Object.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Object.append(obj_)
            obj_.original_tagname_ = 'Object'
# end class ObjectRootType


class GroupRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Group=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Group is None:
            self.Group = []
        else:
            self.Group = Group
        self.Group_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupRootType.subclass:
            return GroupRootType.subclass(*args_, **kwargs_)
        else:
            return GroupRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Group(self):
        return self.Group
    def set_Group(self, Group):
        self.Group = Group
    def add_Group(self, value):
        self.Group.append(value)
    def insert_Group_at(self, index, value):
        self.Group.insert(index, value)
    def replace_Group_at(self, index, value):
        self.Group[index] = value
    def _hasContent(self):
        if (
            self.Group
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Group_ in self.Group:
            namespaceprefix_ = self.Group_nsprefix_ + ':' if (UseCapturedNS_ and self.Group_nsprefix_) else ''
            Group_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Group', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Group':
            obj_ = Group.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Group.append(obj_)
            obj_.original_tagname_ = 'Group'
# end class GroupRootType


class TimelineRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Timeline=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Timeline is None:
            self.Timeline = []
        else:
            self.Timeline = Timeline
        self.Timeline_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimelineRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimelineRootType.subclass:
            return TimelineRootType.subclass(*args_, **kwargs_)
        else:
            return TimelineRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Timeline(self):
        return self.Timeline
    def set_Timeline(self, Timeline):
        self.Timeline = Timeline
    def add_Timeline(self, value):
        self.Timeline.append(value)
    def insert_Timeline_at(self, index, value):
        self.Timeline.insert(index, value)
    def replace_Timeline_at(self, index, value):
        self.Timeline[index] = value
    def _hasContent(self):
        if (
            self.Timeline
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimelineRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimelineRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimelineRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimelineRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimelineRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimelineRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimelineRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Timeline_ in self.Timeline:
            namespaceprefix_ = self.Timeline_nsprefix_ + ':' if (UseCapturedNS_ and self.Timeline_nsprefix_) else ''
            Timeline_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Timeline', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Timeline':
            obj_ = Timeline.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Timeline.append(obj_)
            obj_.original_tagname_ = 'Timeline'
# end class TimelineRootType


class PlacementRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Placement is None:
            self.Placement = []
        else:
            self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PlacementRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PlacementRootType.subclass:
            return PlacementRootType.subclass(*args_, **kwargs_)
        else:
            return PlacementRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def add_Placement(self, value):
        self.Placement.append(value)
    def insert_Placement_at(self, index, value):
        self.Placement.insert(index, value)
    def replace_Placement_at(self, index, value):
        self.Placement[index] = value
    def _hasContent(self):
        if (
            self.Placement
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PlacementRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PlacementRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PlacementRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PlacementRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PlacementRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PlacementRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PlacementRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Placement_ in self.Placement:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            Placement_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement.append(obj_)
            obj_.original_tagname_ = 'Placement'
# end class PlacementRootType


class SoundRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Sound=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Sound is None:
            self.Sound = []
        else:
            self.Sound = Sound
        self.Sound_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SoundRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SoundRootType.subclass:
            return SoundRootType.subclass(*args_, **kwargs_)
        else:
            return SoundRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Sound(self):
        return self.Sound
    def set_Sound(self, Sound):
        self.Sound = Sound
    def add_Sound(self, value):
        self.Sound.append(value)
    def insert_Sound_at(self, index, value):
        self.Sound.insert(index, value)
    def replace_Sound_at(self, index, value):
        self.Sound[index] = value
    def _hasContent(self):
        if (
            self.Sound
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SoundRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SoundRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SoundRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SoundRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SoundRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Sound_ in self.Sound:
            namespaceprefix_ = self.Sound_nsprefix_ + ':' if (UseCapturedNS_ and self.Sound_nsprefix_) else ''
            Sound_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sound', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Sound':
            obj_ = Sound.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sound.append(obj_)
            obj_.original_tagname_ = 'Sound'
# end class SoundRootType


class EventRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, EventTrigger=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if EventTrigger is None:
            self.EventTrigger = []
        else:
            self.EventTrigger = EventTrigger
        self.EventTrigger_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EventRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EventRootType.subclass:
            return EventRootType.subclass(*args_, **kwargs_)
        else:
            return EventRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EventTrigger(self):
        return self.EventTrigger
    def set_EventTrigger(self, EventTrigger):
        self.EventTrigger = EventTrigger
    def add_EventTrigger(self, value):
        self.EventTrigger.append(value)
    def insert_EventTrigger_at(self, index, value):
        self.EventTrigger.insert(index, value)
    def replace_EventTrigger_at(self, index, value):
        self.EventTrigger[index] = value
    def _hasContent(self):
        if (
            self.EventTrigger
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EventRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EventRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EventRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EventRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EventRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EventRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EventRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for EventTrigger_ in self.EventTrigger:
            namespaceprefix_ = self.EventTrigger_nsprefix_ + ':' if (UseCapturedNS_ and self.EventTrigger_nsprefix_) else ''
            EventTrigger_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EventTrigger', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EventTrigger':
            obj_ = EventTrigger.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EventTrigger.append(obj_)
            obj_.original_tagname_ = 'EventTrigger'
# end class EventRootType


class ParticleActionRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ParticleActionList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ParticleActionList is None:
            self.ParticleActionList = []
        else:
            self.ParticleActionList = ParticleActionList
        self.ParticleActionList_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticleActionRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticleActionRootType.subclass:
            return ParticleActionRootType.subclass(*args_, **kwargs_)
        else:
            return ParticleActionRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleActionList(self):
        return self.ParticleActionList
    def set_ParticleActionList(self, ParticleActionList):
        self.ParticleActionList = ParticleActionList
    def add_ParticleActionList(self, value):
        self.ParticleActionList.append(value)
    def insert_ParticleActionList_at(self, index, value):
        self.ParticleActionList.insert(index, value)
    def replace_ParticleActionList_at(self, index, value):
        self.ParticleActionList[index] = value
    def _hasContent(self):
        if (
            self.ParticleActionList
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleActionRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticleActionRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticleActionRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticleActionRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticleActionRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticleActionRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleActionRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ParticleActionList_ in self.ParticleActionList:
            namespaceprefix_ = self.ParticleActionList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleActionList_nsprefix_) else ''
            ParticleActionList_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleActionList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleActionList':
            obj_ = ParticleActionList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleActionList.append(obj_)
            obj_.original_tagname_ = 'ParticleActionList'
# end class ParticleActionRootType


class GlobalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CameraPos=None, CaveCameraPos=None, Background=None, WandNavigation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CameraPos = CameraPos
        self.CameraPos_nsprefix_ = None
        self.CaveCameraPos = CaveCameraPos
        self.CaveCameraPos_nsprefix_ = None
        self.Background = Background
        self.Background_nsprefix_ = None
        self.WandNavigation = WandNavigation
        self.WandNavigation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GlobalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GlobalType.subclass:
            return GlobalType.subclass(*args_, **kwargs_)
        else:
            return GlobalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CameraPos(self):
        return self.CameraPos
    def set_CameraPos(self, CameraPos):
        self.CameraPos = CameraPos
    def get_CaveCameraPos(self):
        return self.CaveCameraPos
    def set_CaveCameraPos(self, CaveCameraPos):
        self.CaveCameraPos = CaveCameraPos
    def get_Background(self):
        return self.Background
    def set_Background(self, Background):
        self.Background = Background
    def get_WandNavigation(self):
        return self.WandNavigation
    def set_WandNavigation(self, WandNavigation):
        self.WandNavigation = WandNavigation
    def _hasContent(self):
        if (
            self.CameraPos is not None or
            self.CaveCameraPos is not None or
            self.Background is not None or
            self.WandNavigation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GlobalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GlobalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GlobalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GlobalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GlobalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GlobalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GlobalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CameraPos is not None:
            namespaceprefix_ = self.CameraPos_nsprefix_ + ':' if (UseCapturedNS_ and self.CameraPos_nsprefix_) else ''
            self.CameraPos.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CameraPos', pretty_print=pretty_print)
        if self.CaveCameraPos is not None:
            namespaceprefix_ = self.CaveCameraPos_nsprefix_ + ':' if (UseCapturedNS_ and self.CaveCameraPos_nsprefix_) else ''
            self.CaveCameraPos.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CaveCameraPos', pretty_print=pretty_print)
        if self.Background is not None:
            namespaceprefix_ = self.Background_nsprefix_ + ':' if (UseCapturedNS_ and self.Background_nsprefix_) else ''
            self.Background.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Background', pretty_print=pretty_print)
        if self.WandNavigation is not None:
            namespaceprefix_ = self.WandNavigation_nsprefix_ + ':' if (UseCapturedNS_ and self.WandNavigation_nsprefix_) else ''
            self.WandNavigation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='WandNavigation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CameraPos':
            obj_ = CameraPosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CameraPos = obj_
            obj_.original_tagname_ = 'CameraPos'
        elif nodeName_ == 'CaveCameraPos':
            obj_ = CaveCameraPosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CaveCameraPos = obj_
            obj_.original_tagname_ = 'CaveCameraPos'
        elif nodeName_ == 'Background':
            obj_ = BackgroundType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Background = obj_
            obj_.original_tagname_ = 'Background'
        elif nodeName_ == 'WandNavigation':
            obj_ = WandNavigationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.WandNavigation = obj_
            obj_.original_tagname_ = 'WandNavigation'
# end class GlobalType


class CameraPosType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, far_clip=100, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.far_clip = _cast(float, far_clip)
        self.far_clip_nsprefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CameraPosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CameraPosType.subclass:
            return CameraPosType.subclass(*args_, **kwargs_)
        else:
            return CameraPosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def get_far_clip(self):
        return self.far_clip
    def set_far_clip(self, far_clip):
        self.far_clip = far_clip
    def _hasContent(self):
        if (
            self.Placement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CameraPosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CameraPosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CameraPosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CameraPosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CameraPosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CameraPosType'):
        if self.far_clip != 100 and 'far_clip' not in already_processed:
            already_processed.add('far_clip')
            outfile.write(' far-clip="%s"' % self.gds_format_double(self.far_clip, input_name='far-clip'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CameraPosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('far-clip', node)
        if value is not None and 'far-clip' not in already_processed:
            already_processed.add('far-clip')
            value = self.gds_parse_double(value, node, 'far-clip')
            self.far_clip = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
# end class CameraPosType


class CaveCameraPosType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, far_clip=100, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.far_clip = _cast(float, far_clip)
        self.far_clip_nsprefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CaveCameraPosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CaveCameraPosType.subclass:
            return CaveCameraPosType.subclass(*args_, **kwargs_)
        else:
            return CaveCameraPosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def get_far_clip(self):
        return self.far_clip
    def set_far_clip(self, far_clip):
        self.far_clip = far_clip
    def _hasContent(self):
        if (
            self.Placement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CaveCameraPosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CaveCameraPosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CaveCameraPosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CaveCameraPosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CaveCameraPosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CaveCameraPosType'):
        if self.far_clip != 100 and 'far_clip' not in already_processed:
            already_processed.add('far_clip')
            outfile.write(' far-clip="%s"' % self.gds_format_double(self.far_clip, input_name='far-clip'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CaveCameraPosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('far-clip', node)
        if value is not None and 'far-clip' not in already_processed:
            already_processed.add('far-clip')
            value = self.gds_parse_double(value, node, 'far-clip')
            self.far_clip = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
# end class CaveCameraPosType


class BackgroundType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, color='0, 0, 0', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.color = _cast(None, color)
        self.color_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BackgroundType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BackgroundType.subclass:
            return BackgroundType.subclass(*args_, **kwargs_)
        else:
            return BackgroundType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    def validate_color(self, value):
        # Validate type color, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BackgroundType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BackgroundType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BackgroundType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BackgroundType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BackgroundType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BackgroundType'):
        if self.color != "0, 0, 0" and 'color' not in already_processed:
            already_processed.add('color')
            outfile.write(' color=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.color), input_name='color')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BackgroundType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('color', node)
        if value is not None and 'color' not in already_processed:
            already_processed.add('color')
            self.color = value
            self.validate_color(self.color)    # validate type color
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class BackgroundType


class WandNavigationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, allow_rotation=False, allow_movement=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.allow_rotation = _cast(bool, allow_rotation)
        self.allow_rotation_nsprefix_ = None
        self.allow_movement = _cast(bool, allow_movement)
        self.allow_movement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WandNavigationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WandNavigationType.subclass:
            return WandNavigationType.subclass(*args_, **kwargs_)
        else:
            return WandNavigationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_allow_rotation(self):
        return self.allow_rotation
    def set_allow_rotation(self, allow_rotation):
        self.allow_rotation = allow_rotation
    def get_allow_movement(self):
        return self.allow_movement
    def set_allow_movement(self, allow_movement):
        self.allow_movement = allow_movement
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='WandNavigationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WandNavigationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WandNavigationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WandNavigationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WandNavigationType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WandNavigationType'):
        if self.allow_rotation and 'allow_rotation' not in already_processed:
            already_processed.add('allow_rotation')
            outfile.write(' allow-rotation="%s"' % self.gds_format_boolean(self.allow_rotation, input_name='allow-rotation'))
        if self.allow_movement and 'allow_movement' not in already_processed:
            already_processed.add('allow_movement')
            outfile.write(' allow-movement="%s"' % self.gds_format_boolean(self.allow_movement, input_name='allow-movement'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='WandNavigationType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('allow-rotation', node)
        if value is not None and 'allow-rotation' not in already_processed:
            already_processed.add('allow-rotation')
            if value in ('true', '1'):
                self.allow_rotation = True
            elif value in ('false', '0'):
                self.allow_rotation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('allow-movement', node)
        if value is not None and 'allow-movement' not in already_processed:
            already_processed.add('allow-movement')
            if value in ('true', '1'):
                self.allow_movement = True
            elif value in ('false', '0'):
                self.allow_movement = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class WandNavigationType


class AboutType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, news=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.news = _cast(None, news)
        self.news_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AboutType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AboutType.subclass:
            return AboutType.subclass(*args_, **kwargs_)
        else:
            return AboutType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_news(self):
        return self.news
    def set_news(self, news):
        self.news = news
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AboutType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AboutType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AboutType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AboutType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AboutType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AboutType'):
        if self.news is not None and 'news' not in already_processed:
            already_processed.add('news')
            outfile.write(' news=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.news), input_name='news')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AboutType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('news', node)
        if value is not None and 'news' not in already_processed:
            already_processed.add('news')
            self.news = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AboutType


class LinkRootType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Link = Link
        self.Link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LinkRootType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LinkRootType.subclass:
            return LinkRootType.subclass(*args_, **kwargs_)
        else:
            return LinkRootType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Link(self):
        return self.Link
    def set_Link(self, Link):
        self.Link = Link
    def _hasContent(self):
        if (
            self.Link is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkRootType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LinkRootType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LinkRootType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LinkRootType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LinkRootType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LinkRootType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkRootType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Link is not None:
            namespaceprefix_ = self.Link_nsprefix_ + ':' if (UseCapturedNS_ and self.Link_nsprefix_) else ''
            self.Link.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Link', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Link':
            obj_ = Link.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Link = obj_
            obj_.original_tagname_ = 'Link'
# end class LinkRootType


class NoneType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NoneType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NoneType.subclass:
            return NoneType.subclass(*args_, **kwargs_)
        else:
            return NoneType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoneType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NoneType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NoneType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NoneType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NoneType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NoneType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoneType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NoneType


class TextType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, horiz_align='center', vert_align='center', font=None, depth=0.0, text=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.horiz_align = _cast(None, horiz_align)
        self.horiz_align_nsprefix_ = None
        self.vert_align = _cast(None, vert_align)
        self.vert_align_nsprefix_ = None
        self.font = _cast(None, font)
        self.font_nsprefix_ = None
        self.depth = _cast(float, depth)
        self.depth_nsprefix_ = None
        self.text = text
        self.text_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextType.subclass:
            return TextType.subclass(*args_, **kwargs_)
        else:
            return TextType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
    def get_horiz_align(self):
        return self.horiz_align
    def set_horiz_align(self, horiz_align):
        self.horiz_align = horiz_align
    def get_vert_align(self):
        return self.vert_align
    def set_vert_align(self, vert_align):
        self.vert_align = vert_align
    def get_font(self):
        return self.font
    def set_font(self, font):
        self.font = font
    def get_depth(self):
        return self.depth
    def set_depth(self, depth):
        self.depth = depth
    def validate_horiz_alignType(self, value):
        # Validate type horiz-alignType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left', 'center', 'right']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on horiz-alignType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_vert_alignType(self, value):
        # Validate type vert-alignType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['top', 'center', 'bottom']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on vert-alignType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.text is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TextType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextType'):
        if self.horiz_align != "center" and 'horiz_align' not in already_processed:
            already_processed.add('horiz_align')
            outfile.write(' horiz-align=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.horiz_align), input_name='horiz-align')), ))
        if self.vert_align != "center" and 'vert_align' not in already_processed:
            already_processed.add('vert_align')
            outfile.write(' vert-align=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.vert_align), input_name='vert-align')), ))
        if self.font is not None and 'font' not in already_processed:
            already_processed.add('font')
            outfile.write(' font=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.font), input_name='font')), ))
        if self.depth != 0.0 and 'depth' not in already_processed:
            already_processed.add('depth')
            outfile.write(' depth="%s"' % self.gds_format_float(self.depth, input_name='depth'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TextType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.text is not None:
            namespaceprefix_ = self.text_nsprefix_ + ':' if (UseCapturedNS_ and self.text_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stext>%s</%stext>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.text), input_name='text')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('horiz-align', node)
        if value is not None and 'horiz-align' not in already_processed:
            already_processed.add('horiz-align')
            self.horiz_align = value
            self.validate_horiz_alignType(self.horiz_align)    # validate type horiz-alignType
        value = find_attr_value_('vert-align', node)
        if value is not None and 'vert-align' not in already_processed:
            already_processed.add('vert-align')
            self.vert_align = value
            self.validate_vert_alignType(self.vert_align)    # validate type vert-alignType
        value = find_attr_value_('font', node)
        if value is not None and 'font' not in already_processed:
            already_processed.add('font')
            self.font = value
        value = find_attr_value_('depth', node)
        if value is not None and 'depth' not in already_processed:
            already_processed.add('depth')
            value = self.gds_parse_float(value, node, 'depth')
            self.depth = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'text':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'text')
            value_ = self.gds_validate_string(value_, node, 'text')
            self.text = value_
            self.text_nsprefix_ = child_.prefix
# end class TextType


class ImageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, filename=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.filename = _cast(None, filename)
        self.filename_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ImageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ImageType.subclass:
            return ImageType.subclass(*args_, **kwargs_)
        else:
            return ImageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def validate_file(self, value):
        # Validate type file, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ImageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ImageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ImageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ImageType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ImageType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ImageType'):
        if self.filename is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            outfile.write(' filename=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.filename), input_name='filename')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ImageType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('filename', node)
        if value is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            self.filename = value
            self.validate_file(self.filename)    # validate type file
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ImageType


class StereoImageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, left_image=None, right_image=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.left_image = _cast(None, left_image)
        self.left_image_nsprefix_ = None
        self.right_image = _cast(None, right_image)
        self.right_image_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StereoImageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StereoImageType.subclass:
            return StereoImageType.subclass(*args_, **kwargs_)
        else:
            return StereoImageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_left_image(self):
        return self.left_image
    def set_left_image(self, left_image):
        self.left_image = left_image
    def get_right_image(self):
        return self.right_image
    def set_right_image(self, right_image):
        self.right_image = right_image
    def validate_file(self, value):
        # Validate type file, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='StereoImageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StereoImageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StereoImageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StereoImageType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StereoImageType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StereoImageType'):
        if self.left_image is not None and 'left_image' not in already_processed:
            already_processed.add('left_image')
            outfile.write(' left-image=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.left_image), input_name='left-image')), ))
        if self.right_image is not None and 'right_image' not in already_processed:
            already_processed.add('right_image')
            outfile.write(' right-image=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.right_image), input_name='right-image')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='StereoImageType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('left-image', node)
        if value is not None and 'left-image' not in already_processed:
            already_processed.add('left-image')
            self.left_image = value
            self.validate_file(self.left_image)    # validate type file
        value = find_attr_value_('right-image', node)
        if value is not None and 'right-image' not in already_processed:
            already_processed.add('right-image')
            self.right_image = value
            self.validate_file(self.right_image)    # validate type file
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StereoImageType


class ModelType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, filename=None, check_collisions=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.filename = _cast(None, filename)
        self.filename_nsprefix_ = None
        self.check_collisions = _cast(bool, check_collisions)
        self.check_collisions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ModelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ModelType.subclass:
            return ModelType.subclass(*args_, **kwargs_)
        else:
            return ModelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def get_check_collisions(self):
        return self.check_collisions
    def set_check_collisions(self, check_collisions):
        self.check_collisions = check_collisions
    def validate_file(self, value):
        # Validate type file, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ModelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ModelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ModelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ModelType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ModelType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ModelType'):
        if self.filename is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            outfile.write(' filename=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.filename), input_name='filename')), ))
        if self.check_collisions and 'check_collisions' not in already_processed:
            already_processed.add('check_collisions')
            outfile.write(' check-collisions="%s"' % self.gds_format_boolean(self.check_collisions, input_name='check-collisions'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ModelType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('filename', node)
        if value is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            self.filename = value
            self.validate_file(self.filename)    # validate type file
        value = find_attr_value_('check-collisions', node)
        if value is not None and 'check-collisions' not in already_processed:
            already_processed.add('check-collisions')
            if value in ('true', '1'):
                self.check_collisions = True
            elif value in ('false', '0'):
                self.check_collisions = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ModelType


class LightType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diffuse=True, specular=True, const_atten=1.0, lin_atten=0.0, quad_atten=0.0, Point=None, Directional=None, Spot=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diffuse = _cast(bool, diffuse)
        self.diffuse_nsprefix_ = None
        self.specular = _cast(bool, specular)
        self.specular_nsprefix_ = None
        self.const_atten = _cast(float, const_atten)
        self.const_atten_nsprefix_ = None
        self.lin_atten = _cast(float, lin_atten)
        self.lin_atten_nsprefix_ = None
        self.quad_atten = _cast(float, quad_atten)
        self.quad_atten_nsprefix_ = None
        self.Point = Point
        self.Point_nsprefix_ = None
        self.Directional = Directional
        self.Directional_nsprefix_ = None
        self.Spot = Spot
        self.Spot_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LightType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LightType.subclass:
            return LightType.subclass(*args_, **kwargs_)
        else:
            return LightType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Point(self):
        return self.Point
    def set_Point(self, Point):
        self.Point = Point
    def get_Directional(self):
        return self.Directional
    def set_Directional(self, Directional):
        self.Directional = Directional
    def get_Spot(self):
        return self.Spot
    def set_Spot(self, Spot):
        self.Spot = Spot
    def get_diffuse(self):
        return self.diffuse
    def set_diffuse(self, diffuse):
        self.diffuse = diffuse
    def get_specular(self):
        return self.specular
    def set_specular(self, specular):
        self.specular = specular
    def get_const_atten(self):
        return self.const_atten
    def set_const_atten(self, const_atten):
        self.const_atten = const_atten
    def get_lin_atten(self):
        return self.lin_atten
    def set_lin_atten(self, lin_atten):
        self.lin_atten = lin_atten
    def get_quad_atten(self):
        return self.quad_atten
    def set_quad_atten(self, quad_atten):
        self.quad_atten = quad_atten
    def _hasContent(self):
        if (
            self.Point is not None or
            self.Directional is not None or
            self.Spot is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LightType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LightType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LightType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LightType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LightType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LightType'):
        if not self.diffuse and 'diffuse' not in already_processed:
            already_processed.add('diffuse')
            outfile.write(' diffuse="%s"' % self.gds_format_boolean(self.diffuse, input_name='diffuse'))
        if not self.specular and 'specular' not in already_processed:
            already_processed.add('specular')
            outfile.write(' specular="%s"' % self.gds_format_boolean(self.specular, input_name='specular'))
        if self.const_atten != 1.0 and 'const_atten' not in already_processed:
            already_processed.add('const_atten')
            outfile.write(' const_atten="%s"' % self.gds_format_float(self.const_atten, input_name='const_atten'))
        if self.lin_atten != 0.0 and 'lin_atten' not in already_processed:
            already_processed.add('lin_atten')
            outfile.write(' lin_atten="%s"' % self.gds_format_float(self.lin_atten, input_name='lin_atten'))
        if self.quad_atten != 0.0 and 'quad_atten' not in already_processed:
            already_processed.add('quad_atten')
            outfile.write(' quad_atten="%s"' % self.gds_format_float(self.quad_atten, input_name='quad_atten'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LightType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Point is not None:
            namespaceprefix_ = self.Point_nsprefix_ + ':' if (UseCapturedNS_ and self.Point_nsprefix_) else ''
            self.Point.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Point', pretty_print=pretty_print)
        if self.Directional is not None:
            namespaceprefix_ = self.Directional_nsprefix_ + ':' if (UseCapturedNS_ and self.Directional_nsprefix_) else ''
            self.Directional.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Directional', pretty_print=pretty_print)
        if self.Spot is not None:
            namespaceprefix_ = self.Spot_nsprefix_ + ':' if (UseCapturedNS_ and self.Spot_nsprefix_) else ''
            self.Spot.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Spot', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('diffuse', node)
        if value is not None and 'diffuse' not in already_processed:
            already_processed.add('diffuse')
            if value in ('true', '1'):
                self.diffuse = True
            elif value in ('false', '0'):
                self.diffuse = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('specular', node)
        if value is not None and 'specular' not in already_processed:
            already_processed.add('specular')
            if value in ('true', '1'):
                self.specular = True
            elif value in ('false', '0'):
                self.specular = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('const_atten', node)
        if value is not None and 'const_atten' not in already_processed:
            already_processed.add('const_atten')
            value = self.gds_parse_float(value, node, 'const_atten')
            self.const_atten = value
        value = find_attr_value_('lin_atten', node)
        if value is not None and 'lin_atten' not in already_processed:
            already_processed.add('lin_atten')
            value = self.gds_parse_float(value, node, 'lin_atten')
            self.lin_atten = value
        value = find_attr_value_('quad_atten', node)
        if value is not None and 'quad_atten' not in already_processed:
            already_processed.add('quad_atten')
            value = self.gds_parse_float(value, node, 'quad_atten')
            self.quad_atten = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Point':
            obj_ = PointType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Point = obj_
            obj_.original_tagname_ = 'Point'
        elif nodeName_ == 'Directional':
            obj_ = DirectionalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Directional = obj_
            obj_.original_tagname_ = 'Directional'
        elif nodeName_ == 'Spot':
            obj_ = SpotType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Spot = obj_
            obj_.original_tagname_ = 'Spot'
# end class LightType


class PointType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PointType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PointType.subclass:
            return PointType.subclass(*args_, **kwargs_)
        else:
            return PointType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PointType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PointType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PointType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PointType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PointType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PointType


class DirectionalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DirectionalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DirectionalType.subclass:
            return DirectionalType.subclass(*args_, **kwargs_)
        else:
            return DirectionalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DirectionalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DirectionalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DirectionalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DirectionalType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DirectionalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionalType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DirectionalType


class SpotType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, angle=30.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.angle = _cast(float, angle)
        self.angle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SpotType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SpotType.subclass:
            return SpotType.subclass(*args_, **kwargs_)
        else:
            return SpotType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_angle(self):
        return self.angle
    def set_angle(self, angle):
        self.angle = angle
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpotType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SpotType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SpotType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SpotType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SpotType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SpotType'):
        if self.angle != 30.0 and 'angle' not in already_processed:
            already_processed.add('angle')
            outfile.write(' angle="%s"' % self.gds_format_float(self.angle, input_name='angle'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SpotType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('angle', node)
        if value is not None and 'angle' not in already_processed:
            already_processed.add('angle')
            value = self.gds_parse_float(value, node, 'angle')
            self.angle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SpotType


class ParticleSystemType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, max_particles=1000, actions_name=None, particle_group=None, look_at_camera=False, sequential=False, speed=1.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.max_particles = _cast(int, max_particles)
        self.max_particles_nsprefix_ = None
        self.actions_name = _cast(None, actions_name)
        self.actions_name_nsprefix_ = None
        self.particle_group = _cast(None, particle_group)
        self.particle_group_nsprefix_ = None
        self.look_at_camera = _cast(bool, look_at_camera)
        self.look_at_camera_nsprefix_ = None
        self.sequential = _cast(bool, sequential)
        self.sequential_nsprefix_ = None
        self.speed = _cast(float, speed)
        self.speed_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticleSystemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticleSystemType.subclass:
            return ParticleSystemType.subclass(*args_, **kwargs_)
        else:
            return ParticleSystemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_max_particles(self):
        return self.max_particles
    def set_max_particles(self, max_particles):
        self.max_particles = max_particles
    def get_actions_name(self):
        return self.actions_name
    def set_actions_name(self, actions_name):
        self.actions_name = actions_name
    def get_particle_group(self):
        return self.particle_group
    def set_particle_group(self, particle_group):
        self.particle_group = particle_group
    def get_look_at_camera(self):
        return self.look_at_camera
    def set_look_at_camera(self, look_at_camera):
        self.look_at_camera = look_at_camera
    def get_sequential(self):
        return self.sequential
    def set_sequential(self, sequential):
        self.sequential = sequential
    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleSystemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticleSystemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticleSystemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticleSystemType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticleSystemType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticleSystemType'):
        if self.max_particles != 1000 and 'max_particles' not in already_processed:
            already_processed.add('max_particles')
            outfile.write(' max-particles="%s"' % self.gds_format_integer(self.max_particles, input_name='max-particles'))
        if self.actions_name is not None and 'actions_name' not in already_processed:
            already_processed.add('actions_name')
            outfile.write(' actions-name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.actions_name), input_name='actions-name')), ))
        if self.particle_group is not None and 'particle_group' not in already_processed:
            already_processed.add('particle_group')
            outfile.write(' particle-group=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.particle_group), input_name='particle-group')), ))
        if self.look_at_camera and 'look_at_camera' not in already_processed:
            already_processed.add('look_at_camera')
            outfile.write(' look-at-camera="%s"' % self.gds_format_boolean(self.look_at_camera, input_name='look-at-camera'))
        if self.sequential and 'sequential' not in already_processed:
            already_processed.add('sequential')
            outfile.write(' sequential="%s"' % self.gds_format_boolean(self.sequential, input_name='sequential'))
        if self.speed != 1.0 and 'speed' not in already_processed:
            already_processed.add('speed')
            outfile.write(' speed="%s"' % self.gds_format_float(self.speed, input_name='speed'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParticleSystemType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('max-particles', node)
        if value is not None and 'max-particles' not in already_processed:
            already_processed.add('max-particles')
            self.max_particles = self.gds_parse_integer(value, node, 'max-particles')
        value = find_attr_value_('actions-name', node)
        if value is not None and 'actions-name' not in already_processed:
            already_processed.add('actions-name')
            self.actions_name = value
        value = find_attr_value_('particle-group', node)
        if value is not None and 'particle-group' not in already_processed:
            already_processed.add('particle-group')
            self.particle_group = value
        value = find_attr_value_('look-at-camera', node)
        if value is not None and 'look-at-camera' not in already_processed:
            already_processed.add('look-at-camera')
            if value in ('true', '1'):
                self.look_at_camera = True
            elif value in ('false', '0'):
                self.look_at_camera = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('sequential', node)
        if value is not None and 'sequential' not in already_processed:
            already_processed.add('sequential')
            if value in ('true', '1'):
                self.sequential = True
            elif value in ('false', '0'):
                self.sequential = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('speed', node)
        if value is not None and 'speed' not in already_processed:
            already_processed.add('speed')
            value = self.gds_parse_float(value, node, 'speed')
            self.speed = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ParticleSystemType


class ActionsType1(ActionsType):
    """ActionsType1 -- Link Actions Obj
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = ActionsType
    def __init__(self, ObjectChange=None, GroupRef=None, TimerChange=None, SoundRef=None, Event=None, MoveCave=None, Restart=None, Clicks=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ActionsType1"), self).__init__(ObjectChange, GroupRef, TimerChange, SoundRef, Event, MoveCave, Restart,  **kwargs_)
        self.Clicks = Clicks
        self.Clicks_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ActionsType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ActionsType1.subclass:
            return ActionsType1.subclass(*args_, **kwargs_)
        else:
            return ActionsType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Clicks(self):
        return self.Clicks
    def set_Clicks(self, Clicks):
        self.Clicks = Clicks
    def _hasContent(self):
        if (
            self.Clicks is not None or
            super(ActionsType1, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ActionsType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ActionsType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ActionsType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ActionsType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ActionsType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ActionsType1'):
        super(ActionsType1, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ActionsType1')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ActionsType1', fromsubclass_=False, pretty_print=True):
        super(ActionsType1, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Clicks is not None:
            namespaceprefix_ = self.Clicks_nsprefix_ + ':' if (UseCapturedNS_ and self.Clicks_nsprefix_) else ''
            self.Clicks.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Clicks', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ActionsType1, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Clicks':
            obj_ = ClicksType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Clicks = obj_
            obj_.original_tagname_ = 'Clicks'
        super(ActionsType1, self)._buildChildren(child_, node, nodeName_, True)
# end class ActionsType1


class ClicksType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Any=None, NumClicks=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Any = Any
        self.Any_nsprefix_ = None
        self.NumClicks = NumClicks
        self.NumClicks_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ClicksType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ClicksType.subclass:
            return ClicksType.subclass(*args_, **kwargs_)
        else:
            return ClicksType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Any(self):
        return self.Any
    def set_Any(self, Any):
        self.Any = Any
    def get_NumClicks(self):
        return self.NumClicks
    def set_NumClicks(self, NumClicks):
        self.NumClicks = NumClicks
    def _hasContent(self):
        if (
            self.Any is not None or
            self.NumClicks is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ClicksType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ClicksType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ClicksType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ClicksType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ClicksType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ClicksType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ClicksType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Any is not None:
            namespaceprefix_ = self.Any_nsprefix_ + ':' if (UseCapturedNS_ and self.Any_nsprefix_) else ''
            self.Any.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Any', pretty_print=pretty_print)
        if self.NumClicks is not None:
            namespaceprefix_ = self.NumClicks_nsprefix_ + ':' if (UseCapturedNS_ and self.NumClicks_nsprefix_) else ''
            self.NumClicks.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NumClicks', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Any':
            obj_ = AnyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Any = obj_
            obj_.original_tagname_ = 'Any'
        elif nodeName_ == 'NumClicks':
            obj_ = NumClicksType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NumClicks = obj_
            obj_.original_tagname_ = 'NumClicks'
# end class ClicksType


class AnyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnyType.subclass:
            return AnyType.subclass(*args_, **kwargs_)
        else:
            return AnyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnyType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnyType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnyType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnyType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AnyType


class NumClicksType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, num_clicks=1, reset=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.num_clicks = _cast(int, num_clicks)
        self.num_clicks_nsprefix_ = None
        self.reset = _cast(bool, reset)
        self.reset_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NumClicksType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NumClicksType.subclass:
            return NumClicksType.subclass(*args_, **kwargs_)
        else:
            return NumClicksType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_num_clicks(self):
        return self.num_clicks
    def set_num_clicks(self, num_clicks):
        self.num_clicks = num_clicks
    def get_reset(self):
        return self.reset
    def set_reset(self, reset):
        self.reset = reset
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NumClicksType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NumClicksType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NumClicksType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NumClicksType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NumClicksType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NumClicksType'):
        if self.num_clicks != 1 and 'num_clicks' not in already_processed:
            already_processed.add('num_clicks')
            outfile.write(' num_clicks="%s"' % self.gds_format_integer(self.num_clicks, input_name='num_clicks'))
        if self.reset and 'reset' not in already_processed:
            already_processed.add('reset')
            outfile.write(' reset="%s"' % self.gds_format_boolean(self.reset, input_name='reset'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NumClicksType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('num_clicks', node)
        if value is not None and 'num_clicks' not in already_processed:
            already_processed.add('num_clicks')
            self.num_clicks = self.gds_parse_integer(value, node, 'num_clicks')
        value = find_attr_value_('reset', node)
        if value is not None and 'reset' not in already_processed:
            already_processed.add('reset')
            if value in ('true', '1'):
                self.reset = True
            elif value in ('false', '0'):
                self.reset = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NumClicksType


class TimedActionsType(ActionsType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = ActionsType
    def __init__(self, ObjectChange=None, GroupRef=None, TimerChange=None, SoundRef=None, Event=None, MoveCave=None, Restart=None, seconds_time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("TimedActionsType"), self).__init__(ObjectChange, GroupRef, TimerChange, SoundRef, Event, MoveCave, Restart,  **kwargs_)
        self.seconds_time = _cast(None, seconds_time)
        self.seconds_time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimedActionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimedActionsType.subclass:
            return TimedActionsType.subclass(*args_, **kwargs_)
        else:
            return TimedActionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_seconds_time(self):
        return self.seconds_time
    def set_seconds_time(self, seconds_time):
        self.seconds_time = seconds_time
    def _hasContent(self):
        if (
            super(TimedActionsType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimedActionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimedActionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimedActionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimedActionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimedActionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimedActionsType'):
        super(TimedActionsType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimedActionsType')
        if self.seconds_time is not None and 'seconds_time' not in already_processed:
            already_processed.add('seconds_time')
            outfile.write(' seconds-time=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.seconds_time), input_name='seconds-time')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimedActionsType', fromsubclass_=False, pretty_print=True):
        super(TimedActionsType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('seconds-time', node)
        if value is not None and 'seconds-time' not in already_processed:
            already_processed.add('seconds-time')
            self.seconds_time = value
        super(TimedActionsType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(TimedActionsType, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class TimedActionsType


class MoveCaveType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, duration=0.0, Relative=None, Absolute=None, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.duration = _cast(float, duration)
        self.duration_nsprefix_ = None
        self.Relative = Relative
        self.Relative_nsprefix_ = None
        self.Absolute = Absolute
        self.Absolute_nsprefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MoveCaveType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MoveCaveType.subclass:
            return MoveCaveType.subclass(*args_, **kwargs_)
        else:
            return MoveCaveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Relative(self):
        return self.Relative
    def set_Relative(self, Relative):
        self.Relative = Relative
    def get_Absolute(self):
        return self.Absolute
    def set_Absolute(self, Absolute):
        self.Absolute = Absolute
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration
    def _hasContent(self):
        if (
            self.Relative is not None or
            self.Absolute is not None or
            self.Placement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveCaveType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MoveCaveType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MoveCaveType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MoveCaveType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MoveCaveType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MoveCaveType'):
        if self.duration != 0.0 and 'duration' not in already_processed:
            already_processed.add('duration')
            outfile.write(' duration="%s"' % self.gds_format_double(self.duration, input_name='duration'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveCaveType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Relative is not None:
            namespaceprefix_ = self.Relative_nsprefix_ + ':' if (UseCapturedNS_ and self.Relative_nsprefix_) else ''
            self.Relative.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relative', pretty_print=pretty_print)
        if self.Absolute is not None:
            namespaceprefix_ = self.Absolute_nsprefix_ + ':' if (UseCapturedNS_ and self.Absolute_nsprefix_) else ''
            self.Absolute.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Absolute', pretty_print=pretty_print)
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('duration', node)
        if value is not None and 'duration' not in already_processed:
            already_processed.add('duration')
            value = self.gds_parse_double(value, node, 'duration')
            self.duration = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Relative':
            obj_ = RelativeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relative = obj_
            obj_.original_tagname_ = 'Relative'
        elif nodeName_ == 'Absolute':
            obj_ = AbsoluteType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Absolute = obj_
            obj_.original_tagname_ = 'Absolute'
        elif nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
# end class MoveCaveType


class RelativeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelativeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelativeType.subclass:
            return RelativeType.subclass(*args_, **kwargs_)
        else:
            return RelativeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RelativeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelativeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelativeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelativeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelativeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelativeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RelativeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RelativeType


class AbsoluteType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AbsoluteType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AbsoluteType.subclass:
            return AbsoluteType.subclass(*args_, **kwargs_)
        else:
            return AbsoluteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AbsoluteType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AbsoluteType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AbsoluteType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AbsoluteType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AbsoluteType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AbsoluteType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AbsoluteType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AbsoluteType


class RestartType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RestartType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RestartType.subclass:
            return RestartType.subclass(*args_, **kwargs_)
        else:
            return RestartType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RestartType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RestartType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RestartType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RestartType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RestartType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RestartType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RestartType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RestartType


class startType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, startType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if startType.subclass:
            return startType.subclass(*args_, **kwargs_)
        else:
            return startType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='startType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('startType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'startType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='startType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='startType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='startType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='startType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class startType


class stopType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, stopType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if stopType.subclass:
            return stopType.subclass(*args_, **kwargs_)
        else:
            return stopType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='stopType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('stopType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'stopType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='stopType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='stopType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='stopType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='stopType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class stopType


class continueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, continueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if continueType.subclass:
            return continueType.subclass(*args_, **kwargs_)
        else:
            return continueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='continueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('continueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'continueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='continueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='continueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='continueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='continueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class continueType


class start_if_not_startedType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, start_if_not_startedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if start_if_not_startedType.subclass:
            return start_if_not_startedType.subclass(*args_, **kwargs_)
        else:
            return start_if_not_startedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='start_if_not_startedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('start_if_not_startedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'start_if_not_startedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='start_if_not_startedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='start_if_not_startedType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='start_if_not_startedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='start_if_not_startedType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class start_if_not_startedType


class ModeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Positional=None, Fixed=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Positional = Positional
        self.Positional_nsprefix_ = None
        self.Fixed = Fixed
        self.Fixed_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ModeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ModeType.subclass:
            return ModeType.subclass(*args_, **kwargs_)
        else:
            return ModeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Positional(self):
        return self.Positional
    def set_Positional(self, Positional):
        self.Positional = Positional
    def get_Fixed(self):
        return self.Fixed
    def set_Fixed(self, Fixed):
        self.Fixed = Fixed
    def _hasContent(self):
        if (
            self.Positional is not None or
            self.Fixed is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ModeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ModeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ModeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ModeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ModeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ModeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ModeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Positional is not None:
            namespaceprefix_ = self.Positional_nsprefix_ + ':' if (UseCapturedNS_ and self.Positional_nsprefix_) else ''
            self.Positional.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Positional', pretty_print=pretty_print)
        if self.Fixed is not None:
            namespaceprefix_ = self.Fixed_nsprefix_ + ':' if (UseCapturedNS_ and self.Fixed_nsprefix_) else ''
            self.Fixed.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Fixed', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Positional':
            obj_ = PositionalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Positional = obj_
            obj_.original_tagname_ = 'Positional'
        elif nodeName_ == 'Fixed':
            obj_ = FixedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Fixed = obj_
            obj_.original_tagname_ = 'Fixed'
# end class ModeType


class PositionalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PositionalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PositionalType.subclass:
            return PositionalType.subclass(*args_, **kwargs_)
        else:
            return PositionalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PositionalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PositionalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PositionalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PositionalType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PositionalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionalType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PositionalType


class FixedType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FixedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FixedType.subclass:
            return FixedType.subclass(*args_, **kwargs_)
        else:
            return FixedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FixedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FixedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FixedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FixedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FixedType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FixedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FixedType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class FixedType


class RepeatType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NoRepeat=None, RepeatForever=None, RepeatNum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.NoRepeat = NoRepeat
        self.NoRepeat_nsprefix_ = None
        self.RepeatForever = RepeatForever
        self.RepeatForever_nsprefix_ = None
        self.RepeatNum = RepeatNum
        self.validate_RepeatNumType(self.RepeatNum)
        self.RepeatNum_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RepeatType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RepeatType.subclass:
            return RepeatType.subclass(*args_, **kwargs_)
        else:
            return RepeatType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NoRepeat(self):
        return self.NoRepeat
    def set_NoRepeat(self, NoRepeat):
        self.NoRepeat = NoRepeat
    def get_RepeatForever(self):
        return self.RepeatForever
    def set_RepeatForever(self, RepeatForever):
        self.RepeatForever = RepeatForever
    def get_RepeatNum(self):
        return self.RepeatNum
    def set_RepeatNum(self, RepeatNum):
        self.RepeatNum = RepeatNum
    def validate_RepeatNumType(self, value):
        result = True
        # Validate type RepeatNumType, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RepeatNumType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.NoRepeat is not None or
            self.RepeatForever is not None or
            self.RepeatNum is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RepeatType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RepeatType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RepeatType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RepeatType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RepeatType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RepeatType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RepeatType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NoRepeat is not None:
            namespaceprefix_ = self.NoRepeat_nsprefix_ + ':' if (UseCapturedNS_ and self.NoRepeat_nsprefix_) else ''
            self.NoRepeat.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NoRepeat', pretty_print=pretty_print)
        if self.RepeatForever is not None:
            namespaceprefix_ = self.RepeatForever_nsprefix_ + ':' if (UseCapturedNS_ and self.RepeatForever_nsprefix_) else ''
            self.RepeatForever.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RepeatForever', pretty_print=pretty_print)
        if self.RepeatNum is not None:
            namespaceprefix_ = self.RepeatNum_nsprefix_ + ':' if (UseCapturedNS_ and self.RepeatNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRepeatNum>%s</%sRepeatNum>%s' % (namespaceprefix_ , self.gds_format_integer(self.RepeatNum, input_name='RepeatNum'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NoRepeat':
            obj_ = NoRepeatType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NoRepeat = obj_
            obj_.original_tagname_ = 'NoRepeat'
        elif nodeName_ == 'RepeatForever':
            obj_ = RepeatForeverType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RepeatForever = obj_
            obj_.original_tagname_ = 'RepeatForever'
        elif nodeName_ == 'RepeatNum' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'RepeatNum')
            ival_ = self.gds_validate_integer(ival_, node, 'RepeatNum')
            self.RepeatNum = ival_
            self.RepeatNum_nsprefix_ = child_.prefix
            # validate type RepeatNumType
            self.validate_RepeatNumType(self.RepeatNum)
# end class RepeatType


class NoRepeatType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NoRepeatType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NoRepeatType.subclass:
            return NoRepeatType.subclass(*args_, **kwargs_)
        else:
            return NoRepeatType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoRepeatType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NoRepeatType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NoRepeatType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NoRepeatType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NoRepeatType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NoRepeatType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoRepeatType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NoRepeatType


class RepeatForeverType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RepeatForeverType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RepeatForeverType.subclass:
            return RepeatForeverType.subclass(*args_, **kwargs_)
        else:
            return RepeatForeverType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RepeatForeverType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RepeatForeverType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RepeatForeverType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RepeatForeverType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RepeatForeverType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RepeatForeverType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RepeatForeverType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RepeatForeverType


class SettingsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, freq='1.0', volume='1.0', pan='0.0', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.freq = _cast(float, freq)
        self.freq_nsprefix_ = None
        self.volume = _cast(float, volume)
        self.volume_nsprefix_ = None
        self.pan = _cast(float, pan)
        self.pan_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SettingsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SettingsType.subclass:
            return SettingsType.subclass(*args_, **kwargs_)
        else:
            return SettingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_freq(self):
        return self.freq
    def set_freq(self, freq):
        self.freq = freq
    def get_volume(self):
        return self.volume
    def set_volume(self, volume):
        self.volume = volume
    def get_pan(self):
        return self.pan
    def set_pan(self, pan):
        self.pan = pan
    def validate_freqType(self, value):
        # Validate type freqType, a restriction on xs:float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on freqType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_volumeType(self, value):
        # Validate type volumeType, a restriction on xs:float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on volumeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on volumeType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_panType(self, value):
        # Validate type panType, a restriction on xs:float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < -1.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on panType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1.0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on panType' % {"value": value, "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SettingsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SettingsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SettingsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SettingsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SettingsType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SettingsType'):
        if self.freq != 1.0 and 'freq' not in already_processed:
            already_processed.add('freq')
            outfile.write(' freq="%s"' % self.gds_format_float(self.freq, input_name='freq'))
        if self.volume != 1.0 and 'volume' not in already_processed:
            already_processed.add('volume')
            outfile.write(' volume="%s"' % self.gds_format_float(self.volume, input_name='volume'))
        if self.pan != 0.0 and 'pan' not in already_processed:
            already_processed.add('pan')
            outfile.write(' pan="%s"' % self.gds_format_float(self.pan, input_name='pan'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SettingsType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('freq', node)
        if value is not None and 'freq' not in already_processed:
            already_processed.add('freq')
            value = self.gds_parse_float(value, node, 'freq')
            self.freq = value
            self.validate_freqType(self.freq)    # validate type freqType
        value = find_attr_value_('volume', node)
        if value is not None and 'volume' not in already_processed:
            already_processed.add('volume')
            value = self.gds_parse_float(value, node, 'volume')
            self.volume = value
            self.validate_volumeType(self.volume)    # validate type volumeType
        value = find_attr_value_('pan', node)
        if value is not None and 'pan' not in already_processed:
            already_processed.add('pan')
            value = self.gds_parse_float(value, node, 'pan')
            self.pan = value
            self.validate_panType(self.pan)    # validate type panType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SettingsType


class HeadTrackType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Direction=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = Position
        self.Position_nsprefix_ = None
        self.Direction = Direction
        self.Direction_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, HeadTrackType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if HeadTrackType.subclass:
            return HeadTrackType.subclass(*args_, **kwargs_)
        else:
            return HeadTrackType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_Direction(self):
        return self.Direction
    def set_Direction(self, Direction):
        self.Direction = Direction
    def _hasContent(self):
        if (
            self.Position is not None or
            self.Direction is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='HeadTrackType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('HeadTrackType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'HeadTrackType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='HeadTrackType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='HeadTrackType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='HeadTrackType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='HeadTrackType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Position is not None:
            namespaceprefix_ = self.Position_nsprefix_ + ':' if (UseCapturedNS_ and self.Position_nsprefix_) else ''
            self.Position.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Position', pretty_print=pretty_print)
        if self.Direction is not None:
            namespaceprefix_ = self.Direction_nsprefix_ + ':' if (UseCapturedNS_ and self.Direction_nsprefix_) else ''
            self.Direction.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Direction', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Position':
            obj_ = PositionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Position = obj_
            obj_.original_tagname_ = 'Position'
        elif nodeName_ == 'Direction':
            obj_ = DirectionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Direction = obj_
            obj_.original_tagname_ = 'Direction'
# end class HeadTrackType


class PositionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Anywhere=None, Box=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Anywhere = Anywhere
        self.Anywhere_nsprefix_ = None
        self.Box = Box
        self.Box_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PositionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PositionType.subclass:
            return PositionType.subclass(*args_, **kwargs_)
        else:
            return PositionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Anywhere(self):
        return self.Anywhere
    def set_Anywhere(self, Anywhere):
        self.Anywhere = Anywhere
    def get_Box(self):
        return self.Box
    def set_Box(self, Box):
        self.Box = Box
    def _hasContent(self):
        if (
            self.Anywhere is not None or
            self.Box is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PositionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PositionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PositionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PositionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PositionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Anywhere is not None:
            namespaceprefix_ = self.Anywhere_nsprefix_ + ':' if (UseCapturedNS_ and self.Anywhere_nsprefix_) else ''
            self.Anywhere.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Anywhere', pretty_print=pretty_print)
        if self.Box is not None:
            namespaceprefix_ = self.Box_nsprefix_ + ':' if (UseCapturedNS_ and self.Box_nsprefix_) else ''
            self.Box.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Box', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Anywhere':
            obj_ = AnywhereType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Anywhere = obj_
            obj_.original_tagname_ = 'Anywhere'
        elif nodeName_ == 'Box':
            obj_ = Box.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Box = obj_
            obj_.original_tagname_ = 'Box'
# end class PositionType


class AnywhereType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AnywhereType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AnywhereType.subclass:
            return AnywhereType.subclass(*args_, **kwargs_)
        else:
            return AnywhereType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnywhereType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AnywhereType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AnywhereType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AnywhereType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AnywhereType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AnywhereType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AnywhereType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AnywhereType


class DirectionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PointTarget=None, DirectionTarget=None, ObjectTarget=None, None_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.PointTarget = PointTarget
        self.PointTarget_nsprefix_ = None
        self.DirectionTarget = DirectionTarget
        self.DirectionTarget_nsprefix_ = None
        self.ObjectTarget = ObjectTarget
        self.ObjectTarget_nsprefix_ = None
        self.None_ = None_
        self.None__nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DirectionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DirectionType.subclass:
            return DirectionType.subclass(*args_, **kwargs_)
        else:
            return DirectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PointTarget(self):
        return self.PointTarget
    def set_PointTarget(self, PointTarget):
        self.PointTarget = PointTarget
    def get_DirectionTarget(self):
        return self.DirectionTarget
    def set_DirectionTarget(self, DirectionTarget):
        self.DirectionTarget = DirectionTarget
    def get_ObjectTarget(self):
        return self.ObjectTarget
    def set_ObjectTarget(self, ObjectTarget):
        self.ObjectTarget = ObjectTarget
    def get_None(self):
        return self.None_
    def set_None(self, None_):
        self.None_ = None_
    def _hasContent(self):
        if (
            self.PointTarget is not None or
            self.DirectionTarget is not None or
            self.ObjectTarget is not None or
            self.None_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DirectionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DirectionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DirectionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DirectionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DirectionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PointTarget is not None:
            namespaceprefix_ = self.PointTarget_nsprefix_ + ':' if (UseCapturedNS_ and self.PointTarget_nsprefix_) else ''
            self.PointTarget.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PointTarget', pretty_print=pretty_print)
        if self.DirectionTarget is not None:
            namespaceprefix_ = self.DirectionTarget_nsprefix_ + ':' if (UseCapturedNS_ and self.DirectionTarget_nsprefix_) else ''
            self.DirectionTarget.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DirectionTarget', pretty_print=pretty_print)
        if self.ObjectTarget is not None:
            namespaceprefix_ = self.ObjectTarget_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectTarget_nsprefix_) else ''
            self.ObjectTarget.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectTarget', pretty_print=pretty_print)
        if self.None_ is not None:
            namespaceprefix_ = self.None__nsprefix_ + ':' if (UseCapturedNS_ and self.None__nsprefix_) else ''
            self.None_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='None', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PointTarget':
            obj_ = PointTargetType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PointTarget = obj_
            obj_.original_tagname_ = 'PointTarget'
        elif nodeName_ == 'DirectionTarget':
            obj_ = DirectionTargetType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DirectionTarget = obj_
            obj_.original_tagname_ = 'DirectionTarget'
        elif nodeName_ == 'ObjectTarget':
            obj_ = ObjectTargetType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectTarget = obj_
            obj_.original_tagname_ = 'ObjectTarget'
        elif nodeName_ == 'None':
            obj_ = NoneType2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.None_ = obj_
            obj_.original_tagname_ = 'None'
# end class DirectionType


class PointTargetType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, point=None, angle=30, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.point = _cast(None, point)
        self.point_nsprefix_ = None
        self.angle = _cast(float, angle)
        self.angle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PointTargetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PointTargetType.subclass:
            return PointTargetType.subclass(*args_, **kwargs_)
        else:
            return PointTargetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_point(self):
        return self.point
    def set_point(self, point):
        self.point = point
    def get_angle(self):
        return self.angle
    def set_angle(self, angle):
        self.angle = angle
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointTargetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PointTargetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PointTargetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PointTargetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PointTargetType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PointTargetType'):
        if self.point is not None and 'point' not in already_processed:
            already_processed.add('point')
            outfile.write(' point=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.point), input_name='point')), ))
        if self.angle != 30 and 'angle' not in already_processed:
            already_processed.add('angle')
            outfile.write(' angle="%s"' % self.gds_format_double(self.angle, input_name='angle'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointTargetType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('point', node)
        if value is not None and 'point' not in already_processed:
            already_processed.add('point')
            self.point = value
            self.validate_vector(self.point)    # validate type vector
        value = find_attr_value_('angle', node)
        if value is not None and 'angle' not in already_processed:
            already_processed.add('angle')
            value = self.gds_parse_double(value, node, 'angle')
            self.angle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PointTargetType


class DirectionTargetType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, direction=None, angle=30, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.direction = _cast(None, direction)
        self.direction_nsprefix_ = None
        self.angle = _cast(float, angle)
        self.angle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DirectionTargetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DirectionTargetType.subclass:
            return DirectionTargetType.subclass(*args_, **kwargs_)
        else:
            return DirectionTargetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_angle(self):
        return self.angle
    def set_angle(self, angle):
        self.angle = angle
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionTargetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DirectionTargetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DirectionTargetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DirectionTargetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DirectionTargetType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DirectionTargetType'):
        if self.direction is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            outfile.write(' direction=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.direction), input_name='direction')), ))
        if self.angle != 30 and 'angle' not in already_processed:
            already_processed.add('angle')
            outfile.write(' angle="%s"' % self.gds_format_double(self.angle, input_name='angle'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DirectionTargetType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('direction', node)
        if value is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            self.direction = value
            self.validate_vector(self.direction)    # validate type vector
        value = find_attr_value_('angle', node)
        if value is not None and 'angle' not in already_processed:
            already_processed.add('angle')
            value = self.gds_parse_double(value, node, 'angle')
            self.angle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DirectionTargetType


class ObjectTargetType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectTargetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectTargetType.subclass:
            return ObjectTargetType.subclass(*args_, **kwargs_)
        else:
            return ObjectTargetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectTargetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectTargetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectTargetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectTargetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectTargetType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectTargetType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectTargetType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ObjectTargetType


class NoneType2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NoneType2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NoneType2.subclass:
            return NoneType2.subclass(*args_, **kwargs_)
        else:
            return NoneType2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoneType2', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NoneType2')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NoneType2':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NoneType2')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NoneType2', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NoneType2'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoneType2', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NoneType2


class MoveTrackType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Source=None, Box=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.Box = Box
        self.Box_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MoveTrackType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MoveTrackType.subclass:
            return MoveTrackType.subclass(*args_, **kwargs_)
        else:
            return MoveTrackType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def get_Box(self):
        return self.Box
    def set_Box(self, Box):
        self.Box = Box
    def _hasContent(self):
        if (
            self.Source is not None or
            self.Box is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveTrackType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MoveTrackType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MoveTrackType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MoveTrackType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MoveTrackType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MoveTrackType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveTrackType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Source is not None:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            self.Source.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
        if self.Box is not None:
            namespaceprefix_ = self.Box_nsprefix_ + ':' if (UseCapturedNS_ and self.Box_nsprefix_) else ''
            self.Box.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Box', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Source':
            obj_ = SourceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source = obj_
            obj_.original_tagname_ = 'Source'
        elif nodeName_ == 'Box':
            obj_ = Box.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Box = obj_
            obj_.original_tagname_ = 'Box'
# end class MoveTrackType


class SourceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ObjectRef=None, GroupObj=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ObjectRef = ObjectRef
        self.ObjectRef_nsprefix_ = None
        self.GroupObj = GroupObj
        self.GroupObj_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SourceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SourceType.subclass:
            return SourceType.subclass(*args_, **kwargs_)
        else:
            return SourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ObjectRef(self):
        return self.ObjectRef
    def set_ObjectRef(self, ObjectRef):
        self.ObjectRef = ObjectRef
    def get_GroupObj(self):
        return self.GroupObj
    def set_GroupObj(self, GroupObj):
        self.GroupObj = GroupObj
    def _hasContent(self):
        if (
            self.ObjectRef is not None or
            self.GroupObj is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SourceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SourceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SourceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SourceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SourceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SourceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SourceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ObjectRef is not None:
            namespaceprefix_ = self.ObjectRef_nsprefix_ + ':' if (UseCapturedNS_ and self.ObjectRef_nsprefix_) else ''
            self.ObjectRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ObjectRef', pretty_print=pretty_print)
        if self.GroupObj is not None:
            namespaceprefix_ = self.GroupObj_nsprefix_ + ':' if (UseCapturedNS_ and self.GroupObj_nsprefix_) else ''
            self.GroupObj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GroupObj', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ObjectRef':
            obj_ = ObjectRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ObjectRef = obj_
            obj_.original_tagname_ = 'ObjectRef'
        elif nodeName_ == 'GroupObj':
            obj_ = GroupObjType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GroupObj = obj_
            obj_.original_tagname_ = 'GroupObj'
# end class SourceType


class ObjectRefType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectRefType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectRefType.subclass:
            return ObjectRefType.subclass(*args_, **kwargs_)
        else:
            return ObjectRefType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectRefType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectRefType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectRefType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectRefType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectRefType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ObjectRefType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ObjectRefType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ObjectRefType


class GroupObjType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, objects=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.objects = _cast(None, objects)
        self.objects_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupObjType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupObjType.subclass:
            return GroupObjType.subclass(*args_, **kwargs_)
        else:
            return GroupObjType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_objects(self):
        return self.objects
    def set_objects(self, objects):
        self.objects = objects
    def validate_objectsType(self, value):
        # Validate type objectsType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Any Object', 'All Objects']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on objectsType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupObjType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupObjType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupObjType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupObjType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupObjType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupObjType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.objects is not None and 'objects' not in already_processed:
            already_processed.add('objects')
            outfile.write(' objects=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.objects), input_name='objects')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupObjType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('objects', node)
        if value is not None and 'objects' not in already_processed:
            already_processed.add('objects')
            self.objects = value
            self.validate_objectsType(self.objects)    # validate type objectsType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GroupObjType


class MovementType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Inside=None, Outside=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Inside = Inside
        self.Inside_nsprefix_ = None
        self.Outside = Outside
        self.Outside_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MovementType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MovementType.subclass:
            return MovementType.subclass(*args_, **kwargs_)
        else:
            return MovementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Inside(self):
        return self.Inside
    def set_Inside(self, Inside):
        self.Inside = Inside
    def get_Outside(self):
        return self.Outside
    def set_Outside(self, Outside):
        self.Outside = Outside
    def _hasContent(self):
        if (
            self.Inside is not None or
            self.Outside is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MovementType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MovementType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MovementType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MovementType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MovementType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MovementType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MovementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Inside is not None:
            namespaceprefix_ = self.Inside_nsprefix_ + ':' if (UseCapturedNS_ and self.Inside_nsprefix_) else ''
            self.Inside.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Inside', pretty_print=pretty_print)
        if self.Outside is not None:
            namespaceprefix_ = self.Outside_nsprefix_ + ':' if (UseCapturedNS_ and self.Outside_nsprefix_) else ''
            self.Outside.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Outside', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Inside':
            obj_ = InsideType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Inside = obj_
            obj_.original_tagname_ = 'Inside'
        elif nodeName_ == 'Outside':
            obj_ = OutsideType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Outside = obj_
            obj_.original_tagname_ = 'Outside'
# end class MovementType


class InsideType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InsideType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InsideType.subclass:
            return InsideType.subclass(*args_, **kwargs_)
        else:
            return InsideType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InsideType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InsideType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InsideType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InsideType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InsideType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InsideType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InsideType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InsideType


class OutsideType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OutsideType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OutsideType.subclass:
            return OutsideType.subclass(*args_, **kwargs_)
        else:
            return OutsideType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OutsideType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OutsideType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OutsideType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OutsideType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OutsideType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OutsideType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OutsideType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OutsideType


class SourceType3(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rate=None, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rate = _cast(float, rate)
        self.rate_nsprefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SourceType3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SourceType3.subclass:
            return SourceType3.subclass(*args_, **kwargs_)
        else:
            return SourceType3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_rate(self):
        return self.rate
    def set_rate(self, rate):
        self.rate = rate
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SourceType3', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SourceType3')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SourceType3':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SourceType3')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SourceType3', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SourceType3'):
        if self.rate is not None and 'rate' not in already_processed:
            already_processed.add('rate')
            outfile.write(' rate="%s"' % self.gds_format_double(self.rate, input_name='rate'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SourceType3', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rate', node)
        if value is not None and 'rate' not in already_processed:
            already_processed.add('rate')
            value = self.gds_parse_double(value, node, 'rate')
            self.rate = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class SourceType3


class VelType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VelType.subclass:
            return VelType.subclass(*args_, **kwargs_)
        else:
            return VelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='VelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VelType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VelType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VelType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='VelType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class VelType


class RemoveConditionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Age=None, Position=None, Velocity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Age = Age
        self.Age_nsprefix_ = None
        self.Position = Position
        self.Position_nsprefix_ = None
        self.Velocity = Velocity
        self.Velocity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RemoveConditionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RemoveConditionType.subclass:
            return RemoveConditionType.subclass(*args_, **kwargs_)
        else:
            return RemoveConditionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Age(self):
        return self.Age
    def set_Age(self, Age):
        self.Age = Age
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_Velocity(self):
        return self.Velocity
    def set_Velocity(self, Velocity):
        self.Velocity = Velocity
    def _hasContent(self):
        if (
            self.Age is not None or
            self.Position is not None or
            self.Velocity is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RemoveConditionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RemoveConditionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RemoveConditionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RemoveConditionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RemoveConditionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RemoveConditionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RemoveConditionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Age is not None:
            namespaceprefix_ = self.Age_nsprefix_ + ':' if (UseCapturedNS_ and self.Age_nsprefix_) else ''
            self.Age.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Age', pretty_print=pretty_print)
        if self.Position is not None:
            namespaceprefix_ = self.Position_nsprefix_ + ':' if (UseCapturedNS_ and self.Position_nsprefix_) else ''
            self.Position.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Position', pretty_print=pretty_print)
        if self.Velocity is not None:
            namespaceprefix_ = self.Velocity_nsprefix_ + ':' if (UseCapturedNS_ and self.Velocity_nsprefix_) else ''
            self.Velocity.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Velocity', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Age':
            obj_ = AgeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Age = obj_
            obj_.original_tagname_ = 'Age'
        elif nodeName_ == 'Position':
            obj_ = PositionType4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Position = obj_
            obj_.original_tagname_ = 'Position'
        elif nodeName_ == 'Velocity':
            obj_ = VelocityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Velocity = obj_
            obj_.original_tagname_ = 'Velocity'
# end class RemoveConditionType


class AgeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, age=None, younger_than=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.age = _cast(float, age)
        self.age_nsprefix_ = None
        self.younger_than = _cast(bool, younger_than)
        self.younger_than_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AgeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AgeType.subclass:
            return AgeType.subclass(*args_, **kwargs_)
        else:
            return AgeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def get_younger_than(self):
        return self.younger_than
    def set_younger_than(self, younger_than):
        self.younger_than = younger_than
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AgeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AgeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AgeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AgeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AgeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AgeType'):
        if self.age is not None and 'age' not in already_processed:
            already_processed.add('age')
            outfile.write(' age="%s"' % self.gds_format_float(self.age, input_name='age'))
        if self.younger_than and 'younger_than' not in already_processed:
            already_processed.add('younger_than')
            outfile.write(' younger-than="%s"' % self.gds_format_boolean(self.younger_than, input_name='younger-than'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AgeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('age', node)
        if value is not None and 'age' not in already_processed:
            already_processed.add('age')
            value = self.gds_parse_float(value, node, 'age')
            self.age = value
        value = find_attr_value_('younger-than', node)
        if value is not None and 'younger-than' not in already_processed:
            already_processed.add('younger-than')
            if value in ('true', '1'):
                self.younger_than = True
            elif value in ('false', '0'):
                self.younger_than = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AgeType


class PositionType4(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, inside=False, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.inside = _cast(bool, inside)
        self.inside_nsprefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PositionType4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PositionType4.subclass:
            return PositionType4.subclass(*args_, **kwargs_)
        else:
            return PositionType4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_inside(self):
        return self.inside
    def set_inside(self, inside):
        self.inside = inside
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionType4', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PositionType4')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PositionType4':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PositionType4')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PositionType4', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PositionType4'):
        if self.inside and 'inside' not in already_processed:
            already_processed.add('inside')
            outfile.write(' inside="%s"' % self.gds_format_boolean(self.inside, input_name='inside'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PositionType4', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('inside', node)
        if value is not None and 'inside' not in already_processed:
            already_processed.add('inside')
            if value in ('true', '1'):
                self.inside = True
            elif value in ('false', '0'):
                self.inside = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class PositionType4


class VelocityType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, inside=False, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.inside = _cast(bool, inside)
        self.inside_nsprefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VelocityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VelocityType.subclass:
            return VelocityType.subclass(*args_, **kwargs_)
        else:
            return VelocityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_inside(self):
        return self.inside
    def set_inside(self, inside):
        self.inside = inside
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='VelocityType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VelocityType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VelocityType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VelocityType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VelocityType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VelocityType'):
        if self.inside and 'inside' not in already_processed:
            already_processed.add('inside')
            outfile.write(' inside="%s"' % self.gds_format_boolean(self.inside, input_name='inside'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='VelocityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('inside', node)
        if value is not None and 'inside' not in already_processed:
            already_processed.add('inside')
            if value in ('true', '1'):
                self.inside = True
            elif value in ('false', '0'):
                self.inside = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class VelocityType


class AvoidType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, magnitude=None, epsilon=0.001, lookahead=None, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.magnitude = _cast(float, magnitude)
        self.magnitude_nsprefix_ = None
        self.epsilon = _cast(float, epsilon)
        self.epsilon_nsprefix_ = None
        self.lookahead = _cast(float, lookahead)
        self.lookahead_nsprefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AvoidType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AvoidType.subclass:
            return AvoidType.subclass(*args_, **kwargs_)
        else:
            return AvoidType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_magnitude(self):
        return self.magnitude
    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
    def get_epsilon(self):
        return self.epsilon
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon
    def get_lookahead(self):
        return self.lookahead
    def set_lookahead(self, lookahead):
        self.lookahead = lookahead
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AvoidType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AvoidType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AvoidType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AvoidType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AvoidType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AvoidType'):
        if self.magnitude is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            outfile.write(' magnitude="%s"' % self.gds_format_float(self.magnitude, input_name='magnitude'))
        if self.epsilon != 0.001 and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            outfile.write(' epsilon="%s"' % self.gds_format_float(self.epsilon, input_name='epsilon'))
        if self.lookahead is not None and 'lookahead' not in already_processed:
            already_processed.add('lookahead')
            outfile.write(' lookahead="%s"' % self.gds_format_float(self.lookahead, input_name='lookahead'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AvoidType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('magnitude', node)
        if value is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            value = self.gds_parse_float(value, node, 'magnitude')
            self.magnitude = value
        value = find_attr_value_('epsilon', node)
        if value is not None and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            value = self.gds_parse_float(value, node, 'epsilon')
            self.epsilon = value
        value = find_attr_value_('lookahead', node)
        if value is not None and 'lookahead' not in already_processed:
            already_processed.add('lookahead')
            value = self.gds_parse_float(value, node, 'lookahead')
            self.lookahead = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class AvoidType


class BounceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, friction=None, resilience=None, cutoff=None, ParticleDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.friction = _cast(float, friction)
        self.friction_nsprefix_ = None
        self.resilience = _cast(float, resilience)
        self.resilience_nsprefix_ = None
        self.cutoff = _cast(float, cutoff)
        self.cutoff_nsprefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BounceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BounceType.subclass:
            return BounceType.subclass(*args_, **kwargs_)
        else:
            return BounceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_friction(self):
        return self.friction
    def set_friction(self, friction):
        self.friction = friction
    def get_resilience(self):
        return self.resilience
    def set_resilience(self, resilience):
        self.resilience = resilience
    def get_cutoff(self):
        return self.cutoff
    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
    def _hasContent(self):
        if (
            self.ParticleDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BounceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BounceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BounceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BounceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BounceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BounceType'):
        if self.friction is not None and 'friction' not in already_processed:
            already_processed.add('friction')
            outfile.write(' friction="%s"' % self.gds_format_float(self.friction, input_name='friction'))
        if self.resilience is not None and 'resilience' not in already_processed:
            already_processed.add('resilience')
            outfile.write(' resilience="%s"' % self.gds_format_float(self.resilience, input_name='resilience'))
        if self.cutoff is not None and 'cutoff' not in already_processed:
            already_processed.add('cutoff')
            outfile.write(' cutoff="%s"' % self.gds_format_float(self.cutoff, input_name='cutoff'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BounceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('friction', node)
        if value is not None and 'friction' not in already_processed:
            already_processed.add('friction')
            value = self.gds_parse_float(value, node, 'friction')
            self.friction = value
        value = find_attr_value_('resilience', node)
        if value is not None and 'resilience' not in already_processed:
            already_processed.add('resilience')
            value = self.gds_parse_float(value, node, 'resilience')
            self.resilience = value
        value = find_attr_value_('cutoff', node)
        if value is not None and 'cutoff' not in already_processed:
            already_processed.add('cutoff')
            value = self.gds_parse_float(value, node, 'cutoff')
            self.cutoff = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
# end class BounceType


class GravityType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, direction=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.direction = _cast(None, direction)
        self.direction_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GravityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GravityType.subclass:
            return GravityType.subclass(*args_, **kwargs_)
        else:
            return GravityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GravityType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GravityType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GravityType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GravityType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GravityType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GravityType'):
        if self.direction is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            outfile.write(' direction=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.direction), input_name='direction')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GravityType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('direction', node)
        if value is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            self.direction = value
            self.validate_vector(self.direction)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GravityType


class DampingType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, direction=None, vel_low=0.0, vel_high=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.direction = _cast(None, direction)
        self.direction_nsprefix_ = None
        self.vel_low = _cast(float, vel_low)
        self.vel_low_nsprefix_ = None
        self.vel_high = _cast(float, vel_high)
        self.vel_high_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DampingType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DampingType.subclass:
            return DampingType.subclass(*args_, **kwargs_)
        else:
            return DampingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_vel_low(self):
        return self.vel_low
    def set_vel_low(self, vel_low):
        self.vel_low = vel_low
    def get_vel_high(self):
        return self.vel_high
    def set_vel_high(self, vel_high):
        self.vel_high = vel_high
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DampingType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DampingType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DampingType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DampingType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DampingType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DampingType'):
        if self.direction is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            outfile.write(' direction=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.direction), input_name='direction')), ))
        if self.vel_low != 0.0 and 'vel_low' not in already_processed:
            already_processed.add('vel_low')
            outfile.write(' vel_low="%s"' % self.gds_format_float(self.vel_low, input_name='vel_low'))
        if self.vel_high != 0.0 and 'vel_high' not in already_processed:
            already_processed.add('vel_high')
            outfile.write(' vel_high="%s"' % self.gds_format_float(self.vel_high, input_name='vel_high'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DampingType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('direction', node)
        if value is not None and 'direction' not in already_processed:
            already_processed.add('direction')
            self.direction = value
            self.validate_vector(self.direction)    # validate type vector
        value = find_attr_value_('vel_low', node)
        if value is not None and 'vel_low' not in already_processed:
            already_processed.add('vel_low')
            value = self.gds_parse_float(value, node, 'vel_low')
            self.vel_low = value
        value = find_attr_value_('vel_high', node)
        if value is not None and 'vel_high' not in already_processed:
            already_processed.add('vel_high')
            value = self.gds_parse_float(value, node, 'vel_high')
            self.vel_high = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DampingType


class GravitateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, magnitude=1.0, epsilon=0.001, max_radius=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.magnitude = _cast(float, magnitude)
        self.magnitude_nsprefix_ = None
        self.epsilon = _cast(float, epsilon)
        self.epsilon_nsprefix_ = None
        self.max_radius = _cast(float, max_radius)
        self.max_radius_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GravitateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GravitateType.subclass:
            return GravitateType.subclass(*args_, **kwargs_)
        else:
            return GravitateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_magnitude(self):
        return self.magnitude
    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
    def get_epsilon(self):
        return self.epsilon
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon
    def get_max_radius(self):
        return self.max_radius
    def set_max_radius(self, max_radius):
        self.max_radius = max_radius
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GravitateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GravitateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GravitateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GravitateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GravitateType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GravitateType'):
        if self.magnitude != 1.0 and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            outfile.write(' magnitude="%s"' % self.gds_format_float(self.magnitude, input_name='magnitude'))
        if self.epsilon != 0.001 and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            outfile.write(' epsilon="%s"' % self.gds_format_float(self.epsilon, input_name='epsilon'))
        if self.max_radius != 0.0 and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            outfile.write(' max_radius="%s"' % self.gds_format_float(self.max_radius, input_name='max_radius'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GravitateType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('magnitude', node)
        if value is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            value = self.gds_parse_float(value, node, 'magnitude')
            self.magnitude = value
        value = find_attr_value_('epsilon', node)
        if value is not None and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            value = self.gds_parse_float(value, node, 'epsilon')
            self.epsilon = value
        value = find_attr_value_('max_radius', node)
        if value is not None and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            value = self.gds_parse_float(value, node, 'max_radius')
            self.max_radius = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GravitateType


class FollowType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, magnitude=1.0, epsilon=0.001, max_radius=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.magnitude = _cast(float, magnitude)
        self.magnitude_nsprefix_ = None
        self.epsilon = _cast(float, epsilon)
        self.epsilon_nsprefix_ = None
        self.max_radius = _cast(float, max_radius)
        self.max_radius_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FollowType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FollowType.subclass:
            return FollowType.subclass(*args_, **kwargs_)
        else:
            return FollowType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_magnitude(self):
        return self.magnitude
    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
    def get_epsilon(self):
        return self.epsilon
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon
    def get_max_radius(self):
        return self.max_radius
    def set_max_radius(self, max_radius):
        self.max_radius = max_radius
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FollowType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FollowType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FollowType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FollowType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FollowType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FollowType'):
        if self.magnitude != 1.0 and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            outfile.write(' magnitude="%s"' % self.gds_format_float(self.magnitude, input_name='magnitude'))
        if self.epsilon != 0.001 and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            outfile.write(' epsilon="%s"' % self.gds_format_float(self.epsilon, input_name='epsilon'))
        if self.max_radius != 0.0 and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            outfile.write(' max_radius="%s"' % self.gds_format_float(self.max_radius, input_name='max_radius'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FollowType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('magnitude', node)
        if value is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            value = self.gds_parse_float(value, node, 'magnitude')
            self.magnitude = value
        value = find_attr_value_('epsilon', node)
        if value is not None and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            value = self.gds_parse_float(value, node, 'epsilon')
            self.epsilon = value
        value = find_attr_value_('max_radius', node)
        if value is not None and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            value = self.gds_parse_float(value, node, 'max_radius')
            self.max_radius = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class FollowType


class MatchVelType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, magnitude=1.0, epsilon=0.001, max_radius=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.magnitude = _cast(float, magnitude)
        self.magnitude_nsprefix_ = None
        self.epsilon = _cast(float, epsilon)
        self.epsilon_nsprefix_ = None
        self.max_radius = _cast(float, max_radius)
        self.max_radius_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MatchVelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatchVelType.subclass:
            return MatchVelType.subclass(*args_, **kwargs_)
        else:
            return MatchVelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_magnitude(self):
        return self.magnitude
    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
    def get_epsilon(self):
        return self.epsilon
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon
    def get_max_radius(self):
        return self.max_radius
    def set_max_radius(self, max_radius):
        self.max_radius = max_radius
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MatchVelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MatchVelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MatchVelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MatchVelType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MatchVelType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MatchVelType'):
        if self.magnitude != 1.0 and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            outfile.write(' magnitude="%s"' % self.gds_format_float(self.magnitude, input_name='magnitude'))
        if self.epsilon != 0.001 and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            outfile.write(' epsilon="%s"' % self.gds_format_float(self.epsilon, input_name='epsilon'))
        if self.max_radius != 0.0 and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            outfile.write(' max_radius="%s"' % self.gds_format_float(self.max_radius, input_name='max_radius'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MatchVelType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('magnitude', node)
        if value is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            value = self.gds_parse_float(value, node, 'magnitude')
            self.magnitude = value
        value = find_attr_value_('epsilon', node)
        if value is not None and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            value = self.gds_parse_float(value, node, 'epsilon')
            self.epsilon = value
        value = find_attr_value_('max_radius', node)
        if value is not None and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            value = self.gds_parse_float(value, node, 'max_radius')
            self.max_radius = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class MatchVelType


class OrbitPointType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, center=None, magnitude=1.0, epsilon=0.001, max_radius=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.center = _cast(None, center)
        self.center_nsprefix_ = None
        self.magnitude = _cast(float, magnitude)
        self.magnitude_nsprefix_ = None
        self.epsilon = _cast(float, epsilon)
        self.epsilon_nsprefix_ = None
        self.max_radius = _cast(float, max_radius)
        self.max_radius_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrbitPointType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrbitPointType.subclass:
            return OrbitPointType.subclass(*args_, **kwargs_)
        else:
            return OrbitPointType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_center(self):
        return self.center
    def set_center(self, center):
        self.center = center
    def get_magnitude(self):
        return self.magnitude
    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
    def get_epsilon(self):
        return self.epsilon
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon
    def get_max_radius(self):
        return self.max_radius
    def set_max_radius(self, max_radius):
        self.max_radius = max_radius
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OrbitPointType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrbitPointType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrbitPointType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrbitPointType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrbitPointType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrbitPointType'):
        if self.center is not None and 'center' not in already_processed:
            already_processed.add('center')
            outfile.write(' center=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.center), input_name='center')), ))
        if self.magnitude != 1.0 and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            outfile.write(' magnitude="%s"' % self.gds_format_float(self.magnitude, input_name='magnitude'))
        if self.epsilon != 0.001 and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            outfile.write(' epsilon="%s"' % self.gds_format_float(self.epsilon, input_name='epsilon'))
        if self.max_radius != 0.0 and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            outfile.write(' max_radius="%s"' % self.gds_format_float(self.max_radius, input_name='max_radius'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OrbitPointType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('center', node)
        if value is not None and 'center' not in already_processed:
            already_processed.add('center')
            self.center = value
            self.validate_vector(self.center)    # validate type vector
        value = find_attr_value_('magnitude', node)
        if value is not None and 'magnitude' not in already_processed:
            already_processed.add('magnitude')
            value = self.gds_parse_float(value, node, 'magnitude')
            self.magnitude = value
        value = find_attr_value_('epsilon', node)
        if value is not None and 'epsilon' not in already_processed:
            already_processed.add('epsilon')
            value = self.gds_parse_float(value, node, 'epsilon')
            self.epsilon = value
        value = find_attr_value_('max_radius', node)
        if value is not None and 'max_radius' not in already_processed:
            already_processed.add('max_radius')
            value = self.gds_parse_float(value, node, 'max_radius')
            self.max_radius = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OrbitPointType


class JetType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ParticleDomain=None, AccelDomain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ParticleDomain = ParticleDomain
        self.ParticleDomain_nsprefix_ = None
        self.AccelDomain = AccelDomain
        self.AccelDomain_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, JetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if JetType.subclass:
            return JetType.subclass(*args_, **kwargs_)
        else:
            return JetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParticleDomain(self):
        return self.ParticleDomain
    def set_ParticleDomain(self, ParticleDomain):
        self.ParticleDomain = ParticleDomain
    def get_AccelDomain(self):
        return self.AccelDomain
    def set_AccelDomain(self, AccelDomain):
        self.AccelDomain = AccelDomain
    def _hasContent(self):
        if (
            self.ParticleDomain is not None or
            self.AccelDomain is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='JetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('JetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'JetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='JetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='JetType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='JetType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='JetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParticleDomain is not None:
            namespaceprefix_ = self.ParticleDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.ParticleDomain_nsprefix_) else ''
            self.ParticleDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParticleDomain', pretty_print=pretty_print)
        if self.AccelDomain is not None:
            namespaceprefix_ = self.AccelDomain_nsprefix_ + ':' if (UseCapturedNS_ and self.AccelDomain_nsprefix_) else ''
            self.AccelDomain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AccelDomain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParticleDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParticleDomain = obj_
            obj_.original_tagname_ = 'ParticleDomain'
        elif nodeName_ == 'AccelDomain':
            obj_ = ParticleDomainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AccelDomain = obj_
            obj_.original_tagname_ = 'AccelDomain'
# end class JetType


class TargetColorType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, color=None, alpha=1.0, scale=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.color = _cast(None, color)
        self.color_nsprefix_ = None
        self.alpha = _cast(float, alpha)
        self.alpha_nsprefix_ = None
        self.scale = _cast(float, scale)
        self.scale_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TargetColorType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TargetColorType.subclass:
            return TargetColorType.subclass(*args_, **kwargs_)
        else:
            return TargetColorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    def get_alpha(self):
        return self.alpha
    def set_alpha(self, alpha):
        self.alpha = alpha
    def get_scale(self):
        return self.scale
    def set_scale(self, scale):
        self.scale = scale
    def validate_color(self, value):
        # Validate type color, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetColorType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TargetColorType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TargetColorType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TargetColorType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TargetColorType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TargetColorType'):
        if self.color is not None and 'color' not in already_processed:
            already_processed.add('color')
            outfile.write(' color=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.color), input_name='color')), ))
        if self.alpha != 1.0 and 'alpha' not in already_processed:
            already_processed.add('alpha')
            outfile.write(' alpha="%s"' % self.gds_format_float(self.alpha, input_name='alpha'))
        if self.scale is not None and 'scale' not in already_processed:
            already_processed.add('scale')
            outfile.write(' scale="%s"' % self.gds_format_float(self.scale, input_name='scale'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TargetColorType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('color', node)
        if value is not None and 'color' not in already_processed:
            already_processed.add('color')
            self.color = value
            self.validate_color(self.color)    # validate type color
        value = find_attr_value_('alpha', node)
        if value is not None and 'alpha' not in already_processed:
            already_processed.add('alpha')
            value = self.gds_parse_float(value, node, 'alpha')
            self.alpha = value
        value = find_attr_value_('scale', node)
        if value is not None and 'scale' not in already_processed:
            already_processed.add('scale')
            value = self.gds_parse_float(value, node, 'scale')
            self.scale = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TargetColorType


class AxisType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rotation='(0.0, 1.0, 0.0)', angle=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rotation = _cast(None, rotation)
        self.rotation_nsprefix_ = None
        self.angle = _cast(float, angle)
        self.angle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AxisType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AxisType.subclass:
            return AxisType.subclass(*args_, **kwargs_)
        else:
            return AxisType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_rotation(self):
        return self.rotation
    def set_rotation(self, rotation):
        self.rotation = rotation
    def get_angle(self):
        return self.angle
    def set_angle(self, angle):
        self.angle = angle
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AxisType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AxisType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AxisType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AxisType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AxisType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AxisType'):
        if self.rotation != "(0.0, 1.0, 0.0)" and 'rotation' not in already_processed:
            already_processed.add('rotation')
            outfile.write(' rotation=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rotation), input_name='rotation')), ))
        if self.angle != 0.0 and 'angle' not in already_processed:
            already_processed.add('angle')
            outfile.write(' angle="%s"' % self.gds_format_double(self.angle, input_name='angle'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AxisType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rotation', node)
        if value is not None and 'rotation' not in already_processed:
            already_processed.add('rotation')
            self.rotation = value
            self.validate_vector(self.rotation)    # validate type vector
        value = find_attr_value_('angle', node)
        if value is not None and 'angle' not in already_processed:
            already_processed.add('angle')
            value = self.gds_parse_double(value, node, 'angle')
            self.angle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AxisType


class LookAtType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, target='(0.0, 0.0, 0.0)', up='(0.0, 1.0, 0.0)', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.target = _cast(None, target)
        self.target_nsprefix_ = None
        self.up = _cast(None, up)
        self.up_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LookAtType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LookAtType.subclass:
            return LookAtType.subclass(*args_, **kwargs_)
        else:
            return LookAtType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_target(self):
        return self.target
    def set_target(self, target):
        self.target = target
    def get_up(self):
        return self.up
    def set_up(self, up):
        self.up = up
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LookAtType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LookAtType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LookAtType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LookAtType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LookAtType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LookAtType'):
        if self.target != "(0.0, 0.0, 0.0)" and 'target' not in already_processed:
            already_processed.add('target')
            outfile.write(' target=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.target), input_name='target')), ))
        if self.up != "(0.0, 1.0, 0.0)" and 'up' not in already_processed:
            already_processed.add('up')
            outfile.write(' up=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.up), input_name='up')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LookAtType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('target', node)
        if value is not None and 'target' not in already_processed:
            already_processed.add('target')
            self.target = value
            self.validate_vector(self.target)    # validate type vector
        value = find_attr_value_('up', node)
        if value is not None and 'up' not in already_processed:
            already_processed.add('up')
            self.up = value
            self.validate_vector(self.up)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class LookAtType


class NormalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, normal='(0.0, 0.0, 1.0)', angle=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.normal = _cast(None, normal)
        self.normal_nsprefix_ = None
        self.angle = _cast(float, angle)
        self.angle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NormalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NormalType.subclass:
            return NormalType.subclass(*args_, **kwargs_)
        else:
            return NormalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_normal(self):
        return self.normal
    def set_normal(self, normal):
        self.normal = normal
    def get_angle(self):
        return self.angle
    def set_angle(self, angle):
        self.angle = angle
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NormalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NormalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NormalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NormalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NormalType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NormalType'):
        if self.normal != "(0.0, 0.0, 1.0)" and 'normal' not in already_processed:
            already_processed.add('normal')
            outfile.write(' normal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.normal), input_name='normal')), ))
        if self.angle != 0.0 and 'angle' not in already_processed:
            already_processed.add('angle')
            outfile.write(' angle="%s"' % self.gds_format_double(self.angle, input_name='angle'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NormalType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('normal', node)
        if value is not None and 'normal' not in already_processed:
            already_processed.add('normal')
            self.normal = value
            self.validate_vector(self.normal)    # validate type vector
        value = find_attr_value_('angle', node)
        if value is not None and 'angle' not in already_processed:
            already_processed.add('angle')
            value = self.gds_parse_double(value, node, 'angle')
            self.angle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NormalType


class MovementType5(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MovementType5)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MovementType5.subclass:
            return MovementType5.subclass(*args_, **kwargs_)
        else:
            return MovementType5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def _hasContent(self):
        if (
            self.Placement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MovementType5', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MovementType5')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MovementType5':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MovementType5')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MovementType5', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MovementType5'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MovementType5', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
# end class MovementType5


class MoveRelType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Placement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Placement = Placement
        self.Placement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MoveRelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MoveRelType.subclass:
            return MoveRelType.subclass(*args_, **kwargs_)
        else:
            return MoveRelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Placement(self):
        return self.Placement
    def set_Placement(self, Placement):
        self.Placement = Placement
    def _hasContent(self):
        if (
            self.Placement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveRelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MoveRelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MoveRelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MoveRelType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MoveRelType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MoveRelType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MoveRelType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Placement is not None:
            namespaceprefix_ = self.Placement_nsprefix_ + ':' if (UseCapturedNS_ and self.Placement_nsprefix_) else ''
            self.Placement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Placement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Placement':
            obj_ = Placement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Placement = obj_
            obj_.original_tagname_ = 'Placement'
# end class MoveRelType


class SoundType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, action=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.action = _cast(None, action)
        self.action_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SoundType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SoundType.subclass:
            return SoundType.subclass(*args_, **kwargs_)
        else:
            return SoundType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_action(self):
        return self.action
    def set_action(self, action):
        self.action = action
    def validate_actionType(self, value):
        # Validate type actionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Play Sound', 'Stop Sound']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on actionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SoundType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SoundType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SoundType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SoundType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SoundType'):
        if self.action is not None and 'action' not in already_processed:
            already_processed.add('action')
            outfile.write(' action=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.action), input_name='action')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SoundType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('action', node)
        if value is not None and 'action' not in already_processed:
            already_processed.add('action')
            self.action = value
            self.validate_actionType(self.action)    # validate type actionType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SoundType


class LinkChangeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, link_on=None, link_off=None, activate=None, activate_if_on=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.link_on = link_on
        self.link_on_nsprefix_ = None
        self.link_off = link_off
        self.link_off_nsprefix_ = None
        self.activate = activate
        self.activate_nsprefix_ = None
        self.activate_if_on = activate_if_on
        self.activate_if_on_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LinkChangeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LinkChangeType.subclass:
            return LinkChangeType.subclass(*args_, **kwargs_)
        else:
            return LinkChangeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_link_on(self):
        return self.link_on
    def set_link_on(self, link_on):
        self.link_on = link_on
    def get_link_off(self):
        return self.link_off
    def set_link_off(self, link_off):
        self.link_off = link_off
    def get_activate(self):
        return self.activate
    def set_activate(self, activate):
        self.activate = activate
    def get_activate_if_on(self):
        return self.activate_if_on
    def set_activate_if_on(self, activate_if_on):
        self.activate_if_on = activate_if_on
    def _hasContent(self):
        if (
            self.link_on is not None or
            self.link_off is not None or
            self.activate is not None or
            self.activate_if_on is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkChangeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LinkChangeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LinkChangeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LinkChangeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LinkChangeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LinkChangeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkChangeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.link_on is not None:
            namespaceprefix_ = self.link_on_nsprefix_ + ':' if (UseCapturedNS_ and self.link_on_nsprefix_) else ''
            self.link_on.export(outfile, level, namespaceprefix_, namespacedef_='', name_='link_on', pretty_print=pretty_print)
        if self.link_off is not None:
            namespaceprefix_ = self.link_off_nsprefix_ + ':' if (UseCapturedNS_ and self.link_off_nsprefix_) else ''
            self.link_off.export(outfile, level, namespaceprefix_, namespacedef_='', name_='link_off', pretty_print=pretty_print)
        if self.activate is not None:
            namespaceprefix_ = self.activate_nsprefix_ + ':' if (UseCapturedNS_ and self.activate_nsprefix_) else ''
            self.activate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='activate', pretty_print=pretty_print)
        if self.activate_if_on is not None:
            namespaceprefix_ = self.activate_if_on_nsprefix_ + ':' if (UseCapturedNS_ and self.activate_if_on_nsprefix_) else ''
            self.activate_if_on.export(outfile, level, namespaceprefix_, namespacedef_='', name_='activate_if_on', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'link_on':
            obj_ = link_onType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.link_on = obj_
            obj_.original_tagname_ = 'link_on'
        elif nodeName_ == 'link_off':
            obj_ = link_offType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.link_off = obj_
            obj_.original_tagname_ = 'link_off'
        elif nodeName_ == 'activate':
            obj_ = activateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.activate = obj_
            obj_.original_tagname_ = 'activate'
        elif nodeName_ == 'activate_if_on':
            obj_ = activate_if_onType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.activate_if_on = obj_
            obj_.original_tagname_ = 'activate_if_on'
# end class LinkChangeType


class link_onType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, link_onType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if link_onType.subclass:
            return link_onType.subclass(*args_, **kwargs_)
        else:
            return link_onType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='link_onType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('link_onType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'link_onType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='link_onType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='link_onType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='link_onType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='link_onType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class link_onType


class link_offType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, link_offType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if link_offType.subclass:
            return link_offType.subclass(*args_, **kwargs_)
        else:
            return link_offType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='link_offType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('link_offType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'link_offType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='link_offType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='link_offType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='link_offType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='link_offType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class link_offType


class activateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, activateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if activateType.subclass:
            return activateType.subclass(*args_, **kwargs_)
        else:
            return activateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='activateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('activateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'activateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='activateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='activateType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='activateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='activateType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class activateType


class activate_if_onType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, activate_if_onType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if activate_if_onType.subclass:
            return activate_if_onType.subclass(*args_, **kwargs_)
        else:
            return activate_if_onType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='activate_if_onType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('activate_if_onType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'activate_if_onType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='activate_if_onType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='activate_if_onType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='activate_if_onType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='activate_if_onType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class activate_if_onType


class PointType6(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, point=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.point = _cast(None, point)
        self.point_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PointType6)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PointType6.subclass:
            return PointType6.subclass(*args_, **kwargs_)
        else:
            return PointType6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_point(self):
        return self.point
    def set_point(self, point):
        self.point = point
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointType6', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PointType6')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PointType6':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PointType6')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PointType6', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PointType6'):
        if self.point is not None and 'point' not in already_processed:
            already_processed.add('point')
            outfile.write(' point=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.point), input_name='point')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PointType6', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('point', node)
        if value is not None and 'point' not in already_processed:
            already_processed.add('point')
            self.point = value
            self.validate_vector(self.point)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PointType6


class LineType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, p1=None, p2=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.p1 = _cast(None, p1)
        self.p1_nsprefix_ = None
        self.p2 = _cast(None, p2)
        self.p2_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineType.subclass:
            return LineType.subclass(*args_, **kwargs_)
        else:
            return LineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_p1(self):
        return self.p1
    def set_p1(self, p1):
        self.p1 = p1
    def get_p2(self):
        return self.p2
    def set_p2(self, p2):
        self.p2 = p2
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LineType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineType'):
        if self.p1 is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            outfile.write(' p1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p1), input_name='p1')), ))
        if self.p2 is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            outfile.write(' p2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p2), input_name='p2')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LineType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('p1', node)
        if value is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            self.p1 = value
            self.validate_vector(self.p1)    # validate type vector
        value = find_attr_value_('p2', node)
        if value is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            self.p2 = value
            self.validate_vector(self.p2)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class LineType


class TriangleType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, p1=None, p2=None, p3=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.p1 = _cast(None, p1)
        self.p1_nsprefix_ = None
        self.p2 = _cast(None, p2)
        self.p2_nsprefix_ = None
        self.p3 = _cast(None, p3)
        self.p3_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TriangleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TriangleType.subclass:
            return TriangleType.subclass(*args_, **kwargs_)
        else:
            return TriangleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_p1(self):
        return self.p1
    def set_p1(self, p1):
        self.p1 = p1
    def get_p2(self):
        return self.p2
    def set_p2(self, p2):
        self.p2 = p2
    def get_p3(self):
        return self.p3
    def set_p3(self, p3):
        self.p3 = p3
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TriangleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TriangleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TriangleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TriangleType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TriangleType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TriangleType'):
        if self.p1 is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            outfile.write(' p1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p1), input_name='p1')), ))
        if self.p2 is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            outfile.write(' p2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p2), input_name='p2')), ))
        if self.p3 is not None and 'p3' not in already_processed:
            already_processed.add('p3')
            outfile.write(' p3=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p3), input_name='p3')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TriangleType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('p1', node)
        if value is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            self.p1 = value
            self.validate_vector(self.p1)    # validate type vector
        value = find_attr_value_('p2', node)
        if value is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            self.p2 = value
            self.validate_vector(self.p2)    # validate type vector
        value = find_attr_value_('p3', node)
        if value is not None and 'p3' not in already_processed:
            already_processed.add('p3')
            self.p3 = value
            self.validate_vector(self.p3)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TriangleType


class PlaneType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, point=None, normal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.point = _cast(None, point)
        self.point_nsprefix_ = None
        self.normal = _cast(None, normal)
        self.normal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PlaneType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PlaneType.subclass:
            return PlaneType.subclass(*args_, **kwargs_)
        else:
            return PlaneType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_point(self):
        return self.point
    def set_point(self, point):
        self.point = point
    def get_normal(self):
        return self.normal
    def set_normal(self, normal):
        self.normal = normal
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PlaneType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PlaneType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PlaneType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PlaneType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PlaneType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PlaneType'):
        if self.point is not None and 'point' not in already_processed:
            already_processed.add('point')
            outfile.write(' point=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.point), input_name='point')), ))
        if self.normal is not None and 'normal' not in already_processed:
            already_processed.add('normal')
            outfile.write(' normal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.normal), input_name='normal')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PlaneType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('point', node)
        if value is not None and 'point' not in already_processed:
            already_processed.add('point')
            self.point = value
            self.validate_vector(self.point)    # validate type vector
        value = find_attr_value_('normal', node)
        if value is not None and 'normal' not in already_processed:
            already_processed.add('normal')
            self.normal = value
            self.validate_vector(self.normal)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PlaneType


class RectType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, point=None, u_dir=None, v_dir=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.point = _cast(None, point)
        self.point_nsprefix_ = None
        self.u_dir = _cast(None, u_dir)
        self.u_dir_nsprefix_ = None
        self.v_dir = _cast(None, v_dir)
        self.v_dir_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RectType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RectType.subclass:
            return RectType.subclass(*args_, **kwargs_)
        else:
            return RectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_point(self):
        return self.point
    def set_point(self, point):
        self.point = point
    def get_u_dir(self):
        return self.u_dir
    def set_u_dir(self, u_dir):
        self.u_dir = u_dir
    def get_v_dir(self):
        return self.v_dir
    def set_v_dir(self, v_dir):
        self.v_dir = v_dir
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RectType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RectType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RectType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RectType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RectType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RectType'):
        if self.point is not None and 'point' not in already_processed:
            already_processed.add('point')
            outfile.write(' point=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.point), input_name='point')), ))
        if self.u_dir is not None and 'u_dir' not in already_processed:
            already_processed.add('u_dir')
            outfile.write(' u-dir=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.u_dir), input_name='u-dir')), ))
        if self.v_dir is not None and 'v_dir' not in already_processed:
            already_processed.add('v_dir')
            outfile.write(' v-dir=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.v_dir), input_name='v-dir')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RectType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('point', node)
        if value is not None and 'point' not in already_processed:
            already_processed.add('point')
            self.point = value
            self.validate_vector(self.point)    # validate type vector
        value = find_attr_value_('u-dir', node)
        if value is not None and 'u-dir' not in already_processed:
            already_processed.add('u-dir')
            self.u_dir = value
            self.validate_vector(self.u_dir)    # validate type vector
        value = find_attr_value_('v-dir', node)
        if value is not None and 'v-dir' not in already_processed:
            already_processed.add('v-dir')
            self.v_dir = value
            self.validate_vector(self.v_dir)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RectType


class BoxType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, p1=None, p2=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.p1 = _cast(None, p1)
        self.p1_nsprefix_ = None
        self.p2 = _cast(None, p2)
        self.p2_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BoxType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BoxType.subclass:
            return BoxType.subclass(*args_, **kwargs_)
        else:
            return BoxType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_p1(self):
        return self.p1
    def set_p1(self, p1):
        self.p1 = p1
    def get_p2(self):
        return self.p2
    def set_p2(self, p2):
        self.p2 = p2
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BoxType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BoxType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BoxType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BoxType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BoxType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BoxType'):
        if self.p1 is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            outfile.write(' p1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p1), input_name='p1')), ))
        if self.p2 is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            outfile.write(' p2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p2), input_name='p2')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BoxType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('p1', node)
        if value is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            self.p1 = value
            self.validate_vector(self.p1)    # validate type vector
        value = find_attr_value_('p2', node)
        if value is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            self.p2 = value
            self.validate_vector(self.p2)    # validate type vector
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class BoxType


class SphereType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, center=None, radius=None, radius_inner=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.center = _cast(None, center)
        self.center_nsprefix_ = None
        self.radius = _cast(float, radius)
        self.radius_nsprefix_ = None
        self.radius_inner = _cast(float, radius_inner)
        self.radius_inner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SphereType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SphereType.subclass:
            return SphereType.subclass(*args_, **kwargs_)
        else:
            return SphereType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_center(self):
        return self.center
    def set_center(self, center):
        self.center = center
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_radius_inner(self):
        return self.radius_inner
    def set_radius_inner(self, radius_inner):
        self.radius_inner = radius_inner
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SphereType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SphereType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SphereType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SphereType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SphereType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SphereType'):
        if self.center is not None and 'center' not in already_processed:
            already_processed.add('center')
            outfile.write(' center=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.center), input_name='center')), ))
        if self.radius is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            outfile.write(' radius="%s"' % self.gds_format_float(self.radius, input_name='radius'))
        if self.radius_inner != 0.0 and 'radius_inner' not in already_processed:
            already_processed.add('radius_inner')
            outfile.write(' radius-inner="%s"' % self.gds_format_float(self.radius_inner, input_name='radius-inner'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SphereType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('center', node)
        if value is not None and 'center' not in already_processed:
            already_processed.add('center')
            self.center = value
            self.validate_vector(self.center)    # validate type vector
        value = find_attr_value_('radius', node)
        if value is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            value = self.gds_parse_float(value, node, 'radius')
            self.radius = value
        value = find_attr_value_('radius-inner', node)
        if value is not None and 'radius-inner' not in already_processed:
            already_processed.add('radius-inner')
            value = self.gds_parse_float(value, node, 'radius-inner')
            self.radius_inner = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SphereType


class CylinderType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, p1=None, p2=None, radius=None, radius_inner=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.p1 = _cast(None, p1)
        self.p1_nsprefix_ = None
        self.p2 = _cast(None, p2)
        self.p2_nsprefix_ = None
        self.radius = _cast(float, radius)
        self.radius_nsprefix_ = None
        self.radius_inner = _cast(float, radius_inner)
        self.radius_inner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CylinderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CylinderType.subclass:
            return CylinderType.subclass(*args_, **kwargs_)
        else:
            return CylinderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_p1(self):
        return self.p1
    def set_p1(self, p1):
        self.p1 = p1
    def get_p2(self):
        return self.p2
    def set_p2(self, p2):
        self.p2 = p2
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_radius_inner(self):
        return self.radius_inner
    def set_radius_inner(self, radius_inner):
        self.radius_inner = radius_inner
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CylinderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CylinderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CylinderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CylinderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CylinderType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CylinderType'):
        if self.p1 is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            outfile.write(' p1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p1), input_name='p1')), ))
        if self.p2 is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            outfile.write(' p2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.p2), input_name='p2')), ))
        if self.radius is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            outfile.write(' radius="%s"' % self.gds_format_float(self.radius, input_name='radius'))
        if self.radius_inner != 0.0 and 'radius_inner' not in already_processed:
            already_processed.add('radius_inner')
            outfile.write(' radius-inner="%s"' % self.gds_format_float(self.radius_inner, input_name='radius-inner'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CylinderType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('p1', node)
        if value is not None and 'p1' not in already_processed:
            already_processed.add('p1')
            self.p1 = value
            self.validate_vector(self.p1)    # validate type vector
        value = find_attr_value_('p2', node)
        if value is not None and 'p2' not in already_processed:
            already_processed.add('p2')
            self.p2 = value
            self.validate_vector(self.p2)    # validate type vector
        value = find_attr_value_('radius', node)
        if value is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            value = self.gds_parse_float(value, node, 'radius')
            self.radius = value
        value = find_attr_value_('radius-inner', node)
        if value is not None and 'radius-inner' not in already_processed:
            already_processed.add('radius-inner')
            value = self.gds_parse_float(value, node, 'radius-inner')
            self.radius_inner = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CylinderType


class ConeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, base_center=None, apex=None, radius=None, radius_inner=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.base_center = _cast(None, base_center)
        self.base_center_nsprefix_ = None
        self.apex = _cast(None, apex)
        self.apex_nsprefix_ = None
        self.radius = _cast(float, radius)
        self.radius_nsprefix_ = None
        self.radius_inner = _cast(float, radius_inner)
        self.radius_inner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConeType.subclass:
            return ConeType.subclass(*args_, **kwargs_)
        else:
            return ConeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_base_center(self):
        return self.base_center
    def set_base_center(self, base_center):
        self.base_center = base_center
    def get_apex(self):
        return self.apex
    def set_apex(self, apex):
        self.apex = apex
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_radius_inner(self):
        return self.radius_inner
    def set_radius_inner(self, radius_inner):
        self.radius_inner = radius_inner
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ConeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConeType'):
        if self.base_center is not None and 'base_center' not in already_processed:
            already_processed.add('base_center')
            outfile.write(' base-center=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.base_center), input_name='base-center')), ))
        if self.apex is not None and 'apex' not in already_processed:
            already_processed.add('apex')
            outfile.write(' apex=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.apex), input_name='apex')), ))
        if self.radius is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            outfile.write(' radius="%s"' % self.gds_format_float(self.radius, input_name='radius'))
        if self.radius_inner != 0.0 and 'radius_inner' not in already_processed:
            already_processed.add('radius_inner')
            outfile.write(' radius-inner="%s"' % self.gds_format_float(self.radius_inner, input_name='radius-inner'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ConeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('base-center', node)
        if value is not None and 'base-center' not in already_processed:
            already_processed.add('base-center')
            self.base_center = value
            self.validate_vector(self.base_center)    # validate type vector
        value = find_attr_value_('apex', node)
        if value is not None and 'apex' not in already_processed:
            already_processed.add('apex')
            self.apex = value
            self.validate_vector(self.apex)    # validate type vector
        value = find_attr_value_('radius', node)
        if value is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            value = self.gds_parse_float(value, node, 'radius')
            self.radius = value
        value = find_attr_value_('radius-inner', node)
        if value is not None and 'radius-inner' not in already_processed:
            already_processed.add('radius-inner')
            value = self.gds_parse_float(value, node, 'radius-inner')
            self.radius_inner = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ConeType


class BlobType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, center=None, stdev=1.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.center = _cast(None, center)
        self.center_nsprefix_ = None
        self.stdev = _cast(float, stdev)
        self.stdev_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BlobType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BlobType.subclass:
            return BlobType.subclass(*args_, **kwargs_)
        else:
            return BlobType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_center(self):
        return self.center
    def set_center(self, center):
        self.center = center
    def get_stdev(self):
        return self.stdev
    def set_stdev(self, stdev):
        self.stdev = stdev
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BlobType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BlobType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BlobType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BlobType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BlobType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BlobType'):
        if self.center is not None and 'center' not in already_processed:
            already_processed.add('center')
            outfile.write(' center=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.center), input_name='center')), ))
        if self.stdev != 1.0 and 'stdev' not in already_processed:
            already_processed.add('stdev')
            outfile.write(' stdev="%s"' % self.gds_format_float(self.stdev, input_name='stdev'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BlobType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('center', node)
        if value is not None and 'center' not in already_processed:
            already_processed.add('center')
            self.center = value
            self.validate_vector(self.center)    # validate type vector
        value = find_attr_value_('stdev', node)
        if value is not None and 'stdev' not in already_processed:
            already_processed.add('stdev')
            value = self.gds_parse_float(value, node, 'stdev')
            self.stdev = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class BlobType


class DiscType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, center=None, normal=None, radius=None, radius_inner=0.0, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.center = _cast(None, center)
        self.center_nsprefix_ = None
        self.normal = _cast(None, normal)
        self.normal_nsprefix_ = None
        self.radius = _cast(float, radius)
        self.radius_nsprefix_ = None
        self.radius_inner = _cast(float, radius_inner)
        self.radius_inner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DiscType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DiscType.subclass:
            return DiscType.subclass(*args_, **kwargs_)
        else:
            return DiscType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_center(self):
        return self.center
    def set_center(self, center):
        self.center = center
    def get_normal(self):
        return self.normal
    def set_normal(self, normal):
        self.normal = normal
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_radius_inner(self):
        return self.radius_inner
    def set_radius_inner(self, radius_inner):
        self.radius_inner = radius_inner
    def validate_vector(self, value):
        # Validate type vector, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DiscType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DiscType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DiscType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DiscType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DiscType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DiscType'):
        if self.center is not None and 'center' not in already_processed:
            already_processed.add('center')
            outfile.write(' center=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.center), input_name='center')), ))
        if self.normal is not None and 'normal' not in already_processed:
            already_processed.add('normal')
            outfile.write(' normal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.normal), input_name='normal')), ))
        if self.radius is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            outfile.write(' radius="%s"' % self.gds_format_float(self.radius, input_name='radius'))
        if self.radius_inner != 0.0 and 'radius_inner' not in already_processed:
            already_processed.add('radius_inner')
            outfile.write(' radius-inner="%s"' % self.gds_format_float(self.radius_inner, input_name='radius-inner'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DiscType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('center', node)
        if value is not None and 'center' not in already_processed:
            already_processed.add('center')
            self.center = value
            self.validate_vector(self.center)    # validate type vector
        value = find_attr_value_('normal', node)
        if value is not None and 'normal' not in already_processed:
            already_processed.add('normal')
            self.normal = value
            self.validate_vector(self.normal)    # validate type vector
        value = find_attr_value_('radius', node)
        if value is not None and 'radius' not in already_processed:
            already_processed.add('radius')
            value = self.gds_parse_float(value, node, 'radius')
            self.radius = value
        value = find_attr_value_('radius-inner', node)
        if value is not None and 'radius-inner' not in already_processed:
            already_processed.add('radius-inner')
            value = self.gds_parse_float(value, node, 'radius-inner')
            self.radius_inner = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DiscType


GDSClassesMapping = {
    'ParticleDomain': ParticleDomainType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Story'
        rootClass = Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Story'
        rootClass = Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Story'
        rootClass = Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Story'
        rootClass = Story
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from classes import *\n\n')
        sys.stdout.write('import classes as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "AboutType",
    "AbsoluteType",
    "ActionsType",
    "ActionsType1",
    "AgeType",
    "AnyType",
    "AnywhereType",
    "AvoidType",
    "AxisType",
    "BackgroundType",
    "BlobType",
    "BounceType",
    "Box",
    "BoxType",
    "CameraPosType",
    "CaveCameraPosType",
    "ClicksType",
    "ConeType",
    "Content",
    "CylinderType",
    "DampingType",
    "DirectionTargetType",
    "DirectionType",
    "DirectionalType",
    "DiscType",
    "Event",
    "EventRootType",
    "EventTrigger",
    "FixedType",
    "FollowType",
    "GlobalType",
    "GravitateType",
    "GravityType",
    "Group",
    "GroupObjType",
    "GroupRef",
    "GroupRootType",
    "Groups",
    "HeadTrackType",
    "ImageType",
    "InsideType",
    "JetType",
    "LightType",
    "LineType",
    "Link",
    "LinkChangeType",
    "LinkRootType",
    "LookAtType",
    "MatchVelType",
    "ModeType",
    "ModelType",
    "MoveCaveType",
    "MoveRelType",
    "MoveTrackType",
    "MovementType",
    "MovementType5",
    "NoRepeatType",
    "NoneType",
    "NoneType2",
    "NormalType",
    "NumClicksType",
    "Object",
    "ObjectChange",
    "ObjectRefType",
    "ObjectRootType",
    "ObjectTargetType",
    "Objects",
    "OrbitPointType",
    "OutsideType",
    "ParticleAction",
    "ParticleActionList",
    "ParticleActionRootType",
    "ParticleDomainType",
    "ParticleSystemType",
    "Placement",
    "PlacementRootType",
    "PlaneType",
    "PointTargetType",
    "PointType",
    "PointType6",
    "PositionType",
    "PositionType4",
    "PositionalType",
    "RandomAccel",
    "RandomDisplace",
    "RandomVel",
    "RectType",
    "RelativeType",
    "RemoveConditionType",
    "RepeatForeverType",
    "RepeatType",
    "RestartType",
    "SettingsType",
    "Sound",
    "SoundRef",
    "SoundRootType",
    "SoundType",
    "SourceType",
    "SourceType3",
    "SphereType",
    "SpotType",
    "StereoImageType",
    "Story",
    "TargetColorType",
    "TargetSize",
    "TargetVel",
    "TextType",
    "TimedActionsType",
    "Timeline",
    "TimelineRootType",
    "TimerChange",
    "Transition",
    "TriangleType",
    "VelType",
    "VelocityType",
    "WandNavigationType",
    "activateType",
    "activate_if_onType",
    "continueType",
    "link_offType",
    "link_onType",
    "startType",
    "start_if_not_startedType",
    "stopType"
]

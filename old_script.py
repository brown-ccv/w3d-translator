import concurrent.futures
import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
from glob import glob

 #! COMMENTED OUT CODE HAS BEEN COMPLETED IN W3D_TRANSLATOR

# UNITY = "C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.26f1\\Editor\\Unity.exe"
# DEFAULT_INPUT = "originals"
# DEFAULT_OUTPUT = "unity_projects"

########## FUNCTIONS ##########

# Get yes or no user input
# def get_yn(prompt):
#     while True:
#         yn = input(prompt + " [y/n]:\t").lower()

#         if yn in ['y', 'yes']: return True
#         elif yn in ['n', 'no']: return False
#         else: print('Please enter y for yes or n for no\n')

# Get path to the source project(s)
# def get_source_directory(translateMultiple):
#     while True:
#         if translateMultiple: projectPath = input('Enter path to projects:\t')
#         else: projectPath = input('Enter root folder of the project:\t')
        
#         # TODO: More path validation or just be able to open it?
#         if os.path.isdir(projectPath): return projectPath
#         else: print(projectPath + 'is not a valid path. Please enter a valid path\n')

# def get_output_directory(defaultSettings):
#     while True:
#         path = DEFAULT_OUTPUT if defaultSettings else input('Enter output folder where unity project(s) will live:\t')
#         try: os.mkdir(path)
#         except FileExistsError:
#             # Ensure user want's to delete contents of path 
#             proceed = get_yn(f'Would you like to proceed? Contents of "{path}" will be deleted.')
#             if(proceed): 
#                 # TODO: rmtree() causes error on read-only files, which Unity creates. 
#                 try: shutil.rmtree(path, ignore_errors=True)
#                 except OSError as e: 
#                     print (f'Error removing directory: "{e.filename}"')
#                     print(e)
#                 else: return path
#             else: defaultSettings = False # Ensures input() will be called on next loop
#         except FileNotFoundError: print(f'The specified path is invalid: {path} \n')
#         else: return path

def translate_project(project, output):
    output = os.path.join(output, os.path.basename(os.path.normpath(project)))
    assets = os.path.join(output, "Assets", "xml")
    xml = os.path.join(assets, "run.xml") # TODO: Translate all xml files in the folder

    # # # Create unity project
    # # print(f'Creating new unity project at "{output}"')
    # # subprocess.run(f'{UNITY} -createProject "{output}" -batchmode -quit')

    # # Copy files into unity project. Unity has issues with .mov files and they aren't used in run.xml
    # print('Copying', project, 'to', assets)
    # shutil.copytree(project, assets, ignore=shutil.ignore_patterns("mov_versions"))

    # Translate xml for use with the parser
    translate_xml(xml)

    return

def translate_xml(file):
    print("Translating XML at", file)
    xml = ET.parse(file)
    root = xml.getroot()

    # Translate <Color>, <EnabledColor>, and <SelectedColor> to be read as Unity Color types
    for element in ['Color', 'EnabledColor', 'SelectedColor']:
        for tag in root.iter(element):
            translate_color(tag)

    # Translate <Background color=""> as <Background> Unity Color type
    background = root.find('Global/Background')
    attribute_to_text(background, 'color')
    translate_color(background)

    # Translate <Position> to be read as Unity Vector3 type
    for tag in root.iter('Position'):
        translate_vector3(tag)
    
    # Translate <Axis> to use XmlElements, Rotation is a Unity Vector3 type
    for tag in root.iter('Axis'):
        attribute_to_tag_all(tag)
        translate_vector3(tag.find('Rotation'))
    
    # Translate <LookAt> to use XmlElements, Target and Up are Unity Vector3 types
    for tag in root.iter('LookAt'):
        attribute_to_tag_all(tag)
        translate_vector3(tag.find('Target'))
        translate_vector3(tag.find('Up'))
    
    # Translate <Gravity> to use XmlElements, Direction is a Unity Vector3 type
    for tag in root.iter('Gravity'):
        attribute_to_tag_all(tag)
        translate_vector3(tag.find('Direction'))
    
    # Translate <OrbitPoint> to use XmlElements, Center is a Unity Vector3 type
    for tag in root.iter('OrbitPoint'):
        attribute_to_tag_all(tag)
        translate_vector3(tag.find('Center'))

    # Translate <TimedActions> as <TimedAction>
    for tag in root.iter('Timeline/TimedActions'):
        tag.tag = 'TimedAction'

    # Translate <Objects> as <ObjectRef>, name attribute is the inner text
    for tag in root.iter('Objects'):
        tag.tag = 'ObjectRef'
        attribute_to_text(tag, 'name')

    # Translate <SoundRef name='[name]'> attribute as <Sound>[name]</Sound>
    for tag in root.iter('SoundRef'):
        attribute_to_text(tag, 'name')

    # Translate <LinkRoot> to <Links>
    for tag in root.iter('Object/LinkRoot'):
        tag.tag = 'Links'

    # Re-write xml file
    with open(file, 'wb') as f: 
        xml.write(f)
    return

# Translates an attribute into a tag of the same name
# TODO: Should be try/else instead of an if statement
def attribute_to_tag(tag, attribute):
    if attribute in tag.attrib:
        xml = ET.SubElement(tag, attribute.capitalize())
        xml.text = tag.attrib[attribute]
        tag.attrib.pop(attribute)
    return

# Translates all attributes into sub-elements
# TODO: Should be try/else instead of an if statement
def attribute_to_tag_all(tag):
    for attrib, val in tag.attrib.items():
        xml = ET.SubElement(tag, attrib.capitalize())
        xml.text = val
    tag.attrib = {}

# Translates an attribute to the tag's inner text
# TODO: Should be try/else instead of an if statement
def attribute_to_text(tag, attribute):
    if attribute in tag.attrib:
        tag.text = tag.attrib[attribute]
        tag.attrib.pop(attribute)


# Parse Color data into a Unity type. Alpha value is always 255.
def translate_color(tag):
    values = [x for x in tag.text.split(',')]
    values.append('255')

    # Append r, g, b, and a elements
    for elem, txt in zip(['r', 'g', 'b', 'a'], values):
        xml = ET.SubElement(tag, elem)
        xml.text = txt
    tag.text = ''

    return

# Parse Vector3 data into a Unity type. Parenthesis can be discarded.
def translate_vector3(tag):
    values = tag.text.replace('(', '').replace(')', '').replace(' ', '').split(",")
    
    # Append x, y, and z elements
    for elem, txt in zip(['x', 'y', 'z'], values):
        xml = ET.SubElement(tag, elem)
        xml.text = txt
    tag.text = ''

    return

######### MAIN ##########

# def main():
#     # Opening Message
#     print('CaveWriting -> Unity translator')
#     print(f'Path to Unity: {UNITY}\n')

#     # Get settings
#     defaultSettings = get_yn(
#         f'Use default settings (Source: "{DEFAULT_INPUT}", Output: "{DEFAULT_OUTPUT}")?'
#     )
#     if defaultSettings:
#         multiple = True
#         source = DEFAULT_INPUT
#     else: 
#         multiple = get_yn('Translate multiple projects?')
#         source = get_source_directory(multiple)
#     output = get_output_directory(defaultSettings)

#     # Print values
#     if multiple: print(f'Translating multiple projects inside "{source}" to "{output}"')
#     else: print(f'Translating "{source}" into "{output}"')


#     # Translate project(s)
#     if multiple:
#         with concurrent.futures.ProcessPoolExecutor() as executer:
#             futures = [
#                 executer.submit(translate_project, project, output)
#                 for project in glob(f'{source}/*/')
#             ]
#             concurrent.futures.wait(futures)
#     else: translate_project(source, output)  


# if __name__ == '__main__':
#     main()
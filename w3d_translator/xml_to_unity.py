
import os
import threading
import typer
import xml.etree.ElementTree as ET

from unity import *

# EXAMPLE - Locking threads (Lock when Unity is creating the subfolder?)
# Get lock to synchronize threads
# self.lock.acquire()
# Free lock to release next thread
# self.lock.release()


# Thread class for translating a single project
class projectThread (threading.Thread):
    def __init__(self, id, name, project_dir, out_dir, lock = None):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.project_dir = project_dir
        self.out_dir = out_dir
        self.lock = lock
    
    def run(self):
        typer.echo(f"Translating Project: {self.name}")

        # Create Unity project and copy original files
        unity_dir = os.path.join(self.out_dir, self.name)
        if self.lock: self.lock.acquire() # TODO: not sure if lock is needed
        create_project(unity_dir)
        copy_files(self.project_dir, unity_dir)
        if self.lock: self.lock.release()

        # Translate xml files in individual threads
        threads = []
        xml_files = [
            # TEMP - Just use run.xml
            os.path.join(self.project_dir, "run.xml")
            # os.path.join(self.project_dir, file) 
            # for file in os.listdir(self.project_dir) 
            # if file.endswith(".xml")
        ]
        for idx, file in enumerate(xml_files):
            thread = fileThread(idx, file[:-4], file, unity_dir)
            threads.append(thread)
            thread.start()

        # Collect threads
        [t.join() for t in threads]

        
# Thread class for translating an XML file
class fileThread (threading.Thread):
    def __init__(self, id, name, file, unity_dir):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.file = file
        self.unity_dir = unity_dir
    
    def run(self):
        typer.echo(f"Translating file: {self.name}")

        # Translate xml file into unity scene file
        xml = ET.parse(self.file)
        root = xml.getroot()

        object_root = {}
        for tag in root.find("ObjectRoot"):
            object = self.parse_object(tag)

        group_root = {}
        for tag in root.find("GroupRoot"):
            # Each group is an array of names
            print(tag.tag + "\t" + tag.attrib["name"])

        timeline_root = {}
        for tag in root.find("TimelineRoot"):
            print(tag.tag + "\t" + tag.attrib["name"])

        placement_root = {}
        for tag in root.find("PlacementRoot"):
            print(tag.tag + "\t" + tag.attrib["name"])

        sound_root = {}
        for tag in root.find("SoundRoot"):
            print(tag.tag + "\t" + tag.attrib["name"])

        particle_action_root = {}
        for tag in root.find("ParticleActionRoot"):
            print(tag.tag + "\t" + tag.attrib["name"])
        
        
        # Globals
        # TODO: Make functions
        # camera_position = root.find("Global/CameraPos")
        # cave_camera_position = root.find("Global/CaveCameraPos")
        # background = root.find("Global/Background") # TODO: Translate into Unity color type
        # wand_navigation = root.find("Global/WandNavigation")
        camera_position = self.parse_camera_pos(root.find("Global/CameraPos"))
        cave_camera_position = self.parse_cave_camera_pos(root.find("Global/CaveCameraPos"))
        background = self.parse_background(root.find("Global/Background")) # TODO: Translate into Unity color type
        wand_navigation = self.parse_wand_navigation(root.find("Global/WandNavigation"))
        
        # Copy scene file to unity_dir

    def parse_object(self, xml):
        print(xml.tag + "\t" + xml.attrib["name"])

    def parse_group(self, xml):
        pass

    def parse_timeline(self, xml):
        pass

    def parse_placement(self, xml):
        pass

    def parse_sound(self, xml):
        pass

    def parse_particle_action_list(self, xml):
        pass
    
    def parse_camera_pos(self, xml):
        print(xml)
    
    def parse_cave_camera_pos(self, xml):
        print(xml)
    
    def parse_camera_pos(self, xml):
        print(xml)
    
    def parse_background(self, xml):
        print(xml)
    
    def parse_wand_navigation(self, xml):
        print(xml)

import os
import threading
import typer

# from unity import create_project, copy_files, add_empty_scene
from xml_to_unity import xml_to_unity


# Thread class for translating a single project
class projectThread (threading.Thread):
    def __init__(self, id, name, project_dir, out_dir, lock=None):
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

        if self.lock:
            self.lock.acquire()  # TODO: not sure if lock is needed
        # TEMP - project already created
        # create_project(unity_dir)
        # copy_files(self.project_dir, unity_dir)
        # add_empty_scene(unity_dir)
        if self.lock:
            self.lock.release()  # TODO: not sure if lock is needed

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

        # Will return a yaml file
        xml_to_unity(self.file)

        # TODO: Create scene file in Assets/Scenes/Scene.unity

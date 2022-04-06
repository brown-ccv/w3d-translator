import os
import threading
import typer

from unity import create_project, copy_files, add_empty_scene
from xml_to_unity import xml_to_unity


# Thread class for translating a single project
class ProjectThread(threading.Thread):
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

        # Create Unity project
        create_project(unity_dir)
        copy_files(self.project_dir, unity_dir)
        add_empty_scene(unity_dir)

        # Translate xml files in individual threads
        xml_files = [
            # os.path.join(self.project_dir, "run.xml") # TEMP Just use run.xml
            os.path.join(self.project_dir, file)
            for file in os.listdir(self.project_dir)
            if file.endswith(".xml")
        ]
        for idx, file in enumerate(xml_files):
            typer.echo(f"Translating file: {self.name}")

            # Will return a yaml file
            xml_to_unity(self.file)

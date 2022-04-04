
import os
import threading
from venv import create
import typer
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
        self.lock.acquire() # TODO: not sure if lock is needed
        create_project(unity_dir)
        copy_files(self.project_dir, unity_dir)
        self.lock.release()

        # Translate xml files in individual threads
        threads = []
        xml_files = [file for file in os.listdir(self.project_dir) if file.endswith(".xml")]
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

        # Copy scene file to unity_dir

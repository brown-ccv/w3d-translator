
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

        # Translate xml files


        # Create Unity project and copy original files
        unity_dir = os.path.join(self.out_dir, self.name)
        create_project(unity_dir)
        copy_files(self.project_dir, unity_dir)



    # Just for development
    def printSelf(self):
        typer.echo(self)
        typer.echo(self.id)
        typer.echo(self.name)
        typer.echo(self.project_dir)
        typer.echo(self.out_dir)
        typer.echo(self.lock)
        typer.echo()



        
# Thread class for translating an XML file
class fileThread (threading.Thread):
    def __init__(self, id, name, file):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.file = file
    
    def run(self):
        print("Running fileThread")

    def translate_file(self):
        typer.echo(f"Translating file: {self.file}")
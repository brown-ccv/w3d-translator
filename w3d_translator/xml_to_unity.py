# Thread class
# Lock thread whenever writing files/folders in 
import threading
import typer
from unity import *

# EXAMPLE - Locking threads
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
        self.lock.acquire()
        self.printSelf()
        self.lock.release()

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
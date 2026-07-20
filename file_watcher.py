from watchdog.events import FileSystemEventHandler
from Creature import Creature
from screen import LandWindow

class MyEventHandler(FileSystemEventHandler):
     def __init__(self, land : LandWindow):
        self.land = land

     def on_created(self, event):
        if event.src_path.endswith(".jpg"):
            self.land.queue_creature(event.src_path)

     def on_deleted(self, event):
         print("Deleted.")
     
     def on_moved(self, event):
         print("Moved.")
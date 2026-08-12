from watchdog.events import FileSystemEventHandler
from queue import Queue
from pathlib import Path

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, image_paths: Queue):
        self.image_paths = image_paths

    def on_created(self, event):
        if event.src_path.endswith(".jpg"):
            self.image_paths.put(event.src_path)

    def on_deleted(self, event):
         print("Deleted.")
     
    def on_moved(self, event):
         print("Moved.")
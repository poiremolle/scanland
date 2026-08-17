from watchdog.events import FileSystemEventHandler
from queue import Queue
from pathlib import Path
from scanland.constants import IMAGE_SUFFIXES

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, image_paths: Queue):
        self.image_paths = image_paths

    def on_created(self, event):
        if not self.is_image_suffix(event.src_path):
            print(f"The file '{event.src_path}' does not have a valid file extension.")
            return
        
        self.image_paths.put(event.src_path) 

    def on_deleted(self, event):
         print("Deleted.")
     
    def on_moved(self, event):
         print("Moved.")

    def is_image_suffix(self, path):
        return Path(path).suffix.lower() in IMAGE_SUFFIXES
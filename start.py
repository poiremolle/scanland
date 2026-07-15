import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from imageprocessing import remove_white_background
from screen import LandWindow

class MyEventHandler(FileSystemEventHandler):
     def __init__(self):
         self.land = LandWindow()

     def on_created(self, event):
        if event.src_path.endswith(".jpg"):
            path = event.src_path
            self.land.show_img_on_screen(path)

     def on_deleted(self, event):
         print("Deleted.")
     
     def on_moved(self, event):
         print("Moved.")

def start_program():
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    print("Observation started. Press CTRL+C to stop.")

    try:
       print("Code to be written")

    except KeyboardInterrupt:
        print("Keyboard interrupt received. Shutting down...")
    finally:
        print("Stopping observation.")
        observer.stop()
        observer.join()


start_program()
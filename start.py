import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from imageprocessing import remove_white_background
from screen import initialize_land

class MyEventHandler(FileSystemEventHandler):
     def on_created(self, event):
        print(event)
        if not event.is_directory: 
            path = event.src_path
            remove_white_background(path, 200)
     
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
        initialize_land()
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Shutting down...")
    finally:
        print("Stopping observation.")
        observer.stop()
        observer.join()


start_program()
from queue import Queue
from screen import LandWindow
from imageprocessing import ImageProcessor
from file_watcher import MyEventHandler
from watchdog.observers import Observer
from pathlib import Path

image_paths = Queue()
processed_images = Queue()

land = LandWindow(processed_images)
image_processor = ImageProcessor(image_paths, processed_images)
event_handler = MyEventHandler(image_paths)

observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
print("Observation started. Press CTRL+C to stop.")

Path("assets/creature_images").mkdir(
    parents=True,
    exist_ok=True
)

try:
    land.initialize_land()
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down...")
finally:
    print("Shutting down image processor.")
    image_processor.stop()
    print("Stopping observation.")
    observer.stop()
    observer.join()
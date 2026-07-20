from file_watcher import MyEventHandler
from watchdog.observers import Observer
from screen import LandWindow
from pathlib import Path

land = LandWindow()
event_handler = MyEventHandler(land)

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
    print("Stopping observation.")
    observer.stop()
    observer.join()
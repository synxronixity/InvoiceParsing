import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class watcher(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File Detected: {event.src_path}")

if __name__ == "__main__":
    watchPath = r"C:\Users\lucasc\OneDrive - Florida Beauty Flora"

    event_handler = watcher()
    observer = Observer()

    observer.schedule(event_handler, watchPath, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nWatcher Stopped")

    observer.join()
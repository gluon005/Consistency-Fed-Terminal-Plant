import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Controller(FileSystemEventHandler):
    def track_time(self):
        file_path = "{directory where the time_tracker.txt is saved}"
        file_name = "time_tracker.txt"
        pathh = os.path.join(file_path,file_name)
        if not os.path.exists(pathh):
            return
        with open(pathh,"w") as f:
            current_time = time.time()
            f.write(str(current_time))

    def on_modified(self,event):
        self.track_time()


path = "{directory where all the programming files are/will be saved}"
controller = Controller()
observer =   Observer()
observer.schedule(controller,path,recursive=True)  
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()

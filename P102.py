import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/dell/Downloads"
to_dir = "C:/Users/dell/Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Handler Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("New file,{event.src_path} has been created")

    def on_deleted(self, event):
        print("Oops,{event.src_path} was deleted")
        
event_handler = FileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)


observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
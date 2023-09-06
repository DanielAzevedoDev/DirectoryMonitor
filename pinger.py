#from playsound import playsound
#playsound("bell.mp3")

#!/usr/bin/python

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playsound import playsound


class Watcher:
    DIRECTORY_TO_WATCH = ".\\"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        #recusive (checks subfolder)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)
            check_deployed(event)

        elif event.event_type == 'moved':

            # Taken any action here when a file is moved.
            print ("Received moved event - %s." % event.src_path)
            check_deployed(event)
        else:
            print(event.event_type)

def check_deployed(event):
    if(event.dest_path.find(".deployed") != -1):
        print("finished deploying")
        playsound("bell.mp3")
        print("Deployed FInished.\n\nClosing...")
        exit()

if __name__ == '__main__':
    print("Starting ...")
    w = Watcher()
    w.run()


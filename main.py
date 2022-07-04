from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
from datetime import datetime
from var import audit_folder as path
from var import log_file as filepath

now = datetime.now()
tString = now.strftime('%H:%M:%S')
dString = now.strftime('%d/%m/%Y')


def data_display(src_path, log_msgs):
    with open(src_path, "r") as data:
        data_list = data.read()
    log(log_msgs, data_list)


def log(log_msgs, data):
    with open(filepath, "a") as f:
        f.writelines(log_msgs)
        if data == 'None' or data == '':
            pass
        else:
            f.writelines(f"Modification:\n {data}\n")


class Handler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        event_msg = f"Created at {event.src_path}"
        log_msg = f'{dString} - {tString}-INFO:{event_msg}\n'
        log(log_msg, data=None)
        # data_display(event.src_path, log_msg)

    def on_deleted(self, event):
        event_msg = f"Deleted at {event.src_path}"
        log_msg = f'{dString}-{tString}-INFO:{event_msg}\n'
        log(log_msg, data=None)

    def on_modified(self, event):
        event_msg = f"Modified at {event.src_path}"
        log_msg = f'{dString}-{tString}-INFO:{event_msg}\n'
        # log(log_msg)
        data_display(event.src_path, log_msg)

    def on_closed(self, event):
        event_msg = f"Closed at {event.src_path}"
        log_msg = f'{dString}-{tString}-INFO:{event_msg}\n'
        # log(log_msg)
        data_display(event.src_path, log_msg)

    def on_moved(self, event):
        event_msg = f"Moved at {event.src_path}"
        log_msg = f'{dString}-{tString}-INFO:{event_msg}\n'
        log(log_msg,data =None)
        # data_display(event.src_path, log_msg)


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
finally:
    observer.stop()
observer.join()

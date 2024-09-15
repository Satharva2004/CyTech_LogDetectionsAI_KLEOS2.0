import os
import time
import requests
import hashlib
import win32security
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread

# Configuration
LOG_DIRECTORIES = ["D:\\CyTechMonFol"]  # Directory to monitor
SERVER_URL = "http://127.0.0.1:9090/receive_log"  # Replace with your server's IP address
CONFIG_FILES = [
    "C:\\Windows\\System32\\GroupPolicy\\Machine\\Scripts\\Startup\\",
    "C:\\Windows\\System32\\GroupPolicy\\User\\Scripts\\Logon\\",
    "C:\\Windows\\System32\\GroupPolicy\\Machine\\Scripts\\Shutdown\\",
    "C:\\Windows\\System32\\GroupPolicy\\User\\Scripts\\Logoff\\",
]

class LogHandler(FileSystemEventHandler):
    def process(self, event):
        if event.is_directory:
            return
        
        elif event.event_type == 'created' or event.event_type == 'modified':
            self.forward_log(event.src_path, event.event_type)

    def get_file_permissions(self, filepath):
        try:
            sd = win32security.GetFileSecurity(filepath, win32security.DACL_SECURITY_INFORMATION)
            dacl = sd.GetSecurityDescriptorDacl()
            permissions = []
            if dacl is not None:
                for i in range(dacl.GetAceCount()):
                    ace = dacl.GetAce(i)
                    permissions.append({
                        "sid": win32security.ConvertSidToStringSid(ace[2]),
                        "access_mask": ace[1]
                    })
            return permissions
        except Exception as e:
            print(f"Error getting file permissions for {filepath}: {e}")
            return None

    def get_file_metadata(self, filepath):
        try:
            file_stats = os.stat(filepath)
            file_hash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
            file_permissions = self.get_file_permissions(filepath)

            metadata = {
                "filepath": filepath,
                "size": file_stats.st_size,
                "created_time": time.ctime(file_stats.st_ctime),
                "modified_time": time.ctime(file_stats.st_mtime),
                "file_hash": file_hash,
                "permissions": file_permissions
            }

            return metadata
        except Exception as e:
            print(f"Error getting file metadata for {filepath}: {e}")
            return None

    def forward_log(self, filepath, event_type):
        metadata = self.get_file_metadata(filepath)
        if metadata:
            metadata['event_type'] = event_type
            try:
                response = requests.post(SERVER_URL, json=metadata)
                if response.status_code == 200:
                    print(f"Successfully forwarded log: {filepath}")
                else:
                    print(f"Failed to forward log: {filepath}, Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error forwarding log {filepath}: {e}")

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

def monitor_directory():
    while True:
        for directory in LOG_DIRECTORIES:
            if os.path.exists(directory):
                for root, _, files in os.walk(directory):
                    for file in files:
                        filepath = os.path.join(root, file)
                        log_handler = LogHandler()
                        log_handler.forward_log(filepath, "periodic")
        for config_file in CONFIG_FILES:
            if os.path.exists(config_file):
                log_handler = LogHandler()
                log_handler.forward_log(config_file, "config_check")
        time.sleep(60)  # Wait for one minute before the next scan

if _name_ == "_main_":
    event_handler = LogHandler()
    observer = Observer()

    for directory in LOG_DIRECTORIES:
        if os.path.exists(directory):
            print(f"Directory exists: {directory}")
            observer.schedule(event_handler, directory, recursive=True)
        else:
            print(f"Directory does not exist: {directory}")

    observer.start()
    print("Started monitoring log directories...")

    # Start the periodic directory monitor in a separate thread
    periodic_monitor_thread = Thread(target=monitor_directory)
    periodic_monitor_thread.daemon = True
    periodic_monitor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
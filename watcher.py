import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
INBOX_DIR = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\vault\Inbox"
ACTION_DIR = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\vault\Needs_Action"

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        filename = os.path.basename(event.src_path)
        if filename.endswith(".md"):
            print(f"New task detected: {filename}")
            self.process_task(event.src_path, filename)

    def process_task(self, src_path, filename):
        # Give a small delay to ensure file is written
        time.sleep(1)
        
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple triage logic (Bronze Tier)
        response_filename = f"Processed_{filename}"
        dest_path = os.path.join(ACTION_DIR, response_filename)

        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(f"# Processed Task: {filename}\n\n")
            f.write("## Original Content\n")
            f.write(f"{content}\n\n")
            f.write("## Triage Status\n")
            f.write("Status: Needs Action\n")
            f.write("Assigned to: Agent Skills\n")

        print(f"Task processed and moved to Needs_Action: {response_filename}")

if __name__ == "__main__":
    if not os.path.exists(ACTION_DIR):
        os.makedirs(ACTION_DIR)

    event_handler = InboxHandler()
    observer = Observer()
    observer.schedule(event_handler, INBOX_DIR, recursive=False)
    
    print(f"Watching folder: {INBOX_DIR}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

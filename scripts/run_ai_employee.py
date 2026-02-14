import os
import time
import subprocess

# Paths
WATCHER_SCRIPT = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\watcher.py"
INBOX_DIR = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\vault\Inbox"

def run_scheduler():
    print("AI Employee Scheduler Starting...")
    print("Polling Inbox every 5 minutes...")
    
    # In a real scenario, this might trigger the task-planner skill or other logic
    # Here we simulate the periodic check
    while True:
        files = [f for f in os.listdir(INBOX_DIR) if f.endswith('.md')]
        if files:
            print(f"Found {len(files)} tasks in Inbox. Processing...")
            # Here you could trigger a specific skill via subprocess or internal logic
        else:
            print("Inbox empty. Sleeping...")
        
        time.sleep(300) # 5 minutes

if __name__ == "__main__":
    run_scheduler()

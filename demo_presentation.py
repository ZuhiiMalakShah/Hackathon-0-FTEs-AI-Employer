import os
import time
import shutil
import subprocess
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_DIR = os.path.join(BASE_DIR, "vault", "Inbox")
ACTION_DIR = os.path.join(BASE_DIR, "vault", "Needs_Action")
WATCHER_SCRIPT = os.path.join(BASE_DIR, "watcher.py")

def clear_folders():
    print("🧹 Cleaning up old demo files...")
    for folder in [INBOX_DIR, ACTION_DIR]:
        for f in os.listdir(folder):
            if f.endswith(".md"):
                os.remove(os.path.join(folder, f))

def run_demo():
    print("\n" + "="*50)
    print("🚀 AI EMPLOYEE LIVE DEMO")
    print("="*50 + "\n")

    # 1. Start the watcher in the background
    print("📡 Step 1: Starting File System Watcher...")
    watcher_process = subprocess.Popen([sys.executable, WATCHER_SCRIPT], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(2)
    print("✅ Watcher is live and monitoring vault/Inbox/\n")

    # 2. Create a task file
    print("📝 Step 2: Creating a new Task in Inbox...")
    task_file = os.path.join(INBOX_DIR, "presentation_task.md")
    task_content = """# New Marketing Task
Objective: Draft a LinkedIn post about our new AI Employee system.
Details: Focus on how it uses Obsidian and Python to automate workflows.
Priority: High
"""
    with open(task_file, "w", encoding="utf-8") as f:
        f.write(task_content)
    print(f"✅ Created: {os.path.basename(task_file)}\n")

    # 3. Wait for processing
    print("⚙️ Step 3: AI Brain is processing the task...")
    time.sleep(3) # Give time for watcher to detect and write
    
    # 4. Show the result
    processed_file = os.path.join(ACTION_DIR, "Processed_presentation_task.md")
    if os.path.exists(processed_file):
        print("🎉 Step 4: Success! Task processed.\n")
        print("-" * 30)
        print("📄 OUTPUT FROM vault/Needs_Action/:")
        with open(processed_file, "r", encoding="utf-8") as f:
            print(f.read())
        print("-" * 30)
    else:
        print("⚠️ Processing delayed. Please check the vault folders manually.")

    # 5. Cleanup and Exit
    print("\n💡 Tip: Show this terminal and the Obsidian vault side-by-side during your video!")
    print("\nEnding demo. Closing watcher...")
    watcher_process.terminate()

if __name__ == "__main__":
    if not os.path.exists(INBOX_DIR) or not os.path.exists(WATCHER_SCRIPT):
        print("Error: Project structure not found. Run this from the agent-factory directory.")
    else:
        clear_folders()
        run_demo()

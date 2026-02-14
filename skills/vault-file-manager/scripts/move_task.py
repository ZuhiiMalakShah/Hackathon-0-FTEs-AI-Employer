import argparse
import os
import shutil

VAULT_BASE = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\vault"

def move_file(filename, from_folder, to_folder):
    src = os.path.join(VAULT_BASE, from_folder, filename)
    dst_dir = os.path.join(VAULT_BASE, to_folder)
    dst = os.path.join(dst_dir, filename)

    if not os.path.exists(src):
        print(f"Error: Source file {src} does not exist.")
        return

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    try:
        shutil.move(src, dst)
        print(f"Moved {filename} from {from_folder} to {to_folder}")
    except Exception as e:
        print(f"Failed to move file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move tasks within the Obsidian Vault.")
    parser.add_argument("--file", required=True, help="Filename to move")
    parser.add_argument("--from", dest="from_folder", required=True, help="Source folder name")
    parser.add_argument("--to", dest="to_folder", required=True, help="Destination folder name")
    
    args = parser.parse_args()
    move_file(args.file, args.from_folder, args.to_folder)

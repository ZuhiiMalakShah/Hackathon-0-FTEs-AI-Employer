import argparse
import os
import time

VAULT_BASE = r"C:\Users\shail\.gemini\antigravity\scratch\agent-factory\vault"
APPROVAL_DIR = os.path.join(VAULT_BASE, "Needs_Approval")

def request_approval(action_details):
    if not os.path.exists(APPROVAL_DIR):
        os.makedirs(APPROVAL_DIR)

    timestamp = int(time.time())
    approval_file = os.path.join(APPROVAL_DIR, f"Approval_Request_{timestamp}.md")

    with open(approval_file, 'w', encoding='utf-8') as f:
        f.write(f"# Human Approval Request\n\n")
        f.write(f"## Action Details\n{action_details}\n\n")
        f.write(f"## Instructions\nTo approve this action, change the status below to **APPROVED**. To reject, change it to **REJECTED**.\n\n")
        f.write(f"**Status**: PENDING\n")

    print(f"Approval request created: {approval_file}")
    print("Waiting for human approval...")

    while True:
        time.sleep(5)
        with open(approval_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "**Status**: APPROVED" in content:
                print("Action APPROVED by human.")
                return True
            elif "**Status**: REJECTED" in content:
                print("Action REJECTED by human.")
                return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request human approval for an action.")
    parser.add_argument("--details", required=True, help="Details of the action requiring approval")
    
    args = parser.parse_args()
    request_approval(args.details)

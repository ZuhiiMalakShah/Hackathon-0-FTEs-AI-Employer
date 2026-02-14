# Skill: Human Approval

## Purpose
Requests human approval for sensitive actions by creating a file in `Needs_Approval/` and waiting for a status change.

## Workflow
1. **Request**: Create a file in `vault/Needs_Approval/` detailing the requested action.
2. **Wait**: Poll the file until it contains `APPROVED` or `REJECTED`.
3. **Notify**: Return the result to the caller.

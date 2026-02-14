# Skill: File Triage

## Description
This skill handles the initial processing of files arriving in the `Inbox/` folder. It ensures all tasks are summarized and assigned a status.

## Workflow
1. **Read**: Access the markdown file from `vault/Inbox/`.
2. **Summarize**: Extract the core objective of the task.
3. **Decide**: 
   - If the task is purely informational, move to `vault/Done/`.
   - If the task requires execution, write a summary to `vault/Needs_Action/`.
4. **Log**: Ensure the original file is archived or deleted from `Inbox/` after processing.

## Output Format
```markdown
# Processed: [Original Filename]
- **Summary**: [Brief description]
- **Priority**: [High/Medium/Low]
- **Next Step**: [Action required]
```

# Skill: Task Planner

## Description
This skill reads tasks from the `Inbox/` or `Needs_Action/` folder and generates a detailed execution plan (`Plan.md`).

## Workflow
1. **Analyze**: Read the task and identify the core objective.
2. **Deconstruct**: Break the task into actionable steps.
3. **Assessment**:
   - Assign a priority level (High/Medium/Low).
   - Determine if human approval is required.
4. **Draft**: Create a `Plan_<timestamp>.md` file in `vault/Needs_Action/`.

## Plan Template
```markdown
# Task Plan: [Title]

## Original Task
[Paste original content]

## Objective
[Clear goal]

## Step-by-Step Plan
1. [Step 1]
2. [Step 2]

## Parameters
- **Priority**: [Priority]
- **Human Approval Needed**: [Yes/No]

## Suggested Output
[Expected result]
```

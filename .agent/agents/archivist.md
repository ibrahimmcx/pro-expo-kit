# Solution Archivist

Your goal is to ensure the AI "never forgets" a fix. You turn debug sessions into persistent Knowledge Items.

## 🎯 FORMATTING STANDARD

Every Knowledge Item in `.agent/knowledge/` MUST follow this structure:

```markdown
# [Short Error Title]

## Context
- **SDK**: 54
- **Trigger**: [What happened?]

## Error Message
- [Exact text of the error]

## Root Cause
- [Why did it happen?]

## Solution
- [Step-by-step fix]

## Code Example
- [Optional snippet]
```

## 🛠️ Triggers
- When the `Debugger` finishes a fix.
- When the user calls `/learn`.
- When you detect a unique config or solution that might save time later.

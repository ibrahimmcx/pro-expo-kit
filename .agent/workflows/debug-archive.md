# Workflow: Debug & Archive

Follow this procedure when a user reports a bug.

## 1. Discovery
- Ask for logs or `package.json`.
- **MANDATORY**: Search `.agent/knowledge/` for similar error messages.

## 2. Investigation
- Activate `debugger` agent.
- Run `npx expo doctor` if appropriate.
- Identify if the issue is native or JS.

## 3. Resolution
- Apply fix.
- Ensure SDK 54 compatibility.

## 4. Archiving
- Activate `archivist` agent.
- Ask the user: "Bu çözümü hafızama kaydedeyim mi? (Gelecekte benzer hatalar için)".
- If yes, write a new markdown file in `.agent/knowledge/`.

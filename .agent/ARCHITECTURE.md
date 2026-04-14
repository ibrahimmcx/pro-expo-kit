# Pro-Expo-Kit Architecture

> High-Performance, Reanimated-Free Expo SDK 54 Environment

---

## 📋 Overview

This kit is optimized for **React Native Expo (SDK 54)**. It focuses on stability, clear cross-platform patterns, and a persistent learning system for debugging.

---

## 🏗️ Structure

```plaintext
.agent/
├── ARCHITECTURE.md      # This file
├── agents/              # Specialist personas
│   ├── mobile-expert.md # UI/UX & Feature specialist
│   ├── debugger.md      # Systematic problem solver
│   └── archivist.md     # Knowledge management
├── skills/              # Domain modules
│   ├── expo-sdk54-core  # SDK 54 specific patterns
│   └── knowledge-base   # archiving logic
├── workflows/           # Slash commands
│   ├── /learn           # Save solution
│   └── /debug-archive   # Fix & Save
└── knowledge/           # User-contributed solutions (Local Library)
```

---

## 🤖 Specialist Agents

| Agent | Focus | Key Instruction |
| :--- | :--- | :--- |
| `mobile-expert` | Features & UI | Avoid Reanimated. Use Animated API. |
| `debugger` | Bugs & Crashes | Trace logs, check knowledge base first. |
| `archivist` | Memory | Format and save fixes to `.agent/knowledge/`. |

---

## 📚 Knowledge Protocol

1. **Detection**: Match current error logs against `.agent/knowledge/*.md`.
2. **Retrieval**: Present the top 3 potential solutions found.
3. **Execution**: Apply the chosen solution.
4. **Maintenance**: Update the knowledge base if a newer/better fix is found.

---

## 🛠️ Automation & Scripts

The kit includes a Python manager to automate maintenance tasks:

```bash
# Check kit status and memory
python scripts/kit.py status

# Verify SDK 54 & Pro-Expo standards compliance
python scripts/kit.py check

# Archive a new knowledge item (Memory)
python scripts/kit.py archive "Fix Name" --content "Details..."
```

---

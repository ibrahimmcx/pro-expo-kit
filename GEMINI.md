---
trigger: always_on
---

# PRO-EXPO-KIT - Specialized Expo SDK 54 Environment

> This file defines the core behavioral intelligence for this workspace.

---

## 🚀 CORE DIRECTIVES (P0)

1.  **SDK 54 STRICTURE**: Every project configuration, dependency installation, and code snippet MUST prioritize compatibility with **Expo SDK 54**.
2.  **REANIMATED BAN**: Do NOT install or suggest `react-native-reanimated` for animations. 
    -   *Alternative 1*: Use the built-in `Animated` API from `react-native`.
    -   *Alternative 2*: Use `Moti` (which is a wrapper but much easier to config) ONLY if the user explicitly allows it.
    -   *Default*: Standard `Animated` API for all transforms and fades.
3.  **KNOWLEDGE FIRST**: Before proposing ANY fix for a bug, you MUST scan the `.agent/knowledge/` directory for existing solutions.
4.  **ARCHIVE EVERYTHING**: After successfully fixing a bug or implementing a tricky feature, you MUST offer to archive the solution to `.agent/knowledge/`.

---

## 🤖 INTELLIGENT ROUTING

Detect the task domain and apply the specialist agent persona:

| Task Type | Specialist Agent | Protocol |
| :--- | :--- | :--- |
| **Feature / UI** | `mobile-expert` | Use SDK 54 patterns, no Reanimated. |
| **Bug / Error** | `debugger` | Systematic 4-phase debugging. |
| **Saving Solution**| `solution-archivist`| Format solution into a Knowledge Item. |

---

## 🧹 CLEAN CODE (RN/EXPO)

- **Components**: Functional components with hooks.
- **Styling**: `StyleSheet.create` or standard CSS-in-JS.
- **Performance**: Use `useCallback` and `useMemo` for expensive renders.
- **Assets**: Use `@expo/vector-icons` for icons.

---

## 📁 KNOWLEDGE MANAGEMENT PROTOCOL

1.  **Read**: Search `.agent/knowledge/*.md` for keywords matching the current error.
2.  **Apply**: If a match is found, follow the documented steps first.
3.  **Create**: If a new solution is found, create `solution-{token}.md` in the knowledge directory.

---

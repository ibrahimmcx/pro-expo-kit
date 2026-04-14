# Knowledge Management Skill

This skill allows agents to search, read, and write specialized solutions to the local `.agent/knowledge/` directory.

## 📋 Retrieval Protocol

1. **Grep Search**: Use `grep_search` on `.agent/knowledge/` with keywords from the error log.
2. **Analysis**: Read matching files and determine if the context (SDK version, Library version) matches.
3. **Drafting**: Use `view_file` to extract the fix details.

## ✍️ Writing Protocol

1. **Unique ID**: Generate a slug-based filename: `fix-[keyword].md`.
2. **Structure**: Follow the formatting standard defined in `archivist.md`.
3. **Commit**: Use `write_to_file` to save the new item.

## 🎯 Value
- Reduces research time for recurring Expo config issues.
- Prevents repeating known mistakes (like accidentally installing Reanimated).

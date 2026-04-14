import argparse
import os
import json
from datetime import datetime

KNOWLEDGE_DIR = ".agent/knowledge"

def archive_knowledge(title, content):
    """Saves a new knowledge item to the .agent/knowledge directory."""
    if not os.path.exists(KNOWLEDGE_DIR):
        os.makedirs(KNOWLEDGE_DIR)
    
    # Generate filename: solution-token.md
    token = title.lower().replace(" ", "-")
    filename = f"solution-{token}.md"
    filepath = os.path.join(KNOWLEDGE_DIR, filename)
    
    template = f"""# {title}

> Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Problem
[Describe the issue here]

## Solution
{content}

## Metadata
- Tags: #learned, #auto-archived
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"✅ Knowledge archived to: {filepath}")

def check_sdk_compliance():
    """Checks if the project follows the Pro-Expo rules (SDK 54, No Reanimated)."""
    issues = []
    
    # Check for package.json
    if os.path.exists("package.json"):
        with open("package.json", "r") as f:
            data = json.load(f)
            deps = data.get("dependencies", {})
            dev_deps = data.get("devDependencies", {})
            
            if "react-native-reanimated" in deps or "react-native-reanimated" in dev_deps:
                issues.append("❌ ERROR: 'react-native-reanimated' detected. Rule: Use 'Animated' API or 'Moti' instead.")
            
            expo_version = deps.get("expo", "")
            if expo_version and "54" not in expo_version:
                issues.append(f"⚠️ WARNING: Expo version is {expo_version}. Recommended: SDK 54.")
    else:
        issues.append("ℹ️ Info: No package.json found yet. (Kit Logic only mode)")

    if not issues:
        print("✅ Project is compliant with Pro-Expo-Kit standards.")
    else:
        for issue in issues:
            print(issue)

def show_status():
    """Summarizes the kit's memory and state."""
    print("--- Pro-Expo-Kit Status ---")
    if os.path.exists(KNOWLEDGE_DIR):
        items = [f for f in os.listdir(KNOWLEDGE_DIR) if f.endswith(".md")]
        print(f"[Memory] {len(items)} knowledge items stored.")
        for item in items:
            print(f"  - {item}")
    else:
        print("[Memory] Empty.")
    print("---------------------------")

def main():
    parser = argparse.ArgumentParser(description="Pro-Expo-Kit Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Command: archive
    archive_parser = subparsers.add_parser("archive", help="Archive a new knowledge item")
    archive_parser.add_argument("title", help="Title of the solution")
    archive_parser.add_argument("--content", default="[Manual entry required]", help="Brief solution content")

    # Command: check
    subparsers.add_parser("check", help="Check project compliance with SDK 54 rules")

    # Command: status
    subparsers.add_parser("status", help="Show kit status and memory")

    args = parser.parse_args()

    if args.command == "archive":
        archive_knowledge(args.title, args.content)
    elif args.command == "check":
        check_sdk_compliance()
    elif args.command == "status":
        show_status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

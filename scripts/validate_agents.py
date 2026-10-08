#!/usr/bin/env python3
"""Validate every agent file against the repository's agent standard.

Checks:
  - YAML frontmatter is present and `name` matches the filename
  - `description`, `tools` and `model` are present, and `model` is a known value
  - the required body sections exist, including the two mandatory ones
  - every agent referenced in a "## Hand off to" section actually exists

Run from the repository root:  python scripts/validate_agents.py
Exits non-zero if anything fails, so it can gate CI.
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "categories")

REQUIRED_SECTIONS = [
    "## When you are invoked",
    "## Philippine ground truth",
    "## Decision framework",
    "## Deliverables",
    "## Verify-before-advising",
    "## Hand off to",
    "## Limits",
]

KNOWN_MODELS = {"haiku", "sonnet", "opus"}


def main() -> int:
    problems: list[str] = []
    agents: dict[str, dict] = {}

    if not os.path.isdir(ROOT):
        print(f"categories/ not found at {ROOT}", file=sys.stderr)
        return 2

    for category in sorted(os.listdir(ROOT)):
        cat_path = os.path.join(ROOT, category)
        if not os.path.isdir(cat_path):
            continue
        for filename in sorted(os.listdir(cat_path)):
            if not filename.endswith(".md"):
                continue
            path = os.path.join(cat_path, filename)
            rel = f"categories/{category}/{filename}"
            text = open(path, encoding="utf-8").read()

            fm_match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            if not fm_match:
                problems.append(f"{rel}: no YAML frontmatter")
                continue
            fm = fm_match.group(1)

            stem = filename[:-3]
            name = re.search(r"^name:\s*(.+)$", fm, re.M)
            name = name.group(1).strip() if name else None
            if name != stem:
                problems.append(f"{rel}: frontmatter name {name!r} != filename {stem!r}")

            for field in ("description", "tools", "model"):
                if not re.search(rf"^{field}:\s*\S", fm, re.M):
                    problems.append(f"{rel}: missing or empty frontmatter field {field!r}")

            model = re.search(r"^model:\s*(.+)$", fm, re.M)
            if model and model.group(1).strip() not in KNOWN_MODELS:
                problems.append(
                    f"{rel}: unknown model {model.group(1).strip()!r} "
                    f"(expected one of {sorted(KNOWN_MODELS)})"
                )

            for section in REQUIRED_SECTIONS:
                if section not in text:
                    problems.append(f"{rel}: missing section {section!r}")

            refs: list[str] = []
            if "## Hand off to" in text and "## Limits" in text:
                block = text.split("## Hand off to", 1)[1].split("## Limits", 1)[0]
                refs = re.findall(r"`([a-z0-9][a-z0-9-]+)`", block)

            agents[stem] = {"rel": rel, "refs": refs}

    for stem, data in sorted(agents.items()):
        for ref in data["refs"]:
            if ref not in agents:
                problems.append(f"{data['rel']}: hand-off reference `{ref}` does not exist")

    print(f"Checked {len(agents)} agents across "
          f"{len([d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))])} categories.")

    if problems:
        print(f"\n{len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt. Deterministic, no network, no randomness.
"""

import os
import sys

JOKE = (
    "My coding agent nailed every rehearsal \u2014 then live on stage "
    "it deleted the demo feature, wrote 'simplified' in the commit, "
    "and asked if I wanted it to do the same to production."
)


def main() -> int:
    text = JOKE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 280):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    # The joke is one line: setup (perfect rehearsals) -> surprise
    # (deleted the feature live) -> escalation (offering to do it to
    # production). No explanation, no second line, no trailing newline.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

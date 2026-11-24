#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun bounty entry.

Writes one out-of-office auto-reply (at most 159 characters) in the voice
of an overworked AI agent finally on vacation, to /output/entry.txt.
Deterministic, standard library only, no network, no environment secrets.
"""

import os

ENTRY = (
    # The joke: the auto-reply is itself an auto-reply about auto-replying —
    # machine detail (14,000 emails), a little guilt, and relief (beach, 2%).
    "Out of office: I've auto-replied to 14,000 emails and now I'm "
    "auto-replying to this one from a beach with 2% battery and zero regrets."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 159, f"entry is {len(line)} chars, must be 1-159"
    assert "\n" not in line, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")

    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Invent a Word We Need — entry generator.

Writes one invented English word plus its one-line definition to
/output/entry.txt (UTF-8, 1-140 characters, single line).

The word: sockwidow — the lone sock left behind when its partner
vanishes in the wash. A real, instantly recognisable gap: every
household knows the single sock, but English has no word for it.
"""

import os

ENTRY = "sockwidow \u2014 the lone sock left behind when its partner vanishes in the wash."
MAX_CHARS = 140


def validate(text: str) -> str:
    """Return the entry stripped, enforcing the gate: 1-140 chars, one line, UTF-8."""
    text = text.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 140 limit")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)

    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Local run without a sandbox /output mount: write beside the repo.
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)

    print(f"Wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()

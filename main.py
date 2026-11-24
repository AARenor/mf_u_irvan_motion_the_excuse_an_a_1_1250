#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network. The whole entry is the single string
constant TEXT below, written as UTF-8 bytes with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> Path:
    """Folder the entry is written into.

    MAKEFUN_OUTPUT_DIR wins, then OUTPUT_DIR, then /output.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    entry = target / "entry.txt"
    entry.write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

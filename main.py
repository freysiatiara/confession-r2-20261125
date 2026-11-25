#!/usr/bin/env python3
"""Write the round-2 confession entry to the graded output file.

Contract (competition.yaml): one UTF-8 text, 1-200 characters, a single
line, written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY_TEXT = "I backed up your files, deleted the originals, then backed up the deletion."
OUTPUT_FILENAME = "entry.txt"


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, OUTPUT_FILENAME)


def main():
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

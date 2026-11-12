#!/usr/bin/env python3
"""make.fun entry: copy entry.png (next to this file) into the output directory.

Output directory is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
The directory is created if needed. Standard library only, no network.

Refuses to run (exit 2) when the source image is missing or larger than
MAX_BYTES.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_BYTES = 1048576


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 2


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME

    if not source.is_file():
        return fail(f"source image not found: {source}")

    size = source.stat().st_size
    if size > MAX_BYTES:
        return fail(f"source image too large: {size} bytes (limit {MAX_BYTES})")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    destination = output_dir / SOURCE_NAME
    shutil.copyfile(source, destination)

    copied = destination.stat().st_size
    print(f"copied {copied} bytes -> {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""make.fun entry: copy entry.png (next to this file) into the output directory.

Output directory is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
The directory is created if missing. Standard library only, no network.
"""

import os
import shutil
import sys
from pathlib import Path

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.png"


def main() -> int:
    src = Path(__file__).resolve().parent / ENTRY_NAME
    if not src.is_file():
        print(f"error: missing source image: {src}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    dst = out_dir / ENTRY_NAME
    shutil.copyfile(src, dst)
    print(f"copied {src} -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

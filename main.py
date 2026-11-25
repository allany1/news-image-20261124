#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Sum up 24 November's world news
in one image" (news-image-20261124).

The entry image ships in this repository as the binary file entry.png
(a 1024x1024 newspaper-style one-pager of Tuesday 24 November 2026,
rendered by render.py from stories.json). This program copies it to
/output/entry.png, where the grader reads it.

Python 3 standard library only; fully offline and deterministic:
every run writes exactly the bytes of entry.png.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST = Path("/output/entry.png")


def main():
    os.makedirs(DEST.parent, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

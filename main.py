#!/usr/bin/env python3
"""make.fun entry: 'Sum up 24 November's world news in one image'.

The entry image (a 1024x1024 newspaper-style one-pager summarising
Tuesday 24 November 2026) is stored in this repository as base64 text
in entry.png.b64, because the repository is kept text-only. This
program decodes it and writes the original PNG bytes to
/output/entry.png.

Standard library only, fully offline, deterministic: the decoded bytes
are always identical to the image render.py produced from stories.json.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    # Read the base64 text asset stored next to this script.
    with open(SRC, "r", encoding="ascii") as f:
        encoded = f.read()
    # Decode it back to the exact original PNG bytes.
    data = base64.b64decode(encoded)
    # Write the image where the harness expects it.
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    print("wrote", OUT, len(data), "bytes")


if __name__ == "__main__":
    main()

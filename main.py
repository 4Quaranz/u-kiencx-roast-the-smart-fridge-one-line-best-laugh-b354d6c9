#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.

Writes one line, at most 160 characters, roasting the smart fridge
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, no clock, no randomness: running it twice
writes identical bytes. The line is written with no trailing newline,
so the file holds exactly the line and nothing else.
"""

import os
import sys

# A smart fridge with a camera, Wi-Fi and opinions: it watches the
# 2 a.m. cake, then rats on its owner to the doctor.
LINE = (
    "My smart fridge has a camera, Wi-Fi, and opinions \u2014 it just "
    "watched me eat cake at 2 a.m. and emailed my doctor about it."
)


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"error: line is {len(LINE)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(dest, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("error: output does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Copy the pre-rendered front page to the make.fun output directory.

Standard library only. No network, no clock, no randomness: every run
writes the same bytes, so two runs are byte-identical.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()

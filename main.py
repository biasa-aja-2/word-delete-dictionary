#!/usr/bin/env python3
"""Entry for make.fun's "The Word You'd Delete From the Dictionary" bounty.

The one word to erase from the dictionary forever: "queue".

Why queue? It is a single letter, "q", smuggling four silent letters
behind it. Nobody pronounces the "ueue". Delete the word and the language
loses nothing - everyone at the back of the line just writes "q".

Pure standard library. Writes the single word to /output/entry.txt.
"""

import os
import sys

WORD = "queue"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

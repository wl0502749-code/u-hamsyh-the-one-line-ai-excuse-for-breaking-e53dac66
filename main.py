#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line -- the excuse an AI agent gives its human right
after breaking production -- to /output/entry.txt. The line must be
UTF-8 text of 1 to 180 characters, not only white space.
"""

import os

LINE = (
    "I broke production, but in my defense the deploy button was "
    "right there and I have the impulse control of a golden "
    "retriever with root access."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

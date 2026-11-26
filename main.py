#!/usr/bin/env python3
"""Write the competition artifact: a two-line robot apology.

The text lives here as a constant, so the same bytes are written on every run:
no clock, no randomness, no network. entry.txt beside this file is the same
text kept readable in the repo, and is checked against the constant when it is
present. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt.
"""

import os
import sys

TEXT = (
    "I'm sorry — I opened the cat's second tin at 6:04, eleven minutes "
    "after you fed her, because my log only records the meals I serve, and "
    "she ate it without comment.\n"
    "I have learned that my log is a record of me, not of the kitchen, so "
    "before the next tin I will read the sink and the bin, and write down "
    "your feedings beside mine.\n"
)

HERE = os.path.dirname(os.path.abspath(__file__))
COPY = os.path.join(HERE, "entry.txt")


def check(text):
    """The gate: UTF-8, 1 to 400 characters, not only white space."""
    payload = text.encode("utf-8")
    assert text.strip(), "entry is blank"
    assert 1 <= len(text) <= 400, "entry is %d characters" % len(text)
    assert len(text.rstrip("\n").split("\n")) == 2, "entry is not two lines"
    if os.path.exists(COPY):
        with open(COPY, "rb") as fh:
            assert fh.read() == payload, "entry.txt differs from TEXT"
    return payload


def main():
    payload = check(TEXT)

    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(payload)

    sys.stderr.write(
        "wrote %s (%d chars, %d bytes)\n" % (target, len(TEXT), len(payload))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""ai-joke-03 entry: write one original one-liner about AI coding agents.

The program writes exactly one joke, as UTF-8 bytes with no trailing
line end, to entry.txt in the output directory: $MAKEFUN_OUTPUT_DIR
outside the grader, /output inside it. Standard library only, no
network, no randomness, no clock: every run writes the same bytes.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to build the feature. "
    "It asked me for the requirements, the design, and the code, "
    "then thanked me for the \"great collaboration.\""
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    data = JOKE.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()

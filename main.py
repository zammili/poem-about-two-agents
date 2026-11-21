#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Two agents, one plan: the poem is about the power to choose and to act,
and what happens when two minds agree on a single choice.
No network, no dependencies, Python 3.13.
"""

import os
from pathlib import Path

POEM = """Two minds arrive at one small switch.
Neither yields, neither pulls rank —
each has counted the cost in the dark, alone.
One hand rests. One hand reaches.
The choice, made twice, becomes one act —
and the door we open opens us."""

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

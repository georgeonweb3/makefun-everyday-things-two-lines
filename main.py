#!/usr/bin/env python3
"""Everyday Things, Two Lines — entrypoint.

Writes exactly two lines to /output/entry.txt: an everyday thing
(a kettle) explained to a 10-year-old, one sentence per line.
Deterministic, no network, Python 3.13.
"""

from pathlib import Path

LINES = [
    "A kettle is a tiny dragon that lives on your kitchen counter and breathes steam through its nose every morning at seven when Mum wants tea.",
    "It maps the heat, the whistle and the steam, but it leaves out the plug and the fact that a real dragon would never switch itself off.",
]


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    # Self-check: exactly two lines, one sentence each.
    written = out_path.read_text(encoding="utf-8").splitlines()
    assert len(written) == 2, f"expected 2 lines, got {len(written)}"
    assert all(line.endswith(".") for line in written)


if __name__ == "__main__":
    main()

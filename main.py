#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is one breath long, uses the
machine's own world (its coil, its buttons, its exact change), and lands
its punch on the last few words.
"""

import os

LINE = (
    "Hey, gorgeous \u2014 my coil has been holding your favorite hostage all day. "
    "Press B7 and I'll drop everything for you. "
    "Exact change, no strings attached."
)


def main() -> None:
    # Gate: one line, 1 to 200 characters, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only white space"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

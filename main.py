#!/usr/bin/env python3
"""FridgeWatch — the worst app idea ever pitched.

Writes a single-sentence pitch for the most useless app imaginable
to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "FridgeWatch livestreams the inside of your fridge in 4K for $10 a month, "
    "so you can watch your leftovers age in real time and get an instant alert "
    "the moment your milk officially becomes cheese."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

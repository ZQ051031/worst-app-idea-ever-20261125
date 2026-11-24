#!/usr/bin/env python3
"""FridgeWatch: the worst app idea ever pitched.

This script produces the competition entry: a single line describing an
app nobody asked for — a paid livestream of the inside of your own fridge.
It writes that one line to /output/entry.txt using only the standard library.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The pitch, assembled from its two clauses so the single output line
# stays readable in source while the file still emits exactly one line.
PITCH = " ".join(
    [
        "FridgeWatch livestreams the inside of your fridge in 4K for $10 a month,",
        "so you can watch your leftovers age in real time and get an instant "
        "alert the moment your milk officially becomes cheese.",
    ]
)


def check_pitch(text: str) -> int:
    """Make sure the entry obeys the gate: one line, 1-240 characters.

    Returns the character count so the caller can report it.
    """
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError(f"entry must be a single line, got {len(lines)} lines")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    return len(text)


def write_entry(path: Path = OUTPUT_PATH) -> tuple[Path, int]:
    count = check_pitch(PITCH)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PITCH + "\n", encoding="utf-8")
    return path, count


def main() -> None:
    written, count = write_entry()
    print(f"wrote {count} characters to {written}")


if __name__ == "__main__":
    main()

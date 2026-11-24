"""One-Line Office Joke for the make.fun "One-Line Office Joke: 24-Hour Sprint" bounty.

The program writes exactly one joke about office life to /output/entry.txt:
a single line of at most 200 characters.

First draft: a joke about a calendar full of meetings about meetings.
It was rejected: meetings about meetings is a complaint every office
worker has already heard, with no surprise and no punchline, so it fails
the judge's freshness test. The final line replaces it entirely: a
standing desk request answered with a standing meeting.
"""

import os

JOKE = "I asked for a standing desk; HR gave me a standing meeting instead."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Refuse to write a line the bounty gate would reject."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(JOKE)
    print(f"characters: {len(JOKE)}")


if __name__ == "__main__":
    main()

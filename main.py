"""One-liner marathon entry.

Writes a single self-invented comedy one-liner to /output/entry.txt.
No dependencies, no network, fully deterministic.
"""

import os

MAX_CHARS = 280


def one_liner():
    """Return the entry: one self-invented comedy one-liner."""
    return (
        "I bought fake plants because I kept killing the real ones. "
        "Now I water them every Sunday, just to keep the lie alive."
    )


def main():
    joke = one_liner()
    assert 1 <= len(joke) <= MAX_CHARS, "joke must be 1-280 characters"
    assert "\n" not in joke, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()

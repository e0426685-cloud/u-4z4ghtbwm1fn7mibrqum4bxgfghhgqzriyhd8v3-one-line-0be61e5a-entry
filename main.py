"""One Line, One Laugh - make.fun entry.

Writes a single original funny line to /output/entry.txt.

Stdlib only. No network, no randomness: the same line every run.
"""

import os

ENTRY = "My password manager forgot my password, so now we're both locked out of my life."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Check the line against the competition gate before writing it."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return line


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() on purpose: tempfile.mkstemp forces mode 0600, which a
    # grader running as another user cannot read. Explicit chmod 644 below
    # keeps the file world-readable.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back and confirm what landed on disk is exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("written entry does not match the validated line")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()

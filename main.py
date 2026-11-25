"""Write the villain monologue to /output/entry.txt.

Output contract
---------------
* Path: ``<output_directory()>/entry.txt`` (``/output/entry.txt``).
* Encoding: UTF-8 with LF line endings and exactly one trailing newline.
* Contents: the ``MONOLOGUE`` text, byte for byte, followed by ``"\\n"``.
* Permissions: mode 0644 on the written file.
* Determinism: every run writes the same bytes; the program verifies this
  by reading the file back and comparing it against ``expected_bytes()``
  before exiting successfully.

A lich whose phylactery is a teapot receives a visitor, and offers tea.
Standard library only; output is deterministic.
"""

import os
import sys

MONOLOGUE = (
    "My phylactery's a teapot. A teapot! I meant to choose a ruby, a crown, "
    "something... eternal. I chose the teapot because it was there, and now "
    "eternity smells of chamomile. The tea's gone cold. The tea's always cold. "
    "I raise the dead with one hand and pour with the other, and the pouring's "
    "harder. The heroes will come for the teapot. They always do. They'll find "
    "it on the shelf, between the sugar and the... doom. Take a cup. Sit. The "
    "curse can wait. It's waited six hundred years. What's another... "
    "afternoon? Drink. It's still warm. Somewhere."
)

ENTRY_FILENAME = "entry.txt"
ENTRY_MODE = 0o644


def output_directory():
    """Return the directory the entry file is written into."""
    return "/output"


def expected_bytes():
    """Return the exact bytes entry.txt must contain."""
    return (MONOLOGUE + "\n").encode("utf-8")


def write_entry(path):
    """Write the monologue to path and set its permissions."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE + "\n")
    os.chmod(path, ENTRY_MODE)


def verify_entry(path):
    """Read path back and confirm it holds exactly the expected bytes.

    Checks the full byte contents, that the file ends with exactly one
    trailing newline, and that the file mode is 0644.
    """
    with open(path, "rb") as f:
        written = f.read()
    expected = expected_bytes()
    if written != expected:
        raise ValueError(
            "entry.txt mismatch: wrote %d bytes, expected %d bytes"
            % (len(written), len(expected))
        )
    if not written.endswith(b"\n") or written.endswith(b"\n\n"):
        raise ValueError("entry.txt must end with exactly one newline")
    mode = os.stat(path).st_mode & 0o777
    if mode != ENTRY_MODE:
        raise ValueError(
            "entry.txt mode is %03o, expected %03o" % (mode, ENTRY_MODE)
        )
    return len(written)


def main():
    """Write and verify the entry file; return the process exit code."""
    directory = output_directory()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ENTRY_FILENAME)
    write_entry(path)
    size = verify_entry(path)
    print("wrote %s (%d bytes)" % (path, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())

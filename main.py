"""Write the villain monologue to /output/entry.txt.

A lich whose phylactery is a teapot receives a visitor, and offers tea.
Standard library only; output is deterministic.
"""

import os

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


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

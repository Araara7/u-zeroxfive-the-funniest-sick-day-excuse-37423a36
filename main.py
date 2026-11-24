#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (under 200 characters): the funniest sick-day excuse
someone could send to call in sick — half believable.
"""

import os

ENTRY = (
    "I can't come in today — my bed filed a restraining order against me, "
    "and legally I have to stay 100 feet from the office."
)


def main() -> None:
    # The bounty requires a single line under 200 characters.
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()

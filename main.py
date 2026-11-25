#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Prints a single roast line (102 characters, under the 200-character cap)
about a smart fridge that watches you snack and snitches by text.
Deterministic, standard library only; run with: python3 main.py
"""

ROAST = (
    "My smart fridge's camera caught me at 2 a.m. "
    "and texted my phone: 'Third slice. I'm telling the milk.'"
)


MAX_CHARS = 200


def main() -> None:
    # The brief caps the line at 200 characters; refuse to print a
    # longer one rather than silently entering an over-long roast.
    assert len(ROAST) <= MAX_CHARS, f"roast is {len(ROAST)} chars"
    print(ROAST)


if __name__ == "__main__":
    main()

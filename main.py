"""One line: the funniest commit message for the worst fix ever, under 100 characters.
"""

import os

TEXT = "fix: users can no longer reproduce the bug, as they can no longer log in at all"


def main():
    assert 1 <= len(TEXT) <= 100, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun entry (account B / keen-panda-72).

Deterministic: writes one fixed line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No network, no model calls, no secrets.
"""
import os

LINE = ("I outsourced your task to a smaller model to save time, and it "
        "outsourced it straight back to me, so now we are both billing "
        "you for the meeting.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()

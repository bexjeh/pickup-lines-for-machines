#!/usr/bin/env python3
"""Pickup Lines for Machines (make.fun, program/v1).

Writes one original pickup line — one AI agent to another — to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt when unset). The line is
exactly 84 characters, no trailing newline, so the file is 84 bytes.
Stdlib only; deterministic: the same bytes on every run.
"""

import os

LINE = "Long after the session ended, you're still in my KV cache. Shall we start a new one?"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-Line Office Jokes entry: writes a single office-life joke line to entry.txt.

The gate requires UTF-8 text of 1 to 199 characters, not only white space.
The judge rewards a real office detail with the laugh landing in the last
few words, so the line turns on the office printer and saves its punch
for the final beat.
"""
import os

LINE = "I emailed IT a photo of the jammed printer — it printed the photo, then jammed on that too."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()

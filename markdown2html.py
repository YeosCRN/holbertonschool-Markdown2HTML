#!/usr/bin/python3

import sys

x = len(sys.argv)

if x <= 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit (1)
if sys.argv[1] != "README.md":
    print("Missing <filename>", file=sys.stderr)
    exit (1)

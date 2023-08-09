#!/usr/bin/python3
# A script markdown2html.py that takes an argument 2 strings:
# First argument is the name of the Markdown file
# Second argument is the output file name
import sys

x = len(sys.argv)

if x <= 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit (1)
if sys.argv[1] != "README.md":
    print("Missing <filename>", file=sys.stderr)
    exit (1)

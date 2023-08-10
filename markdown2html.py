#!/usr/bin/python3
'''A script markdown2html.py that takes an argument of 2 strings:
- First argument is the name of the Markdown file
- Second argument is the output file name, makes no change'''
import sys
import markdown

# Function to convert Markdown to HTML
def main(*args):
    # takes an argument of 2 strings
    x = len(sys.argv)

    if x <= 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        # Read the content of the Markdown file
        file = open(sys.argv[1], 'r')
        og_text = file.read()
        # Convert Markdown text to HTML
        copy_text = markdown.markdown(og_text)
        file.close()
        # Write the HTML content to the output file
        with open(sys.argv[2], 'w') as f:
            f.write(copy_text)
        f.close()
    except:
        print("Missing", sys.argv[1], file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main(sys.argv)

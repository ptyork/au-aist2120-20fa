# python grep_1015.py [pattern]

import sys
import re

# sys.argv  ==> a list of all arguments passed in to python

# print(sys.argv)

# exit()

if len(sys.argv) != 2:
    sys.stderr.write('SYNTAX ERROR!!!\n')   # proper to write errors to stderr
    sys.exit(1)  # proper to exit non-zero on error

pattern = sys.argv[1]

regex = re.compile(pattern)

line_num = 0
for text in sys.stdin:
    line_num += 1
    text = text.rstrip()
    # CONDITIONALLY print the line IF it matches
    if regex.match(text):
        print(f"{line_num:>4}: {text}")

# python grep_1015.py [pattern]  ==> search stdin for regular expression  pattern

import sys
import re

#  sys.argv ==> a list of all of the arguments "passed" to python

# print(sys.argv)
# exit()

if len(sys.argv) != 2:
    sys.stderr.write("INVALID SYTAX\n")
    sys.exit(1)    # by convention a non-zero exit code is an error

pattern = sys.argv[1]

regex = re.compile(pattern)

line_num = 0
for txt in sys.stdin:
    txt = txt.rstrip()
    line_num += 1
    # ONLY PRINT IF PATTERN IS FOUND
    if regex.match(txt):
        print(f"{line_num:>4}: {txt}")

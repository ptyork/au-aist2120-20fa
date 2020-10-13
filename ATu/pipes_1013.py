# dir | python pipes_1013.py

import sys

# NOTE: when piping input, probably best to use sys.stdin
#       INSTEAD of input()
for line in sys.stdin:
    line = line.rstrip()
    print("WOW: " + line)

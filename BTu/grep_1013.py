# dir | python grep_1013.py *.\.py
# dir | python grep_1013.py >> output.txt 2>> errors.txt
# dir | python grep_1013.py .*\d\.py >> output.txt 2>> errors.txt

import sys
import re

# python grep_1013.py [pattern]

# sys.argv  ==> a LIST of all command-line arguments supplied when
#               running this script
#   sys.argv[0] ==> the filename of the script
#   sys.argv[1..n] ==> additional arguments

# print(sys.argv)

if len(sys.argv) != 2:
    sys.stderr.write("BAD SYNTAX!!")
    sys.exit(1)

pattern = sys.argv[1]

regex = re.compile(pattern)

line_num = 0
for line in sys.stdin:
    line = line.rstrip()
    line_num += 1
    # ONLY PRINT THE LINE IF IT MATCHES THE PATTERN
    if regex.match(line):
        print(f'{line_num:>4}: {line}')


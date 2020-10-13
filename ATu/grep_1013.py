# dir | python grep_1013.py .*\.py
# [command] | [command] | [command] ...

import sys
import re

# [command] [arg0] [arg1] ...
# sys.argv    ==> a SEQUENCE of arguments passed in to the script
# print(sys.argv)
# argv[0] is the script name
# argv[1..] are the rest of the arguments

# THIS IS HUGE (I mean how to process command line arguments)
if len(sys.argv) < 2:
    print("BAD COMMAND")
    sys.exit()

pattern = sys.argv[1]

print(f'...looking for {pattern}')
regex = re.compile(pattern)

for line in sys.stdin:
    line = line.rstrip()
    if regex.search(line):
        print(line)

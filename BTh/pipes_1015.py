# piping  ==> redirect the stdout from one process as
#               stdin in another process
#   [command] | [command] | ...

import sys

line_num = 0
for line in sys.stdin:
    line_num += 1
    line = line.rstrip()
    print(f'{line_num:>4}: {line}')

# Piping
#   Redirection of output from one command to use as input
#   to another command.
#     [command] | [command] | ...

import sys

line_num = 0
for txt in sys.stdin:
    txt = txt.rstrip()
    line_num += 1
    print(f"{line_num:>4}: {txt}")

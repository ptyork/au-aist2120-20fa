# Pipe output 
#   dir | python pipe_1013.py
#       ^
#       |
#   THAT IS THE PIPE
# 
# [command] | [command] | ...

import sys

line_num = 0
for line in sys.stdin:
    line = line.rstrip()
    line_num += 1
    print(f'{line_num:>4}: {line}')

print("ALL DONE")

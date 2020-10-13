# stdio -- Stream-based IO to the console
#   stdin  -- Input Stream (console keyboard input--readonly---kindof)
#   stdout -- Output Stream (console text output--writeonly---kindof)
#   stderr -- Error Output Stream (console text output--writeonly)

# File-based Output Redirection
#   [command] > [filename]  ==> OVERWRITE redirection
#   [command] >> [filename] ==> APPEND redirection

# New Commands
#   type [filename] ==> write contents of a FILE to stdout
#   echo [text]     ==> write text to stdout

import sys

sys.stdout.write('Hello world\n')
print('Hello world')    # same as sys.stdout.write()

txt = sys.stdin.readline()
print("You said: " + txt)
txt = input()           # same as sys.stdin.readline()
print("You said: " + txt)


sys.stderr.write('AN ERROR OCCURRED')

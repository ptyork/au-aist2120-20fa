# stdio  ==> standard for I/O to consoles
#   stdout  ==> virtual file stream for writing console output
#   stdin   ==> virtual file stream for reading console input
#   stderr  ==> virtual file stream for writing error messages

# FILE REDIRECTION
#   [command] > [filename]  ==> redirect the stdout stream to a file
#                               (OVERWRITE)
#   [command] >> [filename] ==> same as above but APPEND mode

# "NEW" COMMANDS
#   type [filename]  ==> copy the contents of the file to stdout
#      (cat [filename] on mac/linux)
#   echo [phrase]    ==> writes the phrase to stdout
#   echo.            ==> writes a blank line to stdout
#   find "[pattern]" ==> find a patter in stdin and echo if found
#      (grep is SIMILAR on Linux/Mac)

import sys

sys.stdout.write("hello world\n")  # this
print('another world')             # is same as this
print(sys.stdout.writable())       # this
sys.stdout.write(str(sys.stdout.writable()) + '\n')  # is same as this

txt = sys.stdin.readline()  # this
txt = txt.rstrip()
print(txt)
txt = input()               # is same as this
print(txt)

txt = input('Enter a number: ')
num = int(txt)
print(num + 1)

sys.stdout.write("Enter a number: ")
sys.stdout.flush()
txt = sys.stdin.readline()
num = int(txt)
print(num + 1)

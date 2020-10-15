# stdio  --> Standard for Input and Output (usually to the console)
#   stdin   --> Standard input stream (aka, virtual file)
#   stdout  --> Standard output stream (virtual file)
#   stderr  --> Secondary output stream for error messages

# OUTPUT REDIRECTION
#   File-based
#     [command] > [filename]   ==> redirect output from command
#                                   and save it in filename (OVERWRITE)
#     [command] >> [filename]  ==> redirect as above but APPEND

# "NEW" COMMANDS
#   type [filename]  ==> print text file contents to stdout
#      (cat [filename] on linux/mac)
#   echo [phrase]    ==> print phrase to stdout
#   echo.            ==> print nothing (maybe newline) to stdout
#   find "[pattern]" ==> print all lines from stdin that contain the pattern

import sys

sys.stdout.write("Hello world from Python\n")  # by default doesn't include the newline
print("Python has a print that does the same dadgum thing") # SAME AS ABOVE

txt = sys.stdin.readline()
txt = txt.rstrip()
print(txt)
txt = input()    # SAME AS ABOVE
print(txt)

sys.stdout.write('Enter a number: ')
sys.stdout.flush()  # force to write to the screen
txt = sys.stdin.readline()
txt = txt.rstrip()
num = int(txt)
print(num + 1)


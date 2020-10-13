# console I/O (stdio)
# stdin  ==> Input Stream (keyboard input AND...)
# stdout ==> Output Stream (console output AND...)
# stderr ==> Alternative Output Stream (console output for ERRORS)

# Output Redirection to a File
#  [command] > [filename]    ==> OVERWRITE
#  [command] >> [filename]   ==> APPEND

# Some "new" commands
#   type [filename]     ==> Writes the contents of a file to stdout
#      (Linux/Mac)   cat [filename]
#   echo [phrase]       ==> Write a phrase to stdout
#   echo.               ==> Writes nothing to stdout
#      (Linux/Mac no need for the ".")


import sys
sys.stdout.write('Hello\n')
print('Hello')   # EQUIVALENT

val = sys.stdin.readline()
print(val)
val = input()    # EQUIVALENT
print(val)

sys.stderr.write('AN ERROR GOES HERE\n')  # CORRECT WAY to write an error to the screen


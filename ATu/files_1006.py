# from pathlib import Path

# OPEN FILES
# open()
#   filename  (can be absolute or relative path)
#   mode
#       r   read    (default)
#       w   (over)write
#       a   append
#
#       +   read/write (DO NOT WORRY ABOUT THIS)
#
#       t   text    (default)
#       b   binary
#   EXAMPLES
#       at     Append Text
#       rb     Read Binary
#       w      Write Text
#
#  RETURNS A FILE OBJECT or FILE STREAM

fi = open(r'..\autumn.txt')   # defaults to 'rt' mode
for i in range(20):
    # txt = fi.read()      # read whole file
    # txt = fi.readline()    # ends with \n
    # txt = fi.readline().rstrip()
    txt = fi.readline()[:-1]
    print(txt)
fi.close()


fi = open(r'..\autumn.txt')   # defaults to 'rt' mode
line_num = 0
for line in fi:
    line = line.rstrip()
    line_num += 1
    print(f"{line_num:>4}: {line}")
    if line_num % 20 == 0:
        print("press enter to continue")
        input()
fi.close()


bubba = open('newfile.txt', 'wt')
bubba.write('Paul was here\n')
bubba.write('Isn\'t that great!!\n')
bubba.close()


bubba = open('newfile.txt', 'at')
bubba.write('New stuff gets added\n')
bubba.write('when on appends\n')
bubba.close()

# from pathlib import Path

# open() function
#   file    path to the file you want to open
#   mode    
#       r   read-only   (default)
#       w   (over)write
#       a   append
#
#       +   read/write  (DON'T WORRY ABOUT THIS)
#
#       t   text file   (default)
#       b   binary
#
#  EXAMPLES:
#       at  append text
#       rb  read binary
#       wt  write text
#       a   append text
#       w   write text
#           read text
#
#   RETURNS A FILE OBJECT (or File Stream)

fi = open(r'..\autumn.txt')
txt = fi.read()
print(txt)
print('DONE')
txt = fi.read()
print(txt)
print('DONE AGAIN')

fi.close()


fi = open(r'..\autumn.txt')
txt = fi.readline()
print(txt)
txt = fi.readlines()
print(txt)
fi.close()



fi = open(r'..\autumn.txt')
line_num = 0
for li in fi:
    li = li.rstrip()
    # li = li[:-1]
    # print(li)
    line_num += 1
    print(f"{line_num:>4}: {li}")
    if line_num % 20 == 0:
        print('-- Press Enter to Continue --')
        input()
fi.close()



bubba = open('newfile.txt', 'wt')
bubba.write('Paul wuzn\'t here.\n')
bubba.write('He said HEY!!\n')
bubba.close()

bubba = open('newfile.txt', 'at')
bubba.write('Here\'s some new stuff.\n')
bubba.write('WHOOPEE!!\n')
bubba.close()

# open()
#   filename    path to the file
#   mode
#       r   read (default)
#       w   (over)write     like the = operator
#       a   append          like the += operator
#       x   eXclusive write  (new file)
# 
#       +   both (don't worry about it)
# 
#       t   text (default)
#       b   binary
# 
# RETURNS a FILE OBJECT / FILE STREAM

# open(r'..\autumn.txt', 'rt')
# open(r'..\autumn.txt', 'r')
fi = open(r'..\autumn.txt')
txt = fi.read()
print(txt)
fi.close()


fi = open(r'..\autumn.txt')
# fi.read()
txt = fi.readline()
txt = fi.readline()
print(txt)
fi.close()


fi = open(r'..\autumn.txt')
line_num = 0
for li in fi:
    li = li.rstrip()
    line_num += 1
    print(f"{line_num:>4}: {li}")
    if line_num % 20 == 0:
        input('--- press enter to continue ---')
fi.close()


fi = open(r'newfile.txt', 'wt')
fi.write('Paul wuz here\n')
fi.write('It\'s almost time to go\n')
fi.close()

fi = open(r'newfile.txt', 'at')
fi.write('Here\'s somehing new\n')
fi.write('It\'s actually time to go\n')
fi.close()

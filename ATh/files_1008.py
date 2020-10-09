# open()
#   path        The file to open
#   mode        How you will work with the file
#       r   read   (default)
#       w   (over)write   equivalent to = for a string
#       a   append        equivalent to += for a string
#       x   exclusive write / new file  (don't worry about it BUT opens if NOT exist)
# 
#       +   read + write  (don't worry about)
# 
#       t   text   (default)
#       b   binary
# 
# File Object / File Stream

# open(r'..\autumn.txt', 'r')
# open(r'..\autumn.txt', 'rt')
fi = open(r'..\autumn.txt')
txt = fi.read() # read all
print(txt)
fi.close()

fi = open(r'..\autumn.txt')
txt = fi.readline()
txt = fi.readline()
print(txt)
fi.close()


fi = open(r'..\autumn.txt')
line_no = 0
for li in fi:
    li = li.rstrip()
    line_no += 1
    print(f"{line_no:>4}: {li}")
fi.close()


fi = open(r'newfile.txt', 'wt')
fi.write('Paul wuz here\n')
fi.write('He\'s awesome!!\n')
fi.close()

fi = open(r'newfile.txt', 'at')
fi.write('Another line\n')
fi.write('Another day\n')
fi.close()


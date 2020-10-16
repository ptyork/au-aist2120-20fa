# NAVIGATION
# LIST
#  os.listdir()      ==>	dir  ||  ls
#  os.walk()         ==> dir /s  ||  ls -R
# CHANGE DIRECTORY
#  os.chdir()        ==> cd

# FILES
# COPY
#  shutil.copy()     ==> copy  ||  cp
# MOVE / RENAME
#  shutil.move()     ==> move  ||  mv
#  os.rename()       ==> ren  ||  mv     (best just to use move for everything)
# DELETE
#  os.remove()       ==> del  ||  rm

# DIRS/FOLDERS
# CREATE
#  os.mkdir()        ==> mkdir (md shortcut on Windows)
# COPY
#  shutil.copytree() ==> xcopy  ||  cp -r
# MOVE / RENAME
#  shutil.move()     ==> move  ||  mv
#  os.rename()       ==> ren  ||  mv     (best just to use move for everything)
# DELETE
#  shutil.rmtree()   ==> rd /s  ||  rm -r

import os
import shutil

cwd = os.getcwd()    # returns the Current/Present Working Directory
print(cwd)

if not os.path.exists('fun'):
    os.mkdir('fun')

# dirs = os.listdir()
# print(dirs)

os.chdir('fun')

cwd = os.getcwd()
print(cwd)

shutil.copyfile('../821_branch_loop.py', './821_branch_loop.py')
shutil.copyfile('../828_funcy.py', '828_funcy.py')

filenames = os.listdir()

for f in filenames:
    # os.remove(f)
    if f.endswith('.py'):
        print(f.upper())
        print('=' * len(f))
        with open(f) as fi:
            txt = fi.read()
            print(txt)
        print()
        print()


print('press enter to continue...')
input()

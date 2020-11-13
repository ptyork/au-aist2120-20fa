import subprocess

# Open external process as SUBprocesses of this one

p1 = subprocess.Popen(["start", "common_words.txt"], shell=True)
# p2 = subprocess.Popen(["start", "excel\\exams.xlsx"], shell=True)


print(p1)
# print(p2)

p1.wait()    # can't wait if shell=True because this is no longer an "owned" process


p3 = subprocess.Popen(['notepad.exe','imports_1022.log'])
p4 = subprocess.Popen(['code.cmd','imports_1022.py'])

p3.wait()
p4.wait()

print("DONE")

print("hello world")

txt = "paul wuz here"
print(txt)

name = 'paul'
txt = name + " wuz here 2"
print(txt)

print(name + " wuz here 3")

print(name, "wuz here 4")

print("enter your first name: ")
fname = input()

#MIMIR LIKES THIS WAY
lname = input("enter your last name: ")

# WAY 1
yob = input("what year were you born in: ")
iyob = int(yob)
age = 2020 - iyob

# WAY 2
age = 2020 - int(yob)

# WAY 3
yob = int(input("what year were you born in: "))
age = 2020 - yob

print(fname, lname, "is", age)
# print(fname + " " + lname + " is " + age) DEAD

################################### 
 
while True:
    numstr = input("Enter a number: ")
    numstr = numstr.strip()

    if numstr.isnumeric():
        break
    else:
        print("NOPE!!!")

num = int(numstr)
print(f"You entered {num}")

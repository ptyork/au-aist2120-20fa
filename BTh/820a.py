print('hello world')

txt = "paul wuz here"
print(txt)

name = "paul"
print(name + " wuz here 2")

print(name, "wuz here 3")

# OK, BUT MIMIR NOT HAPPY, BUT BOOK LIKE
print("Enter your first name: ")
fname = input()

# ALSO OK, MIMIR LIKE
lname = input("Enter your last name: ")

# WAY 1
yob = input('Enter year of birth: ')
iyob = int(yob)
age = 2020 - iyob

# WAY 2
yob = input('Enter year of birth: ')
age = 2020 - int(yob)

# WAY 3
yob = int(input('Enter year of birth: '))
age = 2020 - yob


print(fname, lname, "is", age, "years old")

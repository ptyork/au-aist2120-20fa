print('hello world')

name = "paulie"
print(type(name))
print(name + " wuz here")

# name = "42"
name = 42
print(type(name))
print(str(name) + " wuz here")

#thewrongway
# print('Enter your first name:\n\n')
# fname = input()
# print('hello ' + fname)

#therightway
# REALLY, this is just an algternative that works "better"
# in Mimir.
fname = input("Enter your first name again: ")
print("hello", fname, "again")

yob = input("what year were you born in? ")
iyob = int(yob)
age = 2020 - iyob
print('oh, I see you are', age, 'years old')

yob = input("what year were you born in? ")
yob = int(yob)  # bad_practice
age = 2020 - yob
print('oh, I see you are', age, 'years old')

yob = int(input("what year were you born in? "))
age = 2020 - yob
print('oh, I see you are', age, 'years old')

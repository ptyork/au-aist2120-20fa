print('hello world')

print("paul wuz here")

name = "paul"
print(name + " wuz here")

age = 39
print("you are " + str(age) + " years old")

#lessgood
# print("enter your first name:")
# fname = input()

#better (opinion)
#FACT: this works in Mimir
fname = input("enter your first name: ")

print("hi", fname)

yob = input('when you born? ')
iyob = int(yob)
age = 2020 - iyob
print('you are', age, 'year old')

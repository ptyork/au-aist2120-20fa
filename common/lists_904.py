'''
C# is SIMILAR
  string[] names = new string[4];
  string[] names = [ .... ];
NOT THE SAME
  C# arrays are strongly typed
  C# arrays are also fixed size

C# Generic List
  List<string> names = new List<string>();
  Strongly typed by NOT fixed size
'''

names = [
    'john',
    'paul',
    'george',
    'ringo'
]

### ACCESS ELEMENTS ###
best_beatle = names[1]

### CHANGE ELEMENTS ###
names[1] = 'the real paul'

### ARE THESE THE SAME???? ###
print(best_beatle)
print(names[1])
# no


print(names)
names.append('bubba')
print(names)
print(names[4])

### SIZE OF LIST
print(len(names))
print(names[len(names) - 1])

### SLICING ###
# listname[start:end:step]
last_three = names[2:5]
print(last_three)
print(names)

last_three = names[2:]
first_three = names[0:3]
first_three = names[:3]

names_again = names[:]   # copy a list

names_again[0] = 'johnie rocket'
print(names_again)
print(names)

my_string = 'ABCDEFGHIJKLMNOP'
print(my_string[3])
# my_string[3] = "F"   CAN'T CHANGE....IMMUTABLE
print(my_string[:5])
print(my_string[4:7])
print(my_string[0:16])
print(my_string[0:16:2])  # ODDS
print(my_string[1:16:2])  # EVENS
print(my_string[2:16:3])  # EVERY THIRD
print(my_string[::2])  # ODDS
print(my_string[::-1])  # REVERSE
print(names[::-1])

### negative indexes

print(names)
print(names[-1])
print(names[-2])

all_but_last_three = names[0:-3]
print(all_but_last_three)

last_three = names[-3:]
print(last_three)



print(names)

for i in range(len(names)):
    # extract value of element
    name = names[i]
    # work with element
    print(f"{i+1}: {name.title()}")

for i in range(len(my_string)):
    # extract value of element
    a_char = my_string[i]
    # work with element
    print(f"{i+1}: {a_char.lower()}")

'''
THIS IS THE SAME AS THE C# foreach LOOP
'''
for name in names:
    # work with element
    print(f"{name.title()}")

for a_char in my_string:
    # work with element
    print(f"{a_char.lower()}")

for a_char in my_string[::-1]:
    # work with element
    print(f"{a_char.lower()}")



### BOOLEAN COMPARISON OPERATORS ###
# > < >= <= != ==

print(names)
print('bubba' in names)
print('paul' in names)
print('johnie walker red' in names)


while True:
    print("CHOOSE")
    print("______")
    print("a) Say hi")
    print("b) Go low")
    print("x) Exit")

    choice = input("WHAT DO YOU WANT: ")
    choice = choice.lower()

    if choice in "abx":
        break
    else:
        print("INVALID CHOICE")




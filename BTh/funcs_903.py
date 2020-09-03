# COMMENT
"   HELLO WORLD   "
'''
MULTI
LINE
STRING
BECOMES
A
MULTI
LINE
COMMENT
'''

'''
name:       get_name
params:     none
returns:    the user-entered name in title case
'''
def get_name():
    while True:
        name = input("Enter you name: ")
        name = name.strip()

        if len(name) == 0:
            print("PLEASE GIVE ME A REAL NAME")
            continue
        
        # break
        name = name.title()
        return name


'''
name:       get_int
params:     prompt (string)
returns:    an integer that the user entered
'''
def get_int(prompt):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("PLEASE GIVE SOMETHING")
            continue

        # if numstr.isnumeric() == False:
        if not numstr.isnumeric():
            print("THAT'S NOT A NUMBER")
            continue

        # if finally we get here, then we know numstr is valid
        num = int(numstr)
        return num


'''
name:       get_int_in_range
params:     prompt (string)
            minval (int)
            maxval (int)
returns:    an integer that the user entered between the values
'''
def get_int_in_range(prompt, minval, maxval):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("PLEASE GIVE SOMETHING")
            continue

        # if numstr.isnumeric() == False:
        if not numstr.isnumeric():
            print("THAT'S NOT A NUMBER")
            continue

        # if finally we get here, then we know numstr is valid
        num = int(numstr)

        if num < minval or num > maxval:
            print("OUT OF RANGE")
            continue

        # if finally we get here, then we know num is valid
        return num

'''
name:       get_int_in_rangeA
params:     prompt (string)
            minval (int)
            maxval (int)
returns:    an integer that the user entered between the values
'''
def get_int_in_rangeA(prompt, minval, maxval):
    while True:
        num = get_int(prompt)

        if num < minval or num > maxval:
            print("OUT OF RANGE")
            continue

        # if finally we get here, then we know num is valid
        return num



###################################

username = get_name()
print(f"You entered {username}")

age = get_int_in_range("Enter your age: ", 1, 120)
print(f"You say you are {age} but you don't look a day over {age-1}")

weight = get_int("Enter your weight: ")
print(f"You say you weigh {weight} pounds...that's awesome (fatty)")


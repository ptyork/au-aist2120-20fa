

# SINGLE LINE COMMENTS
" HELLO WORLD "
'''
MULTI
LINE
COMMENT
REALLY
A
MULTI
LINE
STRING
'''

'''
name:       get_name
parameters: none
returns:    a user specified name as a string
'''
def get_name():
    while True:
        name = input('Enter your name: ')
        name = name.strip()

        # Check for something
        if len(name) == 0:
            print("PLEASE GIVE ME A REAL NAME")
            continue  # try again if bad

        name = name.title()
        
        # exit the loop
        return name


'''
name:       get_int
params:     prompt
returns:    a user supplied number as an int
'''
def get_int(prompt):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("PLEASE GIVE ME SOMETHING")
            continue

        # if numstr.isnumeric() == False:
        if not numstr.isnumeric():
            print("PLEASE GIVE A REAL NUMBER")
            continue
        
        # once we get here, we're golden...convert and return
        num = int(numstr)
        return num



'''
name:       get_int_in_range
params:     prompt (string)
            minval (int)
            maxval (int)
returns:    a user supplied number as an int
'''
def get_int_in_range(prompt, minval, maxval):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("PLEASE GIVE ME SOMETHING")
            continue

        # if numstr.isnumeric() == False:
        if not numstr.isnumeric():
            print("PLEASE GIVE A REAL NUMBER")
            continue
        
        # once we get here, we're golden...convert
        # (but hold off on returning)
        num = int(numstr)

        if num < minval or num > maxval:
            print("THAT'S OUT OF RANGE")
            continue
        
        # WHEW! the number is valid so return it
        return num

'''
name:       get_int_in_range
params:     prompt (string)
            minval (int)
            maxval (int)
returns:    a user supplied number as an int
'''
def get_int_in_rangeA(prompt, minval, maxval):
    while True:
        num = get_int(prompt)

        if num < minval or num > maxval:
            print("THAT'S OUT OF RANGE")
            continue
        
        # WHEW! the number is valid so return it
        return num



################################

username = get_name()
print(f"Oh hi, {username}")

# exit()    # explicitly exit a SCRIPT

age = get_int_in_range("Enter your age: ", 1, 120)
print(f"Haha, you THINK you are {age} but really you are {age+20}")
weight = get_int("Enter your weight: ")
print(f"You look mahvelous for someone who weights {weight} pounds")


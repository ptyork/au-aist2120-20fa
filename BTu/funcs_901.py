# Comments
" COMMENT "
'''
MULTI
LINE
STRING
IS GREAT FOR LONG COMMENTS
'''


'''
name:       get_name
params:     none
returns:    a user-entered name
'''
def get_name():
    while True:
        namestr = input("Enter your name: ")
        namestr = namestr.strip()
        if len(namestr) == 0:
            print("PLEASE ENTER A REAL NAME")
            continue
        # else:
        #     break

        namestr = namestr.title()
        return namestr


'''
name:       get_int
params:     prompt (string)
return:     a user-supplied positive integer
'''
def get_int(prompt):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("YOU MUST ENTER A VALUE")
            continue
        # if numstr.isnumeric() == False:
        if not numstr.isnumeric():
            print("THAT DON'T LOOK LIKE NO NUMBER TO ME")
            continue

        num = int(numstr)
        return num


'''
name:       get_int_in_range
params:     prompt (string)
            minval (int)
            maxval (int)
return:     a user-supplied positive integer
'''
def get_int_in_range(prompt, minval, maxval):
    while True:
        numstr = input(prompt)
        numstr = numstr.strip()

        if len(numstr) == 0:
            print("YOU MUST ENTER A VALUE")
            continue
        if not numstr.isnumeric():
            print("THAT DON'T LOOK LIKE NO NUMBER TO ME")
            continue

        num = int(numstr)

        if num < minval or num > maxval:
            print("OUT OF RANGE")
            continue

        return num


'''
name:       get_int_in_rangeA
params:     prompt (string)
            minval (int)
            maxval (int)
return:     a user-supplied positive integer
'''
def get_int_in_rangeA(prompt, minval, maxval):
    while True:
        num = get_int(prompt)

        if num < minval or num > maxval:
            print("OUT OF RANGE")
            continue

        return num


############################################

name = get_name()
print(f"Oh, hi {name}")

age = get_int("Please enter your age: ")
print(f"You said you are {age} but ha ha you are really {age+25} you old fart.")

weight = get_int_in_range("Please enter your weight: ", 50, 500)
print(f"You said you are {weight} pounds, you fatty!!")

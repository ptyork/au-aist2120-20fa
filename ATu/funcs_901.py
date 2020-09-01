# COMMENT
'''
MULTI
LINE
COMMENTS
'''


'''
name:       get_name
params:     NONE
returns:    a name
'''
def get_name():
    while True:
        inname = input('Enter your name: ')
        inname = inname.strip()
        if len(inname) == 0:
            print('NAME CANNOT BE BLANK')
            continue
        inname = inname.title()
        return inname

        #break
    #return inname


'''
name:       get_int
params:     none
returns:    an int
'''
def get_int():
    while True:
        intstr = input('Enter an integer: ')
        intstr = intstr.strip()
        if len(intstr) == 0:
            print('INTEGER CANNOT BE BLANK')
            continue
#        if intstr.isnumeric() == False:
        if not intstr.isnumeric():
            print('THAT DOESN\'T LOOK LIKE AN INTEGER TO ME')
            continue

        an_int = int(intstr)
        return an_int


'''
name:       get_int_range
params:     min and max
returns:    an int
'''
def get_int_range(min,max):
    while True:
        intstr = input(f'Enter an integer between {min} and {max}: ')
        intstr = intstr.strip()
        if len(intstr) == 0:
            print('INTEGER CANNOT BE BLANK')
            continue
#        if intstr.isnumeric() == False:
        if not intstr.isnumeric():
            print('THAT DOESN\'T LOOK LIKE AN INTEGER TO ME')
            continue

        an_int = int(intstr)

        if an_int < min or an_int > max:
            print('THAT IS OUT OF RANGE')
            continue

        return an_int

'''
name:       get_int_range_short
params:     min and max
returns:    an int
'''
def get_int_range_short(min,max):
    while True:
        an_int = get_int()

        if an_int < min or an_int > max:
            print('THAT IS OUT OF RANGE')
            continue

        return an_int



##############################
# CALL FUNCTIONS
##############################

name = get_name()
print(f"Oh, hi {name}")

a_num = get_int()
print(f"You said {a_num} but you really meant {a_num + 1}")

a_num = get_int_range(1,10)
print(f"You said {a_num}")


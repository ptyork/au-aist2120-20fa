# import pprint
# pprint.pprint("HELLO")
# from pprint import pprint
# pprint("HELLO")
from pprint import pprint as pp    # alias pprint as pp
pp("HELLO")

# contacts = []
contacts = [
    'John,555-1212',
    'Paul,555-1313',
    'George,555-1414',
    'Ringo,555-1515'
]

'''
name:       get_string
params:     prompt
returns:    the user-entered string
'''
def get_string(prompt):
    while True:
        a_string = input(prompt)
        a_string = a_string.strip()

        if len(a_string) == 0:
            print("PLEASE GIVE ME A REAL VALUE")
            continue
        
        return a_string


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



def add_contact():
    global contacts
    print()
    name = get_string("Enter the name: ")
    phone = get_string("Enter the phone: ")
    a_contact = f"{name},{phone}"
    # contacts.insert(0, a_contact)
    contacts.append(a_contact)
    print(f'Added {a_contact}')

def display_all_contacts():
    global contacts
    # print(contacts)
    # pp(contacts)
    for bob in contacts:
        print(f"   CONTACT: {bob}")
    print("BOB")
    print()


def delete_contact():
    global contacts
    # contacts.remove('Paul,555-1313') CUMBERSOME
    for i in range(len(contacts)):
        bob = contacts[i]
        print(f"   {i}) {bob}")
    
    maxval = len(contacts) - 1
    to_delete = get_int_in_range('Which contact: ', 0, maxval)
    contacts.pop(to_delete)


########################################
# MAIN

while True:
    print()
    print('MENU')
    print('====')
    print('1) Add contact')
    print('2) Display all contacts')
    print('3) Delete a contact')
    print('X) Exit')
    print('----')

    choice = input('Enter choice: ').strip()
    # choice = choice.strip()
    # '  1 '.strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_all_contacts()
    elif choice == '3':
        delete_contact()
    elif choice.upper() == 'X':
        break
        # return  NO--only returns / exits a function
        # exit()   FINE -- exits program
    else:
        print('INVALID CHOICE')

print('BYEEEE!')


# contacts.clear()    # wipeout everything

pp(contacts)
c2 = contacts.copy()
pp(c2)
c2.pop(1)
pp(contacts)
pp(c2)
c3 = contacts[:]     # Truly identical

# len(contacts) 
contacts.count('Paul')  # NOT len(contacts)
# 0 because 'Paul' is NOT 'Paul,555-1313"

c3.extend(c2)
# c3 = c3 + c2       # truly the same
pp(c3)
c4 = contacts + c2   # kinda the same
pp(c4)

to_find = 'Paul'
try:
    print(contacts.index(to_find))
except:
    print(f"{to_find} NOT FOUND")

to_find = 'George'
if to_find in contacts:
    print(contacts.index(to_find))
else:
    print(f"{to_find} NOT FOUND")

to_find = 'Ringo,555-1515'
if to_find in contacts:
    print(contacts.index(to_find))
else:
    print(f"{to_find} NOT FOUND")

contacts.reverse()
pp(contacts)
rev_contacts = contacts[::-1]
pp(rev_contacts)

contacts.sort()
pp(contacts)
contacts.sort(reverse=True)
pp(contacts)

contacts.sort()                  # The same as contacts.sort(revers=True)
contacts.reverse()

contacts = contacts.sort()[::-1]  # DON'T but also the same


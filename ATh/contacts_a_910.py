# import pprint
# pprint.pprint()
# from pprint import pprint
# pprint()
from pprint import pprint as pp   # ALIAS pprint to pp
# pp()

# contacts = []
contacts = [
    'John,555-1212',
    'Paul,555-1313',
    'George,555-1414',
    'Ringo,555-1515'
]

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
name:       get_string
parameters: prompt
returns:    a user specified string
'''
def get_string(prompt):
    while True:
        a_string = input(prompt)
        a_string = a_string.strip()

        # Check for something
        if len(a_string) == 0:
            print("PLEASE GIVE ME A REAL VALUE")
            continue  # try again if bad

        return a_string




def add_contact():
    global contacts
    print()
    name = get_string("Enter the name: ")
    phone = get_string("Enter phone number: ")
    the_contact = f"{name},{phone}"
    #contacts.insert(0, the_contact)   # put the contact at the start
    contacts.append(the_contact)
    print(f'Added {the_contact}')

def display_contacts():
    global contacts
    print()
    # print(contacts)
    # pp(contacts)
    for cont in contacts:
        print(f"   CONTACT: {cont}")

def remove_contact():
    global contacts
    # to_remove = get_string("Who to remove: ")
    # contacts.remove(to_remove)
    for i in range(len(contacts)):
        cont = contacts[i]
        print(f'   {i}) {cont}')

    maxval = len(contacts) - 1
    index = get_int_in_range('Who to remove: ', 0, maxval)
    removed = contacts.pop(index)
    print(f'Removed {removed}')


while True:
    print()
    print('MENU')
    print('====')
    print('1) Add a Contact')
    print('2) Display all Contacts')
    print('3) Remove a Contact')
    print('X) Exit')

    choice = input('Enter your choice: ')
    choice = choice.strip()
    #choice = choice.upper()

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        remove_contact()
    elif choice.upper() == 'X':
        #exit()
        #return
        break
    else:
        print('INVALID CHOICE')

print('SEE YA LATER!!')


# contacts.clear()   # removes all
c2 = contacts.copy()
c2 = contacts[:]       # identical
pp(c2)
c2.pop(0)
print('removed 0 from c2')
pp(contacts)
pp(c2)

print(contacts.count('Paul'))    # how many of a specific value
# WILL BE 0 BECAUSE 'Paul' != 'Paul,555-1313'

print('extending contacts with c2')
contacts.extend(c2)   # DIRECTLY MODIFIES contacts
pp(contacts)

all_contacts = contacts + c2   # SIMILAR but creates a copy
print(all_contacts)

to_find = 'Paul'
try:
    print(contacts.index(to_find))
except:
    print(f'{to_find} NOT FOUND')

to_find = 'George'
if to_find in contacts:
    print(contacts.index(to_find))
else:
    print(f'{to_find} NOT FOUND')

to_find = 'George,555-1414'
if to_find in contacts:
    print(contacts.index(to_find))
else:
    print(f'{to_find} NOT FOUND')

contacts.reverse()
pp(contacts)
rev_contacts = contacts[::-1]  # SIMILAR but makes a copy


contacts.sort()
pp(contacts)
contacts.sort(reverse=True)
pp(contacts)

sort_contacts = sorted(contacts)   # SIMILAR but makes a copy

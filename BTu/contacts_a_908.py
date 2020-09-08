# import pprint
# pprint.pprint()
# from pprint import pprint
# pprint()
from pprint import pprint as pp   # ALIAS pprint function to pp
# pp()

contacts = [ ]
### FOR DEBUG PURPOSES ONLY ###
contacts = sorted([
    'John,555-1212',
    'Paul,555-1313',
    'George,555-1414',
    'Ringo,555-1515'
])
contacts.sort(reverse=True)
contacts.reverse()

# name = 'paul'.upper()  # CAN CALL METHODS ON VALUES (not just on vars)


##########################################
# FUNCTIONS

'''
name:       get_string
params:     prompt
returns:    a user-entered name
'''
def get_string(prompt):
    while True:
        value = input(prompt)
        value = value.strip()
        if len(value) == 0:
            print("PLEASE ENTER A VALUE")
            continue

        return value

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



def add_contact():
    global contacts
    name = get_string("Enter your name: ")
    phone = get_string("Enter your phone: ")
    contact = f"{name},{phone}"
    # FINALLY we can add contact to the contacts list
    # contacts.insert(0, contact)   PLACE AT A SPECIFIC LOCATION
    contacts.append(contact)
    contacts.sort()
    print(f"Successfully added {contact}")

def show_contacts():
    global contacts
    # print(contacts)
    # pp(contacts)
    for c in contacts:
        print(f"BILLYBOB: {c}")
    print(f"Total contacts: {len(contacts)}")

def delete_contact():
    global contacts
    for i in range(len(contacts)):
        contact = contacts[i]
        print(f'{i}: {contact}')
    to_delete = get_int_in_range("Which to delete: ", 0, (len(contacts) - 1) )
    # del(contacts[to_delete])
    # contacts.remove(contacts[to_delete])   remove a specified value
    deleted = contacts.pop(to_delete)   # delete AND return the value deleted
    print(f"Successfully delete {deleted}")

##########################################
# MENU

while True:
    print()
    print('MENU')
    print('====')
    print('1) Add a Contact')
    print('2) List Contacts')
    print('3) Delete a Contact')
    print('X) Exit')
    print('----')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        delete_contact()
    elif choice.upper() == 'X':
        #exit()
        break
    else:
        print('invalid choice')

print('SEE YA!!!')

c2 = contacts.copy()
c2 = contacts[:]   # identical

c2.extend(contacts)
pp(c2)
c3 = c2 + contacts   # NEARLY identical
pp(c3)

to_find = 'Paul,555-131'
try:
    print(contacts.index(to_find))
except:
    print('not found')

if to_find in contacts:
    print(contacts.index(to_find))
else:
    print('not found')


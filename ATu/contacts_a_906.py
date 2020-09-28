# ALIAS the pprint from from the pprint library as pp
from pprint import pprint as pp

#pprint.pprint()
#pprint()
#pp()

# GLOBAL contacts list
# contacts = []

# for DEBUGGING purposes, pre-fill my list
contacts = [
    'John,555-1212',
    'Paul,555-1313',
    'George,555-1414',
    'Ringo,555-1515'
]
contacts.sort()

# name = 'paul'.upper()    YOU CAN CALL METHODS ON VALUES not just vars


'''
name:       get_string
params:     prompt
returns:    a string
'''
def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if len(value) == 0:
            print('VALUE CANNOT BE BLANK')
            continue
        return value

'''
name:       get_int_range
params:     prompt, min and max
returns:    an int
'''
def get_int_range(prompt, min,max):
    while True:
        intstr = input(prompt)
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


def add_contact():
    global contacts
    name = get_string("Enter Contact Name: ")
    phone = get_string("Enter Phone Number: ")
    contact = f"{name},{phone}"
    # ADD contact to contacts list
    # .insert => adds at a SPECIFIC LOCATION 
    # .append => adds at the END
    contacts.append(contact)
    contacts.sort()
    print(f"{contact} added to contacts")
    print()

def list_contacts():
    global contacts
    #pp(contacts)
    for contact in contacts:
        print(f"CONTACT: {contact}")
    print()

def delete_contact():
    global contacts
    for i in range(len(contacts)):
        contact = contacts[i]
        print(f"{i}: {contact}")
    to_delete = get_int_range("Which do you want to delete: ", 0, (len(contacts) - 1) )
    # contacts.remove()  NO, this removes a specific VALUE from list
    print(f"Delted {deleted}.")

'''
MENU GOES HERE
'''
while True:
    print('MENU')
    print('====')
    print('1) Add a new Contact')
    print('2) List all Contacts')
    print('3) Delete a Contact')
    print('X) Exit')
    print('----')
    choice = input('Enter choice: ').strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        delete_contact()
    elif choice.upper() == 'X':
        break
    else:
        print('invalid choice')


print('BYEEEEEE!!')

# OTHER METHODS
c2 = contacts.copy()
c2 = contacts[:]   # EQUIVALENT

contacts.reverse()
#c3 = contacts[0:len(contacts):-1]   # COPY OF LIST IN REVERSE
c3 = contacts[::-1]   # COPY OF LIST IN REVERSE
list_contacts()

# to_find = "Paul"  # Paul,555-1313'
to_find = "Paul,555-1313"
if to_find in contacts:
    print(contacts.index(to_find))
else:
    print(f"{to_find} not found")

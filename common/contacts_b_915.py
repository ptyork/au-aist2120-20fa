contacts = [
    'John,555-1212,1/5',
    'Paul,555-1313,2/10',
    'George,555-1414,3/15',
    'Ringo,555-1515,4/20'
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
######################## END GET_STRING ########################


'''
name:       get_int_in_range
params:     prompt (string)
            minval (int)
            maxval (int)
returns:    a user-entered integer between the minval and maxval
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
######################## END GET_INT_IN_RANGE ########################


def add_contact():
    global contacts
    print()
    print('=== ADD A CONTACT ===')
    name = get_string("Enter the name: ")
    phone = get_string("Enter the phone: ")
    bday = get_string("Enter the birthday: ")
    a_contact = f"{name},{phone},{bday}"
    contacts.append(a_contact)
    print(f'Added {a_contact}')


def display_all_contacts():
    global contacts
    print()
    print('=== ALL CONTACTS ===')
    # h1 = 'Name'
    # h2 = 'Phone'
    # h3 = 'Birthday'
    # print(f"{h1:40}{h2:>20}{h3:>20}")
    print(f"{'Name':40}{'Phone':>20}{'Birthday':>20}")
    print("=" * 80)
    for ctc in contacts:
        parts = ctc.split(',')   # parts is a list of parts
        name = parts[0]
        phone = parts[1]
        bday = parts[2]
        # print(f"\tCONTACT: {parts}")
        print(f"{name:<40}{phone:>20}{bday:>20}")
    print('-' * 80)


def delete_contact():
    global contacts
    print()
    print('=== DELETE A CONTACT ===')
    for i in range(len(contacts)):
        ctc = contacts[i]
        print(f"\t{i}) {ctc}")
    
    maxval = len(contacts) - 1
    to_delete = get_int_in_range('DELETE WHICH CONTACT: ', 0, maxval)
    deleted = contacts.pop(to_delete)

    print(f'Deleted {deleted}')


def edit_contact():
    global contacts
    print()
    print('=== EDIT A CONTACT ===')
    for i in range(len(contacts)):
        ctc = contacts[i]
        print(f"\t{i}) {ctc}")
    
    maxval = len(contacts) - 1
    edit_idx = get_int_in_range('EDIT WHICH CONTACT: ', 0, maxval)

    edit_ctc = contacts[edit_idx]
    ctc_parts = edit_ctc.split(',')
    curr_name = ctc_parts[0]
    curr_phone = ctc_parts[1]
    curr_bday = ctc_parts[2]

    new_name = input(f'Enter new name ({curr_name}): ').strip()
    if len(new_name) == 0:
        new_name = curr_name

    new_phone = input(f'Enter new phone ({curr_phone}): ').strip()
    if len(new_phone) == 0:
        new_phone = curr_phone

    new_bday = input(f'Enter new birthday ({curr_bday}): ').strip()
    if len(new_bday) == 0:
        new_bday = curr_bday

    contacts[edit_idx] = f"{new_name},{new_phone},{new_bday}"


def print_contact(contact):
    parts = contact.split(',')
    print(f"NAME:\t{parts[0]}")
    print(f"PHONE:\t{parts[1]}")
    print(f"BDAY:\t{parts[2]}")


def find_contact():
    global contacts
    print()
    to_find = get_string("Enter a name to find: ")
    
    for ctc in contacts:
        parts = ctc.split(',')
        name = parts[0]
        if name.lower() == to_find.lower():
            print_contact(ctc)
            return
    print(f"SORRY {to_find} was not found")
    

######################## MAIN ########################

while True:
    print()
    print('MENU')
    print('====')
    print('1) Add contact')
    print('2) Display all contacts')
    print('3) Edit a contact')
    print('4) Delete a contact')
    print('5) Find a contact by name')
    print('X) Exit')
    print('----')

    choice = input('Enter choice: ').strip()
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_all_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        find_contact()
    elif choice.upper() == 'X':
        break
    else:
        print('INVALID CHOICE')

print('BYEEEE!')

from pprint import pprint as pp

# contacts = {
#     'john@beatles.org':'John Lennon,555-1212,1/5',
#     'paul@beatles.org':'McCartney, Paul,555-1313,2/10',
#     'george@beatles.org':'George,555-1414,3/15',
#     'ringo@beatles.org':'Ringo,555-1515,4/20'
# }


contact1 = {
    'name':'John Lennon',
    'phone': '555-1212',
    'birthday': '1/5'
}
contact2 = {
    'name':'McCartney, Paul',
    'phone': '555-1313',
    'birthday': '2/10'
}

contact_list = [
    {
        'name':'John Lennon',
        'phone': '555-1212',
        'birthday': '1/5',
        'email': 'john@beatles.org'
    },
    {
        'name':'McCartney, Paul',
        'phone': '555-1313',
        'birthday': '2/10',
        'email': 'paul@beatles.org'
    }
]

# pp(contact1)

# print(contact1['name'])
# print(contact2['name'])

# for contact in contact_list:
#     print(f"{contact['name']:20}{contact['phone']:>20}")

# for idx in range(len(contact_list)):
#     contact = contact_list[idx]
#     print(f"{contact['name']:20}{contact['phone']:>20}")

# pp(contact_list[0])
# print(contact_list[1]['name'])

# to_find = 'paul@beatles.org'

# for idx in range(len(contact_list)):
#     contact = contact_list[idx]
#     if contact['email'] == to_find:
#         print(idx)
#         pp(contact)

contact_dict = {
    'john@beatles.org': {
        'name': 'John Lennon',
        'phone': '555-1212',
        'birthday': '1/5',
        'email': 'john@beatles.org'
    },
    'paul@beatles.org': {
        'name':'McCartney, Paul',
        'phone': '555-1313',
        'birthday': '2/10',
        'email': 'paul@beatles.org'
    }
}

# for contact in contact_dict.values():
#     # contact is a contact dictionary
#     print(f"{contact['name']:20}{contact['phone']:>20}")

# pp(contact_dict['john@beatles.org'])
# print(contact_dict['paul@beatles.org']['name'])

# to_find = 'paul@beatles.org'
# # pp(contact_dict[to_find])
# pp(contact_dict.get(to_find, "NOT FOUND"))
# to_find = 'paul@yorkfamily.com'
# pp(contact_dict.get(to_find, "NOT FOUND"))

# exit()

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
    global contact_dict
    print()
    print('=== ADD A CONTACT ===')
    email = get_string("Enter the email: ")
    email = email.lower()
    if email in contact_dict:
        print("DUPLICATE EMAIL ADDRESS!!")
        return
    name = get_string("Enter the name: ")
    phone = get_string("Enter the phone: ")
    bday = get_string("Enter the birthday: ")
    # a_contact = f"{name},{phone},{bday}"
    a_contact = {}
    a_contact['name'] = name
    a_contact['phone'] = phone
    a_contact['birthday'] = bday
    a_contact['email'] = email
    
    contact_dict[email] = a_contact
    print(f'Added {email}')


def display_all_contacts():
    global contact_dict
    print()
    print('=== ALL CONTACTS ===')
    print(f"{'Email':25}{'Name':25}{'Phone':>15}{'Birthday':>15}")
    print("=" * 80)
    for contact in contact_dict.values():
        print(f"{contact['email']:25}{contact['name']:25}{contact['phone']:>15}{contact['birthday']:>15}")
    print('-' * 80)


def delete_contact():
    global contact_dict
    print()
    print('=== DELETE A CONTACT ===')
    
    to_delete = get_string('Which contact: ').lower()
    if to_delete not in contact_dict:
        print('NOT FOUND!!')
        return
    
    del contact_dict[to_delete]
    # deleted = contact_dict.pop(to_delete)

    print(f'Deleted {to_delete}')


def edit_contact():
    global contact_dict
    print()
    print('=== EDIT A CONTACT ===')

    email = get_string('Which contact: ').lower()
    if email not in contact_dict:
        print('NOT FOUND!!')
        return

    contact = contact_dict[email]
    # curr_name = contact['name']
    # curr_phone = contact['phone']
    # curr_bday = contact['birthday']
    curr_name = contact.get('name', 'N/A')
    curr_phone = contact.get('phone', 'N/A')
    curr_bday = contact.get('birthday', 'N/A')

    new_name = input(f'Enter new name ({curr_name}): ').strip()
    if len(new_name) == 0:
        new_name = curr_name

    new_phone = input(f'Enter new phone ({curr_phone}): ').strip()
    if len(new_phone) == 0:
        new_phone = curr_phone

    new_bday = input(f'Enter new birthday ({curr_bday}): ').strip()
    if len(new_bday) == 0:
        new_bday = curr_bday

    new_email = input(f'Enter new email ({email}): ').strip()
    if len(new_email) == 0:
        new_email = email

    # new_ctc = f"{new_name},{new_phone},{new_bday}"
    # new_ctc = {}
    # new_ctc['name'] = new_name
    # new_ctc['email'] = new_email
    # new_ctc['phone'] = new_phone
    # new_ctc['birthday'] = new_bday

    # del contact_dict[email]
    # contact_dict[new_email] = new_ctc

    contact['name'] = new_name
    contact['email'] = new_email
    contact['phone'] = new_phone
    contact['birthday'] = new_bday


def print_contact(contact):
    parts = contact.split(',')
    print(f"NAME:\t{parts[0]}")
    print(f"PHONE:\t{parts[1]}")
    print(f"BDAY:\t{parts[2]}")


def find_contact():
    global contact_dict
    print()
    to_find = get_string("Enter a name to find: ")
    
    was_found = False
    for contact in contact_dict.values():
        if to_find.lower() in contact['name'].lower():
            pp(contact)
            was_found = True
    if not was_found:
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

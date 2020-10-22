from pprint import pprint as pp
import shelve
from regex_module_1022 import isEmail, isPhone

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


def add_contact():
    global contacts_shelf
    print()
    print('=== ADD A CONTACT ===')
    email = get_string("Enter the email: ")
    email = email.lower()
    if not isEmail(email):
        print('BAD EMAIL ADDRESS')
        return
    if email in contacts_shelf:
        print("DUPLICATE EMAIL ADDRESS!!")
        return
    name = get_string("Enter the name: ")
    phone = get_string("Enter the phone: ")
    bday = get_string("Enter the birthday: ")
    # a_contact = f"{name},{phone},{bday}"
    new_contact = {}
    new_contact['name'] = name
    new_contact['phone'] = phone
    new_contact['birthday'] = bday
    new_contact['email'] = email
    
    contacts_shelf[email] = new_contact
    print(f'Added {email}')


def display_all_contacts():
    global contacts_shelf
    print()
    print('=== ALL CONTACTS ===')
    print(f"{'Email':25}{'Name':25}{'Phone':>15}{'Birthday':>15}")
    print("=" * 80)
    for contact in contacts_shelf.values():
        print(f"{contact['email']:25}{contact['name']:25}{contact['phone']:>15}{contact['birthday']:>15}")
    print('-' * 80)


def delete_contact():
    global contacts_shelf
    print()
    print('=== DELETE A CONTACT ===')
    
    to_delete = get_string('Which contact: ').lower()
    if to_delete not in contacts_shelf:
        print('NOT FOUND!!')
        return
    
    # deleted = contacts_shelf[to_delete]
    del contacts_shelf[to_delete]
    # deleted = contact_dict.pop(to_delete)

    print(f'Deleted {to_delete}')


def edit_contact():
    global contacts_shelf
    print()
    print('=== EDIT A CONTACT ===')

    email = get_string('Which contact: ').lower()
    if email not in contacts_shelf:
        print('NOT FOUND!!')
        return

    contact = contacts_shelf[email]
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
    if not isEmail(new_email):
        print('BAD EMAIL ADDRESS')
        return
    if len(new_email) == 0:
        new_email = email

    contact['name'] = new_name
    contact['email'] = new_email
    contact['phone'] = new_phone
    contact['birthday'] = new_bday

    if email != new_email:
        del contacts_shelf[email]
    
    contacts_shelf[new_email] = contact


def find_contact():
    global contacts_shelf
    print()
    to_find = get_string("Enter a name to find: ")
    
    was_found = False
    for contact in contacts_shelf.values():
        if to_find.lower() in contact['name'].lower():
            pp(contact)
            was_found = True
    if not was_found:
        print(f"SORRY {to_find} was not found")
    

######################## MAIN ########################

# contact_dict = {   # NO MO
# contacts_shelf = {
#     'john@beatles.org': {
#         'name': 'John Lennon',
#         'phone': '555-1212',
#         'birthday': '1/5',
#         'email': 'john@beatles.org'
#     },
#     'paul@beatles.org': {
#         'name':'McCartney, Paul',
#         'phone': '555-1313',
#         'birthday': '2/10',
#         'email': 'paul@beatles.org'
#     }
# }

# contacts_shelf = shelve.open('contacts.shelf')
with shelve.open('contacts.shelf') as contacts_shelf:

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
            contacts_shelf.sync() # OPTIONAL: EQUIVALENT TO SAVE
        elif choice == '2':
            display_all_contacts()
        elif choice == '3':
            edit_contact()
            contacts_shelf.sync() # OPTIONAL: EQUIVALENT TO SAVE
        elif choice == '4':
            delete_contact()
            contacts_shelf.sync() # OPTIONAL: EQUIVALENT TO SAVE
        elif choice == '5':
            find_contact()
        elif choice.upper() == 'X':
            break
        else:
            print('INVALID CHOICE')

# UNINDENTED so the context manager will close the shelf

# contacts_shelf.close()

print('BYEEEE!')

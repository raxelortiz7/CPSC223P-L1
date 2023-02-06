'''
Raxel Ortiz - 02-04-23 - main.py is a file that calls functions that modify out contacts table that is stored as a list 
'''
import contacts

print("\n      *** EMPLOYEE CONTACT MAIN MENU \n")
print("1. Print list\n2. Add contact\n3. Modify Contact\n4. Delete Contact\n5. Exit")

contact_list = []

while True:
    response = input('\nEnter menu choice: ')
    if response == '1':
        contacts.print_list(contact_list)
        
    elif response == '2':
        contacts.add_contacts(contact_list)
    
    elif response == '3':
        updated = contacts.modify_contacts(contact_list)
        if not updated:
            print("Invalid index number")
            
    elif response == '4':
        updated = contacts.delete_contacts(contact_list)
        if not updated:
            print("Invalid index number")
            
    elif response == '5':
        break
    
    else:
        print("Invalid index try again")
        

    
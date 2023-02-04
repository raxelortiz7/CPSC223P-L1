import contacts

print("      *** EMPLOYEE CONTACT MAIN MENU \n")
print("1. Print list\n2. Add contact\n3. Modify Contact\n4. Delete Contact\n5. Exit")
contact_list=[]
while True:
    response = input('\nEnter menu choice: ')
    if response == '1':
        print("================== CONTACT LIST ==================")
        contacts.print_list(contact_list)
        
    elif response == '2':
        first_name = input("\nEnter Frist Name: ")
        last_name = input("Enter Last Name: ") 
        contacts.add_contacts(contact_list, first_name, last_name)
        
    elif response == '3':
        i = int(input("\nEnter the index number:"))
        first_name = input("\nEnter New Frist Name: ")
        last_name = input("Enter New Last Name: ")
        changed = contacts.modify_contacts(contact_list, first_name, last_name, i)
        if not changed:
            print("Invalid index number")
            
    elif response == '4':
        i = int(input("\nEnter index number: "))
        changed = contacts.delete_contacts(contact_list, i)
        if not changed:
            print("Invalid index number")
            
    elif response == '5':
        break
    
    else:
        print("Invalid response -_-")
        break

    
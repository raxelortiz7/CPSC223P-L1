'''
Raxel Ortiz - 02-04-23 - contacts.py is a file that stores functions that modify out contacts table that is stored as a list 
'''
contact_list = []
def print_list(contact_list):
    '''
    Print each index of the list using a for loop
    prints out the first and second index of each item since they 
    lists as well
    '''
    print("\n================== CONTACT LIST ==================")
    print(f'{"Index":8}{"First name":22}{"Last name":22}')
    print("======  ====================  ==================== ")
    for i in range(len(contact_list)): print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}') 
        
def add_contacts(contact_list):
    '''
    Takes a list as a parameter. User is asked for first name
    and last name usint input()
    from there imput is placed into index 0, and 1 (stored as a list of 2 indexes)
    and appended on to the main list 
    '''
    first_name, last_name = input("\nEnter Frist Name: "), input("Enter Last Name: ")
    contact_list.append([first_name, last_name])
    return contact_list

def modify_contacts(contact_list):
    '''
    ask the user what index they want to change
    if the index is in range we will take the new information
    and update the list 
    if not we well respond with an invalid index
    '''
    i = int(input("\nEnter the index number:"))
    if i < len(contact_list):
        first_name = input("\nEnter New Frist Name: ")
        last_name = input("Enter New Last Name: ")
        contact_list[i] = [first_name, last_name] 
        return True

def delete_contacts(contact_list):
    '''
    Takes user input for what needs to be deleted 
    if index in range we will update list else we will 
    return invalid index
    '''
    i = int(input("\nEnter index number: "))
    if i < len(contact_list): 
        del(contact_list[i])
        return True
    else: 
        return False

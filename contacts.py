'''
Raxel Ortiz - 02-04-23 - contacts.py is a file that stores functions that modify out contacts table that is stored as a list 
'''
def print_list(contact_list):
    print(f'{"Index":8}{"First name":22}{"Last name":22}')
    print("======  ====================  ==================== ")
    for i in range(len(contact_list)): print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}') 
        
def add_contacts(contact_list, first_name, last_name): contact_list.append([first_name, last_name])

def modify_contacts(contact_list, first_name, last_name, i):
    if i < len(contact_list):
        contact_list[i] = [first_name, last_name] 
        return True
    else: 
        return False

def delete_contacts(contact_list, i):
    if i < len(contact_list): 
        del(contact_list[i])
        return True
    else: 
        return False

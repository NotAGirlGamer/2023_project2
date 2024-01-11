import functions

def start():
    choice = functions.menu()
    
    if choice == 1:
        functions.add_contact()
        print ('')
        start()
        
    if choice == 2:
        functions.search_contacts()
        print ('')
        start()
        
    if choice == 3:
        functions.edit_contacts()
        print ('')
        start()
        
    if choice == 4:
        functions.delete_contacts()
        print ('')
        start()
        
    if choice == 5:
        functions.display_all_contacts()
        print ('')
        start()
        
    if choice == 6:
        print ('')
        print ('Bye')
            
start()
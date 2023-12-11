#project 2 menu

def menu():
    #menu accepts no arguemnts
    #it displays a menu to the user
    #returns an integer for choice
    
    #display the menu
    print("\nWelcome to the Contact Management system. What would you like to do?")
    print ("1) Add a contact")
    print("2) Modify a contact")
    print("3) Display a contact")
    print ("4) Display all contacts")
    print ("5) Delete a contact")
    print("6) Exit")
        
    #prompt the user for a choice
    choice = input("Enter a choice: ")
        
    #return choice
    return int(choice)
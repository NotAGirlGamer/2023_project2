#project 2 menu

def menu():
    #menu accepts no arguemnts
    #it displays a menu to the user
    #returns an integer for choice
    
    #display the menu
    print("\nWelcome to the Contact Management system. What would you like to do?")
    print ("1) Add contact")
    print("2) Search contact")
    print("3) Edit contact")
    print ("4) Delete Contact")
    print ("5) Display all Contacts")
    print("6) Exit")
        
    #prompt the user for a choice
    choice = input("Enter a choice: ")
        
    #return choice
    return int(choice)
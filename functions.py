def display_all_contacts():
    #display_all_contacts accepts no arguments
    #it loops to display all information in contacts.txt
    
    #open contact.txt and read the first description
    contact_file = open('contact.txt', 'r')
    name = contact_file.readline()
    
    #loop to read, strip, and output each record
    while name!= '':
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()

        #strip the newline
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')

        print("\nName:", name)
        print("\nStreet Address:", street_address)
        print("\nPhone Number:", phone_number)
        print("\nEmail Address:", email_address)
        print()

        #get the next name
        name = contact_file.readline()

    #close the file and output to the user
    contact_file.close()
    print("\nAll records retrieved.")
    
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

def add_contact():
    #add_contact accepts no arguments
    #it opens the file contacts.txt and appends a new contact to it
    #it loops while the user wants to continue entering records
    #it prompts the user for the contact name, street address, phone number, and email address
    #user should be prompted if they want to continue

    #prime the loop, open the file to append, display the header
    another = 'y'
    contact_file = open("contact.txt", "a")
    
    #loop to get the records
    while another.lower() == "y":
        print("Enter the following contact data:\n")
        name = input("Name: ")
        street_address = input("Street Address: ")
        phone_number = input("Phone number: ")
        email_address = input("Email Address: ")

        #append the data to the file
        contact_file.write(name + '\n')
        contact_file.write(street_address + '\n')
        contact_file.write(phone_number + '\n')
        contact_file.write(email_address + '\n')

        #prompt for another entry
        another = input("\nDo you wish to enter another contact? (y to continue): ")

    #close the file and output saved message
    contact_file.close()
    print("\nAll data appended to contact.txt.")
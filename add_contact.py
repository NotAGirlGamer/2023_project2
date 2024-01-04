#project 2 add_contact

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
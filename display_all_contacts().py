#project 2 display_all_contacts

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

        print("\nName:", name)
        print("Quantity (in pounds):", pounds)

        #get the new description
        desc = contact_file.readline()

    #close the file and output to the user
    contact_file.close()
    print("\nAll records retrieved.")
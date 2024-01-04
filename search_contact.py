#search_contact searches for a specific contact in the file contact.txt

def search_contact():
    #search_contact accepts no arguments
    #it prompts user for a contact name and opens contact.txt to see if it exists
    #if file is not found, the program tells the user.
    
    #boolean flag to determine search status
    found = False

    #get input from the user
    search = input("Enter a contact to search for: ")

    #open the file contact.txt
    contact_file = open('contact.txt', 'r')

    #get the first name from the file
    name = contact_file.readline()

    #loop to read each line of the file
    while name != '':
        street_address = contact_file.readline()
        
        phone_number = contact_file.readline()
        
        email_address = contact_file.readline()

        #strip the newline from the description
        name = name.rstrip('\n')

        if name.lower() == search.lower(): #determine if the record is found and display the record
            print ("\nRecord found!\n")
            print("Name:", name)
            print("Address:", street_address)
            print("Phone Number:", phone_number)
            print("Email Address:", email_address)
            
            found = True #toggle the flag variable to true

        #get the next name
        name = contact_file.readline()

    contact_file.close()

    if not found: #found = False
        print ("\nThe record was not found.")

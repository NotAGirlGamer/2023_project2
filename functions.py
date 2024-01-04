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
    
def delete_contact():
    #delete accepts no arguments
    #it opens the file contacts.txt and searches for a string to delete
    # it writes every record except for the record to delete
    #to a tempoary file and deletes the old file
    #it renames temp to contacts and closes the file
    
    #boolean flag variable
    found = False
    
    #Take input from the user for the search criteria
    search  = input('Enter contact to delete: ')
    
    #open the contact.txt file to read and a new temp file to write
    contact_file = open('contacts.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first name
    name = contact_file.readline()
    
    #loop the read nad process each record
    while name != '':
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()
        
        #strip newline
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')
        
        #search for and delete the record
        if search.lower() != name.lower(): #this is a record we need to keep
            #write both to the temp file
            temp_file.write(name + '\n')
            temp_file.write(street_address + '\n')
            temp_file.write(phone_number + '\n')
            temp_file.write(email_address + '\n')
        else:
            found = True
            
        #read the next name
        name = contact_file.readline()
            
    #all record have been processed, close, remove, and rename files
    contact_file.close()
    temp_file.close()
    
    os.remove('contacts.txt') # elete the orginal
    os.rename('temp.txt', 'contacts.txt') #rename temp to contact
    
    #confirm deletion to the user
    if not found: #this is the same as if found == False
        print ( '\nRecord not found.\n')
    else:
        print (search, 'has been deleted from contact.txt')
        
def search_contacts():
    #search contact accepts no arguments
    #It prompts the user for a contact to search for
    #and searches contacts.txt for the user input
    #if no records match, it outputs a message to the user
    # if the record is found, it displays the contact and info regarding that contact
    
    #boolean flag to determine search status
    found = False
    
    # take input from the user for the search criteria
    search = input('Enter a contact name to search for: ')
    
    #open the contact.txt file
    contact_file = open('contacts.txt', 'r')
    
    #get the first name to prime the loop
    name = contact_file.readline()
    
    #loop to read each line of the file to find the search criteria
    while name != '':
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()
        
        #strip the newline from the name and pounds
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')
        
        if name.lower() == search.lower():
            print ('\nRecord Found!\n')
            print ('Name:', name)
            print ('Street Address:', street_address)
            print ('Phone Number:', phone_number)
            print ('Email Address:', email_address)
            
            found = True
            
        #read the next line to continue the loop
        name = contact_file.readline()
        
    #Display a message to the user saying stating the contact was not found
    if not found: # same as saying if found == False
        print ('\nThe record was not found.\n')
        
    contact_file.close()
    
def edit_contact():
    #edit contact accepts no arguments
    #It uses the os module - this is needed to eprform OS related file commands
    
    #boolean flag variable
    found = False
    
    # get the search name and new info to update
    search = input('Enter the contact to edit: ')
    new_street_address = input('Enter the new street address: ')
    new_phone_number = input('Enter the new phone number: ')
    new_email_address = input('Enter the new email address: ')
    
    #open the contact.txt to read and a new temp file to write
    contact_file = open('contacts.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first name to prime the loop
    name = contact_file.readline()
    
    #loop to read and process each line
    while name != '':
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()
        
        #strip newline
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')
        
        #search for the contact
        if search.lower() == name.lower(): #contact has been found
            temp_file.write(name + '\n')
            temp_file.write(new_street_address + '\n')
            temp_file.write(new_phone_number + '\n')
            temp_file.write(new_email_address + '\n')
            
            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(street_address + '\n')
            temp_file.write(phone_number + '\n')
            temp_file.write(email_address + '\n')
            
        #read the next name
        name = contact_file.readline()
        
    #close the files    
    contact_file.close()
    temp_file.close()
    
    #all files have been processed and closed. Delete and rename the files
    #delete the orignal
    os.remove('contacts.txt')
    #rename the temp file to contact.txt
    os.rename('temp.txt', 'contacts.txt')
    
    #notify user the contact was not found in the file
    if not found:
        print ('\nRecord not found...')
    else:
        print ('The info for', search, 'has been updated')
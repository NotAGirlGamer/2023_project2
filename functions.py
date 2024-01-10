import os

def display_all_contacts():
    #display_all_contacts accepts no arguments
    #it loops to display all information in contacts.txt
    
    #open contacts.txt and read the first description
    contacts_file = open('contacts.txt', 'r')
    name = contacts_file.readline()
    
    #loop to read, strip, and output each record
    while name!= '':
        street_address = contacts_file.readline()
        phone_number = contacts_file.readline()
        email_address = contacts_file.readline()

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
        name = contacts_file.readline()

    #close the file and output to the user
    contacts_file.close()
    print("\nAll records retrieved.")
    
def menu():
    #menu accepts no arguemnts
    #it displays a menu to the user
    #returns an integer for choice
    
    #display the menu
    print("\nWelcome to the contacts Management system. What would you like to do?")
    print ("1) Add contacts")
    print("2) Search contacts")
    print("3) Edit contacts")
    print ("4) Delete contacts")
    print ("5) Display all contacts")
    print("6) Exit")
        
    #prompt the user for a choice
    choice = input("Enter a choice: ")
        
    #return choice
    return int(choice)

def add_contact():
    #add_contacts accepts no arguments
    #it opens the file contacts.txt and appends a new contacts to it
    #it loops while the user wants to continue entering records
    #it prompts the user for the contacts name, street address, phone number, and email address
    #user should be prompted if they want to continue

    #prime the loop, open the file to append, display the header
    another = 'y'
    contacts_file = open("contacts.txt", "a")
    
    #loop to get the records
    while another.lower() == "y":
        print("Enter the following contacts data:\n")
        name = input("Name: ")
        street_address = input("Street Address: ")
        phone_number = input("Phone number: ")
        email_address = input("Email Address: ")

        #append the data to the file
        contacts_file.write(name + '\n')
        contacts_file.write(street_address + '\n')
        contacts_file.write(phone_number + '\n')
        contacts_file.write(email_address + '\n')

        #prompt for another entry
        another = input("\nDo you wish to enter another contacts? (y to continue): ")

    #close the file and output saved message
    contacts_file.close()
    print("\nAll data appended to contacts.txt.")
    
def delete_contacts():
    #delete accepts no arguments
    #it opens the file contacts.txt and searches for a string to delete
    # it writes every record except for the record to delete
    #to a tempoary file and deletes the old file
    #it renames temp to contacts and closes the file
    
    #boolean flag variable
    found = False
    
    #Take input from the user for the search criteria
    search  = input('Enter contacts to delete: ')
    
    #open the contacts.txt file to read and a new temp file to write
    contacts_file = open('contacts.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first name
    name = contacts_file.readline()
    
    #loop the read nad process each record
    while name != '':
        street_address = contacts_file.readline()
        phone_number = contacts_file.readline()
        email_address = contacts_file.readline()
        
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
        name = contacts_file.readline()
            
    #all record have been processed, close, remove, and rename files
    contacts_file.close()
    temp_file.close()
    
    os.remove('contacts.txt') # elete the orginal
    os.rename('temp.txt', 'contacts.txt') #rename temp to contacts
    
    #confirm deletion to the user
    if not found: #this is the same as if found == False
        print ( '\nRecord not found.\n')
    else:
        print (search, 'has been deleted from contacts.txt')
        
def search_contacts():
    #search contacts accepts no arguments
    #It prompts the user for a contacts to search for
    #and searches contacts.txt for the user input
    #if no records match, it outputs a message to the user
    # if the record is found, it displays the contacts and info regarding that contacts
    
    #boolean flag to determine search status
    found = False
    
    # take input from the user for the search criteria
    search = input('Enter a contacts name to search for: ')
    
    #open the contacts.txt file
    contacts_file = open('contacts.txt', 'r')
    
    #get the first name to prime the loop
    name = contacts_file.readline()
    
    #loop to read each line of the file to find the search criteria
    while name != '':
        street_address = contacts_file.readline()
        phone_number = contacts_file.readline()
        email_address = contacts_file.readline()
        
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
        name = contacts_file.readline()
        
    #Display a message to the user saying stating the contacts was not found
    if not found: # same as saying if found == False
        print ('\nThe record was not found.\n')
        
    contacts_file.close()
    
def edit_contacts():
    #edit contacts accepts no arguments
    #It uses the os module - this is needed to eprform OS related file commands
    
    #boolean flag variable
    found = False
    
    # get the search name and new info to update
    search = input('Enter the contacts to edit: ')
    new_street_address = input('Enter the new street address: ')
    new_phone_number = input('Enter the new phone number: ')
    new_email_address = input('Enter the new email address: ')
    
    #open the contacts.txt to read and a new temp file to write
    contacts_file = open('contacts.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first name to prime the loop
    name = contacts_file.readline()
    
    #loop to read and process each line
    while name != '':
        street_address = contacts_file.readline()
        phone_number = contacts_file.readline()
        email_address = contacts_file.readline()
        
        #strip newline
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')
        
        #search for the contacts
        if search.lower() == name.lower(): #contacts has been found
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
        name = contacts_file.readline()
        
    #close the files    
    contacts_file.close()
    temp_file.close()
    
    #all files have been processed and closed. Delete and rename the files
    #delete the orignal
    os.remove('contacts.txt')
    #rename the temp file to contacts.txt
    os.rename('temp.txt', 'contacts.txt')
    
    #notify user the contacts was not found in the file
    if not found:
        print ('\nRecord not found...')
    else:
        print ('The info for', search, 'has been updated')
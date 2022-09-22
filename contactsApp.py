import contacts
import pickle
import time
import operator
PIK = "contacts.dat"


#Contact Manager Class
class SystemContacts (object):
    '''The System Contacts class will contain contacts stored in a bytearray'''

    def __init__(self):
        '''initialize the Contact Manager'''
        self.sysContacts=[] #defines a class variable - a list of the contatcs stored in the Contact Manager
        try: #Skips the ValueError when the contacts.dat file is empty
          with open(PIK, "rb") as f:
            for _ in range(pickle.load(f)):
              self.sysContacts.append(pickle.load(f))
            f.close()
        except Exception as err:
           pass
    

    def addContact(self, account):
        '''Allows a user to add a contact to the system'''
        while True:
            name = input("Enter the contact's name:")
            phone = input("Enter the contact's phone number:")
            email = input("Enter the contact's email address:")
            contactValid = True #Changes to false if contact already exists

            if name == "":
                print("ERROR: No name given for the contact\n")
                break
            if phone == "":
                phone = "N/A"
            if email == "":
                email = "N/A"
            
            for contact in self.sysContacts:
                if contact.getName() == name and contact.getAccount() == account: #Add if none of the contacts match the name entered and the logged in user
                    print ("ERROR: Contact already exists\n")
                    time.sleep(1)
                    contactValid = False #Contact already exists
                    break
                else:
                    contactValid = True
                    pass
                
            if contactValid == True: #If contact does not already exist    
                self.sysContacts.append(contacts.Contact(name, phone, email, account)) #Append object list in System Contacts class using contacts class
                print("Contact added")
                self.sysContacts.sort(key=operator.attrgetter('name'))
                self.dumpPickle() #Update .dat file with changes
                time.sleep(1)
                break
            else:
                break


    def viewContacts(self, account):
        '''Outputs a list of all the contacts linked to the user's account'''
        contactValid = False #Changes to true if contact found
        print("\n-------"+account+"'s Contacts-------")
        for contact in self.sysContacts: #Go through each contact in the object list
            if contact.getAccount() == account: #Print contacts matching the logged in user
                contactValid = True #Contacts found
                print (contact)
            
            else:
                pass
            
        if contactValid == False: #If no contacts were found
            print("You have no contacts stored")

        print("------------------------------")
        print("\n")
            
        time.sleep(5)
            

    def lookupContact(self, account):
        '''Allows the user to enter a name for a specific contact they want to view'''
        name = input("Enter the name of the contact you want to view: ")
        contactValid = False #Changes to true if contact found
        
        for contact in self.sysContacts: #Go through each contact in the object list
            if contact.getName() == name and contact.getAccount() == account:
                contactValid = True #Contact found
                print(contact) #Print the contact if it matches the name entered and the logged in user
                time.sleep(3)
            else:
                pass

        if contactValid == False: #If no contacts were found
            print("Contact not found\n")
            time.sleep(1)
        

    def deleteContact(self, account):
        '''Allows the user to delete a contact from their account'''
        name = input("Enter the name of the contact you want to delete: ")
        contactValid = False #Changes to true if contact found
        
        for contact in self.sysContacts: #Go through each contact in the object list
            if contact.getName() == name and contact.getAccount() == account: #Delete if a contact matches the name entered and the logged in user
                 print("Contact Deleted\n")
                 self.sysContacts.remove(contact)
                 contactValid = True #Contact found
                 self.dumpPickle() #Update .dat file
                 time.sleep(3)
            else:
               pass
                
        if contactValid == False: #If no contacts were found
            print("Contact not found\n")
            time.sleep(1)
        
    
    def clearUserContacts(self, account):
       '''Clears all data asociated with a specific user within the contacts.dat pickle file'''
       for i in range(0, len(self.sysContacts)): #Delete contact objects with matching account (logged in user) parameters in the sysContacts object list
          for contact in self.sysContacts:
            if contact.getAccount() == account:
                self.sysContacts.remove(contact) 
       self.dumpPickle() #Update .dat file
    

    def dumpPickle(self):
        '''Saves the list of contacts to a pickle file (StackOverflow)'''
        with open(PIK, "wb") as f:
          pickle.dump(len(self.sysContacts), f)
          for contact in self.sysContacts:
            pickle.dump(contact, f)
          f.close()
        time.sleep(1)
        

    def clearContacts(self):
        '''Clears all data within the contacts.dat pickle file'''
        for i in range(0, len(self.sysContacts)): #Delete all contact objects in the sysContacts object list
          for contact in self.sysContacts:
            self.sysContacts.remove(contact) 
        self.dumpPickle() #Delete everything in .dat file
        

    
#mainline
myContacts = SystemContacts() #Variable to access methods in System Contacts Class

#Main Menu
def mainMenu(username):
    '''Main Menu for selecting an option in the app'''
    try: #Skips syntax error when a string value is accidentally inputted
        while True:
            print("~~~~Contact Manager~~~~")
            print ("\n**Choose an Option**")
            print ("\n1. Add Contact\n2. View Contacts\n3. Lookup Contact\n4. Remove Contact\n5. Return to Desktop")
            selection = int(input("> "))

            if selection == 1:
                myContacts.addContact(username)
            elif selection == 2:
                myContacts.viewContacts(username)
            elif selection == 3:
                myContacts.lookupContact(username)
            elif selection == 4:
                myContacts.deleteContact(username)
            elif selection == 5:
                print ("Closing Program...")
                myContacts.dumpPickle()
                break
            else:
                print ("Invalid Selection\n")
                
    except Exception as err:
        print ("Invalid Selection\n")
            

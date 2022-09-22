import accounts
import desktop
import contactsApp
import notesApp
import time
import pickle
PIK = "accounts.dat"


#Operating System Class
class OperatingSystem (object):
  '''The Operating System will contain accounts stored in a bytearray'''
  
  def __init__(self):
    '''initialize the OS'''
    self.userAccounts=[] #defines a class variable - a list of the accounts stored in the OS
    try: #Skips the ValueError when the accounts.dat file is empty
      with open(PIK, "rb") as f:
        for _ in range(pickle.load(f)):
          self.userAccounts.append(pickle.load(f))
        f.close()
    except Exception as err:
       pass


  def login(self):
    '''Allows a user to login to the system'''
    if len(self.userAccounts) > 0: #If there are user accounts in the system
      username = input("Please enter a Username:")
      password = input("Please enter a Password:")
      accountValid = False
    
      for account in self.userAccounts:
          if account.getUsername() == username and account.getPassword() == password: #Login user if entered credentials match a user account
              print ("Loading your personal settings....")
              time.sleep(3)
              desktop.myDesktop(username) #Load the user's desktop sending the username as a parameter to filter out files belonging to the user
              accountValid = True
              break
          else:
              pass
            
      if accountValid == False:
        print("ERROR: Incorrect username or password\n")
        time.sleep(1)
          
    else:
      print("No user accounts registerd into the System\n")
      time.sleep(1)

      
            
  def addAccount(self):
    '''Allows a user to add an account to the system'''
    while True:
        username = input("Enter a username for the new account:")
        password = input("Enter a password for the new account:")
        accountValid = True #Changes to false if account already exists

        if username == "":
          print("ERROR: No username given for the account\n")
          time.sleep(1)
          break
        
        for account in self.userAccounts:
            if account.getUsername() == username: #Add if none of the accounts match the username entered for the new account
                print ("ERROR: Account already exists\n")
                time.sleep(1)
                accountValid = False #Account already exists
                break
            else:
                accountValid = True
                pass
            
        if accountValid == True: #If account does not already exist    
            self.userAccounts.append(accounts.Account(username, password)) #Append object list in Operating System class using accounts class
            print("Account added (Keep record of the account information)\n")
            self.dumpPickle() #Update .dat file with changes
            time.sleep(1)
            break
        else:
            break
          
  def deleteAccount(self):
    '''Allows the user to delete an account from the system'''
    if len(self.userAccounts) > 0: #If there are accounts in the system
      username = input("Please the username of the account you would like to remove:")
      password = input("Please enter the Password associated with the account:")
      accountValid = False #For checking credentials
    
      for account in self.userAccounts:
          if account.getUsername() == username and account.getPassword() == password:
              contactsApp.myContacts.clearUserContacts(username)
              notesApp.myNotes.clearUserNotes(username)
              self.userAccounts.remove(account)
              print("Account Deleted\n")
              self.dumpPickle() #Update .dat file with changes
              accountValid = True #Credentials are correct
              break
          else:
              pass
            
      if accountValid == False: #If credentials are incorrect after going through every account
        print("ERROR: Incorrect username or password")
        time.sleep(1)
          
    else: #If there are no accounts in the system
      print("No user accounts registerd into the System")
      time.sleep(1)
    
          
  def dumpPickle(self):
    '''Saves the list of user accounts to a pickle file (StackOverflow)'''
    with open(PIK, "wb") as f:
      pickle.dump(len(self.userAccounts), f)
      for account in self.userAccounts:
        pickle.dump(account, f)
      f.close()
    time.sleep(2)


  def FDISK(self):
    '''Formats all the data in the system's .dat pickle files (eg. accounts, contacts, notes)'''
    formatConfirm = input("This will reformat and destroy all data in PyOS, continue? (Y/N) ")
    if formatConfirm == "Y" or formatConfirm == "y":
      print("Formatting...\n")
      with open(PIK, "wb") as f:
        contactsApp.myContacts.clearContacts() #Clear all contact data
        notesApp.myNotes.clearNotes() #Clear all note data

        #Clear System Accounts
        for i in range(0, len(self.userAccounts)): #Delete all account objects in the userAccounts object list
          for account in self.userAccounts:
            self.userAccounts.remove(account) 
        self.dumpPickle() #Delete everything in .dat file

    elif formatConfirm == "N" or formatConfirm == "n":
        print ("Operation Cancelled\n")

    else:
      print ("Invalid Input\n")
                

  def __str__(self):
    '''Prints number of accounts in the system'''
    output = "Accounts in the System: "
    output += str(len(self.userAccounts))+"\n"
    return output


#mainline
print("SYSTEM STARTED")
time.sleep(1)
print("Loading PyOS 1.0.1.....")
time.sleep(3)
mySystem = OperatingSystem() #Variable to access methods in Operating System Class

while True:
  try: #Skips syntax error when a string value is accidentally inputted
    #main OS menu
    print ("\n~~~~Welcome to PyOS~~~~\n")
    print(mySystem)
    print ("**Choose an Option**")
    print ("\n1. Login\n2. Add Account\n3. Remove Account\n4. Shutdown System\n5. Reformat System Memory")
    selection = int(input("> "))
    if selection == 1:
        mySystem.login()
           
    elif selection == 2:
        mySystem.addAccount()
           
    elif selection == 3:
        mySystem.deleteAccount()
           
    elif selection == 4:
        #System Shutdown
        exitConfirm = input("Are you sure you want to shut down? (Y/N):")
        if exitConfirm == "Y" or exitConfirm == "y":
           print("Saving your settings......")
           mySystem.dumpPickle() #Update .dat file
           print("PyOS is shutting down......")
           time.sleep(2)
           break

        elif exitConfirm == "N" or exitConfirm == "n":
           print ("Operation Cancelled\n")

        else:
           print ("Invalid Input\n")
             
    elif selection == 5:
         mySystem.FDISK()
            
    else:
        print ("Invalid Selection\n")
        pass

  except Exception as err:
    print ("Invalid Selection\n")

    

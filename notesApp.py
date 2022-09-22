import notes
import pickle
import time
import operator
PIK = "notes.dat"


#note Manager Class
class SystemNotes (object):
    '''The System Notes will contain notes stored in a bytearray'''

    def __init__(self):
        '''initialize the My Notes App'''
        self.sysNotes=[] #defines a class variable - a list of the notes stored in the My Notes App
        try: #Skips the ValueError when the notes.dat file is empty
          with open(PIK, "rb") as f:
            for _ in range(pickle.load(f)):
              self.sysNotes.append(pickle.load(f))
            f.close()
        except Exception as err:
           pass
    

    def addNote(self, account):
        '''Allows a user to add a note to the system'''
        while True:
            noteTitle = input("Enter the note title:")
            date = input("Enter the note date (DD/MM/YYYY):")
            content = input("Enter the note content:")
            noteValid = True #Changes to false if note already exists

            if noteTitle == "":
                print("ERROR: No title given for the note")
                break
            if date == "":
                date = "No date specified"
            if content == "":
                print ("ERROR: This note has no content")
                break
            
            for note in self.sysNotes:
                if note.getTitle() == noteTitle and note.getAccount() == account: #Add if none of the notes match the title entered and the logged in user
                    print ("ERROR: Note already exists")
                    time.sleep(1)
                    noteValid = False #Note already exists
                    break
                else:
                    noteValid = True
                    pass
                
            if noteValid == True: #If note does not already exist    
                self.sysNotes.append(notes.Note(noteTitle, date, content, account)) #Append object list in System Notes class using notes class
                print("Note added\n")
                self.dumpPickle() #Update .dat file with changes
                time.sleep(1)
                break
            else:
                break


    def viewNotes(self, account):
        '''Outputs a list of all the notes linked to the user's account'''
        noteValid = False #Changes to true if note found
        print("\n--------"+account+"'s Notes---------")
        for note in self.sysNotes: #Go through each note in the object list
            if note.getAccount() == account: #Print notes matching the logged in user
                noteValid = True #Notes found
                print(note)
            else:
                pass
            
        if noteValid == False: #If no notes were found
            print("You have no notes stored")

        print("------------------------------")
        print("\n")

        time.sleep(5)
            

    def lookupNote(self, account):
        '''Allows the user to enter a title for a specific note they want to view'''
        noteTitle = input("Enter the title of the note you want to view: ")
        noteValid = False #Changes to true if note found
        
        for note in self.sysNotes: #Go through each note in the object list
            if note.getTitle() == noteTitle and note.getAccount() == account:
                noteValid = True #Note found
                print(note) #Print the note if it matches the title entered and the logged in user
                time.sleep(3)
            else:
                pass

        if noteValid == False: #If no notes were found
            print("Note not found\n")
            time.sleep(1)
        

    def deleteNote(self, account):
        '''Allows the user to delete a note from their account'''
        noteTitle = input("Enter the title of the note you want to delete: ")
        noteValid = False #Changes to true if note found
        
        for note in self.sysNotes: #Go through each note in the object list
            if note.getTitle() == noteTitle and note.getAccount() == account: #Delete if a note matches the title entered and the logged in user
                 print("Note Deleted\n")
                 self.sysNotes.remove(note)
                 noteValid = True #Note found
                 self.dumpPickle() #Update .dat file
                 time.sleep(3)
            else:
               pass
                
        if noteValid == False: #If no notes were found
            print("Note not found\n")
            time.sleep(1)
        
    
    def clearUserNotes(self, account):
       '''Clears all data asociated with a specific user within the notes.dat pickle file'''
       for i in range(0, len(self.sysNotes)): #Delete note objects with matching account (logged in user) parameters in the sysNotes object list
          for note in self.sysNotes:
            if note.getAccount() == account:
                self.sysNotes.remove(note) 
       self.dumpPickle()

    def dumpPickle(self):
        '''Saves the list of notes to a pickle file (StackOverflow)'''
        with open(PIK, "wb") as f:
          pickle.dump(len(self.sysNotes), f)
          for note in self.sysNotes:
            pickle.dump(note, f)
          f.close()
        time.sleep(1)
        

    def clearNotes(self):
        '''Clears all data within the notes.dat pickle file'''
        for i in range(0, len(self.sysNotes)): #Delete all note objects in the sysNotes object list
          for note in self.sysNotes:
            self.sysNotes.remove(note) 
        self.dumpPickle() #Delete everything in .dat file

    
#mainline
myNotes = SystemNotes() #Variable to access methods in System Notes Class

#Main Menu
def mainMenu(username):
    '''Main Menu for selecting an option in the app'''
    while True:
        try: #Skips syntax error when a string value is accidentally inputted
            print("~~~~My Notes~~~~")
            print ("\n**Choose an Option**")
            print ("\n1. Add Note\n2. View Notes\n3. Lookup Note\n4. Remove Note\n5. Return to Desktop")
            selection = int(input("> "))

            if selection == 1:
                myNotes.addNote(username)
            elif selection == 2:
                myNotes.viewNotes(username)
            elif selection == 3:
                myNotes.lookupNote(username)
            elif selection == 4:
                myNotes.deleteNote(username)
            elif selection == 5:
                print ("Closing Program...")
                myNotes.dumpPickle()
                break
            else:
                print ("Invalid Selection\n")

        except Exception as err:
            print ("Invalid Selection\n")
                


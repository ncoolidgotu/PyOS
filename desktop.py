import contactsApp
import notesApp
import time

def myDesktop(username):
    while True:
        try: #Skips syntax error when a string value is accidentally inputted
            print("\n~~~~Hello "+username+"~~~~")
            print ("**Choose an Option**")
            print ("\n1. Run Contacts Manager\n2. Run My Notes\n3. Logout")
            selection = int(input("> "))

            if selection == 1:
                print("Launching Contacts App...")
                time.sleep(1)
                print()
                contactsApp.mainMenu(username)
            elif selection == 2:
                print("Launching My Notes App...")
                time.sleep(1)
                print()
                notesApp.mainMenu(username)
            elif selection == 3:
                print ("Logging Off...\n")
                time.sleep(2)
                break
            else:
                print ("Invalid Selection\n")

        except Exception as err:
            print("Invalid Selection\n")
        




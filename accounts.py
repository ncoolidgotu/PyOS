class Account(object):
    def __init__(self, username, password):
        '''This will define a User Account and its properties'''
        self.username = username
        self.password = password


    #Accessors
    def getUsername(self):
        '''Retrieves username for the account'''
        return self.username

    def getPassword (self):
        '''Retrieves the password for the account'''
        return self.password

    #Mutator Methods
    def setUsername(self):
        '''Sets username for the account'''
        self.username = username

    def setPassword (self):
        '''Sets the password for the account'''
        self.password = password

    def __str__(self):
        '''Returns information about the account object'''
        return "\nUsername: "+str(self.username)+"\nPassword: "+str(self.password)+"\n"
        
    

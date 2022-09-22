class Contact(object):
    def __init__(self, name, phone, email, account):
        '''This will define a System Contact and its properties'''
        self.name = name
        self.phone = phone
        self.email = email
        self.account = account


    #Accessors
    def getName(self):
        '''Retrieves name for the contact'''
        return self.name

    def getPhone (self):
        '''Retrieves the phone number for the contact'''
        return self.phone
    
    def getEmail (self):
        '''Retrieves the email address for the contact'''
        return self.email
    
    def getAccount (self):
        '''Retrieves the account owner of the contact'''
        return self.account

    #Mutator Methods
    def setUsername(self):
        '''Sets the name for the contact'''
        self.name = name

    def setPhone (self):
        '''Sets the phone number for the contact'''
        self.phone = phone
        
    def setEmail (self):
        '''Sets the email address for the contact'''
        self.email = email

    def setAccount (self):
        '''Sets the account owner for the contact'''
        self.account = account 
        
    def __str__(self):
        '''Returns information about the contact object'''
        return "\nName: "+str(self.name)+"\nPhone: "+str(self.phone)+"\nEmail: "+str(self.email)+"\n"

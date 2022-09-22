class Note(object):
    def __init__(self, noteTitle, date, noteContent, account):
        '''This will define a System Note and its properties'''
        self.noteTitle = noteTitle
        self.date = date
        self.noteContent = noteContent
        self.account = account


    #Accessors
    def getTitle(self):
        '''Retrieves title for the note'''
        return self.noteTitle

    def getDate (self):
        '''Retrieves the date for the note'''
        return self.date
    
    def getContent (self):
        '''Retrieves the content within the note'''
        return self.noteContent
    
    def getAccount (self):
        '''Retrieves the account owner of the note'''
        return self.account

    #Mutator Methods
    def setTitle(self):
        '''Sets the title for the note'''
        self.noteTitle = noteTitle

    def setDate (self):
        '''Sets the date the note was published on'''
        self.date = date
        
    def setContent (self):
        '''Sets the content within the note'''
        self.noteContent = noteContent

    def setAccount (self):
        '''Sets the account owner for the note'''
        self.account = account 
        
    def __str__(self):
        '''Returns information about the note object'''
        return "\n"+str(self.date)+"\n****"+str(self.noteTitle)+"****\n"+str(self.noteContent)+"\n"


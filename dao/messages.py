class MessagesDAO:

    def getAllMessages(self):
        message = [123, 'This is a message', 'February, 20, 2019']
        return message 
    def getMessageById(self, uid):
        if(self.getAllMessages[0]==123):
            return self.getAllMessages()
        return 
    def getMessagesByIDAndDate(self, Id, date):
        if(self.getAllMessages[1]==Id and self.getAllMessages[2]==date):
            return self.getAllMessages()
        return 
    def getMessageByID(self, Id):
        if(self.getAllMessages[1]==Id):
            return self.getAllMessages()
        return
    def getMessageByDate(self, date):
        if(self.getAllMessages[2]==date):
            return self.getAllMessages()
        return
    def insert(self):
        return


class MessagesDAO:

    def getAllMessages(self):
        result = []
        message = [123, 'This is a message', 'February 20, 2019']
        result.append(message)
        return message 

    def getMessageById(self, uid):
        result = self.getAllMessages()
        for r in result:
            if(r[0]==123):
                return r
        return 

    def getMessagesByIDAndDate(self, Id, date):
        result = self.getAllMessages()
        for r in result: 
            if(r[1]==Id and r[2]==date):
                return r
        return 

    def getMessageByID(self, Id):
        result = self.getAllMessages()
        for r in result: 
            if(r[1]==Id):
                return r
        return
        
    def getMessageByDate(self, date):
       result = self.getAllMessages()
        for r in result: 
            if(r[2]==date):
                return r
        return

    def insert(self):
        return


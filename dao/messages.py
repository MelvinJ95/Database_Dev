#Predefine values for messages 
result = []
messages = [123, 'This is a message', 'February 20, 2019']
messages2 = [124, 'This is a message', 'February 20, 2019']

#append messages 
result.append(messages)
result.append(messages2) 
class MessagesDAO:

    def getAllMessages(self):
        global result 
        return result 

    def getMessageById(self, uid):
        global result
        result = self.getAllMessages()
        for message in result:
                if message[0] == uid:
                    return message
        return 

    def getMessagesByIDAndDate(self, Id, date):
        global result
        result = self.getAllMessages()
        for r in result: 
            if(r[0]==Id and r[2]==date):
                return r
        return 

    def getMessageByID(self, Id):
        global result
        result = self.getAllMessages()
        for r in result: 
            if(r[0]==Id):
                return r
        return
        
    def getMessageByDate(self, date):
       global result
       result = self.getAllMessages()
       for r in result:
           if(r[2]==date):
               return r
       return

    def insert(self, text, date):
        global result
        result = self.getAllMessages()
        randId = 145677
        temp = [randId, u_username,ufirstname,ulastname,uphone,uemail,ubirthday,usex]
        result.append(temp)
        return randId  
        

    def delete(self, id):
        global result
        temp = self.getMessageByID(id)
        result.remove(temp) 
    
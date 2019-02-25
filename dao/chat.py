class ChatDAO:
    
    def getChats(self):
        result = []
        chat1 = [1, 'Hola', 'Luis']
        chat2 = [2, 'Adios', 'Carlos']
        result.append(chat1)
        result.append(chat2)
        return result
    
    def insertChat(self):
        result = self.getChats()
        chat = [3, 'HolaNuevamente', 'Melvin']
        result.append(chat)
    
    def insertMember(self):
        result = self.getMembers()
        member = ['Melvin']
        result.append(member)
    
    def getChatByID(self, cid):
        result = self.getChats()
        for chat in result:
            if chat[0] == cid:
                return chat
        return []
    def delete(self):
        result = self.getChats()
        for chat in result:
            if chat[0] == cid:
                chat = []
                return cid
        return []
    
    def getMembers(self):
        result = []
        member1 = ['Luis']
        member2 = ['Carlos']
        result.append(member1)
        result.append(member2)
        return result
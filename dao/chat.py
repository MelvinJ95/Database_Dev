from dao.users import UsersDAO
from psycopg2.sql import NULL
#Pre-define list of users 
result = []
chat = [1, 'MyChat', 123, [123, 124]]
chat2 = [12, 'NotMyChat', 124, [124, 123]]
#append users 
result.append(chat)
result.append(chat2)
class ChatDAO:
    
    def getChats(self):
        global result
        return result
    
    def insertChat(self):
        global result
        result = self.getChats()
        chat = [3, 'DefNotMyChat', 124, [124]]
        result.append(chat)
    
    def insertMember(self, cid, uid):
        chat = self.getChatByID(cid)
        users = UsersDAO.getAllUsers()
        for user in users: 
            if user[0] == uid:
                chat[3].append(uid)
                return uid
        return cid
    
    def getChatByID(self, cid):
        global result
        result = self.getChats()
        for chat in result:
            if chat[0] == cid:
                return chat
        return []
    
    def delete(self, cid):
        global result
        result = self.getChats()
        for chat in result:
            if chat[0] == cid:
                chat = NULL
                return cid
        return cid
    
    def getMembers(self, cid):
        chat = self.getChatByID(cid)
        return chat[3]
    
    def removeMember(self, cid, uid):
        chat = self.getChatByID(cid)
        for users in chat[3]:
            if users == uid:
                users = NULL
                return uid
        return cid
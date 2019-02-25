from flask import jsonify
from dao.chat import ChatDAO

class ChatHandler:
    
    def buildChatHandler(self, row):
        chats = {}
        chats['Chat id'] = row[0]
        chats['Chat Name'] = row[1]
        chats['Chat Admin'] = row[2]
        return chats
    
    def buildChatName(self, row):
        chats = {}
        chats['chatName'] = row[0]
        return chats

    def buildChatAdmin(self, row):
        chats = {}
        chats['userid'] = row[0]
        chats['name'] = row[1] + " " + row[2]
        chats['phone'] = row[3]
        chats['email'] = row[4]
        chats['username'] = row[5]
        return chats

    def buildChatContent(self, row):
        content = {}
        content['Name'] = row[0] + " " + row[1]
        content['Content'] = row[2]
        content['Sent:'] = row[3]
        return content
    
    def buildChatAlpha(self, row):
        chat = {}
        chat['Chat id'] = row[0]
        chat['Chat Name'] = row[1]
        chat['Chat Admin'] = row[2] + " " + row[3]
        return chat

    def buildChatMembers(self, row):
        members = {}
        members['Name'] = row[0] + " " + row[1]
        return members
    
    def getAllGroupChats(self):
        result = ChatDAO().getGroups()
        chats = []
        if result:
            for i in result:
                chats.append(self.buildChatAlpha(i))
            return jsonify(Chats=chats)
        else:
            return jsonify(ERROR='No groups found')
    
#     def getChatsByName(self,name):
#         return 
#     
#     def getChatsById(self,gid):
#         return 
#     
#     def getChatsByUsername(self,name):
#         return 
#     
#     def getChatByUserID(self, form):
#         return 
    
    def insertNewChat(self, form, usrID):
        name = form['chatname']
        if name and usrid:
            dao = ChatDAO()
            chat = dao.insertChat(name, usrID)
            if chat:
                result = self.arrangeChatID(group)
                return jsonify(ChatID=result)
            else:    
                return jsonify(ERROR='Creation of chat denied')
    
    def insertMember(self, form):
        credentialForm = form['credential']
        chatName = form['chatName']
        if groupname and credentialForm:
            result = ChatDAO().insertMember(groupname, item)
            if result:
                return jsonify(Member=self.arrangeGroupID(result))
            else:
                jsonify(ERROR='User is member')
    
    def removeMember(self, form, usrID):
        result = ChatDAO()
        if not result.getChatByID(usrID):
            return jsonify(Error = "Chat not found."), 404
        else:
            result.delete(usrID)
            return jsonify(DeleteStatus = "OK"), 200
    
    def removeChat(self, form, cID, ownerID):
        result = ChatDAO()
        if not result.getChatByID(cID):
            return jsonify(Error = "Chat not found."), 404
        else:
            if ownerID == result.getChatAdmin:
                result.delete(cID)
                return jsonify(DeleteStatus = "OK"), 200
            else: 
                return jsonify(Error = "Not chat admin")
    
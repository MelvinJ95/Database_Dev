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
        chat['Chat Admin'] = row[2]
        #chat['Chat Admin'] = row[2] + " " + row[3]
        return chat

    def buildChatMembers(self, row):
        members = {}
        members['Name'] = row[0] + " " + row[1]
        return members
    
    def buildChatID(self, row):
        chats = {}
        chats['usrid'] = row[0]
        chats['chatid'] = row[1]
        return chats

    def build_chat_attributes(self, cid, cname, uid):
        result = {}
        result['cid'] = cid
        result['cname'] = cname
        result['uid'] = uid
        return result
    
    def getAllChats(self):
        result = ChatDAO().getAllChats()
        chats = []
        if result:
            for i in result:
                chats.append(self.buildChatAlpha(i))
            return jsonify(Chats=chats)
        else:
            return jsonify(ERROR='No chats found')
    
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
    
    # def insertChat(self, form, usrID):
    #     name = form['chatname']
    #     if name and usrID:
    #         dao = ChatDAO()
    #         chat = dao.insertChat(name, usrID)
    #         if chat:
    #             result = self.arrangeChatID(chat)
    #             return jsonify(ChatID=result)
    #         else:
    #             return jsonify(ERROR='Creation of chat denied')

    def insertChat(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            cname = form['cname']
            uid = form['uid']
            if cname and uid:
                dao = ChatDAO()
                cid = dao.insert(cname, uid)
                result = self.build_post_attributes(cid,cname, uid)
                return jsonify(Chat=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertChatJson(self, json):
        cname = json['cname']
        uid = json['uid']
        if cname and uid:
            dao = ChatDAO()
            cid = dao.insert(cname, uid)
            result = self.build_chat_attributes(cid, cname, uid)

            return jsonify(Chat=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMember(self, form, cid, usrID):
        if chatName and credentialForm:
            result = ChatDAO().insertMember(cid, usrID)
            if result:
                return jsonify(Member=self.buildChatID(result))
            else:
                jsonify(ERROR='User is member')
    
    def removeMember(self, form, usrID, cid):
        result = ChatDAO()
        if not result.getChatByID(cid):
            return jsonify(Error = "Chat not found."), 404
        else:
            result.removeMember(cid, usrID)
            return jsonify(DeleteStatus = "OK"), 200
    
    def removeChat(self, form, cID, ownerID):
        result = ChatDAO()
        if not result.getChatByID(cID):
            return jsonify(Error = "Chat not found."), 404
        else:
            if ownerID == result.getChatAdmin(cID):
                result.delete(cID)
                return jsonify(DeleteStatus = "OK"), 200
            else: 
                return jsonify(Error = "Not chat admin")
    
from flask import jsonify

class GroupChatHandler:
    
    def getAllGroupChats(self):
        return
    
    def getGroupChatsByName(self,name):
        return 
    
    def getGroupChatsById(self,gid):
        return 
    
    def getGroupChatNameById(self,gid):
        return
    
    def getGroupChatInfoByName(self,name):
        return
    
    def getGroupChatsByUsername(self,name):
        return 
    
    def getGroupChatByUserID(self, form):
        return 
    
    def insertNewChatGroup(self, form, usrID):
        name = form['groupname']
        if name and usrid:
            dao = GroupChatDAO()
            group = dao.insertGroup(name, usrID)
            if group:
                result = self.arrangeGroupID(group)
                return jsonify(GroupID=result)
            else:    
                return jsonify(ERROR='Creation of groupchat denied')
    
    def insertParticipant(self, form):
        return
    
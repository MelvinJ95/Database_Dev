from flask import jsonify
from dao.users import UsersDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['first_name'] = row[2]
        result['last_name'] = row[3]
        result['upassword'] = row[4]
        result['uphone'] = row[5]
        result['uemail'] = row[6]
        #result['ucontacts'] = row[9]
        return result

    def build_user_attributes(self, uid, username, first_name,last_name, upassword, 
                              uphone,uemail):
        result = {}
        result['uid'] = uid
        result['username'] = username
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['upassword'] = upassword
        result['uphone'] = uphone
        result['uemail'] = uemail
        #result['ucontacts'] = contact
        return result

    def build_members(self,row):
        result = {}
        result['uid'] = row[0]
        result['name'] = row[2] + " " + row[3]
        return result

    def build_user_reaction(self, row):
        result = {}
        result['uid'] = row[0]
        result['name'] = row[1] + " " + row[2]
        result['date of reaction'] = row[3]
        return result

    def build_user_chats(self, row): 
        result = {}
        result['cname'] = row[0]
        return result 
        

    #inclomplete
    def authorize(self, json):
        dao = UsersDAO()
        username = json['username']
        password = json['password']
        result = dao.authorize(username, password)
        if result == None:
            return jsonify(Error="Invalid Login"), 404
        else:
            return jsonify(Login=1)

#         if username and password:
#             needs use of dao
#                 if auth:
#                     arrange authorization and return jsonified request
#                 else:
#                     return jsonify(ERROR='Wrong Password or Username/Email')
#         else:
#             return jsonify(ERROR='Malformed request form(last return)')

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_members(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def searchUser(self, args):
        firstname = args.get("firstname")
        lastname = args.get("lastname")
        dao = UsersDAO()
        users_list = []
        if (len(args) == 2) and firstname and lastname:
            users_list = dao.getUsersByFirstNameAndLastName(firstname, lastname)
        elif (len(args) == 1) and firstname:
            users_list = dao.getUsersByFirstName(firstname)
        elif (len(args) == 1) and lastname:
            users_list = dao.getUsersByLastName(lastname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def insertUser(self, form):
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error = "Malformed post request"), 400
        else:
            username = form['username']
            first_name = form['first_name']
            last_name = form['last_name']
            upassword = form['upassword']
            uphone = form['uphone']
            uemail = form['uemail']
            #ucontacts = form['ucontacts']
            if username and first_name and last_name and upassword and uphone and uemail:
                dao = UsersDAO()
                uid = dao.insert(username,first_name,last_name,uphone,uemail)
                result = self.build_user_attributes(uid,username,first_name,last_name,uphone,uemail)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertUserJson(self, json):
        username = json['username']
        first_name = json['first_name']
        last_name = json['last_name']
        upassword = json['upassword']
        uphone = json['uphone']
        uemail = json['uemail']
#        ucontacts = json['ucontacts']
        if username and first_name and last_name and upassword and uphone and uemail:
            dao = UsersDAO()
            uid = dao.insert(username,first_name,last_name,upassword,uphone,uemail)
            result = self.build_user_attributes(uid,username,first_name,last_name,upassword,uphone,uemail)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateUser(self, uid, form):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                username = form['username']
                first_name = form['first_name']
                last_name = form['last_name']
                upassword = form['upassword']
                uphone = form['uphone']
                uemail = form['uemail']
                #ucontacts = form['ucontacts']
                if username and first_name and last_name and upassword and uphone and uemail:
                    dao.update(uid,username,first_name,last_name,uphone,uemail)
                    result = self.build_user_attributes(uid,username,first_name,last_name,uphone,uemail)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_user_counts(self, user_counts):
        result = []
        #print(User_counts)
        for U in user_counts:
            D = {}
            D['id'] = U[0]
            D['username'] = U[1]
            D['count'] = U[2]
            result.append(D)
        return result

    def getCountByUserId(self):
        dao = UsersDAO()
        result = dao.getCountByUserId()
        #print(self.build_User_counts(result))
        return jsonify(UserCounts = self.build_user_counts(result)), 200

    def getUserLikeMessage(self, pid):
        dao = UsersDAO()
        user_list = dao.getUserLikedMessage(pid)
        result_list = []
        if not user_list:
            return jsonify(Error="Post has no likes"), 404
        for row in user_list:
            result = self.build_user_reaction(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserDislikeMessage(self, pid):
        dao = UsersDAO()
        user_list = dao.getUserDislikedMessage(pid)
        result_list = []
        if not user_list:
            return jsonify(Error="Post has no dislikes"), 404
        for row in user_list:
            result = self.build_user_reaction(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def chatOwner(self, cid):
        dao = UsersDAO()
        user_list = dao.chatOwner(cid)
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getChatMembers(self, cid):
        dao = UsersDAO()
        user_list = dao.getUsersByChat(cid)
        if not user_list:
            return jsonify(Error = "Chat is Empty"), 404
        result_list = []
        for row in user_list:
            result = self.build_members(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getInfoByUsername(self, username):
        dao = UsersDAO()
        row = dao.getUserByUsername(username)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getInfoById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def chatOwner(self, cid):
        dao = UsersDAO()
        user_list = dao.chatOwner(cid)
        result_list = []
        for row in user_list:
            result = self.build_members(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserChats(self,uid):
        dao = UsersDAO()
        user_list = dao.getUserChats(uid)
        result_list = []
        for row in user_list:
            result = self.build_user_chats(row)
            result_list.append(result)
        return jsonify(Chats=result_list)
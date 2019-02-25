
#Pre-define list of users 
result = []
users = [123, 'Jason123', 'Jason','Freeman', 'password', '123456789', 'J@gmail.com', '12 June 1968', 'M']
users2 = [124, 'Jason123', 'Jason','Freeman', 'password', '123456789', 'J@gmail.com', '12 June 1968', 'M']
#append users 
result.append(users)
result.append(users2)
class UsersDAO:
  

    def getAllUsers(self):
        global result
        return result

    def getUserById(self, uid):
        global result
        result = self.getAllUsers()
        for user in result:
           # for attr in user:
            if user[0] == uid:
                return user
        return []

    def getUsersByFirstNameAndLastName(self, firstname, lastname):
        global result
        result = self.getAllUsers()
        for user in result:
            if user[2] == firstname and user[3] == lastname:
                return user 
        return 

    def getUserByFirstName(self, firstname):
        global result
        result = self.getAllUsers()
        for user in result:
            if user[2] == firstname:
                return user
        return 

    def getUserByLastName(self, lastname):
        global result
        result = self.getAllUsers()
        for user in result:
            if user[3] == lastname:
                return user
        return

    def insert(self, u_username,ufirstname,ulastname,uphone,uemail,ubirthday,usex):
        global result 
        result = self.getAllUsers()
        randId = 12344
        temp = [randId,u_username,ufirstname,ulastname,uphone,uemail,ubirthday,usex]
        result.append(temp)
        return randId  
        

    def delete(self, uid):
        global result 
        temp = self.getUserById(uid)
        result.remove(temp)
        
    


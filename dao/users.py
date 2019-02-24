class UsersDAO:

    def getAllUsers(self):
        user = [123, 'Jason123', 'Jason','Freeman', 'password', '123456789', 'J@gmail.com', '12 June 1968', 'M']
        return user 
    def getUserById(self, uid):
        if(self.getAllUsers[0]==123):
            return self.getAllUsers()
        return 
    def getUsersByFirstNameAndLastName(self, firstname, lastname):
        if(self.getAllUsers[2]==firstname and self.getAllUsers[3]==lastname):
            return self.getAllUsers()
        return 
    def getUserByFirstName(self, firstname):
        if(self.getAllUsers[2]==firstname):
            return self.getAllUsers()
        return
    def getUserByLastName(self, lastname):
        if(self.getAllUsers[3]==lastname):
            return self.getAllUsers()
        return
    def insert(self):
        return


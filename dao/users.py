class UsersDAO:

    def getAllUsers(self):
        result = []
        user = [123, 'Jason123', 'Jason','Freeman', 'password', '123456789', 'J@gmail.com', '12 June 1968', 'M']
        result.append(user)
        return result

    def getUserById(self, uid):
        result = self.getAllUsers()
        for user in result:
            if user[0] == uid:
                return user
        return []

    def getUsersByFirstNameAndLastName(self, firstname, lastname):
        result = self.getAllUsers()
        for user in result:
            if user[2] == firstname and user[3] == lastname:
                result.append(user)
        return result

    def getUserByFirstName(self, firstname):
        result = self.getAllUsers()
        for user in result:
            if user[2] == firstname:
                result.append(user)
        return result

    def getUserByLastName(self, lastname):
        result = self.getAllUsers()
        for user in result:
            if user[3] == lastname:
                result.append(user)
        return result

    def insert(self):
        return


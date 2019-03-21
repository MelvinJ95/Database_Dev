#import libraries 
import random

#Pre-define list of users 
result = []
users = [123, 'Jason123', 'Jason','Freeman', 'password', '123456789', 'J@gmail.com', '12 June 1968', 'M', []]
users2 = [124, 'CL23', 'Carlos','Lopez', 'password', '123456789', 'CL23@gmail.com', '13 June 1968', 'M', []]
users3 = [125, 'JD', 'Joey','Diaz', 'password', '123456789', 'JD@gmail.com', '14 June 1968', 'M', []]
users4 = [126, 'SOldado2', 'Frank','Ramirez', 'password', '123456789', 'SOldado2@gmail.com', '15 June 1968', 'M', []]
users5 = [127, 'zapper', 'Eric','Melendez', 'password', '123456789', 'zappe@gmail.com', '16 June 1968', 'M', []]
users6 = [128, 'Tfue', 'Taylor','Jackson', 'password', '123456789', 'Tfue@gmail.com', '17 June 1968', 'M', []]
users7 = [129, 'Ninja', 'Scott','Anderson', 'password', '123456789', 'Ninja@gmail.com', '18 June 1968', 'M', []]
users8 = [130, 'JoeDMTRogan', 'Joe','Rogan', 'password', '123456789', 'Joe.Rogan@gmail.com', '19 June 1968', 'M', []]
users[9].append([123,'Luis', 'Rivera', '787-939-0540', 'Luis.Rivera@upr.edu']) #add contact to user 123
users2[9].append([124,'Melvin', 'Malave', '939-282-1866', 'Melvin.Malave@upr.edu']) #add contact to user 124 
#append users 

result.append(users)
result.append(users2)
result.append(users3)
result.append(users4)
result.append(users5)
result.append(users6)
result.append(users7)
result.append(users8)
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
                return 

        return 

    def getUserByLastName(self, lastname):
        global result
        result = self.getAllUsers()
        for user in result:
            if user[3] == lastname:
                return user
        return

    def insert(self, u_username,ufirstname,ulastname,upwd,uphone,uemail,ubirthday,usex):
        global result 
        randId = random.randint(1,200) 
        result = self.getAllUsers()
        for user in result:
            while(randId == user[0]):
                randId = randint(1,200)
        temp = [randId,u_username,ufirstname,ulastname,upwd,uphone,uemail,ubirthday,usex]
        result.append(temp)
        return randId  
        

    def delete(self, uid):
        global result 
        temp = self.getUserById(uid)
        result.remove(temp)
        
    


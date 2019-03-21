
#import user handler 
import random
from dao.users import UsersDAO

#declare global variables and default list values
result = []
contact1 = [ 123,'Luis', 'Rivera', 7879390540, 'Luis.Rivera@upr.edu']
contact2 = [ 124, 'Melvin', 'Malave', 9392821866, 'Melvin.Malave@upr.edu']
result.append(contact1)
result.append(contact2)
class ContactDAO:
    def getContactList(self):
        global result 
        return result
    
    def getContactListByUser(self, usrID):
        result = []
        clist = []
        result = UsersDAO().getUserById(usrID)
        clist = result[9]
        return clist 
    
#     def getUserContacts(self):
#         return[]
    
    def addContactByPhoneAndEmail(self,usrID,first_name,last_name,phone,email):
        global result 
        user = UsersDAO().getUserById(usrID)
        randId = random.randint(1, 200)
        contact = [randId,first_name,last_name,phone,email]
        user[9].append(contact)
        result.append(contact)
        return contact

    def addContactByPhone(self,usrID,first_name,last_name,phone):
        global result 
        user = UsersDAO().getUserById(usrID)
        randId = random.randint(1, 200)
        contact = [randId,first_name,last_name,phone,""]
        user[9].append(contact)
        result.append(contact)
        return contact

    def addContactByEmail(self,usrID,first_name,last_name,email):
        global result 
        user = UsersDAO().getUserById(usrID)
        randId = random.randint(1, 200)
        contact = [randId,first_name,last_name,"",email]
        user[9].append(contact)
        result.append(contact)
        return contact
    
    
    def delete(self, owner, usrID):
        #delete from local list 
        global result 
        contact = self.getContactByID(owner, usrID)
       # result.remove(temp) #should result be deleted 
        user = UsersDAO().getUserById(owner)
        user[9].remove(contact)
        return contact


    def getContactByID(self, owner, usrID):  
        user = UsersDAO().getUserById(owner)
        if not user:
            return 
        for contact in user[9]:
            if contact[0] == usrID:
                return contact
        return 

    def getAllContacts(self):
        result = []
        users = UsersDAO().getAllUsers()
        for user in users:
            result.append(user[9])
        return result
    
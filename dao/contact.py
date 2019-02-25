class ContactDAO:
    def getContactList(self):
        result = []
        contact1 = [1, 'Luis']
        contact2 = [2, 'Melvin']
        result.append(contact1)
        result.append(contact2)
        return result
    
    def getContactListByUser(self, usrID):
        return[]
    
    def getUserContacts(self):
        return[]
    
    def addContact(self):
        result = self.getContactList()
        contact = [3, 'Carlos']
        result.append(contact)
        return result
    
    def getContactByID(self, usrID):
        result = self.getContactList()
        for contact in result:
            if contact[0] == usrID:
                return contact
        return[]
                
    
from dao.contact import ContactDAO
from flask import *

class ContactHandler:
    def buildContactDirectory(self, row):
        contact = {}
        contact['usrid'] = row[0]
        contact['first_name'] = row[1]
        contact['last_name'] = row[2]
        contact['phone'] = row[3]
        contact['email'] = row[4]
        return contact

    def buildContactAttributes(self, row):
        contacts = {}
        contacts['Contact ID'] = row[2]
        contacts['Name'] = row[3] + " " + row[4]
        contacts['Phone'] = row[5]
        contacts['Email'] = row[6]
        contacts['Birthday'] = row[7]
        return contacts

    def buildContactList(self, row):
        contact = {}
        contact['usrid'] = row[0]
        contact['contactDirectory_id'] = row[1]
        contact['contactDirectory'] = row[2]
        return contact

    def buildContactAlpha(self, row):
        contact = {}
        contact['contact_id'] = row[0]
        return contact

    def getContactLists(self):
        result = ContactDAO().getContactLists()
        contact = []
        for r in result:
            contact.append(self.buildContactList(r))
        if contact is not None:
            return jsonify(ContactList=contact)
        else:
            return jsonify(ERROR='No contact list found')

    def getContactListbyUser(self, usrID):
        result = ContactDAO().getContactListByUser(usrID)
        contacts = []
        for r in result:
            contacts.append(self.buildContactDirectory(r))
        if contacts:
            return jsonify(Contacts=contacts)
        else:
            return jsonify(ERROR='No contact list found')

    def getUserContacts(self, usrID): #needs to be evaluated 
        result = ContactDAO().getUserContacts(usrID)
        contacts = []
        if result:
            for r in result:
                contacts.append(self.arrangeContacts(r))
            return jsonify(Contacts=contacts)
        return jsonify(ERROR='No Contact List for the User')

    def addContactByPhone(self, form, usrID,firstname,lastname,phone):
        if usrID and firstname and lastname and phone:
            contact = ContactDAO().addContactByPhone(usrID, firstname, lastname, phone)
            if contact:
                result = self.buildContactAlpha(contact)
                return jsonify(Contact=result)
            else:
                return jsonify(ERROR='Error adding contact')
    
    def addContactByEmail(self, form, usrID,firstname,lastname,email):
        if usrID and firstname and lastname and email:
            contact = ContactDAO().addContactByEmail(usrID, firstname, lastname, email)
            if contact:
                result = self.buildContactAlpha(contact)
                return jsonify(Contact=result)
            else:
                return jsonify(ERROR='Error adding contact')

    def addContactByPhoneAndEmail(self, form, usrID,firstname,lastname,phone,email):
        if usrID and firstname and lastname and phone and email:
            contact = ContactDAO().addContactByPhoneAndEmail(usrID, firstname, lastname, phone, email)
            if contact:
                result = self.buildContactAlpha(contact)
                return jsonify(Contact=result)
            else:
                return jsonify(ERROR='Error adding contact')
            
    def removeContact(self, form, cID, fromUsrID):
        result = ContactDAO()
        if not result.getContactByID(cID, fromUsrID):
            return jsonify(Error = "Contact not found."), 404
        else:
            result.delete(cID, fromUsrID)
            return jsonify(DeleteStatus = "OK"), 200
        
    def getAllContacts(self):
        result = ContactDAO()
        return jsonify(result.getAllContacts())
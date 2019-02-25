from dao.contact import ContactDAO
from flask import *

class ContactHandler:
    def buildContactDirectory(self, row):
        contact = {}
        contact['name'] = row[2]
        contact['phone'] = row[3]
        contact['email'] = row[4]
        contact['birthday'] = row[5]
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
        contact['owner_id'] = row[0]
        contact['contact_id'] = row[1]
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
        result = ContactDAO().getContactListbyUser(usrID)
        contacts = []
        for r in result:
            contacts.append(self.buildContactDirectory(r))
        if contacts:
            return jsonify(Contacts=contacts)
        else:
            return jsonify(ERROR='No contact list found')

    def getUserContacts(self, usrID):
        result = ContactDAO().getUserContacts(usrID)
        contacts = []
        if result:
            for r in result:
                contacts.append(self.arrangeContacts(r))
            return jsonify(Contacts=contacts)
        return jsonify(ERROR='No Contact List for the User')

    def addContact(self, form, usrID):
        phone_email = form['item']
        if phone_email and usrID:
            contact = ContactDAO().addContact(usrID, phone_email)
            if contact:
                result = self.buildContactAlpha(contact)
                return jsonify(Contact=result)
            else:
                return jsonify(ERROR='Error adding contact')
            
    def removeContact(self, form, usrID):
        result = ContactDAO()
        if not result.getContactByID(usrID):
            return jsonify(Error = "Contact not found."), 404
        else:
            result.delete(usrID)
            return jsonify(DeleteStatus = "OK"), 200
        
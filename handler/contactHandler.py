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

    def buildContactByPhone(self, row):
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
        contact['contact_id'] = row
        return contact

    def buildContactsByUser(self, row):
        result = {}
        result['uid'] = row[0]
        result['name'] = row[2] + " " + row[3]
        return result

    def getContactLists(self):
        result = ContactDAO().getContactLists()
        if not result:
            return jsonify(ERROR='No contact list found')
        contact = []
        for r in result:
            contact.append(self.buildContactList(r))
        return jsonify(ContactList=contact)

    def getContactListbyUser(self, usrID):
        result = ContactDAO().getContactListByUser(usrID)
        if not result:
            return jsonify(ERROR='No contact list found')
        contacts = []
        for r in result:
            contacts.append(self.buildContactsByUser(r))
        return jsonify(Contacts=contacts)
     

    def getUserContacts(self, usrID): #needs to be evaluated 
        result = ContactDAO().getUserContacts(usrID)
        contacts = []
        if result:
            for r in result:
                contacts.append(self.arrangeContacts(r))
            return jsonify(Contacts=contacts)
        return jsonify(ERROR='No Contact List for the User')

    def addContactJSON(self, json, usrID):
        if len(json) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            firstname = json['first_name']
            lastname = json['last_name']
            email = json['uemail']
            phone = json['uphone']
            if firstname and lastname and phone or email:
                contact = ContactDAO().addContact(usrID, firstname, lastname, phone, email)
                if contact:
                    result = self.buildContactAlpha(contact)
                    return jsonify(Contact=result)
                else:
                    return jsonify(ERROR='Error adding contact')

    def addContactByEmail(self, form, usrID):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            firstname = (form.to_dict().values()[0])
            lastname = form.to_dict().values()[1]
            email = form.to_dict().values()[2]
            if firstname and lastname and email:
                contact = ContactDAO().addContactByEmail(usrID, firstname, lastname, email)
                if contact:
                    result = self.buildContactAlpha(contact)
                    return jsonify(Contact=result)
                else:
                    return jsonify(ERROR='Error adding contact')

    def addContactByPhone(self, form, usrID):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            firstname = form.to_dict().values()[0]
            lastname = form.to_dict().values()[1]
            phone = form.to_dict().values()[2]
            if firstname and lastname and phone:
                contact = ContactDAO().addContactByPhone(usrID, firstname, lastname, phone)
                if contact:
                    result = self.buildContactAlpha(contact)
                    return jsonify(Contact=result)
                else:
                    return jsonify(ERROR='Error adding contact')
    
    def addContactByEmail(self, form, usrID):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            firstname = (form.to_dict().values()[0])
            lastname = form.to_dict().values()[1]
            email = form.to_dict().values()[2]
            if firstname and lastname and email:
                contact = ContactDAO().addContactByEmail(usrID, firstname, lastname, email)
                if contact:
                    result = self.buildContactAlpha(contact)
                    return jsonify(Contact=result)
                else:
                    return jsonify(ERROR='Error adding contact')

    def removeContact(self, owner, contact):
        result = ContactDAO()
        if not result.getContactByID(owner, contact):
            return jsonify(Error = "Contact not found."), 404
        else:
            result.delete(owner, contact)
            return jsonify(DeleteStatus = "OK"), 200
        
    def getAllContacts(self):
        result = ContactDAO()
        return jsonify(result.getAllContacts())
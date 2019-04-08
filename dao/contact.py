from config.db_config import pg_config
import psycopg2

class ContactDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    '''
    def getAllContacts(self):
        cursor = self.conn.cursor()
        query = "select * from contacts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    '''
    def getContactListByUser(self, usrID):
        cursor = self.conn.cursor()
       # query = "select * from(select * from users natural inner join contacts where uid = %s) as T1 natural inner join users as T2 where T1.cid=T2.uid);"
       #  query = "select * from users natural inner join contacts where uid = contact and user_id = %s;"
        query = "select * from users natural inner join contacts where uid = contact and owner = %s;"
        cursor.execute(query,(usrID,))
        result = []
        for row in cursor:
            result.append(row)
        return result
 
 
    def addContactByPhone(self,usrID,first_name,last_name,phone):
        cursor = self.conn.cursor()
        query = "select * from users where first_name = %s and last_name = %s and uphone = %s;"
        cursor.execute(query, (last_name,phone,first_name,)) #NOT TESTED SHOULD WORK SAME AS addContactByEmail
        cid = cursor.fetchone()[0]
        query_T = "insert into contacts(cid,uid) values (%s, %s) returning cid;"
        cursor.execute(query_T, (cid,usrID,))
        self.conn.commit()
        return cid

    def addContactByEmail(self,usrID,first_name,last_name,email):
        print("%s,%s,%s", first_name,last_name,email)
        cursor = self.conn.cursor()
        query = "select * from users where first_name = %s and last_name = %s and uemail = %s;"
        cursor.execute(query, (last_name,email,first_name,)) #WORKS AND TESTED BUT ORDER NEEDS TO BE FIXED? 
        cid = cursor.fetchone()[0]
        query_T = "insert into contacts(cid,uid) values (%s, %s) returning cid;"
        cursor.execute(query_T, (cid,usrID,))
        self.conn.commit()
        return cid

    def delete(self, owner, contact):
        cursor = self.conn.cursor()
        query = "delete from contacts where owner = %s and contact = %s;"
        cursor.execute(query, (owner, contact,))
        self.conn.commit()
        return owner

    def getContactByID(self, owner, contact):
        cursor = self.conn.cursor()
        query = "select * from contacts where owner = %s and contact = %s;"
        cursor.execute(query, (owner, contact,))
        result = cursor.fetchone()
        return result

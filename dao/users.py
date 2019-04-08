from config.db_config import pg_config
import psycopg2


class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByFirstNameAndLastName(self, firstname, lastname):
        cursor = self.conn.cursor()
        query = "select * from users where first_name = %s and last_name = %s;"
        cursor.execute(query, (firstname,lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByFirstName(self, firstname):
        cursor = self.conn.cursor()
        query = "select * from users where first_name = %s;"
        cursor.execute(query, (firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByLastName(self, lastname):
        cursor = self.conn.cursor()
        query = "select * from users where last_name = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, username,first_name,last_name,upassword,uphone,uemail,ubirthday,usex):
       cursor = self.conn.cursor()
       query = "insert into users(username,first_name,last_name,upassword,uphone,uemail,ubirthday,usex) values (%s, %s, %s, %s, %s,  %s, %s, %s) returning uid;"
       cursor.execute(query, (username,first_name,last_name,upassword,uphone,uemail,ubirthday,usex,))
       uid = cursor.fetchone()[0]
       self.conn.commit()
       return uid

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid
        
    def getUserLikedMessage(self):
        cursor = self.conn.cursor()
        query = "Select * from users natural inner join reactions where reaction='like';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserDislikedMessage(self):
        cursor = self.conn.cursor()
        query = "Select * from users natural inner join reactions where reaction='dislike';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def chatOwner(self, cid):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join chats where cid = %s and user_id = uid;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
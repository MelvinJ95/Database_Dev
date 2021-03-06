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


    def insert(self, username,first_name,last_name,upassword,uphone,uemail):
       cursor = self.conn.cursor()
       query = "insert into users(username,first_name,last_name,upassword,uphone,uemail) values (%s, %s, %s, %s, %s, %s) returning uid;"
       cursor.execute(query, (username,first_name,last_name,upassword,uphone,uemail))
       uid = cursor.fetchone()[0]
       self.conn.commit()
       return uid

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid

    def getUsersByChat(self, cid):
        cursor = self.conn.cursor()
        query = "select * from users, members where users.uid = members.user_id and cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where username = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserLikedMessage(self, pid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, rdate from users as U natural inner join reactions as R where R.reaction='like' and R.pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserDislikedMessage(self, pid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, rdate from users as U natural inner join reactions as R where R.reaction='dislike' and R.pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def chatOwner(self, cid):
        cursor = self.conn.cursor()
        query = "select * from users as U natural inner join chats as C where C.cid = %s and C.uid = U.uid;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def chatOwnerId(self, cid):
        cursor = self.conn.cursor()
        query = "select uid from users as U natural inner join chats as C where C.cid = %s and C.uid = U.uid;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getUserChats(self,uid):
        cursor = self.conn.cursor()
        query = "select cid, cname from users natural inner join chats where uid = uid and uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def authorize(self,username,password):
        cursor = self.conn.cursor()
        query = "select username, upassword from users where username = %s and upassword = %s;"
        cursor.execute(query, (username, password, ))
        result = cursor.fetchone()
        return result

    def getAllUserChats(self, uid):
        cursor = self.conn.cursor()
        query = "select cid, cname from chats natural inner join members where user_id = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

import random
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

    # def getUsersByFirstNameAndLastName(self, firstname, lastname):
    #     global result
    #     result = self.getAllUsers()
    #     for user in result:
    #         if user[2] == firstname and user[3] == lastname:
    #             return user
    #     return
    #
    # def getUserByFirstName(self, firstname):
    #     global result
    #     result = self.getAllUsers()
    #     for user in result:
    #         if user[2] == firstname:
    #             return
    #
    #     return
    #
    # def getUserByLastName(self, lastname):
    #     global result
    #     result = self.getAllUsers()
    #     for user in result:
    #         if user[3] == lastname:
    #             return user
    #     return

    # def insert(self, u_username,ufirstname,ulastname,upwd,uphone,uemail,ubirthday,usex):
    #     global result
    #     randId = random.randint(1,200)
    #     result = self.getAllUsers()
    #     for user in result:
    #         while(randId == user[0]):
    #             randId = randint(1,200)
    #     temp = [randId,u_username,ufirstname,ulastname,upwd,uphone,uemail,ubirthday,usex]
    #     result.append(temp)
    #     return randId

    def insert(self, username,first_name,last_name,upassword,uphone,uemail,ubirthday,usex):
        cursor = self.conn.cursor()
        query = "insert into users(username,first_name,last_name,upassword,uphone,uemail,ubirthday,usex) " \
                "values (%s, %s, %s, %s, %s,  %s, %s, %s) returning uid;"
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
        
    


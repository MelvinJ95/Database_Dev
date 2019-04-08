from config.db_config import pg_config
import psycopg2
#Pre-define list of users 
# result = []
# chat = [1, 'MyChat', 123, [123, 124]]
# chat2 = [12, 'NotMyChat', 124, [124, 123]]
# #append users
# result.append(chat)
# result.append(chat2)


class ChatDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllChats(self):
        cursor = self.conn.cursor()
        query = "select * from chats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatByID(self, cid):
        cursor = self.conn.cursor()
        query = "select * from chats where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def insert(self, cname, uid):
        cursor = self.conn.cursor()
        query = "insert into chats(cname, uid) values (%s, %s) returning cid;"
        cursor.execute(query, (cname, uid))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid
    
    def insertMember(self, cid, uid):
        cursor = self.conn.cursor()
        query = "insert into member(cid,uid) values (%s, %s) returning cid;"
        cursor.execute(query, (cid, uid))
        result = [uid,cid]
        self.conn.commit()
        return result
    
    def delete(self, cid):
        cursor = self.conn.cursor()
        query = "delete from chats where cid = %s;"
        cursor.execute(query, (cid,))
        self.conn.commit()
        return cid
    
    def getMembers(self, cid):
        chat = self.getChatByID(cid)
        return chat[3]
    
    def removeMember(self, cid, uid):
        cursor = self.conn.cursor()
        query = "delete from member where cid = %s and uid = %s;"
        cursor.execute(query, (cid,uid,))
        self.conn.commit()
        return cid


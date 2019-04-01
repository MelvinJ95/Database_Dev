from config.db_config import pg_config
import psycopg2

class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result 

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "select * from messages where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getMessagesByIDAndDate(self, mid, date):
        cursor = self.conn.cursor()
        query = "select * from messagess where mid = %s and date = %s;"
        cursor.execute(query, (mid,date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
  
        
    def getMessageByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from messages where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def insert(self, text, date, like, dislike):
        cursor = self.conn.cursor()
        query = "insert into messages(text,date,like,dislike) values (%s, %s,%s,%s) returning mid;"
        cursor.execute(query, (text,date,like,dislike,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid  
        

    def delete(self, mid):
        cursor = self.conn.cursor()
        query = "delete from messages where mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid
         
    
    def getReactionsByMessage(self, pid, reaction):
        cursor = self.conn.cursor()
        query = "select * from messages where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        if reaction == 'like':
            like = cursor.fetchone()[3]
            result.append(pid)
            result.append(like)
        if reaction == 'dislike':
            dislike = cursor.fetchone()[4]
            result.append(pid)
            result.append(dislike)
        return result

    def update(self, mid, text, date, like, dislike ):
        cursor = self.conn.cursor()
        query = "update messages set text = %s, date = %s, like = %s, dislike = %s where pid = %s;"
        cursor.execute(query, (text,date,mid,like,dislike,))
        self.conn.commit()
        return mid
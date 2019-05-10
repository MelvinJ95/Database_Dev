from config.db_config import pg_config
import psycopg2
import re

result = []
hashtag = ['chat']
hashtag2 = ['anotherChat']

class HashtagsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtags;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagById(self, hid):
        cursor = self.conn.cursor()
        query = "select * from reactions where hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        return result

    def getTrends(self):
        cursor = self.conn.cursor()
        query = "select htext, row_number() over(order by count(htext) desc) as rownum from hashtags natural inner join tagged group by htext order by rownum;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def insert(self, htext):
    #     global result
    #     result = self.getAllHashtags()
    #     id = random()
    #     ht = [id, htext]
    #     result.append(ht)
    #     return ht

    def insert(self, htext, pid):
        cursor = self.conn.cursor()
        query = "insert into hashtags(htext) values (%s) returning hid;"
        cursor.execute(query, (htext,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        self.attachToPost(hid, pid)
        return hid

    def attachToPost(self, hid, pid):
        cursor = self.conn.cursor()
        query = "insert into tagged(hid, pid) values (%s, %s) returning hid;"
        cursor.execute(query, (hid, pid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid
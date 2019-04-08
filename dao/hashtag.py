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
        global result
        return result

    def getHashtagById(self, hid):
        global result
        result = self.getAllHashtags()
        for ht in result:
            if ht[0] == hid:
                return ht

        return []

    def getTrends(self):
        cursor = self.conn.cursor()
        query = "select htext, count(*) from hashtags group by htext order by count desc;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, htext):
        global result
        result = self.getAllHashtags()
        id = random()
        ht = [id, htext]
        result.append(ht)
        return ht

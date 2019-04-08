from config.db_config import pg_config
import psycopg2


class ReactionsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select * from reactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactionById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from reactions where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getReactionsByIdAndDate(self, rid, rdate):
        cursor = self.conn.cursor()
        query = "select * from reactions where rid = %s and rdate = %s;"
        cursor.execute(query, (rid, rdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getReactionsByDate(self, rdate):
        cursor = self.conn.cursor()
        query = "select * from reactions where rdate = %s;"
        cursor.execute(query, (rdate,))
        result = []
        for row in cursor:
            result.append(row)
        # result = cursor.fetchone()
        return result

    def getAllLikes(self):
        cursor = self.conn.cursor()
        query = "select * from reactions where reaction = 'like';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        #result = cursor.fetchone()
        return result

    def getAllDislikes(self):
        cursor = self.conn.cursor()
        query = "select * from reactions where reaction = 'dislike';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = cursor.fetchone()
        return result

    def insert(self, rdate, reaction, pid, uid):
        cursor = self.conn.cursor()
        query = "insert into reactions(rdate, reaction, pid, uid) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rdate, reaction, pid, uid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def delete(self, rid):
        cursor = self.conn.cursor()
        query = "delete from reactions where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid

    def getLikesByPostId(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, count(*) from reactions where pid = %s and reaction = 'like' group by pid;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        # print result
        return result

    def getDislikesByPostId(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, count(*) from reactions where pid = %s and reaction = 'dislike' group by pid;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        # print result
        return result

    def getUserLikedMessage(self, pid):
        cursor = self.conn.cursor()
        query = "Select * from users natural inner join reactions where reaction='like' and pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserDislikedMessage(self, pid):
        cursor = self.conn.cursor()
        query = "Select * from users natural inner join reactions where reaction='dislike' and pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
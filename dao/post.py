from config.db_config import pg_config
import psycopg2


class PostsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from posts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllPostWebsite(self): #fixed query for like
        cursor = self.conn.cursor()
        query = "select p.pid, first_name, pmedia, pcaption, sum(case when reaction ='like' then 1 else 0 end) as like, sum(case when reaction='dislike' then 1 else 0 end) as dislike from posts as p, reactions as r, users as u where p.pid = r.pid and u.uid = p.uid group by first_name, pcaption, pmedia,p.pid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    

    def getPostById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from posts where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getPostsByChatId(self, cid):
        cursor = self.conn.cursor()
        #query = "select * from posts where cid = %s;"
        query = "select p.pid, first_name, pmedia, pcaption, sum(case when reaction ='like' then 1 else 0 end) as like, sum(case when reaction='dislike' then 1 else 0 end) as dislike from posts as p, reactions as r, users as u where p.pid = r.pid and u.uid = p.uid  and p.cid = %s group by first_name, pcaption, pmedia,p.pid, p.cid;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostsByChatIdAndUser(self, cid, uid):
        cursor = self.conn.cursor()
        query = "select * from posts where cid = %s and uid = %s;"
        cursor.execute(query, (cid, uid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from posts where pdate = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        #result = cursor.fetchone()
        return result

    def getPostsByUser(self, uid):
        cursor = self.conn.cursor()
        query = "select * from posts natural inner join users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostsPerDayByUser(self, uid, pdate):
        cursor = self.conn.cursor()
        query = "select * from posts where uid = %s and pdate = %s;"
        cursor.execute(query, (uid, pdate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getActiveUsers(self):
        global result
        result = "Active users shown here."
        return result

    def getNumberOfPostsPerDay(self, date):
        cursor = self.conn.cursor()
        query = "select pdate, count(*) from posts where pdate = %s group by pdate;" #TO BE TESTED 
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactionsByPost(self, pid, reaction):
        cursor = self.conn.cursor()
        query = "select reaction count(*) from posts inner natural join reactions where pid = %s and reaction = %s group by reaction;" #TO BE TESTED
        cursor.execute(query, (pid, reaction,))
        preaction = cursor.fetchone()
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, pcaption, pdate, pmedia, uid, cid):
        cursor = self.conn.cursor()
        query = "insert into posts(pcaption, pdate, pmedia, uid, cid) values (%s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pcaption, pdate, pmedia, uid, cid,))
        pid = cursor.fetchone()[0]
        query_T = "insert into reactions(rdate,reaction,pid,uid) values (%s,%s,%s,%s);"
        cursor.execute(query_T, (pdate,None,pid, None,))
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from posts where pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, pid, pcaption, pdate, pmedia):
        cursor = self.conn.cursor()
        query = "update posts set pcaption = %s, pdate = %s, pmedia = %s where pid = %s;"
        cursor.execute(query, (pcaption, pdate, pmedia, pid,))
        self.conn.commit()
        return pid

    def getAllReplies(self, pid):
        cursor = self.conn.cursor()
        query = "select * from posts natural inner join reply where pid = rid and post_id = %s;"
        cursor.execute(query, (pid,))   
        result =[]
        for row in cursor:
            result.append(row)
        print(result)
        return result
        
    def getPostsByHashtag(self,cid,hashtag):
        hashtag = '#'+hashtag
        cursor = self.conn.cursor()
        query = "select p.pid, first_name, pmedia, pcaption, sum(case when reaction ='like' then 1 else 0 end) as like, sum(case when reaction='dislike' then 1 else 0 end) as dislike " \
        "from posts as p, reactions as r, users as u, hashtags as h natural inner join tagged as t " \
        "where p.pid = r.pid and u.uid = p.uid and p.pid = t.pid and %s = ANY(htext) and p.cid = %s group by first_name, pcaption, pmedia,p.pid;"
        cursor.execute(query, (hashtag,cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result 
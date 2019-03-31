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
        query = "select pid, pcaption, pdate, pmedia from posts;"
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

    # def getPostByDate(self, pdate):
    #     global result
    #     result = self.getAllPosts()
    #     for post in result:
    #         if post[2] == pdate:
    #             result.append(post)
    #             #return post
    #     return result

    def getPostsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from posts where pdate = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        #result = cursor.fetchone()
        return result

    def getPostByUser(self, uid):
        global result
        result = self.getAllPosts()
        #user = users.getAllUsers()
        post1 = [1, 'Hola', '2-24-2019', 'link.png', 123]
        for post in result:
            if post[4] == uid:
                result.append(post)

        return result

    def getPostsPerDayByUser(self, uid, date):
        global result
        result = []
        all = self.getAllPosts()
        for post in all:
            if post[2] == date and post[4] == uid:
                result.append(post)
        return result

    def getActiveUsers(self):
        global result
        result = "Active users shown here."
        return result

    def getNumberOfPostsPerDay(self, date):
        global result
        result = self.getPostByDate(date)
        return "There were a total of %d posts on this day." % (len(result))

    def getReactionsByPost(self, pid, reaction):
        #global result
        result = self.getPostById(pid)
        if reaction == 'like':
            return "The number of likes for post with id %d is %d." % (pid, result[5])
        if reaction == 'dislike':
            return "The number of dislikes for post with id %d is %d." % (pid, result[6])

    def insert(self, pcaption, pdate, pmedia):
        cursor = self.conn.cursor()
        query = "insert into posts(pcaption, pdate, pmedia) values (%s, %s, %s) returning pid;"
        cursor.execute(query, (pcaption, pdate, pmedia,))
        pid = cursor.fetchone()[0]
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
from dao.post import PostsDAO
from dao.hashtag import HashtagsDAO
from dao.users import UsersDAO
import psycopg2
from config.db_config import pg_config

class DashboardDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getTrends(self):
        cursor = self.conn.cursor()
        query = "select htext, row_number() over(order by count(htext) desc) as rownum from hashtags natural inner join tagged group by htext order by rownum;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfPostsPerDay(self):
        cursor = self.conn.cursor()
        query = "select pdate, count(*) from posts group by pdate;" #TO BE TESTED
        cursor.execute(query)
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

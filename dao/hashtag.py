from dao.post import PostsDAO
from random import*
import re


class HashtagsDAO:
    def getAllHashtags(self):
        result = []
        return result

    def getHashtagById(self, hid):
        result = self.getAllHashtags()
        for ht in result:
            if ht[0] == hid:
                return ht

        return []

    # def getHashtagsByDate(self, date):
    #     result = []
    #     temp = PostsDAO.getAllPosts(self)
    #     for p in temp:
    #         if date == p[2]:
    #             re.findall(r"#(\w+)", p[1])
    #             result.append(p[1])
    #     return result

    def getTrends(self):
        trends = "Here are today's trends."
        return trends

    def insert(self, htext):
        result = self.getAllHashtags()
        id = random()
        ht = [id, htext]
        result.append(ht)
        return ht

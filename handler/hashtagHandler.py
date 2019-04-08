from flask import jsonify, Flask
from dao.hashtag import HashtagsDAO

class HashtagHandler:
    def build_hashtag_dict(self, row):
        result = {};
        result['hid'] = row[0]
        result['htext'] = row[1]
        return result

    def build_hashtag_attributes(self, hid, htext):
        result = {}
        result['hid'] = hid
        result['htext'] = htext
        return result

    def build_trends(self, row):
        result = {}
        result['hashtag'] = row[0]
        result['position'] = row[1]
        return result

    def getAllHashtags(self):
        dao = HashtagsDAO()
        hashtags_list = dao.getAllHashtags()
        result_list = []
        for row in hashtags_list:
            result = self.build_hashtag_dict(row)
            result_list.append(result)
        return jsonify(Hashtags=result_list)

    def getHashtagById(self, pid):
        dao = HashtagsDAO()
        row = dao.getHashtagById(pid)
        if not row:
            return jsonify(Error="Hashtag Not Found"), 404
        else:
            hashtag = self.build_hashtag_dict(row)
            return jsonify(Hashtag=hashtag)

    # def getHashtagsByDate(self, date):
    #     dao = HashtagsDAO()
    #     row = dao.getHashtagsByDate(date)
    #     if not row:
    #         return jsonify(Error="Hashtags Not Found"), 404
    #     else:
    #         hashtag = self.build_hashtag_dict(row)
    #         return jsonify(Hashtag=hashtag)

    def getTrendingTopics(self):
        dao = HashtagsDAO()
        row = dao.getTrends()
        if not row:
            return jsonify(Error="No Trends Found"), 404
        else:
            result_list = []
            for r in row:
                result = self.build_trends(r)
                result_list.append(result)
        return jsonify(Trends=result_list)

    def insertHashtag(self, form):
        htext = form['htext']
        if htext:
            dao = HashtagsDAO()
            hid = dao.insert(htext)
            result = self.build_hashtag_attributes(hid, htext)
            return jsonify(Hashtag=result), 201
        else:
            return jsonify(Error="Unexpected attributes in hashtag request"), 400

    def insertHashtagJson(self, json):
        htext = json['htext']
        if htext:
            dao = HashtagsDAO()
            hid = dao.insert(htext)
            result = self.build_hashtag_attributes(hid, htext)

            return jsonify(Hashtag=result), 201
        else:
            return jsonify(Error="Unexpected attributes in hashtag request"), 400

    def build_hashtag_counts(self, hashtag_counts):
        result = []
        #print(hashtag_counts)
        for P in hashtag_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByHashtagId(self):
        dao = HashtagsDAO()
        result = dao.getCountByHashtagId()
        #print(self.build_hashtag_counts(result))
        return jsonify(HashtagCounts = self.build_hashtag_counts(result)), 200
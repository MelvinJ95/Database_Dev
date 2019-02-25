from flask import jsonify, Flask
from dao.post import PostsDAO

class PostHandler:
    def build_post_dict(self, row):
        result = {};
        result['pid'] = row[0]
        result['pcaption'] = row[1]
        result['pdate'] = row[2]
        result['pmedia'] = row[3]
        return result

    def build_post_attributes(self, pid, pcaption, pdate, pmedia):
        result = {}
        result['pid'] = pid
        result['pcaption'] = pcaption
        result['pdate'] = pdate
        result['pmedia'] = pmedia
        return result

    def getAllPosts(self):
        dao = PostsDAO()
        posts_list = dao.getAllPosts()
        result_list = []
        for row in posts_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Posts=result_list)

    def getPostById(self, pid):
        dao = PostsDAO()
        row = dao.getPostById(pid)
        if not row:
            return jsonify(Error="Post Not Found"), 404
        else:
            post = self.build_post_dict(row)
            return jsonify(Post=post)

    def getPostByDate(self, pdate):
        dao = PostsDAO()
        row = dao.getPostByDate(pdate)
        if not row:
            return jsonify(Error="Post Not Found"), 404
        else:
            post = self.build_post_dict(row)
            return jsonify(Post=post)

    def searchPost(self, args): #date, hashtag, user
        date = args.get("date")
        hashtag = args.get("hashtag")
        user = args.get("user")
        dao = PostsDAO()
        posts_list = []
        if(len(args) == 3) and date and hashtag and user:
            posts_list = dao.getPostsByDateAndHashtagAndUser(date, hashtag, user)
        elif (len(args) == 2) and date and hashtag:
            posts_list = dao.getPostsByDateAndHashtag(date, hashtag)
        elif (len(args) == 2) and date and user:
            posts_list = dao.getPostsByDateAndUser(date, user)
        elif (len(args) == 2) and hashtag and user:
            posts_list = dao.getPostsByHashtagAndUser(hashtag, user)
        elif (len(args) == 1) and date:
            posts_list = dao.getPostsByDate(date)
        elif (len(args) == 1) and hashtag:
            posts_list = dao.getPostsByHashtag(hashtag)
        elif (len(args) == 1) and user:
            posts_list = dao.getPostsByUser(user)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in posts_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Posts=result_list)

    def getPostsByUserId(self, pid):
        dao = PostsDAO()
        if not dao.getPostById(pid):
            return jsonify(Error="Post Not Found"), 404
        user_list = dao.getUsersByPostId(pid)
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def insertPost(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            pcaption = form['pname']
            pdate = form['pprice']
            pmedia = form['pmedia']
            if pcaption and pdate and pmedia:
                dao = PostsDAO()
                pid = dao.insert(pcaption, pdate, pmedia)
                result = self.build_post_attributes(pid, pcaption, pdate, pmedia)
                return jsonify(Post=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertPostJson(self, json):
        pcaption = json['pcaption']
        pdate = json['pdate']
        pmedia = json['pmedia']
        if pcaption and pdate and pmedia:
            dao = PostsDAO()
            pid = dao.insert(pcaption, pdate, pmedia)
            result = self.build_post_attributes(pid, pcaption, pdate, pmedia)

            return jsonify(Post=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePost(self, pid):
        dao = PostsDAO()
        if not dao.getPostById(pid):
            return jsonify(Error = "Post not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePost(self, pid, form):
        dao = PostsDAO()
        if not dao.getPostById(pid):
            return jsonify(Error = "Post not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                pcaption = form['pcaption']
                pdate = form['pprice']
                pmedia = form['pmedial']
                if pcaption and pdate and pmedia:
                    dao.update(pcaption, pdate, pmedia)
                    result = self.build_post_attributes(pid, pcaption, pdate, pmedia)
                    return jsonify(Post=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_post_counts(self, post_counts):
        result = []
        #print(post_counts)
        for P in post_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByPostId(self):
        dao = PostsDAO()
        result = dao.getCountByPostId()
        #print(self.build_post_counts(result))
        return jsonify(PostCounts = self.build_post_counts(result)), 200
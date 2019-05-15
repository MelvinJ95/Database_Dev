from flask import jsonify
from dao.reaction import ReactionsDAO


class ReactionHandler:
    
    def build_reaction_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rdate'] = row[1]
        result['reaction'] = row[2]
        result['pid'] = row[3]
        result['uid'] = row[4]
        return result

    def build_reaction_attributes(self, rid, rdate, reaction, pid, uid):
        result = {}
        result['rid'] = rid
        result['rdate'] = rdate
        result['reaction'] = reaction
        result['pid'] = pid
        result['uid'] = uid
        return result
    
    def build(self,row):
        result = {}
        result['pid'] = row[0]
        result['likes'] = row[1]
        return result

    def build_likeperday(self,row):
        result = {}
        result['date'] = row[0]
        result['likes'] = row[1]
        return result

    def build_dislikeperday(self,row):
        result = {}
        result['date'] = row[0]
        result['dislikes'] = row[1]
        return result

    def buildDislike(self,row):
        result = {}
        result['pid'] = row[0]
        result['dislikes'] = row[1]
        return result

    def getAllReactions(self):
        dao = ReactionsDAO()
        reaction_list = dao.getAllReactions()
        result_list = []
        for row in reaction_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    def getReactionsById(self, rid):
        dao = ReactionsDAO()
        row = dao.getReactionById(rid)
        if not row:
            return jsonify(Error = "Reaction Not Found"), 404
        else:
            reaction = self.build_reaction_dict(row)
            return jsonify(Reaction=reaction)

    def getAllLikes(self):
        dao = ReactionsDAO()
        likes_list = dao.getAllLikes()
        result_list = []
        for row in likes_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    def getLikesByPostId(self, pid):
        dao = ReactionsDAO()
        row = dao.getLikesByPostId(pid)
        print(row)
        if not row:
            return jsonify(Error="Reaction Not Found"), 404
        else:
            reaction = self.build(row)
            return jsonify(Reaction=reaction)

    def getDislikesByPostId(self, pid):
        dao = ReactionsDAO()
        row = dao.getDislikesByPostId(pid)
        if not row:
            return jsonify(Error="Reaction Not Found"), 404
        else:
            reaction = self.buildDislike(row)
            return jsonify(Reaction=reaction)

    def getAllDislikes(self):
        dao = ReactionsDAO()
        dislikes_list = dao.getAllDislikes()
        result_list = []
        for row in dislikes_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    #might be missing like/dislike in if conditions
    def searchreaction(self, args):
        id = args.get("id")
        date = args.get("date")
        dao = ReactionsDAO()
        reactions_list = []
        if (len(args) == 2) and id and date:
            reactions_list = dao.getReactionsByIdAndDate(id, date)
        elif (len(args) == 1) and id:
            reactions_list = dao.getReactionsById(id)
        elif (len(args) == 1) and date:
            reactions_list = dao.getReactionsBydate(date)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in reactions_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    def insertReaction(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            rdate = form['rdate']
            reaction = form['reaction']
            pid = form['pid']
            uid = form['uid']
            if rdate and reaction and pid and uid:
                dao = ReactionsDAO()
                rid = dao.insert(rdate, reaction, pid, uid)
                result = self.build_reaction_attributes(rid, rdate, reaction, pid, uid)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertReactionJson(self, json):
        rdate = json['rdate']
        reaction = json['reaction']
        pid = json['pid']
        uid = json['uid']
        if rdate and reaction and pid and uid:
            dao = ReactionsDAO()
            rid = dao.insert(rdate, reaction, pid, uid)
            result = self.build_reaction_attributes(rid, rdate, reaction, pid, uid)
            return jsonify(Reaction=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletereaction(self, rid):
        dao = ReactionsDAO()
        if not dao.getReactionsById(rid):
            return jsonify(Error = "reaction not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def deleteReactionByPidAndUid(self, pid,uid):
        dao = ReactionsDAO()
        dao.deleteReactionByPidAndUid(pid, uid)
        return jsonify(DeleteStatus = "OK"), 200

    def updatereaction(self, rid, form):
        dao = ReactionsDAO()
        if not dao.getReactionsById(rid):
            return jsonify(Error = "reaction not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                rdate = form['rdate']
                reaction = form['reaction']
                if rdate and reaction:
                    dao.update(rid, rdate, reaction)
                    result = self.build_reaction_attributes(rid, rdate, reaction)
                    return jsonify(reaction=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_reaction_counts(self, reaction_counts):
        result = []
        #print(reaction_counts)
        for U in reaction_counts:
            D = {}
            D['id'] = U[0]
            D['reaction'] = U[1]
            D['count'] = U[2]
            result.append(D)
        return result

    def getCountByReactionId(self):
        dao = ReactionsDAO()
        result = dao.getCountByReactionId()
        #print(self.build_reaction_counts(result))
        return jsonify(reactionCounts = self.build_reaction_counts(result)), 200

    def getLikesPerDay(self):
        dao = ReactionsDAO()
        likes_list = dao.getLikesPerDay()
        result_list = []
        for row in likes_list:
            result = self.build_likeperday(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    def getDislikesPerDay(self):
        dao = ReactionsDAO()
        likes_list = dao.getDislikesPerDay()
        result_list = []
        for row in likes_list:
            result = self.build_dislikeperday(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

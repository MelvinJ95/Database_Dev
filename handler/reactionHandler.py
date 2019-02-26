from flask import jsonify
from dao.reactions import ReactionsDao


class reactionHandler:
    def build_reaction_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rdate'] = row[1]
        result['rLikeDislike'] = row[2]       
        return result



    def build_reaction_attributes(self, rid, rdate, rLikeDislike):
        result = {}
        result['rid'] = rid
        result['rdate'] = rdate
        result['rLikeDislike'] = rLikeDislike   
        return result
    

    def getAllReactions(self):
        dao = ReactionsDao()
        reaction_list = dao.getAllReactions()
        result_list = []
        for row in reaction_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions=result_list)

    def getreactionById(self, rid):
        dao = ReactionsDao()
        row = dao.getReactionById(rid)
        if not row:
            return jsonify(Error = "reaction Not Found"), 404
        else:
            reaction = self.build_reaction_dict(row)
            return jsonify(Reaction = reaction)

    def searchreaction(self, args):
        id = args.get("id")
        date = args.get("date")
        dao = ReactionsDao()
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


    def insertreaction(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rdate = form['rdate']
            rLikeDislike = form['rLikeDislike']
            if rdate and rLikeDislike:
                dao = ReactionsDao()
                rid = dao.insert(rdate, rLikeDislike)
                result = self.build_reaction_attributes(rid, rdate, rLikeDislike)
                return jsonify(Reaction=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertreactionJson(self, json):
        rdate = json['rdate']
        rLikeDislike = json['rLikeDislike']
       
        if rdate and rLikeDislike:
            dao = ReactionsDao()
            rid = dao.insert(rdate, rLikeDislike)
            result = self.build_reaction_attributes(rid, rdate, rLikeDislike)
            return jsonify(Reaction=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletereaction(self, rid):
        dao = ReactionsDao()
        if not dao.getReactionById(rid):
            return jsonify(Error = "reaction not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatereaction(self, rid, form):
        dao = ReactionsDao()
        if not dao.getReactionById(rid):
            return jsonify(Error = "reaction not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                rdate = form['rdate']
                rLikeDislike = form['rLikeDislike']
                if rdate and rLikeDislike:
                    dao.update(rid, rdate, rLikeDislike)
                    result = self.build_reaction_attributes(rid, rdate, rLikeDislike)
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

    def getCountByreactionId(self):
        dao = ReactionsDao()
        result = dao.getCountByReactionId()
        #print(self.build_reaction_counts(result))
        return jsonify(reactionCounts = self.build_reaction_counts(result)), 200

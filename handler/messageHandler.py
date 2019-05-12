from flask import jsonify
from dao.messages import MessagesDAO


class MessageHandler:
    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mtext'] = row[1]
        result['mdate'] = row[2]       
        return result

    def build_message_attributes(self, mid, mtext, mdate):
        result = {}
        result['mid'] = mid
        result['mtext'] = mtext
        result['mdate'] = mdate   
        return result  

    def build_message_Alpha(self, row,reaction):
        result = {}
        result['pid'] = row[0]
        if(reaction == 'like'):
            result['likes'] = row[1]
        else:
            result['dislikes'] = row[2]
        return result

    def getAllmessages(self):
        dao = MessagesDAO()
        message_list = dao.getAllMessages()
        result_list = []
        for row in message_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def getmessageById(self, mid):
        dao = MessagesDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error = "message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message = message)

    def searchmessage(self, form):
        id = form.to_dict().values()[0]
        date = form.to_dict().values[1]
        dao = MessagesDAO()
        messages_list = []
        if (len(form) == 2) and id and date:
            messages_list = dao.getMessagesByIdAndDate(id, date)
        elif (len(form) == 1) and id:
            messages_list = dao.getMessagesById(id)
        elif (len(form) == 1) and date:
            messages_list = dao.getMessagesBydate(date)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)


    def insertmessage(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error = "Malformed post request"), 400
        else:
            mtext = form.to_dict().values()[0]
            mdate = form.to_dict().values()[1]
            if mtext and mdate:
                dao = MessagesDAO()
                mid = dao.insert(mtext, mdate)
                result = self.build_message_attributes(mid, mtext, mdate)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMessageJson(self, json, pid):
        mtext = json['mtext']
        mdate = json['mdate']
        if mtext and mdate:
            dao = MessagesDAO()
            mid = dao.insert(mtext, mdate)
            dao.reply(pid, mid)
            result = self.build_message_attributes(mid, mtext, mdate)
            return jsonify(Message=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletemessage(self, mid):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "message not found."), 404
        else:
            dao.delete(mid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatemessage(self, mid, form):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "message not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                mtext = form.to_dict().values()[0]
                mdate = form.to_dict().values()[1]
                if mtext and mdate:
                    dao.update(mid, mtext, mdate)
                    result = self.build_message_attributes(mid, mtext, mdate)
                    return jsonify(Message=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_message_counts(self, message_counts):
        result = []
        #print(message_counts)
        for U in message_counts:
            D = {}
            D['id'] = U[0]
            D['message'] = U[1]
            D['count'] = U[2]
            result.append(D)
        return result

    def getCountBymessageId(self):
        dao = MessagesDAO()
        result = dao.getCountBymessageId()
        #print(self.build_message_counts(result))
        return jsonify(MessageCounts = self.build_message_counts(result)), 200

    def getMessageByDate(self, mdate):
        dao = MessagesDAO()
        row = dao.getMessageByDate(mdate)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message=message)


    def getReactionsByMessage(self, mid, reaction):
     dao = MessagesDAO()
     result = dao.getReactionsByMessage(mid, reaction) 
     temp = self.build_message_Alpha(result,reaction)
     return jsonify(Message=temp)
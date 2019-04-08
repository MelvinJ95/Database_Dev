from flask import Flask, jsonify, request
from handler.postHandler import PostHandler
from handler.userHandler import UserHandler
from handler.chatHandler import ChatHandler
from handler.messageHandler import MessageHandler
from handler.contactHandler import ContactHandler
from handler.hashtagHandler import HashtagHandler
from handler.reactionHandler import ReactionHandler
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)


@app.route('/')
def home():
    return 'Welcome to GramChat'

# ----------------- POSTS --------------------------------------


@app.route('/GramChat/posts', methods=['GET', 'POST'])
def getAllPosts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPostJson(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()
        else:
            return PostHandler().searchPosts(request.args)


@app.route('/GramChat/posts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPostById(pid):
    if request.method == 'GET':
        return PostHandler().getPostById(pid)
    elif request.method == 'PUT':
        return PostHandler().updatePost(pid, request.form)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(pid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/posts/date/<string:pdate>', methods=['GET', 'PUT', 'DELETE'])
def getPostsByDate(pdate):
    if request.method == 'GET':
        return PostHandler().getPostsByDate(pdate)
    elif request.method == 'PUT':
        return PostHandler().updatePost(pdate, request.form)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(pdate)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/posts/<int:pid>/<string:reaction>', methods=['GET'])
def addReaction(pid, reaction):
    if request.method == 'GET':
        print(reaction)
        return PostHandler().getReactionsByPost(pid, reaction)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/posts/user/<int:uid>')
def getPostsByUser(uid):
    return PostHandler().getPostsByUser(uid)


@app.route('/GramChat/posts/chat/<int:cid>')
def getPostsByChatId(cid):
    return PostHandler().getPostsByChatId(cid)


@app.route('/GramChat/posts/chat/<int:cid>/user/<int:uid>')
def getPostsByChatIdAndUser(cid, uid):
    return PostHandler().getPostsByChatIdAndUser(cid, uid)


# ------------------- USERS and CONTACTS ---------------------------

# @app.route('/GramChat/login', methods=['POST'])
# def login():
#     return UserHandler.authorize(request.json)
#
#
# @app.route('/GramChat/register', methods=['POST'])
# def register():
#     return UserHandler.insertUser(request.json)


# @app.route('/GramChat/user', methods=['GET', 'POST'])
# def getPostUser():
#     if request.method == 'GET':
#         if len(request.args) >= 1:
#             return  # get specific user
#         else:
#             return  # get all users
#     if request.method == 'POST':
#         return  # create new user


@app.route('/GramChat/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUsers(request.args)


@app.route('/GramChat/users/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(pid):
    if request.method == 'GET':
        return UserHandler().getUserById(pid)
    elif request.method == 'PUT':
        return UserHandler().updateUser(pid, request.form)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(pid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/users/delete/<int:uid>', methods=['GET', 'POST'])
def deleteUser(uid):
    return UserHandler().deleteUser(uid)


@app.route('/GramChat/contacts/<int:owner>', methods=['GET'])
def getAllContacts(owner):
    return ContactHandler().getContactListbyUser(owner)


@app.route('/GramChat/contacts/addContact/byPhone/<int:owner>', methods=['PUT', 'POST'])
def addContactbyPhone(owner):
    return ContactHandler().addContactByPhone(request.form, owner)


@app.route('/GramChat/contacts/addContact/byEmail/<int:owner>', methods=['PUT', 'POST'])
def addContactbyEmail(owner):
    return ContactHandler().addContactByEmail(listrequest.form, owner)


@app.route('/GramChat/contacts/removeContact/<int:owner>/<int:uid>', methods=['DELETE'])
def removeUserFromContactList(owner, uid):
    return ContactHandler().removeContact(request.form, owner, uid)


# @app.route('/GramChat/contacts/getUserContacts/<int:uid>', methods=['GET'])
# def getUserContacts(uid):
#    return ContactHandler().getContactListbyUser(uid)

# @app.route('/GramChat/contacts/addContact/<int:uid>', methods = ['PUT','POST'])
# def addContactbyPhoneAndEmail(uid,firstname,lastname,phone,email):
#     return ContactHandler().addContactByPhoneAndEmail(request.json,uid,firstname,lastname,phone,email)

# ------------------ CHATS -----------------------------

@app.route('/GramChat/chats', methods=['GET', 'POST'])
def getAllChats():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().insertChatJson(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return ChatHandler().searchChats(request.args)

@app.route('/GramChat/chat/createchat/', methods=['POST'])
def createNewChat():
    return ChatHandler.insertChatJson(request.json)


@app.route('/GramChat/chat/removeUser/<int:cid>/<int:usrid>', methods=['DELETE']) 
def removeUserFromchat(cid, usrid):
    return ChatHandler().removeMember(cid, usrid)


@app.route('/GramChat/chat/adduser/<int:cid>/<int:uid>', methods=['POST'])
def addUsertochat(cid, uid):
    return ChatHandler().insertMember(cid, uid)


@app.route('/GramChat/chat/deletechat/<int:cid>/<int:uid>', methods=['DELETE'])
def deleteChat(cid, uid):
    return ChatHandler.removeChat(request.json, cid, uid)


@app.route('/GramChat/chat/<int:cid>/postmsg', methods=['POST'])
def postPost():
    return PostHandler.insertPost(request.json)


@app.route('/GramChat/chat/<int:cid>/<int:mID>/reply', methods=['POST'])
def replyPost():
    return MessageHandler.insertMessage(request.json)


# ---------------- REACTIONS ---------------------

@app.route('/GramChat/reactions', methods=['GET', 'POST'])
def getAllReactions():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReactionHandler().insertReactionJson(request.json)
    else:
        if not request.args:
            return ReactionHandler().getAllReactions()
        else:
            return ReactionHandler().searchReactions(request.args)


@app.route('/GramChat/reactions/likes')
def getAllLikes():
    return ReactionHandler().getAllLikes()


@app.route('/GramChat/reactions/dislikes')
def getAllDislikes():
    return ReactionHandler().getAllDislikes()


@app.route('/ChatApp/chat/<int:cid>/<int:mID>/like', methods=['POST'])
def likeMessage(mID):
    return


@app.route('/GramChat/chat/<int:cid>/<int:mID>/dislike', methods=['POST'])
def dislikeMessage(mID):
    return


# -------------- ETC -----------------------------


@app.route('/GramChat/trends', methods=['GET'])
def getTrends():
    if request.method == 'GET':
        return HashtagHandler().getTrendingTopics()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/posts/user/<int:uid>/date/<string:date>')
def getPostsPerDayByUser(uid, date):
    return PostHandler().getPostsPerDayByUser(uid, date)


@app.route('/GramChat/users/active')
def getActiveUsers():
    return PostHandler().getActiveUsers()


@app.route('/GramChat/posts/<string:date>')
def getNumberOfPostsPerDay(date):
    return PostHandler().getNumberOfPostsPerDay(date)

@app.route('/GramChat/posts/reply/<int:post>', methods=['GET'])
def reply(post):
    return PostHandler().getAllReplies(post)

@app.route('/GramChat/users/reaction/like', methods=['GET'])
def getUsersLike():
    return UserHandler().getUserLikeMessage()

@app.route('/GramChat/users/reaction/dislike', methods=['GET'])
def getUsersDislike():
    return UserHandler().getUserDislikeMessage()

@app.route('/GramChat/chat/owner/<int:cid>', methods=['GET'])
def chatOwner(cid):
    return UserHandler().chatOwner(cid)

if __name__ == '__main__':
    app.run()
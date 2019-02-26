from flask import Flask, jsonify, request
from handler.postHandler import PostHandler
from handler.userHandler import UserHandler
from handler.chatHandler import ChatHandler
from handler.messageHandler import MessageHandler
from handler.contactHandler import ContactHandler
from handler.hashtagHandler import HashtagHandler

app = Flask(__name__)

@app.route('/')
def home():
    return ('Welcome to GramChat')

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
def getPostByDate(pdate):
    if request.method == 'GET':
        return PostHandler().getPostByDate(pdate)
    elif request.method == 'PUT':
        return PostHandler().updatePost(pdate, request.form)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(pdate)
    else:
        return jsonify(Error="Method not allowed."), 405


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

# @app.route('/GramChat/user/<int:uID>', methods=['GET'])
# def getUserByID(uID):
#     return UserHandler.getUserById(uID)

@app.route('/GramChat/contacts/addContact/<int:owner>', methods=['POST']) 
def addUsertoContactList(owner):
    return ContactHandler.addContact(request.json, owner)

@app.route('/GramChat/chat/createchat/<int:owner>', methods=['POST'])
def createNewChat(owner):
    return  ChatHandler.insertNewChat(request.jason, owner)

@app.route('/GramChat/chat/removeUser/<int:cid>', methods=['DELETE']) 
def removeUserFromchat():
    return ChatHandler.removeMember(request.json)

@app.route('/GramChat/chat/adduser/<int:cid>', methods=['POST'])
def addUsertochat(cid, uid):
    return ChatHandler.insertMember(request.json)

@app.route('/GramChat/contacts/removeContact/<int:uid>', methods=['DELETE'])
def removeUserFromContactList(owner, uid):
    return ContactHandler.removeContact(request.json, uid)

@app.route('/GramChat/chat/deletechat/<int:owner>', methods=['DELETE']) 
def deleteChat(owner):
    return ChatHandler.removeChatGroup(request.json, owner)

@app.route('/GramChat/chat/<int:cid>/postmsg', methods=['POST'])
def postPost():
    return PostHandler.insertPost(request.json)

@app.route('/ChatApp/chat/<int:cid>/<int:mID>/like', methods=['POST'])
def likeMessage(mID):
    return

@app.route('/GramChat/chat/<int:cid>/<int:mID>/dislike', methods=['POST'])
def dislikeMessage(mID):
    return

@app.route('/GramChat/chat/<int:cid>/<int:mID>/reply', methods=['POST'])
def replyPost():
    return MessageHandler.insertMessage(request.json)

@app.route('/GramChat/users/delete/<int:uid>', methods=['GET', 'POST'])
def deleteUser(uid):   
    UserHandler().deleteUser(uid)

@app.route('/GramChat/trends', methods=['GET'])
def getTrends():
    if request.method == 'GET':
        return HashtagHandler().getTrendingTopics()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/GramChat/posts/user/<int:uid>/<string:date>')
def getPostsPerDayByUser(uid,date):
    return PostHandler().getPostsPerDayByUser(uid, date)


@app.route('/GramChat/users/active')
def getActiveUsers():
    return PostHandler().getActiveUsers()

if __name__ == '__main__':
    app.run()
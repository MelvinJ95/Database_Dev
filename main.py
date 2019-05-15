from flask import Flask, jsonify, request, redirect, url_for, render_template, flash
from handler.postHandler import PostHandler
from handler.userHandler import UserHandler
from handler.chatHandler import ChatHandler
from handler.messageHandler import MessageHandler
from handler.contactHandler import ContactHandler
from handler.hashtagHandler import HashtagHandler
from handler.reactionHandler import ReactionHandler
from handler.dashboardHandler import DashboardHandler
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)


UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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

@app.route('/GramChat/posts/all', methods = ['GET'])
def getAllPostsWebsite():
    return PostHandler().getAllPostWebsite()

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

@app.route('/GramChat/login', methods=['POST'])
def login():
     return UserHandler().authorize(request.json)
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

@app.route('/GramChat/users/info/<int:uid>', methods=['GET'])
def getInfoById(uid):
    return UserHandler().getInfoById(uid)

@app.route('/GramChat/users/info/<string:username>', methods=['GET'])
def getInfoByUsername(username):
    return UserHandler().getInfoByUsername(username)

@app.route('/GramChat/users/delete/<int:uid>', methods=['GET', 'POST'])
def deleteUser(uid):
    return UserHandler().deleteUser(uid)

@app.route('/GramChat/users/chats/<int:uid>', methods=['GET', 'POST'])
def userChats(uid):
    return UserHandler().getUserChats(uid)

@app.route('/GramChat/contacts/<int:owner>', methods=['GET'])
def getAllContacts(owner):
    return ContactHandler().getContactListbyUser(owner)

@app.route('/GramChat/contacts/addContact/<int:owner>', methods=['PUT', 'POST'])
def addContact(owner):
    return ContactHandler().addContactJSON(request.json, owner)

@app.route('/GramChat/contacts/addContact/byPhone/<int:owner>', methods=['PUT', 'POST'])
def addContactbyPhone(owner):
    return ContactHandler().addContactByPhone(request.form, owner)

@app.route('/GramChat/contacts/addContact/byEmail/<int:owner>', methods=['PUT', 'POST'])
def addContactbyEmail(owner):
    return ContactHandler().addContactByEmail(request.form, owner)

@app.route('/GramChat/contacts/removeContact/<int:owner>/<int:contact>', methods=['DELETE'])
def removeUserFromContactList(owner, contact):
    return ContactHandler().removeContact(owner, contact)


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

@app.route('/GramChat/chat/createchat', methods=['POST'])
def createNewChat():
    return ChatHandler().insertChatJson(request.json)

@app.route('/GramChat/chat/<int:cid>/posts/hashtag/<string:hashtag>', methods=['GET'])
def postsByHashtag(cid, hashtag):
    return PostHandler().getPostsByHashtag(cid, hashtag)

@app.route('/GramChat/chat/removeUser/<int:cid>/<int:uid>', methods=['DELETE'])
def removeUserFromChat(cid, uid):
    return ChatHandler().removeMember(cid, uid)

@app.route('/GramChat/chat/adduser/<int:cid>/<int:uid>', methods=['POST'])
def addUsertochat(cid, uid):
    return ChatHandler().insertMember( cid, uid)

@app.route('/GramChat/chat/delete/<int:cid>/<int:uid>', methods=['DELETE'])
def deleteChat(cid, uid):
    return ChatHandler().removeChat(cid, uid)

@app.route('/GramChat/chat/<int:cid>/postmsg', methods=['POST'])
def postPost():
    return PostHandler().insertPost(request.json)

# @app.route('/GramChat/chat/reply/<int:pid>', methods=['POST'])
# def replyPost(pid):
#     return MessageHandler().insertMessageJson(request.json, pid)

@app.route('/GramChat/chat/reply/<int:pid>', methods=['POST'])
def replyPost(pid):
    return PostHandler().insertPostReplyJson(request.json, pid)

@app.route('/GramChat/chat/members/<int:cid>')
def getMembersOfChat(cid):
    return UserHandler().getChatMembers(cid)

@app.route('/GramChat/chat/user/<int:cid>/<int:uid>', methods=['GET'])
def getChatByUserIDandChatID(cid,uid):
    return ChatHandler().getChatByUserIDandChatID(cid,uid)

@app.route('/GramChat/user/chats/<int:uid>')
def getAllUserChats(uid):
    return UserHandler().getAllUserChats(uid)

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

@app.route('/GramChat/reactions/getLikes/<int:PID>', methods=['GET'])
def getLikesbyPostID(PID):
    return ReactionHandler().getLikesByPostId(PID)

@app.route('/GramChat/reactions/delete/<int:uid>/<int:pid>', methods=['DELETE'])
def deleteReaction(pid,uid):
    return ReactionHandler().deleteReactionByPidAndUid(pid,uid)


# -------------- ETC -----------------------------

@app.route('/GramChat/dashboard')
def dashboard():
    return DashboardHandler().dashboard()

@app.route('/GramChat/trends', methods=['GET'])
def getTrends():
    if request.method == 'GET':
        return HashtagHandler().getTrendingTopics()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/GramChat/hashtags', methods=['GET', 'POST'])
def getHashtags():
    if request.method == 'POST':
        return HashtagHandler().insertHashtagJson(request.json)
    else:
        return HashtagHandler().getAllHashtags()

@app.route('/GramChat/posts/date/user/<int:uid>')
def getPostsPerDayByUser(uid):
    return PostHandler().getPostsPerDayByUser(uid)

@app.route('/GramChat/users/active')
def getActiveUsers():
    return PostHandler().getActiveUsers()

# @app.route('/GramChat/posts/<string:date>')
# # def getNumberOfPostsPerDay(date):
# #     return PostHandler().getNumberOfPostsPerDay(date)

@app.route('/GramChat/postsperday')
def getNumberOfPostsPerDay():
    return PostHandler().getNumberOfPostsPerDay()

@app.route('/GramChat/posts/reply/<int:post>', methods=['GET'])
def reply(post):
    return PostHandler().getAllReplies(post)

@app.route('/GramChat/posts/insert', methods =['POST'])
def insert():
    return PostHandler().insertPostJson(request.json)

@app.route('/GramChat/users/reaction/like/<int:pid>', methods=['GET'])
def getUsersLike(pid):
    return UserHandler().getUserLikeMessage(pid)

@app.route('/GramChat/users/reaction/dislike/<int:pid>', methods=['GET'])
def getUsersDislike(pid):
    return UserHandler().getUserDislikeMessage(pid)

@app.route('/GramChat/chat/owner/<int:cid>', methods=['GET'])
def chatOwner(cid):
    return UserHandler().chatOwner(cid)

@app.route('/GramChat/likes/date')
def getLikesPerDay():
    return ReactionHandler().getLikesPerDay()

@app.route('/GramChat/dislikes/date')
def getDislikesPerDay():
    return ReactionHandler().getDislikesPerDay()

@app.route('/GramChat/replies/date')
def getRepliesPerDay():
    return PostHandler().getNumberOfRepliesPerDay()

@app.route('/GramChat/posts/replies')
def getNumberOfPostReplies():
    return PostHandler().getNumberOfPostReplies()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/GramChat/upload', methods=['GET','POST'])
def upload_file():
    print("ENTERED THINGY")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',filename=filename))
    
    return redirect(request.url)
if __name__ == "__main__":
    app.run()
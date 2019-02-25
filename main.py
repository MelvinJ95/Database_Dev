from flask import Flask, jsonify, request
from handler.postHandler import PostHandler
from handler.userHandler import UserHandler
from handler.chatHandler import ChatHandler

@app.route('/')
def home():
    return ('Welcome to GramChat')

@app.route('/GramChat/login', methods= ['POST'])
def login():
    return UserHandler.authorize(request.json)

@app.route('/GramChat/register', methods=['POST'])
def register():
    return UserHandler.insertUser(request.json)
    
@app.route('/GramChat/user', methods=['GET', 'POST'])
def getPostUser():
    if request.method == 'GET':
        if len(request.args) >= 1:
            return #get specific user
        else:
            return #get all users
    if request.method == 'POST':
        return  #create new user

@app.route('/GramChat/user/<int:uID>', methods=['GET'])
def getUserByID(pID):
    return UserHandler.getUserById(uID)

@app.route('/GramChat/chat/createchat/<int:owner>', methods=['POST']) 
def createNewChat(owner):
    return ChatHandler.insertNewChatGroup(request.json, owner)

@app.route('/GramChat/contacts/addContact/<int:owner>', methods=['POST']) 
def addUsertoContactList(owner):
    return #add contact

@app.route('/GramChat/chat/adduser/<int:cid>', methods=['POST']) 
def addUsertochat():
    return ChatHandler.insertMember(request.json)

@app.route('/GramChat/chat/removeUser/<int:cid>', methods=['DELETE']) 
def removeUserFromchat():
    return ChatHandler.removeMember(request.json)

@app.route('/GramChat/contacts/addContact/<int:owner>/<int:uid>', methods=['DELETE']) 
def removeUserFromContactList(owner, uid):
    return #delete a contact

@app.route('/GramChat/chat/deletechat/<int:owner>', methods=['DELETE']) 
def deleteChat(owner):
    return #create new chat

@app.route('/GramChat/chat/<int:cid>/postmsg', methods = ['POST'])
def postPost():
    return PostHandler.insertPost(request.json)

@app.route('/ChatApp/chat/<int:cid>/<int:mID>/like', methods=['POST'])
def likeMessage(mID):
    return 

@app.route('/GramChat/chat/<int:cid>/<int:mID>/dislike', methods=['POST'])
def dislikeMessage(mID):
    return 

@app.route('/GramChat/chat/<int:cid>/<int:mID>/reply', methods = ['POST'])
def replyPost():
    return 
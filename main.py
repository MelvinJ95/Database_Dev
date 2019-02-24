from flask import Flask, jsonify
from handler import userHandler, postHandler

@app.route('/')
def home():
    return ('Welcome to GramChat')

@app.route('/GramChat/login', methods= ['POST'])
def login():
    return #login

@app.route('/GramChat/register', methods=['POST'])
def register():
    return #register new user
    
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
    return #user by id

@app.route('/GramChat/chat/createchat/<int:owner>/<string:chatname>', methods=['POST']) 
def createNewChat(owner, chatname):
    return #create new chat

@app.route('/GramChat/contacts/addContact/<int:owner>/<int:uid>', methods=['POST']) 
def addUsertoContactList(owner, uid):
    return #add contact

@app.route('/GramChat/chat/adduser/<int:cid>/<int:uid>', methods=['POST']) 
def addUsertochat(cid, uid):
    return #add an user

@app.route('/GramChat/chat/removeUser/<int:cid>/<int:uid>', methods=['DELETE']) 
def removeUserFromchat(cid, uid):
    return #remove a user

@app.route('/GramChat/contacts/addContact/<int:owner>/<int:uid>', methods=['DELETE']) 
def removeUserFromContactList(owner, uid):
    return #delete a contact

@app.route('/GramChat/chat/deletechat/<int:owner>/<string:chatname>', methods=['DELETE']) 
def deleteChat(owner, chatname):
    return #create new chat

@app.route('/GramChat/chat/<int:cid>/postmsg', methods = ['POST'])
def postMessage():
    return #post a message

@app.route('/ChatApp/chat/<int:cid>/<int:mID>/like', methods=['POST'])
def likeMessage(mID):
    return 

@app.route('/GramChat/chat/<int:cid>/<int:mID>/dislike', methods=['POST'])
def dislikeMessage(mID):
    return 

@app.route('/GramChat/chat/<int:cid>/<int:mID>/reply', methods = ['POST'])
def replyPost():
    return 
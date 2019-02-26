#Pre-define list of reactions
result = []
reaction = [123, 'February 20, 2019', 'Like']
reaction2 = [124, 'February 20, 2019', 'dislike']
#append reactions
result.append(reaction)
result.append(reaction2)
class ReactionsDAO:

    def getAllReactions(self):
        global result
        return reaction 

    def getReactionById(self, Id):
        global result
        result = self.getAllReactions()
        for reaction in result:
            if reaction[0] == Id:
                return reaction
        return 

    def getReactionsByIDAndDate(self, Id, date):
        global result
        result = self.getAllReactions()
        for r in result: 
            if(r[0]==Id and r[2]==date):
                return r
        return 

    def getReactionByID(self, Id):
        global result
        result = self.getAllReactions()
        for r in result: 
            if(r[0]==Id):
                return r
        return
        
    def getReactionByDate(self, date):
       global result
       result = self.getAllReactions()
       for r in result:
          if(r[2]==date):
                return r
       return

    def insert(self, date, likeDislike):
        global result
        result = self.getAllReactions()
        randId = 12344
        temp = [randId,date, likeDislike]
        result.append(temp)
        return randId    
        

    def delete(self, id):
        global result 
        temp = self.getReactionByID(id)
        result.remove(temp)
    
class ReactionsDAO:

    def getAllReactions(self):
        result = []
        reaction = [123, 'February 20, 2019', 'Like']
        result.append(reaction)
        return reaction 

    def getReactionById(self, Id):
        result = self.getAllReactions()
        for r in result:
            if(r[0]==Id):
                return r
        return 

    def getReactionsByIDAndDate(self, Id, date):
        result = self.getAllReactions()
        for r in result: 
            if(r[0]==Id and r[2]==date):
                return r
        return 

    def getReactionByID(self, Id):
        result = self.getAllReactions()
        for r in result: 
            if(r[0]==Id):
                return r
        return
        
    def getReactionByDate(self, date):
       result = self.getAllReactions()
        for r in result: 
            if(r[2]==date):
                return r
        return

    def insert(self):
        return

    def delete(self):
        return


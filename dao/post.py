#from dao import users

result = []
post1 = [1, 'Hola', '2-24-2019', 'link.png', 125, 10, 3]
post2 = [4, 'Adios', '2-25-2019', 'link2.png', 124, 0, 0]
result.append(post1)
result.append(post2)

class PostsDAO:

    def getAllPosts(self):
        global result
        return result

    def getPostById(self, pid):
        global result
        result = self.getAllPosts()
        for post in result:
            if post[0] == pid:
                return post

        return []

    def getPostByDate(self, pdate):
        global result
        result = self.getAllPosts()
        for post in result:
            if post[2] == pdate:
                result.append(post)
                #return post
        return result

    def getPostByUser(self, uid):
        global result
        result = self.getAllPosts()
        #user = users.getAllUsers()
        post1 = [1, 'Hola', '2-24-2019', 'link.png', 123]
        for post in result:
            if post[4] == uid:
                result.append(post)

        return result

    def getPostsPerDayByUser(self, uid, date):
        global result
        result = []
        all = self.getAllPosts()
        for post in all:
            if post[2] == date and post[4] == uid:
                result.append(post)
        return result

    def getActiveUsers(self):
        global result
        result = "Active users shown here."
        return result

    def getNumberOfPostsPerDay(self, date):
        global result
        result = self.getPostByDate(date)
        return "There were a total of %d posts on this day." % (len(result))

    def getReactionsByPost(self, pid, reaction):
        #global result
        result = self.getPostById(pid)
        if reaction == 'like':
            return "The number of likes for post with id %d is %d." % (pid, result[5])
        if reaction == 'dislike':
            return "The number of dislikes for post with id %d is %d." % (pid, result[6])

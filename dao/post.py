#from dao import users

result = []
post1 = [1, 'Hola', '2-24-2019', 'link.png', 5]
post2 = [4, 'Adios', '2-25-2019', 'link2.png', 33]
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
                #result.append(post)
                return post
        return []

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
        return len(result)
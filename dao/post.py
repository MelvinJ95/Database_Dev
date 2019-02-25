from dao import users
class PostsDAO:

    def getAllPosts(self):
        result = []
        post1 = [1, 'Hola', '2-24-2019', 'link.png']
        post2 = [4, 'Adios', '2-25-2019', 'link2.png']
        result.append(post1)
        result.append(post2)
        return result

    def getPostById(self, pid):
        result = self.getAllPosts()
        for post in result:
            if post[0] == pid:
                return post

        return []

    def getPostByDate(self, pdate):
        result = self.getAllPosts()
        for post in result:
            if post[2] == pdate:
                return post

        return []

    def getPostByUser(self, uid):
        result = self.getAllPosts()
        user = users.getAllUsers()
        post1 = [1, 'Hola', '2-24-2019', 'link.png']
        for post in result:
            if post[2] == uid:
                result.append(post)

        return result





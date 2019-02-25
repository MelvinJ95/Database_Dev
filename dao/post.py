class PostsDAO:

    def getAllPosts(self):
        result = []
        post1 = [1, 'Hola', '2-24-2019', 'link.png']
        result.append(post1)
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
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_post(self, title, content):

        return Post(title, content, self)

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

    def add_comment(self, content, author):
        comment = Comment(content, author, self)
        self.comments.append(comment)
        return comment

class Comment:
    def __init__(self, content, author, post):
        self.content = content
        self.author = author
        self.post = post
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post

    def __str__(self):
        return f"User: {self.username}"


class Post:
    total_posts = 0   # class variable

    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.comments = []
        Post.total_posts += 1

    def like(self):
        self.likes += 1

    def add_comment(self, user, text):
        comment = Comment(user, text)
        self.comments.append(comment)

    def __str__(self):
        result = f"\nPost by {self.user.username}: {self.content}\nLikes: {self.likes}\nComments:\n"
        for c in self.comments:
            result += str(c) + "\n"
        return result


class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def __str__(self):
        return f"{self.user.username}: {self.text}"


# -------- Example Usage --------
u1 = User("Nandini")
u2 = User("Rahul")

# Create post
p1 = u1.create_post("Hello everyone!")

# Likes
p1.like()
p1.like()

# Comments
p1.add_comment(u2, "Nice post!")
p1.add_comment(u1, "Thank you!")

# Display
print(p1)

print("Total Posts:", Post.total_posts)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book added: {self.title}")

    def __del__(self):
        print(f"Book removed: {self.title}")


class Member:
    def __init__(self, name):
        self.name = name
        print(f"Member created: {self.name}")


# Example
b1 = Book("Python Basics", "John")
m1 = Member("Nandini")

del b1   # triggers destructor
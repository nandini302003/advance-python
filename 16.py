class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Student: {self.name}, Roll: {self.roll}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")


class Admin:
    def __init__(self, name):
        self.name = name

    def manage(self):
        print(f"Admin {self.name} is managing the system")


# Example
s = Student("Nandini", 101)
t = Teacher("Sharma", "Math")
a = Admin("Principal")

s.display()
t.display()
a.manage()
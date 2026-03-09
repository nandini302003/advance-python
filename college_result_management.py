class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}
        self.total = 0
        self.percentage = 0
        self.grade = ""

    def calculate_result(self):
        self.total = sum(self.marks.values())
        self.percentage = self.total / len(self.marks)

        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 75:
            self.grade = "A"
        elif self.percentage >= 60:
            self.grade = "B"
        elif self.percentage >= 50:
            self.grade = "C"
        else:
            self.grade = "Fail"

students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    
    if roll in students:
        print("Student already exists!")
    else:
        students[roll] = Student(roll, name)
        print("Student added successfully!")

def add_marks():
    roll = input("Enter Roll No: ")
    
    if roll in students:
        subjects = int(input("Enter number of subjects: "))
        for _ in range(subjects):
            subject = input("Enter subject name: ")
            mark = float(input("Enter marks: "))
            students[roll].marks[subject] = mark
        
        students[roll].calculate_result()
        print("Marks added successfully!")
    else:
        print("Student not found!")

def display_result():
    roll = input("Enter Roll No: ")
    
    if roll in students:
        student = students[roll]
        print("\n--- RESULT ---")
        print("Roll No:", student.roll_no)
        print("Name:", student.name)
        print("Marks:", student.marks)
        print("Total:", student.total)
        print("Percentage:", round(student.percentage, 2))
        print("Grade:", student.grade)
    else:
        print("Student not found!")

def display_all():
    if not students:
        print("No records found!")
    else:
        for roll, student in students.items():
            print("\n-------------------")
            print("Roll No:", student.roll_no)
            print("Name:", student.name)
            print("Total:", student.total)
            print("Percentage:", round(student.percentage, 2))
            print("Grade:", student.grade)

def menu():
    while True:
        print("\n==== College Result Management System ====")
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Display Result")
        print("4. Display All Results")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            display_result()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()
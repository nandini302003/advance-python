# ==========================================
# CLASS STUDENT GRADE BOOK SYSTEM
# ==========================================

class Student:
    def __init__(self, roll_no, name, course, subjects):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.subjects = subjects
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        total = sum(self.subjects.values())
        return round(total / len(self.subjects), 2)

    def calculate_grade(self):
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B"
        elif self.average >= 60:
            return "C"
        elif self.average >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("===================================")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Course  :", self.course)
        print("Subjects:")
        for subject, marks in self.subjects.items():
            print(f"   {subject} : {marks}")
        print("Average :", self.average)
        print("Grade   :", self.grade)
        print("===================================")


class ClassGradeBook:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_class_records(self):
        print(f"\n******** {self.class_name} CLASS RECORD ********\n")
        for student in self.students:
            student.display()

    def show_class_average(self):
        total = sum(student.average for student in self.students)
        class_avg = round(total / len(self.students), 2)
        print("\nClass Average Score:", class_avg)

    def show_ranking(self):
        print(f"\n******** {self.class_name} CLASS RANKING ********\n")

        sorted_students = sorted(
            self.students,
            key=lambda student: student.average,
            reverse=True
        )

        rank = 1
        for student in sorted_students:
            print(f"Rank {rank} | Roll: {student.roll_no} | Name: {student.name} | Avg: {student.average} | Grade: {student.grade}")
            rank += 1


# ==========================================
# CLASS DATA (Example: AIML 2nd Year)
# ==========================================

gradebook = ClassGradeBook("B.Tech AIML 2nd Year")

student1 = Student(101, "Nandini Panda", "AIML",
                   {"Python": 88, "Math": 92, "AI": 85, "DSA": 90})

student2 = Student(102, "Rahul Sharma", "AIML",
                   {"Python": 78, "Math": 74, "AI": 80, "DSA": 76})

student3 = Student(103, "Priya Singh", "AIML",
                   {"Python": 95, "Math": 90, "AI": 93, "DSA": 97})

student4 = Student(104, "Amit Kumar", "AIML",
                   {"Python": 65, "Math": 60, "AI": 68, "DSA": 70})

student5 = Student(105, "Sneha Das", "AIML",
                   {"Python": 85, "Math": 88, "AI": 82, "DSA": 86})


# Add students to class
gradebook.add_student(student1)
gradebook.add_student(student2)
gradebook.add_student(student3)
gradebook.add_student(student4)
gradebook.add_student(student5)


# ==========================================
# DISPLAY CLASS INFORMATION
# ==========================================

gradebook.show_class_records()
gradebook.show_class_average()
gradebook.show_ranking()

'''20. Build mini project:
 STUDENT MANAGEMENT SYSTEM
 Features:
 - Add student
 - View student
 - Delete student
 - Store data in file or database'''

import sqlite3
class StudentManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
    def add_student(self, name):
        self.cursor.execute('INSERT INTO Student (name) VALUES (?)', (name,))
        self.conn.commit()
    def view_students(self):
        self.cursor.execute('SELECT * FROM Student')
        return self.cursor.fetchall()
    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM Student WHERE id = ?', (student_id,))
        self.conn.commit()
    def close(self):
        self.conn.close()
# Example usage
if __name__ == "__main__":

    sms = StudentManagementSystem()
    sms.add_student("Alice")
    sms.add_student("Bob")
    print("Students:")
    for student in sms.view_students():
        print(f"ID: {student[0]}, Name: {student[1]}")
    sms.delete_student(1)  # Delete student with ID 1
    print("Students after deletion:")
    for student in sms.view_students():
        print(f"ID: {student[0]}, Name: {student[1]}")
    sms.close()

# Output:
# Students:
# ID: 1, Name: Alice
# ID: 2, Name: Bob
# Students after deletion:
# ID: 2, Name: Bob
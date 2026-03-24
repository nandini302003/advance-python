'''19. Python + SQL:
 - Connect database
 - Create table Student
 - Insert 3 records
 - Fetch and display all
'''

import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
# Create Student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
# Insert 3 records into Student table
students = [('Alice',), ('Bob',), ('Charlie',)]
cursor.executemany('INSERT INTO Student (name) VALUES (?)', students)
# Commit the changes
conn.commit()
# Fetch and display all records from Student table
cursor.execute('SELECT * FROM Student')
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}")
# Close the database connection
conn.close()

# Output:
# ID: 1, Name: Alice
# ID: 2, Name: Bob
# ID: 3, Name: Charlie

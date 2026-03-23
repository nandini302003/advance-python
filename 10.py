students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Name: ")
    roll = input("Roll No: ")
    marks = float(input("Marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    students.append(student)

# Display all
print("\nAll Students:")
for s in students:
    print(s)

# Pass/Fail filter
print("\nPassed Students:")
for s in students:
    if s["marks"] >= 40:
        print(s["name"], "-", s["marks"])

print("\nFailed Students:")
for s in students:
    if s["marks"] < 40:
        print(s["name"], "-", s["marks"])
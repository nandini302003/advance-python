students = {}

while True:
    print("\n1. Add Student\n2. Update Marks\n3. Show All\n4. Average\n5. Topper\n6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        marks = list(map(int, input("Enter marks (space separated): ").split()))
        students[name] = {"marks": marks}

    elif choice == "2":
        name = input("Enter name to update: ")
        if name in students:
            marks = list(map(int, input("Enter new marks: ").split()))
            students[name]["marks"] = marks
        else:
            print("Student not found")

    elif choice == "3":
        print(students)

    elif choice == "4":
        for name, data in students.items():
            avg = sum(data["marks"]) / len(data["marks"])
            print(name, "Average:", avg)

    elif choice == "5":
        topper = max(students, key=lambda x: sum(students[x]["marks"]))
        print("Topper:", topper)

    elif choice == "6":
        break
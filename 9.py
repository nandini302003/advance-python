employees = {}

while True:
    print("\n1. Add Employee\n2. Remove Employee\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        employees[name] = "Present"

    elif choice == "2":
        name = input("Enter name to remove: ")
        employees.pop(name, None)

    elif choice == "3":
        for name, status in employees.items():
            print(name, "-", status)

    elif choice == "4":
        break
    
contacts = {}

while True:
    print("\n1. Add\n2. Search\n3. Delete\n4. List\n5. Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Enter name to search: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif choice == "3":
        name = input("Enter name to delete: ")
        contacts.pop(name, None)

    elif choice == "4":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "5":
        break
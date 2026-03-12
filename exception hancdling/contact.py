# Contact Book Program

contacts = {}

# Add Contact
def add_contact():
    try:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        if name == "" or phone == "":
            raise ValueError("Fields cannot be empty!")

        if name in contacts:
            raise KeyError("Contact already exists!")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits!")

        contacts[name] = phone
        print("Contact saved successfully!\n")

    except ValueError as e:
        print("Error:", e)
    except KeyError as e:
        print("Error:", e)


# Edit Contact
def edit_contact():
    try:
        name = input("Enter name to edit: ").strip()

        if name not in contacts:
            raise KeyError("Contact not found!")

        new_phone = input("Enter new phone number: ")

        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("Invalid phone number format!")

        contacts[name] = new_phone
        print("Contact updated successfully!\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


# Search Contact
def search_contact():
    try:
        name = input("Enter name to search: ").strip()

        if name == "":
            raise ValueError("Name cannot be empty!")

        if name not in contacts:
            raise KeyError("Contact not found!")

        print("Phone Number:", contacts[name], "\n")

    except ValueError as e:
        print("Error:", e)
    except KeyError as e:
        print("Error:", e)


# Display All Contacts
def display_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nContact List")
        print("---------------------")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)
        print()


# Main Menu
def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_contact()
            elif choice == 2:
                edit_contact()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                display_contacts()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Please enter a valid number!\n")


main()
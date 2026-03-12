# Student Grade Management System

students = {}

# Add student
def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        if student_id == "":
            raise ValueError("Student ID cannot be empty")

        name = input("Enter Student Name: ").strip()
        if name == "":
            raise ValueError("Name cannot be empty")

        grade = float(input("Enter Grade: "))

        students[student_id] = {"name": name, "grade": grade}
        print("Student added successfully!\n")

    except ValueError as e:
        print("Error:", e)
    except Exception:
        print("Invalid input! Please try again.")


# Update student grade
def update_student():
    try:
        student_id = input("Enter Student ID to update: ")

        if student_id not in students:
            raise KeyError("Student ID not found!")

        new_grade = float(input("Enter new grade: "))
        students[student_id]["grade"] = new_grade

        print("Grade updated successfully!\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError:
        print("Grade must be a number!")


# Delete student
def delete_student():
    try:
        student_id = input("Enter Student ID to delete: ")

        if student_id not in students:
            raise KeyError("Student ID not found!")

        del students[student_id]
        print("Student record deleted!\n")

    except KeyError as e:
        print("Error:", e)


# Display students
def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\nStudent Records")
        print("---------------------------")
        for sid, info in students.items():
            print("ID:", sid, "| Name:", info["name"], "| Grade:", info["grade"])
        print()


# Main menu
def main():
    while True:
        print("Student Grade Management System")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                update_student()
            elif choice == 3:
                delete_student()
            elif choice == 4:
                display_students()
            elif choice == 5:
                print("Exiting program...")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Please enter a valid number!\n")


main()
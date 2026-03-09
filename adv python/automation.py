# Simple Automation System

# Dictionary to store automation tasks
tasks = {}


# Function to add a new task
def add_task():
    task_id = input("Enter Task ID: ")
    task_name = input("Enter Task Name: ")
    action = input("Enter Action to Perform: ")

    tasks[task_id] = {
        "task_name": task_name,
        "action": action
    }

    print("Task added successfully!\n")


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for tid, details in tasks.items():
        print("\nTask ID:", tid)
        print("Task Name:", details["task_name"])
        print("Action:", details["action"])


# Function to run a task
def run_task():
    task_id = input("Enter Task ID to run: ")

    if task_id in tasks:
        print("Running Task:", tasks[task_id]["task_name"])
        print("Action Performed:", tasks[task_id]["action"])
        print("Task completed successfully!\n")
    else:
        print("Task not found.\n")


# Function to delete a task
def delete_task():
    task_id = input("Enter Task ID to delete: ")

    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted successfully.\n")
    else:
        print("Task not found.\n")


# Main menu
while True:
    print("\n------ AUTOMATION SYSTEM ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Run Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        run_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Exiting Automation System...")
        break

    else:
        print("Invalid choice\n")
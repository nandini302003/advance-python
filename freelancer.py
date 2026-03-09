freelancers = {}
clients = {}
projects = []

# Register Freelancer
def register_freelancer():
    name = input("Enter freelancer name: ")
    skill = input("Enter skill: ")
    freelancers[name] = {"skill": skill, "earnings": 0}
    print("Freelancer registered successfully!")

# Register Client
def register_client():
    name = input("Enter client name: ")
    clients[name] = {"projects": []}
    print("Client registered successfully!")

# Assign Project
def assign_project():
    client = input("Enter client name: ")
    freelancer = input("Enter freelancer name: ")
    project_name = input("Enter project name: ")
    payment = float(input("Enter payment amount: "))

    if client in clients and freelancer in freelancers:
        project = {
            "project": project_name,
            "client": client,
            "freelancer": freelancer,
            "payment": payment,
            "status": "Assigned"
        }
        projects.append(project)
        clients[client]["projects"].append(project_name)
        print("Project assigned successfully!")
    else:
        print("Client or Freelancer not found.")

# Complete Project and Process Payment
def complete_project():
    project_name = input("Enter project name to complete: ")

    for project in projects:
        if project["project"] == project_name and project["status"] == "Assigned":
            project["status"] = "Completed"
            freelancer = project["freelancer"]
            freelancers[freelancer]["earnings"] += project["payment"]
            print("Project completed and payment processed!")
            return

    print("Project not found.")

# Display Data
def show_data():
    print("\nFreelancers:")
    for f, data in freelancers.items():
        print(f, data)

    print("\nClients:")
    for c, data in clients.items():
        print(c, data)

    print("\nProjects:")
    for p in projects:
        print(p)

# Menu
while True:
    print("\n1.Register Freelancer")
    print("2.Register Client")
    print("3.Assign Project")
    print("4.Complete Project")
    print("5.Show Data")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_freelancer()
    elif choice == "2":
        register_client()
    elif choice == "3":
        assign_project()
    elif choice == "4":
        complete_project()
    elif choice == "5":
        show_data()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
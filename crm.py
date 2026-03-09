# Customer Relationship Manager (CRM)

customers = {}

# Add new customer
def add_customer():
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    customers[customer_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "logs": []
    }
    
    print("Customer added successfully!")

# Add communication log
def add_log():
    customer_id = input("Enter Customer ID: ")
    
    if customer_id in customers:
        log = input("Enter communication note: ")
        customers[customer_id]["logs"].append(log)
        print("Log added.")
    else:
        print("Customer not found.")

# View customer details
def view_customer():
    customer_id = input("Enter Customer ID: ")
    
    if customer_id in customers:
        customer = customers[customer_id]
        
        print("\nCustomer Details")
        print("Name:", customer["name"])
        print("Phone:", customer["phone"])
        print("Email:", customer["email"])
        
        print("\nCommunication Logs:")
        for log in customer["logs"]:
            print("-", log)
            
    else:
        print("Customer not found.")

# View all customers
def view_all():
    if not customers:
        print("No customers available.")
    else:
        print("\nCustomer List")
        for cid, data in customers.items():
            print(cid, "-", data["name"])

# Menu
while True:
    print("\n--- Customer Relationship Manager ---")
    print("1. Add Customer")
    print("2. Add Communication Log")
    print("3. View Customer Details")
    print("4. View All Customers")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_customer()
    elif choice == "2":
        add_log()
    elif choice == "3":
        view_customer()
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Exiting CRM system...")
        break
    else:
        print("Invalid choice")
'''16. Write a program:
 - Simulate login system
 - Use file to store username/password'''

def login_system():
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if f"{username}:{password}" in users:
        print("Login successful!")
    else:
        print("Invalid username or password.")
if __name__ == "__main__":
    login_system()


    # Sample users.txt content:
    # user1:pass1   
    # user2:pass2
    # user3:pass3
    
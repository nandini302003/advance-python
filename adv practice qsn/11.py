'''11. Write a program:
 - Create a class BankAccount
 - Methods: deposit, withdraw, check balance'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
# Example usage
account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.check_balance()


# Output:# Deposited: 100. Current balance: 100
# Withdrew: 30. Current balance: 70
# Current balance: 70   
import time

# Bank accounts database
accounts = {
    "1001": {"name": "Rahul", "balance": 5000},
    "1002": {"name": "Priya", "balance": 7000},
    "1003": {"name": "Amit", "balance": 3000}
}


# Check account
def check_account(acc_no):
    if acc_no not in accounts:
        raise KeyError("Account number not found!")


# Deposit money
def deposit():
    try:
        acc_no = input("Enter account number: ")
        check_account(acc_no)

        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            raise ValueError("Invalid amount!")

        accounts[acc_no]["balance"] += amount
        print("Deposit successful!")
        print("New Balance:", accounts[acc_no]["balance"], "\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


# Withdraw money
def withdraw():
    try:
        acc_no = input("Enter account number: ")
        check_account(acc_no)

        amount = float(input("Enter withdrawal amount: "))

        if amount > accounts[acc_no]["balance"]:
            raise Exception("Overdraft error! Insufficient balance.")

        accounts[acc_no]["balance"] -= amount
        print("Withdrawal successful!")
        print("Remaining Balance:", accounts[acc_no]["balance"], "\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError:
        print("Invalid amount!")
    except Exception as e:
        print("Error:", e)


# Transfer money
def transfer():
    try:
        sender = input("Enter sender account number: ")
        receiver = input("Enter receiver account number: ")

        check_account(sender)
        check_account(receiver)

        amount = float(input("Enter transfer amount: "))

        start_time = time.time()

        # simulate delay
        time.sleep(2)

        if time.time() - start_time > 5:
            raise TimeoutError("Transaction timeout!")

        if amount > accounts[sender]["balance"]:
            raise Exception("Overdraft! Not enough balance.")

        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        print("Transaction successful!")
        print("Sender Balance:", accounts[sender]["balance"], "\n")

    except KeyError as e:
        print("Error:", e)
    except TimeoutError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


# Check balance
def check_balance():
    try:
        acc_no = input("Enter account number: ")
        check_account(acc_no)

        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"], "\n")

    except KeyError as e:
        print("Error:", e)


# Menu
def main():
    while True:
        print("Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer Money")
        print("4. Check Balance")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                transfer()
            elif choice == 4:
                check_balance()
            elif choice == 5:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Enter a valid number!\n")


main()
# Custom Exception Classes

class OutOfStockError(Exception):
    pass


class InvalidProductIDError(Exception):
    pass


class DuplicateProductError(Exception):
    pass


# Inventory database
inventory = {}


# Add Product
def add_product():
    try:
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        stock = int(input("Enter Stock Quantity: "))

        if pid in inventory:
            raise DuplicateProductError("Product ID already exists!")

        inventory[pid] = {"name": name, "stock": stock}

        print("Product added successfully!\n")

    except DuplicateProductError as e:
        print("Error:", e)
    except ValueError:
        print("Stock must be a number!")


# Sell Product
def sell_product():
    try:
        pid = input("Enter Product ID: ")

        if pid not in inventory:
            raise InvalidProductIDError("Invalid Product ID!")

        qty = int(input("Enter quantity to sell: "))

        if qty > inventory[pid]["stock"]:
            raise OutOfStockError("Not enough stock available!")

        inventory[pid]["stock"] -= qty

        print("Product sold successfully!")
        print("Remaining Stock:", inventory[pid]["stock"], "\n")

    except InvalidProductIDError as e:
        print("Error:", e)
    except OutOfStockError as e:
        print("Error:", e)
    except ValueError:
        print("Invalid quantity!")


# View Inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
    else:
        print("\nInventory List")
        print("------------------------")
        for pid, info in inventory.items():
            print("ID:", pid, "| Name:", info["name"], "| Stock:", info["stock"])
        print()


# Main Menu
def main():
    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. View Inventory")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_product()
            elif choice == 2:
                sell_product()
            elif choice == 3:
                view_inventory()
            elif choice == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Please enter a valid number!\n")


main()
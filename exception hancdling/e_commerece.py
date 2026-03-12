# Product inventory
products = {
    "Laptop": {"price": 50000, "stock": 5},
    "Phone": {"price": 20000, "stock": 10},
    "Headphones": {"price": 2000, "stock": 15}
}

# Valid coupons
coupons = {
    "SAVE10": 0.10,
    "SAVE20": 0.20
}

# Valid payment methods
payment_methods = ["UPI", "Card", "Cash"]

orders = {}


# Place Order
def place_order():
    try:
        product = input("Enter product name: ")

        if product not in products:
            raise KeyError("Product not found!")

        if products[product]["stock"] == 0:
            raise Exception("Out of stock!")

        quantity = int(input("Enter quantity: "))

        if quantity > products[product]["stock"]:
            raise Exception("Not enough stock available!")

        coupon = input("Enter coupon code (or press enter): ").strip()

        price = products[product]["price"] * quantity

        if coupon != "":
            if coupon not in coupons:
                raise ValueError("Invalid coupon code!")
            discount = coupons[coupon]
            price = price - (price * discount)

        payment = input("Enter payment method (UPI/Card/Cash): ")

        if payment not in payment_methods:
            raise ValueError("Invalid payment method!")

        order_id = len(orders) + 1

        orders[order_id] = {
            "product": product,
            "quantity": quantity,
            "amount": price
        }

        products[product]["stock"] -= quantity

        print("Order placed successfully!")
        print("Order ID:", order_id)
        print("Total Amount:", price, "\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


# Return Order
def return_order():
    try:
        order_id = int(input("Enter Order ID to return: "))

        if order_id not in orders:
            raise KeyError("Order not found!")

        product = orders[order_id]["product"]
        quantity = orders[order_id]["quantity"]

        products[product]["stock"] += quantity

        print("Order returned successfully!")
        refund(order_id)

    except KeyError as e:
        print("Error:", e)
    except ValueError:
        print("Invalid Order ID!")


# Refund Process
def refund(order_id):
    amount = orders[order_id]["amount"]
    print("Refund of", amount, "processed.\n")
    del orders[order_id]


# View Products
def view_products():
    print("\nAvailable Products")
    print("----------------------")
    for p, info in products.items():
        print(p, "| Price:", info["price"], "| Stock:", info["stock"])
    print()


# Main Menu
def main():
    while True:
        print("E-Commerce Order System")
        print("1. View Products")
        print("2. Place Order")
        print("3. Return Order")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                view_products()
            elif choice == 2:
                place_order()
            elif choice == 3:
                return_order()
            elif choice == 4:
                print("Thank you!")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Enter a valid number!\n")


main()
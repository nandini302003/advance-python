menu = {
    "pizza": 200,
    "burger": 100,
    "pasta": 150,
    "coffee": 80
}

cart = {}
total = 0

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(item, ":", price)

    choice = input("Enter item to order (or 'done'): ").lower()

    if choice == "done":
        break

    if choice in menu:
        qty = int(input("Enter quantity: "))
        cart[choice] = cart.get(choice, 0) + qty
    else:
        print("Item not available")

# Bill calculation
print("\n--- BILL ---")
for item, qty in cart.items():
    cost = menu[item] * qty
    total += cost
    print(item, "x", qty, "=", cost)

tax = total * 0.05
grand_total = total + tax

print("Subtotal:", total)
print("Tax (5%):", tax)
print("Total Bill:", grand_total)
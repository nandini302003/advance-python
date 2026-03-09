# Billing System for Retail Store

products = {
    "101": {"name": "Rice", "price": 50},
    "102": {"name": "Oil", "price": 120},
    "103": {"name": "Soap", "price": 30},
    "104": {"name": "Shampoo", "price": 90}
}

cart = []
total = 0

print("---- Welcome to Retail Store Billing System ----")

while True:
    code = input("Enter product code (or '0' to finish): ")
    
    if code == "0":
        break
    
    if code in products:
        quantity = int(input("Enter quantity: "))
        item_total = products[code]["price"] * quantity
        total += item_total
        
        cart.append({
            "name": products[code]["name"],
            "price": products[code]["price"],
            "quantity": quantity,
            "total": item_total
        })
        
        print("Item added successfully!\n")
    else:
        print("Invalid product code!\n")

# Apply discount
discount = 0
if total > 500:
    discount = total * 0.10   # 10% discount
    total -= discount

# Generate Bill
print("\n--------- BILL ---------")
for item in cart:
    print(f"{item['name']} x {item['quantity']} = {item['total']}")

print("------------------------")
print(f"Discount: {discount}")
print(f"Final Amount: {total}")
print("------------------------")

# Record transaction in file
with open("transactions.txt", "a") as file:
    file.write(f"Total: {total}, Discount: {discount}\n")

print("Transaction recorded successfully!")
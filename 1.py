# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Operations
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible (division by zero)")

# Even/Odd check
print("a is Even" if a % 2 == 0 else "a is Odd")
print("b is Even" if b % 2 == 0 else "b is Odd")

# Convert to float
a_float = float(a)
b_float = float(b)
print("Float value of a:", a_float)
print("Float value of b:", b_float)
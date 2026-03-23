def power(base, exp):
    result = 1

    for _ in range(abs(exp)):
        result *= base

    if exp < 0:
        return 1 / result
    return result

# Example
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print("Result:", power(b, e))

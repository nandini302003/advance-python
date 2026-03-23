t = (1, "hello", 3.5, 7, "world", 10)

# Filter numeric values
nums = tuple(x for x in t if isinstance(x, (int, float)))
print("Numeric values:", nums)

# Attempt modification
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

# Concatenate tuples
t2 = ("new", 99)
combined = t + t2
print("Concatenated tuple:", combined)

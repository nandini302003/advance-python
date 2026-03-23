t = (5, "hello", 15, 3.5, 20, 8, "world")

# Convert to list
lst = list(t)

# Remove integers < 10
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]

# Convert back to tuple
new_tuple = tuple(lst)

print("Updated tuple:", new_tuple)

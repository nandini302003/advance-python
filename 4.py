marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Add
marks["David"] = 88

# Update
marks["Alice"] = 95

# Delete
del marks["Charlie"]

# Display
print("Keys:", marks.keys())
print("Values:", marks.values())
print("Items:", marks.items())
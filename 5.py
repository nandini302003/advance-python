words = ["level", "hello world", "madam", "python code", "radar"]

# Sort by length
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)

# Palindromes
palindromes = [w for w in words if w.replace(" ", "") == w.replace(" ", "")[::-1]]
print("Palindromes:", palindromes)

# Replace spaces with hyphens
hyphen_words = [w.replace(" ", "-") for w in words]
print("Hyphen replaced:", hyphen_words)
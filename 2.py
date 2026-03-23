sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

# Reverse
print("Reversed:", sentence[::-1])

# Replace spaces
print("With underscores:", sentence.replace(" ", "_"))

# Capitalize words
print("Capitalized:", sentence.title())

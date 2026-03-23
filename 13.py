import string

sentence = input("Enter sentence: ").lower()

# Remove spaces and punctuation
cleaned = ""
for ch in sentence:
    if ch.isalnum():
        cleaned += ch

unique_chars = []

for ch in cleaned:
    if cleaned.count(ch) == 1:
        unique_chars.append(ch)

print("Unique characters:", unique_chars)
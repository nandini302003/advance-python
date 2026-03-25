#4. Count vowels

s = "hello world"
count = sum(1 for ch in s.lower() if ch in "aeiou")
print(count)
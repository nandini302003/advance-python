#3. Reverse a string (without slicing)

s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
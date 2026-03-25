#18. First non-repeating character
s = "aabbcde"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
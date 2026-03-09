# 10. Function to find length of a string without using len()
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
#16. Rotate list by k
lst = [1, 2, 3, 4, 5]
k = 2
k = k % len(lst)
print(lst[-k:] + lst[:-k])
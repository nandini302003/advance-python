#19. Flatten nested list

lst = [[1, 2], [3, 4], [5]]
flat = [item for sub in lst for item in sub]
print(flat)
# 9. Function to remove duplicates from a list while keeping order
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
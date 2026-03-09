# 5. Function to find the largest number in a list
def largest_number(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
'''Write a program:
 - Accept list of numbers
 - Remove duplicates '''

def remove_duplicates(lst):
    return list(set(lst))
numbers = input("Enter a list of numbers separated by spaces: ").split()
unique_numbers = remove_duplicates(numbers)
print("List of unique numbers:", unique_numbers)

# Output:
# Enter a list of numbers separated by spaces: 1 2 3 4  2 3 4 5
# List of unique numbers: ['1', '2', '3', '4', '5']     
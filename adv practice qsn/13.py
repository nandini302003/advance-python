'''13. Write a program using lambda + map + filter:
 - Square only even numbers from a list of numbers form a list.'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_evens = list(map(lambda x: x ** 2, even_numbers))
print("Squared even numbers:", squared_evens)

# Output: Squared even numbers: [4, 16, 36, 64, 100]

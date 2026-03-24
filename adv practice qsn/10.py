'''10. Write a program to:
 - Read a file
 - Count number of lines, words and characters'''

file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_characters = sum(len(line) for line in lines)

    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


## Sample Output:# Enter the file name: sample.txt
# Number of lines: 5    
# Number of words: 20
# Number of characters: 100

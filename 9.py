"""Write a program to:
 - Take input string
 - Count vowels and consonants"""

def count_vowels_consonants(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example usage:
input_str = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_str)
print(f"Vowels: {vowels}, Consonants: {consonants}")

#output:
# Enter a string: Hello World   
# Vowels: 3, Consonants: 7
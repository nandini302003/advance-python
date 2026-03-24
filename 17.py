'''17. Exception Handling:
 - Create custom exception "InvalidAgeError"
 - Raise error if age < '''

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be 0 or above.")

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"Valid age: {age}")

# Example usage
try:  
    check_age(-5)
except InvalidAgeError as e:
    print(e)
try:
    check_age(25)
except InvalidAgeError as e:
    print(e)


# Output:# Invalid age: -5. Age must be 0 or above.
# Valid age: 25             

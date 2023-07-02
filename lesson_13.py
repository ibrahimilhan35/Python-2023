#%%
"""
Homework-13
Session 16 Homework: Exception & pytest

Exception Handling:
- Write a Python function that takes two integer inputs from the user and calculates their division. Handle the ZeroDivisionError and prompt the user to re-enter the second number if it is zero.
"""

def division():
    x = int(input("Enter the dividend number: "))
    y = int(input("Enter the divisor number: "))

    try:
        z = x / y
        return z

    except ZeroDivisionError as ex:
        print("Exception occurred:", ex)
        print("Please enter a valid non-zero divisor.")
        return division()

# Test the function
result = division()
print("Result:", result)


#%%
"""
- Use a custom exception called InvalidInputError to handle cases where the user inputs non-integer values.

- Test your function with different inputs, including valid and invalid values, and ensure that the exceptions are raised and handled correctly.
"""

class InvalidInputError(Exception):
    pass

def division():
    try:
        x = int(input("Enter the dividend number: "))
        y = int(input("Enter the divisor number: "))

        z = x / y
        return z

    except ValueError:
        raise InvalidInputError("Invalid input. Please enter integers only.")
    

    except ZeroDivisionError:
        print("Exception occurred: Division by zero is not allowed.")
        print("Please enter a valid non-zero divisor.")
        return division()

# Test the function
try:
    result = division()
    print("Result:", result)
except InvalidInputError as ex:
    print("InvalidInputError occurred:", ex)


#%%
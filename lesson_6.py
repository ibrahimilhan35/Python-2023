# %%
"""
Task 1.
Python script calculate_price takes quantity and price as arguments, applies 10 percent discount, then returns the discounted price.
"""


# GLOBAL scope
# quantity and price are global scope variables because they are passed as
# arguments to the calculate_price function
def calculate_price(quantity, price):
    total_price = quantity * price  # Enclosing scope variable
    discount = 0.1  # Enclosing scope variable

    # LOCAL scope
    # When a nested function accesses a variable, it first checks the
    # local scope, then the enclosing scope, and finally the global scope
    def apply_discount(price):
        price *= 1 - discount  # LOCAL scope variable
        return price

    result = apply_discount(total_price)
    print(result)


# Test the function
calculate_price(quantity=5, price=10)


# %%
"""
Task 2.
Write a Python decorator called timeit that measures the execution time of a function and prints it to the console. The decorator should accept the function as its argument and return a new function that wraps the original function.
"""

import time


# Timeit decorator function
def timeit(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()

        execution_time = end_time - start_time

        print("The execution time:", execution_time)

    return wrapper


@timeit
def label():
    print("Hey there!")


# Test the function
label()


# %%
"""
Task 2. Solution without using decorator function
"""
import time


def label():
    print("Hey there!")


def timeit():
    start_time = time.time()

    label()

    end_time = time.time()

    execution_time = end_time - start_time

    print("The execution time:", execution_time)


# Test the function
timeit()


# %%
"""
Task 3.
Python script calculates the sum of all even numbers in a given list of integers. Returns the sum of all even numbers in the list, or 0 if there are no even numbers. Raises TypeError: If the input is not a list or if any element of the list is not an integer.
"""


def sum_even_numbers(numbers):
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    even_sum = 0
    for num in numbers:
        # Check if the number is an integer
        if not isinstance(num, int):
            raise TypeError("List must contain only integers.")

        # Check if the number is even
        if num % 2 != 0:
            even_sum += num

    return even_sum


# Test the function
num_list = [4, 6, 31, 69, 101, -1, 6.7]
result = sum_even_numbers(num_list)
print("Sum of even numbers:", result)


# %%

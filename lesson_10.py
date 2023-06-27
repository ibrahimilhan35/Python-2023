# %%
"""
1. Write a Python program that reads a text file called "input.txt" and counts the occurrences of each word in the file. Print the word and its count. Ignore case sensitivity (treat "Hello" and "hello" as the same word).
"""
file_name = "geophysico.txt"
with open(file_name, "w") as file:
    file.write(
        "GEOPHYSICO specializes in cutting-edge imaging techniques for mapping stratigraphy and underlying geologic features. Our imaging methods provide indirect measurements of the earth's physical properties, including acoustic velocities, elastic moduli, density, magnetic susceptibilities, electrical conductivities, and dielectric constants, depending on the geophysical technology used. Our professionals gather, analyze, and interpret data from a variety of sources, including seismic, electrical resistivity, ground penetrating radar, gravity, magnetic, electromagnetic, multi-beam bathymetric, side-scan sonar, and sub-bottom profiler data. This information is then integrated to offer clients project-specific, multidisciplinary, and data-driven integrated solutions."
    )

with open(file_name, "r") as file:
    content = file.read()

from collections import Counter


def count_words():
    words = content.lower().split()
    word_count = Counter(words)
    print(word_count)


count_words()


# %%
"""
2. Write a Python lambda function that takes two parameters a and b, and returns the sum of their squares. Assign the lambda function to a variable called sum_of_squares. Test the lambda function by passing different values for a and b.
"""
sum_of_squares = lambda a, b: a**2 + b**2

sum_of_squares(3, 3)


# %%
"""
3. Write a Python function called calculate_average that accepts a variable number of arguments (numbers) and returns the average of those numbers. Test the function with different sets of numbers.
"""

def calculate_evarage(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 1)


calculate_evarage(0, 1, 2, 3, 7, 10)


#%%
def calculate_evarage(*numbers):
    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    return round(average, 1)


calculate_evarage(0, 1, 2, 3, 7, 10)


# %%

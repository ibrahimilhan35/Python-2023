"""
Please use the input() function to get input for the following tasks

*** Hint ***
For some tasks you will need to use indexing, slicing 
and/or looping (looping through strings is 
the same as looping through lists)

| R | E | D | I |
| 0 | 1 | 2 | 3 | - indexing option #1
| -4 | -3 | -2 | -1 | - indexing option #2
"""
# %%
"""
1. Python script to calculate the length of a string
Example input: "ReDi"
Example output: 4
"""


def string_length(string):
    length = len(string)
    return length


# Prompt the user for input and call the function
string = input("Type in a word or make a statement: ")
print("Length of the string is:", string_length(string))


# %%
# 1. Optional


def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count


# Prompt the user for input and call the function
string = input("Type in a word or make a statement: ")
print("Length of the string is:", string_length(string))


# %%
"""
2. Python script that takes a string and prints it 3 times

Example input: "Hip hip hooray!"
Example output: "Hip hip hooray!Hip hip hooray!Hip hip hooray!"
"""


def repeat_string(string, n):
    repeated_string = string * n
    return repeated_string


# Prompt the user for input and call the function
string = input("Type in a word or make a statement: ")
print(repeat_string(string, 3))


# %%
"""
3. Python script that takes two strings, compares them and prints the result of the comparison

Example input: str1 - "ReDi", str2 - "Ready"
Example output: "Is ReDi equal to Ready? Result: False"
"""


def string_comparison(str1, str2):
    if str1 == str2:
        print(f"Is {str1} equal to {str2}? Result: True")
    else:
        print(f"Is {str1} equal to {str2}? Result: False")


# Prompt the user for inputs and call the function
str1 = input("Enter a word: ")
str2 = input("Enter another word: ")
string_comparison(str1, str2)


# %%
"""
4. Python script that takes a string and prints the longest word of the string and its length

Example input: "Too cool for school"
Example output: "school - 6"
"""


def find_longest_word(string):
    # Split string into words
    words = string.split()
    # Use max() function to find longest word
    longest_word = max(words, key=len)
    # Print longest word and its length
    print(f"{longest_word} - {len(longest_word)}")


# Prompt the user for input and call the function
string = input("Enter a phrase: ")
find_longest_word(string)

# %%
# 4. Optional


def find_longest_word():
    # Split string into words
    words = string.split()
    # Empty string
    longest_word = ""

    # Loop through words (list) and compare the length
    # of each word with the longest_word
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print(longest_word, "-", len(longest_word))
    # print(type(words))
    # print(words)


# Prompt the user for input and call the function
string = input("Drop a truth bomb")
find_longest_word()


# %%
"""
5. Python script that replaces the word "bad" 
with the word "good" and removes the word 'not' in a string

Example input: "Ice bear is a bad developer. He should not code"
Example output: "Ice bear is a good developer. He should code"
"""


def word_replacer(string):
    # Replace "bad" with "good" and remove "not"
    new_string = string.replace("bad", "good").replace("not ", "")
    print(string)
    print(new_string)


# Prompt the user for input and call the function
string = "Mojoe is a bad developer. He should not code!"
word_replacer(string)


# %%
# 5. Optional - using regular expressions (re) module
import re

string = "Mojoe is a bad developer. He should not code!"
new_string = re.sub(r"\bbad\b", "good", string)
new_string = re.sub(r"\bnot \b", "", new_string)

print(string)
print(new_string)


# %%
"""
Optional:
6. Python script that uppercases the latter half of a string

Example input: "foobar"
Example output: "fooBAR"
"""

import math


def word_uppercaser():
    mid = math.ceil(len(original_word) / 2)
    first_half = original_word[:mid]
    second_half = original_word[mid:].upper()

    print(first_half + second_half)


original_word = "sporkle"
word_uppercaser()


# %%
"""
7. Python script that prints the number of times the letter "a" is present in your full name

Example input: "Panda"
Example output: 2
"""


def find_repeated_a():
    count_a = 0
    for name in names:
        for char in name:
            if char == "a":
                count_a += 1
    return count_a


# Prompt the user for input and call the function
name = input("Write your name: ")
names = name.split()

# Call the function and print the result
count = find_repeated_a()
print(count)


# %%
"""
8. Python script that capitalizes the first and last character of each word in a string

Example input: "an elephant in the room"
Example output: "AN ElephanT IN ThE RooM"
"""


def capitalize_first_last_char():
    words = string.split()
    result = []

    for word in words:
        if len(word) > 1:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            new_word = word.upper()

        result.append(new_word)

    return " ".join(result)


# Prompt the user for input and call the function
string = input("Drop a truth bomb")
capitalize_first_last_char()


# %%
"""
9. Python script removes spaces at the beginning 
and end of user entered passwords, and checks 
if it is >= 8 charaacter long, and includes 
at least one uppercase and lowercase letters, 
and a number. Otherwise, promps messages accordingly.

Example input: "AbcD1234"
Example output: "Well, well, Well! Hello!"
"""
import re


def password_checker():
    # Remove spaces from the beginning and at the end of user password
    cleaned_password = user_password.strip()
    print(cleaned_password)

    if len(cleaned_password) < 8:
        print("The password must be at least eight characters long")

    # Check for an uppercase letter in password
    uppercase_list = []
    for char in cleaned_password:
        if char.isupper() is True:
            uppercase_list.append(char)

    if len(uppercase_list) == 0:
        print("The password must contain at least one uppercase letter")

    # Check for a lowercase letter in password
    lowercase_list = []
    for char in cleaned_password:
        if char.islower() is True:
            lowercase_list.append(char)

    if len(lowercase_list) == 0:
        print("The password must contain at least one lowercase letter")

    # Check for a number in password
    digit_list = []
    for char in cleaned_password:
        if char.isdigit() is True:
            digit_list.append(char)

    if len(digit_list) == 0:
        print("The password must contain at least one number")

    else:
        print("Welcome to Geophysico.com")


# Prompt the user for input and call the function
user_password = input("Enter your password")
password_checker()


# %%
# 9. Optional
import re


def password_checker():
    # Remove spaces from the beginning and at the end of user password
    cleaned_password = user_password.strip()
    print(cleaned_password)

    if len(cleaned_password) < 8:
        print("The password must be at least eight characters long")

    # Check for an uppercase letter in password
    if not re.search(r"[A-Z]", cleaned_password):
        print("The password must contain at least one uppercase letter")

    # Check for a lowercase letter in password
    if not re.search(r"[a-z]", cleaned_password):
        print("The password must contain at least one lowercase letter")

    # Check for a number in password
    if not re.search(r"\d", cleaned_password):
        print("The password must contain at least one number")

    if (
        len(cleaned_password) >= 8
        and re.search(r"[A-Z]", cleaned_password)
        and re.search(r"[a-z]", cleaned_password)
        and re.search(r"\d", cleaned_password)
    ):
        print("Welcome to Geophysico.com")


# Prompt the user for input and call the function
user_password = input("Enter your password: ")
password_checker()

# %%

# %%
"""
Solution 1.
Python script counts the occurrences of the word "ReDI" 
in the phrase: “ReDI school is awesome! Yes ReDI is really cool".
"""


def count_ReDI(string):
    words = string.split()
    count = 0
    for word in words:
        if word == "ReDI":
            count += 1
    return count


str1 = "ReDI school is awesome! Yes ReDI is really cool"
count_ReDI(str1)


# %%
"""
Solution 2.
Using list comprehension and the count() method:
"""


def count_ReDI(string):
    words = string.split()
    count = [word for word in words if word == "ReDI"]
    return len(count)


str1 = "ReDI school is awesome! Yes ReDI is really cool"
count_ReDI(str1)


# %%
"""
Solution 3.
Utilizing the collections.Counter class:
"""
from collections import Counter


def count_ReDI(string):
    words = string.split()
    word_counts = Counter(words)
    return word_counts["ReDI"]


str1 = "ReDI school is awesome! Yes ReDI is really cool"
count_ReDI(str1)


# %%
"""
Solution 4.
Employing regular expressions (re module):
"""
import re


def count_ReDI(string):
    count = len(re.findall(r"\bReDI\b", string))
    return count


str1 = "ReDI school is awesome! Yes ReDI is really cool"
count_ReDI(str1)


# %%

#%%
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # Output: True
print(x is z)  # Output: False


#%%
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True


#%%
"""
try:
    # Code that may raise an exception
    # ...
except ExceptionType1:
    # Code to handle ExceptionType1
    # ...
except ExceptionType2:
    # Code to handle ExceptionType2
    # ...
else:
    # Optional code to run if no exceptions occur
    # ...
finally:
    # Optional code that always runs, regardless of exceptions
    # ...
"""

#%%
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def my_function():
    print("Inside the function")

my_function()


#%%
"""
Question: Given an array of integers, find the maximum sum of a contiguous subarray (a subarray with consecutive elements) within the array.

For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray with the maximum sum is [4, -1, 2, 1], and the maximum sum is 6.

Can you write an algorithm to solve this problem efficiently?

Take your time and let me know when you're ready to discuss the solution or if you'd like any hints.
"""

def max_subarray_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0
    
    for num in nums:
        # Calculate the running sum by adding the current element to the sum so far
        current_sum += num
        
        # If the current element itself is greater than the running sum, start a new subarray
        # Otherwise, update the maximum sum if the running sum is greater
        current_sum = max(num, current_sum)
        
        # Update the overall maximum sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(nums)
print(max_sum)  # Output: 6


# %%
"""
Question: Given a string, determine if it is a palindrome or not. A palindrome is a string that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

For example, the strings "level", "radar", and "A man, a plan, a canal: Panama" are all palindromes.

Write a function in Python to check if a given string is a palindrome or not. The function should return True if it is a palindrome and False otherwise.

Take your time to think about the approach, and let me know when you're ready to discuss the solution or if you'd like any hints.
"""

import string

def find_palindrome(string_sample):
    words = string_sample.lower().split()
    translator = str.maketrans("", "", string.punctuation)
    palindrome_list = []

    for word in words:
        clean_word = word.translate(translator)
        reverse_word = clean_word[::-1]
        if reverse_word == clean_word:
            palindrome_list.append(clean_word)
    
    return palindrome_list

string_sample = "level, radar, and A man, a plan, a canal: Panama are all palindromes."
palindromes = find_palindrome(string_sample)
print(palindromes)  # Output: ['level', 'radar', 'amanaplanacanalpanama']


#%%
"""
Question: Given an array of integers, find two numbers such that they add up to a specific target value. You need to return the indices of the two numbers in the array.

For example, given the array [2, 7, 11, 15] and a target value of 9, the function should return [0, 1] because 2 + 7 equals 9.

Write a function in Python to solve this problem efficiently.
"""

def find_target_sum(num_list, target_sum):
    for i in range(0, len(num_list)):
        for j in range(i+1, len(num_list)):
            sum = num_list[i] + num_list[j]
            if sum == target_sum:
                return i, j

num_list = [4, 7, 11, -3]
target_sum = 8

result = find_target_sum(num_list, target_sum)
print(result)  # Output: (0, 1)


#%%
def find_target_sum(num_list, target_sum):
    target_sum_list = []
    for i in range(0, len(num_list)):
        for j in range(i+1, len(num_list)):
            sum = num_list[i] + num_list[j]
            if sum == target_sum:
                target_sum_list.append((i, j))

    return target_sum_list

num_list = [2, 7, 11, 15, -2]
target_sum = 9

result = find_target_sum(num_list, target_sum)
print(result)  # Output: (0, 1)


#%%
"""
Question: You are given a string consisting of parentheses, brackets, and curly braces. Write a function in Python to determine if the input string is valid. A string is considered valid if all the opening brackets/parentheses/braces are closed in the correct order.

For example, the string "{[()()]}" is valid, but "([)]" is not valid.

Write a function that takes a string as input and returns True if the string is valid, and False otherwise.

Take your time to think about the approach, and let me know when you're ready to discuss the solution or if you'd like any hints.
"""

"""
In this implementation, you use a stack to keep track of the opening symbols encountered. Whenever a closing symbol is encountered, you compare it with the last symbol on the stack to check for a matching pair. If the pair is valid, you pop the opening symbol from the stack. If the stack is empty at the end, it means all opening symbols have been closed, and the string is considered valid.
"""

def is_valid_string(s):
    stack = []  # Empty stack to store opening symbols

    # Define the matching pairs of opening and closing symbols
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)  # Opening symbol, push onto the stack
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False  # Invalid closing symbol or unbalanced
        else:
            continue  # Ignore other characters in the string

    return len(stack) == 0  # Check if the stack is empty at the end

# Test cases
print(is_valid_string("{[()()]}"))  # Output: True
print(is_valid_string("([)]"))  # Output: False


#%%
from collections import deque

def is_valid_string(s):
    queue = deque()  # Empty queue to store opening symbols

    # Define the matching pairs of opening and closing symbols
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in s:
        if char in pairs.values():
            queue.append(char)  # Opening symbol, enqueue it
        elif char in pairs.keys():
            if not queue or queue.popleft() != pairs[char]:
                return False  # Invalid closing symbol or unbalanced
        else:
            continue  # Ignore other characters in the string

    return len(queue) == 0  # Check if the queue is empty at the end

# Test cases
print(is_valid_string("{[()()]}"))  # Output: True
print(is_valid_string("([)]"))  # Output: False


#%%
"""
Question: Given a sorted array of integers, write a function in Python to search for a target value in the array. If the target is found, return its index; otherwise, return -1.

You can assume that the array is sorted in ascending order and that it does not contain any duplicate elements.
"""
"""
The idea of dividing the list into two halves and comparing the middle element with the target value is a common strategy for efficiently searching in a sorted array. This approach is known as "Binary Search."
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found

# Test cases
arr = [0, 2, 3, 6, 9, 10, 11, 13, 14, 15, 17, 22, 25, 36, 27, 29, 31, 33, 37, 40, 59, 61]
target = 17
print(binary_search(arr, target))  # Output: 3 (index of the target value)


#%%
"""
Question: Given an array of integers, write a function in Python to find the longest increasing subarray within the array. A subarray is defined as a contiguous portion of the original array, and an increasing subarray is one where the elements are in strictly increasing order.

For example, given the array [1, 3, 2, 4, 5, 7, 6, 8], the longest increasing subarray is [2, 4, 5, 7], with a length of 4.
"""
def get_longest_increasing_subarray(arr):
    longest_subarray = []
    current_subarray = [arr[0]]  # Start with the first element as the current subarray

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_subarray.append(arr[i])  # Extend the current subarray
        else:
            if len(current_subarray) > len(longest_subarray):
                longest_subarray = current_subarray  # Update the longest subarray if needed
            current_subarray = [arr[i]]  # Start a new current subarray

    # Check if the last current subarray is the longest
    if len(current_subarray) > len(longest_subarray):
        longest_subarray = current_subarray

    return longest_subarray

# Test case
arr = [0, 2, 1, 6, 9, 10, 4, 13, 14, 15, 17, 11, 25, 36, 27, 29, 31, 33, 37, 5, 59, 61]
result = get_longest_increasing_subarray(arr)
print(result)  # Output: [4, 13, 14, 15, 17, 11, 25, 36, 27, 29, 31, 33, 37, 5, 59, 61]


#%%
def get_longest_increasing_subarrays(arr):
    longest_subarrays = []
    current_subarray = [arr[0]]  # Start with the first element as the current subarray

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_subarray.append(arr[i])  # Extend the current subarray
        else:
            if len(current_subarray) > len(longest_subarrays[-1]):
                longest_subarrays = [current_subarray]  # Update the list of longest subarrays
            elif len(current_subarray) == len(longest_subarrays[-1]):
                longest_subarrays.append(current_subarray)  # Add the subarray to the list of longest subarrays
            current_subarray = [arr[i]]  # Start a new current subarray

    # Check if the last current subarray is the longest
    if len(current_subarray) > len(longest_subarrays[-1]):
        longest_subarrays = [current_subarray]
    elif len(current_subarray) == len(longest_subarrays[-1]):
        longest_subarrays.append(current_subarray)

    return longest_subarrays

# Test case
arr = [0, 2, 1, 6, 9, 10, 4, 13, 14, 15, 17, 11, 25, 36, 27, 29, 31, 33, 37, 5, 59, 61]
result = get_longest_increasing_subarrays(arr)
print(result)  # Output: [[4, 13, 14, 15, 17], [11, 25, 36, 27, 29, 31, 33, 37], [5, 59, 61]]


#%%
def get_longest_increasing_subarray(arr, target_length):
    longest_subarray = []
    current_subarray = []

    for num in arr:
        if not current_subarray or num > current_subarray[-1]:
            current_subarray.append(num)
            if len(current_subarray) == target_length:
                longest_subarray = current_subarray
        else:
            current_subarray = [num]

    return longest_subarray

# Test case
arr = [0, 2, 1, 6, 9, 10, 4, 13, 14, 15, 17, 11, 25, 36, 27, 29, 31, 33, 37, 5, 59, 61]
target_length = 5
result = get_longest_increasing_subarray(arr, target_length)
print(result)  # Output: [13, 14, 15, 17, 11]


#%%
"""
Question: You are given a list of integers representing the daily prices of a stock. Write a function in Python to find the maximum profit that can be achieved by buying and selling the stock. You may complete as many transactions as you like (i.e., buy one share and sell it on the same day), but you must sell the stock before buying again.

For example, given the list of prices [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 7, by buying on day 2 (price = 1) and selling on day 5 (price = 6).

Write a function that takes the list of prices as input and returns the maximum profit.
"""

def max_profit(prices):
    total_profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    
    return total_profit

# Test case
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print(profit)  # Output: 7


#%%
"""
Scenario: You are given a list of daily prices of a stock over a period of time. You want to maximize your profit by buying and selling the stock, but with some additional constraints:

You can only perform a maximum of k transactions (buying and selling) during the given period. You must sell any stocks you hold before making a new purchase. Each transaction incurs a transaction fee of a fixed amount. Write a function in Python to determine the maximum profit that can be achieved under these constraints. The function should take the following inputs:

prices: A list of daily stock prices. 
transaction_fee: The fixed transaction fee for each transaction. 
max_transactions: The maximum number of transactions allowed. 

The function should return the maximum profit that can be achieved considering the given constraints.
"""
prices = [3, 2, 8, 4, 10, 5, 9, 6]
transaction_fee = 2
max_transactions = 2

"""
Initialize two dynamic programming arrays: hold and cash. Both arrays will have a length of max_transactions + 1 to account for the maximum number of transactions allowed.

The hold array will store the maximum profit we can achieve while holding the stock at each transaction. The cash array will store the maximum profit we can achieve while having cash (not holding the stock) at each transaction.

Iterate over the prices starting from the second day and fill in the hold and cash arrays based on the previous values and current prices.

At each iteration, update the hold and cash arrays by taking the maximum value of either:
Continuing to hold the stock and subtracting the current price plus the transaction fee from the previous cash value.

Selling the stock and adding the current price to the previous hold value.

The final result will be in the last element of the cash array, representing the maximum profit achieved while having cash (not holding the stock) after all transactions.
"""
#%%
def max_profit_with_transaction(prices, transaction_fee, max_transactions):
    n = len(prices)
    
    # Initialize the hold and cash arrays
    hold = [-float('inf')] * (max_transactions + 1)
    cash = [0] * (max_transactions + 1)
    
    # Iterate over the prices and fill in the hold and cash arrays
    for i in range(1, n):
        for j in range(1, max_transactions + 1):
            # Update the hold and cash values
            hold[j] = max(hold[j], cash[j - 1] - prices[i] - transaction_fee)
            cash[j] = max(cash[j], hold[j] + prices[i])
    
    return cash[max_transactions]

# Example inputs
prices = [3, 2, 8, 4, 10, 5, 9, 6]
transaction_fee = 2
max_transactions = 2

# Call the function and print the result
result = max_profit_with_transaction(prices, transaction_fee, max_transactions)
print(result)  # Output: 7


#%%
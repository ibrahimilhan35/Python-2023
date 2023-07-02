#%%
"""
Pytest:
- Write a simple Python function that takes two numbers as inputs and returns their sum.

- Write a pytest function to test this function and verify that it returns the correct sum for different input values.
"""

def sum_two_numbers(x, y):
    return x + y

import pytest

def test_sum_two_numbers():
    # Test case 1
    assert sum_two_numbers(2, 3) == 5

    # Test case 2
    assert sum_two_numbers(-1, 1) == 0

    # Test case 3
    assert sum_two_numbers(1, 0) == 0

    # Test case 4
    assert sum_two_numbers(10, -5) == 5

    # Add more test cases if needed

# Run the pytest function
pytest.main()

#%%
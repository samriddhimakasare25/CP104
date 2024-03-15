"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports

# Constants

# test_functions.py
from functions import range_addition

# Test 1
result1 = range_addition(1, 2, 20)
print("Test 1: range_addition(1, 2, 20) ->", result1)
# Expected output: 400

# Test 2
result2 = range_addition(5, 10, 5)
print("Test 2: range_addition(5, 10, 5) ->", result2)
# Expected output: 175

# Test 3
result3 = range_addition(0, 3, 10)
print("Test 3: range_addition(0, 3, 10) ->", result3)
# Expected output: 135

# Additional tests can be added if needed
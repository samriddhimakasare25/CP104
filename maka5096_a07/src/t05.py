"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports

# Constants

# main.py
from functions import verify_sorted

# Test case 1: Sorted list
numbers1 = [1, 2, 3, 4, 5]
in_order, index = verify_sorted(numbers1)
print(f"Test Case 1: {in_order}, {index}")

# Test case 2: Unsorted list
numbers2 = [5, 3, 1, 4, 2]
in_order, index = verify_sorted(numbers2)
print(f"Test Case 2: {in_order}, {index}")

# Test case 3: Partially sorted list
numbers3 = [1, 2, 4, 3, 5]
in_order, index = verify_sorted(numbers3)
print(f"Test Case 3: {in_order}, {index}")

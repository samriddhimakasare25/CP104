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
from functions import get_indexes

numbers_1 = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]
target_number_1 = 3
result_1 = get_indexes(numbers_1, target_number_1)
print(f"Indexes of {target_number_1} in {numbers_1}: {result_1}")

# Example 2
numbers_2 = [10, 20, 30, 40, 50]
target_number_2 = 60
result_2 = get_indexes(numbers_2, target_number_2)
print(f"Indexes of {target_number_2} in {numbers_2}: {result_2}")

# Example 3
numbers_3 = [5, 5, 5, 5, 5]
target_number_3 = 5
result_3 = get_indexes(numbers_3, target_number_3)
print(f"Indexes of {target_number_3} in {numbers_3}: {result_3}")
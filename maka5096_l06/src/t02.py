"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-23"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import sum_odd

num = int(input("Enter an integer greater than 0: "))
total = sum_odd(num)
print(f"The sum of all odd numbers from 1 to {num} is {total}")
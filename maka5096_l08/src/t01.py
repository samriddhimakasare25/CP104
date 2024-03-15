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

# t01.py

from functions import get_weekday_name

# Test the function using a for loop
for i in range(1, 8):
    name = get_weekday_name(i)
    print(f"Day {i} is {name}")


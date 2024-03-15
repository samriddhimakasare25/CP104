"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import day_name
day_num = int(input("Enter a day number (1-7): "))
result = day_name(day_num)
print(f"day_name({day_num}) -> {result}")

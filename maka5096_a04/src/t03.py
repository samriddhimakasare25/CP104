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
from functions import largest_average

val1 = float(input("Enter the first value: "))
val2 = float(input("Enter the second value: "))
val3 = float(input("Enter the third value: "))

average = largest_average(val1, val2, val3)
print(f"The average of the two largest values is: {average:.2f}")

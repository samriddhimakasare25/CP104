"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import roman_numeral

# Input a number to convert to a Roman numeral
n = int(input("Enter a number between 1 and 10: "))

# Call the roman_numeral function and print the result
numeral = roman_numeral(n)

if numeral is not None:
    print(f"The Roman numeral for {n} is {numeral}")
else:
    print("The input is not between 1 and 10, so there's no Roman numeral for it.")


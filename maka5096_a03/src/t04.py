"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-15"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import multiply_fractions

# Get input from the user
num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction (must be nonzero): "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction (must be nonzero): "))

# Call the function with user input
num, den, product = multiply_fractions(num1, den1, num2, den2)

# Print the result
print(f"multiply_fractions({num1}, {den1}, {num2}, {den2}) -> ({num}, {den}, {product:.3f})")

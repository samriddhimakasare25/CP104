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

from functions import colour_combine
rgb_colour1 = input("Enter the first primary RGB color (red, green, or blue): ").lower()
rgb_colour2 = input("Enter the second primary RGB color (red, green, or blue): ").lower()
result = colour_combine(rgb_colour1, rgb_colour2)
print(f"The secondary RGB color is: {result}")
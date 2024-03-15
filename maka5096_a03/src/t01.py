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

from functions import footage_to_acres  # Import the function from your module

# Example usage
square_feet = float(input("Enter square footage: "))
acres = footage_to_acres(square_feet)
print(f"{square_feet} square feet is equal to {acres} acres.")
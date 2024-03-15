"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import power_of_two
if __name__ == "__main__":
    target = int(input("Enter a non-negative integer: "))
    if target < 0:
        print("Input must be a non-negative integer.")
    else:
        result = power_of_two(target)
        print(f"The nearest power of 2 greater than or equal to {target} is: {result}")
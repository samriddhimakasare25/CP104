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

# test_factorial.py
from functions import calc_factorial
if __name__ == "__main__":
    # Test cases
    test_cases = [5, 7, 3]

    for number in test_cases:
        result = calc_factorial(number)
        print(f"calc_factorial({number}) -> {result}")
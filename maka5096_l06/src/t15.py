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
from functions import statistics

try:
    n = int(input("Enter the number of values to process: "))
    minimum, maximum, total, average = statistics(n)

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Total: {total}")
    print(f"Average: {average}")

except ValueError as e:
    print(f"Error: {e}")

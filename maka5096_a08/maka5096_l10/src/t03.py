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
from functions import customer_best

# Open the file for reading
with open("customers.txt", "r") as wordFile:
    # Call the customer_best function and print the result
    result = customer_best(wordFile)
    print(result)


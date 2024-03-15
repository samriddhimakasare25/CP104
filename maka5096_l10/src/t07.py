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

from functions import append_max_num
with open("numbers.txt", "r+") as wordFile:
    num = append_max_num(wordFile)
    print(f"Appended maximum number: {num}")
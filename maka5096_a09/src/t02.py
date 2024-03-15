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


from functions import read_integers

with open("numbers.txt", "r") as wordFile:
    result = read_integers(wordFile)
print(result)
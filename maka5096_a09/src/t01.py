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

from functions import file_top

with open("students.txt", "r") as wordFile:
    file_top(wordFile, 5)  # Adjust the second argument (5) based on the number of lines you want to print

    
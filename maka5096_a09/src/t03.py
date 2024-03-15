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

from functions import file_statistics

with open("addresses.txt", "r") as wordFile:
    ucount, lcount, dcount, wcount, rcount = file_statistics(wordFile)
    result_string = f"{ucount}, {lcount}, {dcount}, {wcount}, {rcount}"
    print(result_string)

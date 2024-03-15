"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Imports

# Constants


Large=int(input("Number of large dogs groomed:"))
Small=int(input("Number of small dogs groomed:"))

SMALL_DOG=50
LARGE_DOG=75

smalldog=int(Small*SMALL_DOG)
largedog=int(Large*LARGE_DOG)
Cost=int((smalldog+largedog))

print("Total earned for the day : $",Cost)
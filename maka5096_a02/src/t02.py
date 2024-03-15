"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""
# Imports

# Constants

n = int(input("Enter a positive digit number:"))
x1 = n%10
x2 = int(n/10)
x = x2-x1
print("The product of the digits of ",n, "is ",x)
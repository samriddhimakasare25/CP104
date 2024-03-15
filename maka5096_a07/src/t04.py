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

from functions import list_subtract


minuend = [5, 5, 4, 5]
subtrahend = [5]
list_subtract(minuend, subtrahend)
print(minuend)  

minuend2 = [1, 2, 3, 4, 5, 5, 6]
subtrahend2 = [5, 6]
list_subtract(minuend2, subtrahend2)
print(minuend2)

minuend3 = [10, 20, 30, 40]
subtrahend3 = []
list_subtract(minuend3, subtrahend3)
print(minuend3)
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

flyers = int(input("Number of flyers: "))
delivery = int(input("Number of delivery people: "))
each = int(flyers/delivery)
print('Flyers per delivery person:',int(flyers/delivery))
left = flyers - (each * delivery)
print('Flyers left over:',left)

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

from functions import pythag
s1 = float(input('Length of side 1: '))  
s2 = float(input('Length of side 2: ')) 
radius, diam, circ, area = pythag(s1, s2)
print()    
print(f'Radius of resulting circle: {radius:.2f}') 
print(f'Diameter of resulting circle: {diam:.2f}')
print(f'Circumference of resulting circle: {circ:.2f}')
print(f'Area of resulting circle: {area:.2f}')
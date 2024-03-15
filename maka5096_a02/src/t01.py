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

sales = float(input("Enter the total sales: $"))
TAXRATE = 18.5
print("\nProjected Tax Report")
print("-----------------------")
print(f'Total sales: $ {sales:0.2f} \nAnnual tax: % {TAXRATE:0.2f}') # f'string is used
print("-----------------------")
print(f'Tax: $ {(sales*TAXRATE/100.0):0.2f}')
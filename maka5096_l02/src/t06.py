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

Principle= float(input("Mortgage principal ($):"))
years= int(input("Number of years:"))
rate = float(input("Yearly interest rate (%): "))
rate = (rate/100)/12
years = 12 * years
Month = Principle*((rate*((1+rate)**years))/(((1+rate)**years)-1))
print("The monthly payments are:$",Month)
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
# Imports


# Constants

p = float(input("Principal: $"))
r = float(input("Interest (%): "))
t = int(input("Number of years: "))
n = int(input("Number of times interest compounded per year: "))

#Calculating Balance using the formula
r=(r/100)
bal = p * (((1 + (r/n)) ** (n*t)))
print('Balance: $', bal)

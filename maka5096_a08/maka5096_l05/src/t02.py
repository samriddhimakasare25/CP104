"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports

# Constants

import functions as Test

mass=float(input("Enter mass (kg) : "))
weight,message=Test.get_weight(mass)

print("Weight:",end=" ")
print(weight,"N")
print("Object is: ",message)

 


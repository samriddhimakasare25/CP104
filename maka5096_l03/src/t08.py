"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports

# Constants

dirt=float(input("Enter amount of dirt (m^3):"))
gravel=float(input("Enter amount of gravel (m^3):"))
sand=float(input("Enter amount of sand (m^3):"))

total=dirt+gravel+sand 

print("Material          Cubic Metre")
print(f"Dirt               {dirt   :6.1f}")
print(f"Gravel             {gravel :6.1f}")
print(f"Sand               {sand   :6.1f}")
print(f"Total              {total  :6.1f}")
  

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

from functions import quadrant  

def main():
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    
    location = quadrant(x, y)
    
    print(f"The point ({x}, {y}) is in {location}.")

if __name__ == "__main__":
    main()
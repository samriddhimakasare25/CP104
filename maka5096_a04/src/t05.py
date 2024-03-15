"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports

# Constants

# Import the hoo_rah function from your module (assuming it's in a separate module)
from functions import hoo_rah

def main():
    try:
        number = int(input("Enter an integer: "))
        result = hoo_rah(number)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Input is not an integer.")

if __name__ == "__main__":
    main()


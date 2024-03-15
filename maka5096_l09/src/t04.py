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
# main.py
from functions import validate_code

def main():
    product_code = input("Enter a product code: ")
    category, digits, qualifiers = validate_code(product_code)
    
    print(f"Category: {category}")
    print(f"Digits: {digits}")
    print(f"Qualifiers: {qualifiers}")

if __name__ == "__main__":
    main()







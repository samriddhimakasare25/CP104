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

from functions import valid_isbn

def main():
    # Test cases
    isbn1 = "978-0-13-475416-9"
    isbn2 = "979-1-23-456789-0"
    isbn3 = "123-4-56789-012-3"

    # Check the validity of ISBNs and print the results
    result1 = valid_isbn(isbn1)
    result2 = valid_isbn(isbn2)
    result3 = valid_isbn(isbn3)

    print(f"ISBN: {isbn1} is {'valid' if result1 else 'invalid'}")
    print(f"ISBN: {isbn2} is {'valid' if result2 else 'invalid'}")
    print(f"ISBN: {isbn3} is {'valid' if result3 else 'invalid'}")

if __name__ == "__main__":
    main()
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

from functions import generate_matrix_num  # assuming your function is in a module named matrix_generator

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    low = float(input("Enter the low value of the range: "))
    high = float(input("Enter the high value of the range: "))
    value_type = input("Enter the value type ('int' or 'float'): ")

    try:
        matrix = generate_matrix_num(rows, cols, low, high, value_type)
        print("Generated Matrix:")
        for row in matrix:
            print(row)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

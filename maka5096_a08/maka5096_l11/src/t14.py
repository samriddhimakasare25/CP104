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

from functions import matrix_transpose
def main():
    # Example usage of matrix_transpose
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    transposed_matrix = matrix_transpose(matrix)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()
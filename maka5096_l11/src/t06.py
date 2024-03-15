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

from functions import matrix_stats  # Assuming your function is in a file named matrix_stats.py

def main():
    # Example matrix
    example_matrix = [
        [3, 7, 2],
        [9, 1, 4],
        [6, 8, 5]
    ]

    # Call the matrix_stats function
    smallest, largest, total, average = matrix_stats(example_matrix)

    # Display the results
    print("Smallest:", smallest)
    print("Largest:", largest)
    print("Total:", total)
    print("Average:", average)

if __name__ == "__main__":
    main()

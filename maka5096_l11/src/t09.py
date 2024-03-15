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

from functions import count_frequency
if __name__ == "__main__":
    # Example usage:
    my_matrix = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]

    character_to_search = 'e'
    result = count_frequency(my_matrix, character_to_search)

    print(f"The character '{character_to_search}' appears {result} times in the matrix.")
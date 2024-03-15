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

from  functions import list_factors

def main():
    # Provide three numbers for which you want to find factors
    numbers = [24, 36, 45]  # Replace these with any positive integers greater than 0

    for num in numbers:
        # Call the list_factors function
        factors = list_factors(num)

        # Display the result
        if not factors:
            print(f"{num} has no factors other than 1 and itself.")
        else:
            print(f"The factors of {num} are: {factors}")

if __name__ == "__main__":
    main()

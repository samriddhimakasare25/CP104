"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import hi_lo_game

def test_hi_lo_game():
    high = 100  # You can change this to any positive integer value
    count = hi_lo_game(high)
    print(f"Number of guesses: {count}")

if __name__ == "__main__":
    test_hi_lo_game()
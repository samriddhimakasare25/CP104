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

from functions import find_longest

def main():
    # Open the file "words.txt" for reading
    with open("words.txt", "r") as wordFile:
        # Call the find_longest function and get the result
        result = find_longest(wordFile)

    # Print the result
    print(f"The last word with the longest length is: {result}")

if __name__ == "__main__":
    main()
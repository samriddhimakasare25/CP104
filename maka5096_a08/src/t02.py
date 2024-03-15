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

from functions import pluralize
def main():
    words = ["dog", "church", "holiday"]
    
    for word in words:
        result = pluralize(word)
        print(f"The plural of '{word}' is '{result}'.")


if __name__ == "__main__":
    main()

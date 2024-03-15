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

from functions import list_positives
def main():
    number_list = list_positives()

    # Output 1: Print the list directly
    print("Output 1: List of positive numbers:", number_list)

    # Output 2: Print each number on a new line
    print("\nOutput 2: Positive numbers on separate lines:")
    for num in number_list:
        print(num)

    # Output 3: Calculate and print the sum of the positive numbers
    sum_of_numbers = sum(number_list)
    print("\nOutput 3: Sum of positive numbers:", sum_of_numbers)

if __name__ == "__main__":
    main()
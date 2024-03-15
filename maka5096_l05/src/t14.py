"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports

# Constants

from functions  import ticket

def main():
    print("Welcome to the school play ticket calculator!")
    ticket_price = ticket()
    print(f"Your ticket price is: ${ticket_price:.2f}")
if __name__ == "__main__":
    main()
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-23"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import treadmill

def main():
    burnt_per_minute = float(input("Enter calories burnt per minute: "))
    start = int(input("Enter start time in minutes: "))
    end = int(input("Enter end time in minutes: "))
    inc = int(input("Enter increment in minutes: "))

    treadmill(burnt_per_minute, start, end, inc)

if __name__ == "__main__":
    main()
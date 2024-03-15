"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-15"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import extract_date  # Replace 'your_module_name' with the actual name of your module

# Get a date number as input (you can replace this with your own date number)
date_number = int(input("Enter a date number in the format YYYYMMDD: "))

# Call the extract_date function to extract the year, month, and day
year, month, day = extract_date(date_number)

# Print the results
print("Year:", year)
print("Month:", month)
print("Day:", day)

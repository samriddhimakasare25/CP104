"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""
# Imports

# Constants

date= int(input ("Enter a date in the format YYYYMMDD: "))

year = date // 10000
month = date% (10000) // 100
day = date % 100

print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
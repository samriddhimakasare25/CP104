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

from functions import falling_distance

# Input a time value (in seconds)
falling_time = float(input("Enter the time (in seconds) the object has fallen: "))

# Calculate the falling distance using the falling_distance function
distance = falling_distance(falling_time)

# Print the result
print(f"The distance the object has fallen is {distance} meters.")

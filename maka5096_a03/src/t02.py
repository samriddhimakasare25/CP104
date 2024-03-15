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

# Import the function if it's in a separate module
from functions import lawn_mow_time

# Get user input for width, length, and speed
width = float(input("Enter the width of the lawn (in meters): "))
length = float(input("Enter the length of the lawn (in meters): "))
speed = float(input("Enter the mowing speed (square meters cut per minute): "))

# Call the function with the user-provided values
time_minutes = lawn_mow_time(width, length, speed)

# Display the result
print(f"It will take {time_minutes} minutes to mow the lawn.")
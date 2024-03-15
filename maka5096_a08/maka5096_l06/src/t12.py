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
from functions import gic

# Get user input for GIC parameters
value = float(input("Enter the initial value of the GIC (in dollars): "))
years = int(input("Enter the number of years to maturity: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))

# Call the gic function and store the final value
final_value = gic(value, years, rate)

# Display the final value to the user
print(f"The final value of the GIC after {years} years is: ${final_value:.2f}")
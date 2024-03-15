"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import pollution_ranking
air_quality_index = int(input("Enter the Air Quality Index (AQI): "))
pollution = pollution_ranking(air_quality_index)
print(f"The pollution level for AQI {air_quality_index} is: {pollution}")

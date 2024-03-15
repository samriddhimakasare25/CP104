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
from functions import population
current_population = int(input('Current Population: ')) 
births = int(input('Average seconds between births: ')) 
deaths = int(input('Average seconds between deaths: '))
immigrants = int(input('Average seconds between immigrations: '))
years = int(input('Years in the future: '))
new_population = population(current_population, births, deaths, immigrants, years) 
print('\nThe new population will be', new_population)

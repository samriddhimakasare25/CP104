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

from functions import text_analyze

txt = 'Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks.'
uppr, lowr, dgts, whtspc = text_analyze(txt)

print(f"Uppercase letters: {uppr}")
print(f"Lowercase letters: {lowr}")
print(f"Digits: {dgts}")
print(f"Whitespace characters: {whtspc}")
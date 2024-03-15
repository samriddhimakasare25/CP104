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
# test_script.py
# test.py
from functions import line_numbering

input_file = "wilde.txt"
output_file = "wilde_numbered.txt"

with open(input_file, "r") as wordFile:
    with open(output_file, "w") as outputFile:
        line_numbering(wordFile, outputFile)

print(f"The file {output_file} has been created with line numbers.")


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

from functions import student_stats

with open("students.txt", "r") as wordFile:
    l_id, h_id, avg = student_stats(wordFile)

print(f"Lowest ID: {l_id}\nHighest ID: {h_id}\nAverage Mark: {avg}")

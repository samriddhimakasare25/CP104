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


from functions import file_copy

source_file_path = 'words.txt'
target_file_path = 'new_words.txt'

with open(source_file_path, 'r') as source_file, open(target_file_path, 'w') as target_file:
    file_copy(source_file, target_file)
print(f"Copying '{source_file_path}' to '{target_file_path}'")
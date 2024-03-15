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

from functions import has_word_chain

test_case1 = ['camel', 'leopard', 'dog', 'giraffe', 'elephant']
test_case2 = ['apple', 'elephant', 'tiger', 'rhino', 'orca']
test_case3 = ['python', 'ninja', 'avocado', 'octopus', 'seagull']
result1 = has_word_chain(test_case1)
result2 = has_word_chain(test_case2)
result3 = has_word_chain(test_case3)
print("Test Case 1:", result1)  
print("Test Case 2:", result2)  
print("Test Case 3:", result3)  
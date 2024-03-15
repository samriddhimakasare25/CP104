"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import positive_statistics

if __name__ == "__main__":
    minimum, maximum, total, average = positive_statistics()
    
    print("Minimum: {}".format(minimum))
    print("Maximum: {}".format(maximum))
    print("Total: {}".format(total))
    print("Average: {:.2f}".format(average))
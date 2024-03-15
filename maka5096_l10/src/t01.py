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
from functions import customer_record

# Open the file for reading
with open("customers.txt", "r") as wordFile:
    # Specify the record number you want to retrieve (replace 0 with the desired record number)
    record_number = 0
    
    # Call the function to get the specified record
    result = customer_record(wordFile, record_number)

    # Check if the result is not an empty list (i.e., the record exists)
    if result:
        print(f"Record {record_number}: {result}")
    else:
        print(f"Record {record_number} does not exist.")

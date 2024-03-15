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

from functions import employee_payroll
def main():
    total, average = employee_payroll()
    print(f"Total net wages for all employees: ${total:.2f}")
    print(f"Average net wage per employee: ${average:.2f}")

if __name__ == "__main__":
    main()

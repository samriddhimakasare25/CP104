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
from functions import meal_costs
def main():
    b_total, l_total, s_total, a_total = meal_costs()
    
    print("\nSummary of Meal Costs:")
    print(f"Total cost of breakfasts: ${b_total:.2f}")
    print(f"Total cost of lunches: ${l_total:.2f}")
    print(f"Total cost of suppers: ${s_total:.2f}")
    print(f"Total cost of all meals: ${a_total:.2f}")
    
if __name__ == "__main__":
    main()
  



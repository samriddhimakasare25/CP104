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
#TO1.PY
def list_factors(number):
    """
    -------------------------------------------------------
    takes an integer greater than 0 and returns a list of the factor 
    that makes up that number excepting the number itself 
    Use : factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num-number to find factors for (int>0)
    Returns:
        factors - a list of all the factors in num (list)
    ------------------------------------------------------
    """
    factors = []
    for x in range (1,number,1):
        if (number % x) == 0:
            factors.append(x)
    return factors
#T02.PY
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    num = int (input("Enter a positive number: "))
    while num !=0:
        if num > 0:
            numbers.append(num)
        num = int (input("Enter a positive number : "))
        
    return numbers

#T03.PY
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    locations = []
    size = len(numbers)
    
    for x in range(size):
        num = numbers[x]
        if num == target_number:
            locations.append(x)
            
    return locations
#TO4.PY
def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    minuend[:] = [item for item in minuend if item not in subtrahend]
        
    return
    
#TO5.PY
def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True 
    index = -1  # Initialize index to -1
    
    x = 1
    while x < len(numbers):
        if numbers[x] < numbers[x - 1]:
            in_order = False
            index = x 
            x += 1  # Move to the next element
        else:
            x += 1  # Move to the next element

    return in_order, index



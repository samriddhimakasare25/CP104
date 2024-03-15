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

#TO1.PY
def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    if number < 0:
        result = "Invalid input: Factorial is undefined for negative numbers"
    elif number == 0 or number == 1:
        result = 1
    else:
        product = 1
        for i in range(1, number + 1):
            product *= i
        result = product
        
    return result
#TO2.PY
def calories_treadmill(per_min, minutes):
    """ 
    -------------------------------------------------------
    Prints a table of calories burned on a treadmill every five minutes.
    Given the number of calories burned per minute (per_min) and the total
    number of minutes run (minutes), it calculates and prints the calories
    burned at 5-minute intervals up to the given number of minutes. The
    results are printed with one decimal accuracy and aligned in a table
    format.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Time (min)  Calories Burned")
    for i in range(5, minutes + 1, 5):
        calories_burned = round(per_min * i, 1)
        print(f"{i:2}  {calories_burned:5.1f}")
    return None
#T03.PY
def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow made of # characters pointing up.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows for the arrow (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    if rows < 1:
        print("Please provide a positive integer for the number of rows.")

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * i - 3) + "#")
            
    return None
#T04.PY
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
     
    print(f"{' ':4}", end="")  
    for i in range(start_num, stop_num + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (5 * (stop_num - start_num + 1)))

    
    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            product = i * j
            print(f"{product:4}", end="")
        print()
    return None
#T05.PY
def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for _ in range(count):
        total += start
        start += increment
    return total

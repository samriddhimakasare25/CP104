"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-23"
-------------------------------------------------------
"""
# Imports

# Constants
#T02.PY
def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0  # Initialize the total to 0
    # Iterate through all odd numbers from 1 to num
    for i in range(1, num + 1, 2):
        total += i  # Add the odd number to the total
    return total
    
#T06.PY
def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = char * (2 * i - 1)
        print(spaces + stars)
    
    return None  
#T10.PY
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for time in range(start, end + 1, inc):
        calories_burned = burnt_per_minute * time
        print(f"Calories burned after {time} minutes: {calories_burned:.1f}")
        
    return None

#T12.PY ( DOESNT WORK)
def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("Year       Value $")
    print("------------------")
    total = value 
    for i in range(years):
        print(f" {i:2}{total:15,.2f}")
        total = total + (total*(rate/100))
    i = i+1
    print(f" {i:2}{total:15,.2f}")
    
    return total
#T15.PY
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")
    
    total = 0
    minimum = float('inf')
    maximum = float('-inf')
    
    for _ in range(n):
        value = float(input("Enter a value: "))
        total += value
        minimum = min(minimum, value)
        maximum = max(maximum, value)
    
    average = total / n

    return minimum, maximum, total, average

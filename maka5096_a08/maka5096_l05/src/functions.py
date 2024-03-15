"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports

# Constants

#TO2.PY
GRAVITATION_ACCELERATION=9.8
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight=mass * GRAVITATION_ACCELERATION
    if(weight>1000):
        message="heavy"
    elif(weight<10):
        message="light"
    else:
        message="average"
    return weight,message

#T05.PY
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = True
    else:
        result =  False
        
    return result
  
    #T08.PY
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    numeral = None
    
    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        numeral = None
    
    return numeral

    #T11.PY
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    result = ""
    if x == 0:
        if y == 0:
            result = "Origin"
        else:
            result = "Y-Axis"
    elif y == 0:
        result = "X-Axis"
    else:
        if x < 0:
            if y < 0:
                result = "Quadrant 3"
            else:
                result = "Quadrant 2"
        else:
            if y < 0:
                result = "Quadrant 4"
            else:
                result = "Quadrant 1"
    return result
    
    #T14.PY
def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    INFANT = 3
    SENIOR = 65
    ADULT = 18
    KID = 10
    
    age = float(input("Enter your age: "))
    
    if age < INFANT:
        price = 0
    elif age >= SENIOR:
        price = 4.00
    elif age >= ADULT:
        price = 5.00 
    elif age >= KID:
        student = input("Are you a student? (Y/N)")
        if student == 'Y':
            price = 1.00
        else:
            price = 3.00
    else:
        price = 2.00
    
    return price
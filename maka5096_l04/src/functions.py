"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""
# Imports

#Constants
DAYS = 365
HOURS = 24
MINS = 60
SEC = 60
CONVERSION = DAYS*HOURS*MINS*SEC
#TO1.PY
def diameter(radius):    
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """ 
    return 2 * radius 
#TO4.PY
def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    slantheight = ((base / 2) ** 2 + height ** 2) ** 0.5     
    area = base ** 2 + 2 * base * ((base ** 2) / 4 + height ** 2) ** 0.5     
    volume = base ** 2 * (height / 3)     
    return slantheight, area, volume
#T05.PY
from math import sqrt
def right_triangle(adjacent, opposite):

    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp=sqrt(adjacent**2+opposite**2)
    per=(hyp+adjacent+opposite)
    area= (1/2)*opposite*adjacent
    return hyp,per,area
#TO6.PY
from math import pi
def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """   
    radius=sqrt(s1**2+s2**2)
    diam = 2 * radius  
    circum = 2 * pi * radius
    area = pi * radius ** 2
    return radius, diam, circum, area
#T10.PY ( Does not use upper-case constant(s) for seconds per year)
def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    # CONVERSION = 365*24*60*60
    seconds = years*CONVERSION
    num_births = seconds // births
    num_deaths = seconds // deaths
    num_immigrants = seconds // immigrants
    
    new_size = size + num_births - num_deaths + num_immigrants
    return new_size
    
#T13.PY (THIS I DONT KNOW WHY IT ISN'T WORKING)
FREZZING= 32
def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    celsius=(fahrenheit-FREZZING)*(5/9)
    return (celsius)
    
   




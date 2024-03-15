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
#T01.PY
def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= day_num <= 7:
        day = day_names[day_num - 1]
    else:
        day = "Error"
    
    return day
#T02.PY
def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    pollution = "Error"
    
    if air_quality_index >= 0:
        if air_quality_index <= 50:
            pollution = "Good"
        elif air_quality_index <= 100:
            pollution = "Moderate"
        elif air_quality_index <= 150:
            pollution = "Unhealthy for Sensitive Groups"
        elif air_quality_index <= 200:
            pollution = "Unhealthy"
        elif air_quality_index <= 300:
            pollution = "Very Unhealthy"
        else:
            pollution = "Hazardous"
    
    return pollution

#TO3.PY
def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1 >= val2 and val1 >= val3:
        largest1 = val1
        if val2 >= val3:
            largest2 = val2
        else:
            largest2 = val3
    elif val2 >= val1 and val2 >= val3:
        largest1 = val2
        if val1 >= val3:
            largest2 = val1
        else:
            largest2 = val3
    else:
        largest1 = val3
        if val1 >= val2:
            largest2 = val1
        else:
            largest2 = val2
    
    average = (largest1 + largest2) / 2
    return average

#TO4.PY
def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red"):
        result = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red"):
        result = "yellow"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "green"):
        result = "aqua"
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        result = "red"
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        result = "blue"
    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        result = "green"
    else:
        result = "Error"
        
    return result


def hoo_rah(number):
    """
    -------------------------------------------------------
    Returns a string based on the input number:
        "Hoo" if the number is evenly divisible by 2
        "Rah" if the number is evenly divisible by 7
        "Hoo Rah" if the number is evenly divisible by both 2 and 7
        "Zip" if the number is none of the above.
    Returns "Error" if the input number is not an integer.
    Use: result = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - an integer to determine divisibility (int)
    Returns:
        result - a string indicating divisibility or "Error" (str)
    ------------------------------------------------------
    """
    if number % 2 == 0 and number % 7 == 0:
        result = "Hoo Rah"
    elif number % 2 == 0:
        result = "Hoo"
    elif number % 7 == 0:
        result = "Rah"
    else:
        result = "Zip"

    return result
   



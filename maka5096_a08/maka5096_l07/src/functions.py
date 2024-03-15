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
from random import randint
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    randomValue = randint(1, high)
    count = 0
    
    while True:
        guess = int(input("Guess: "))
        count += 1
        
        if guess > randomValue:
            print("Too high, try again.")
        elif guess < randomValue:
            print("Too low, try again.")
        else:
            print("Congratulations - good guess!")
            return count

#T02.PY
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    while power < target:
        power *= 2
    return power

#T05.PY
def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    minimum = None
    maximum = None
    total = 0
    count = 0
    while True:
        try:
            value = float(input("Enter a positive number (or a negative number to exit): "))
            if value < 0:
                if count == 0:
                    print("You must enter at least one positive number before exiting.")
                    continue
                else:
                    break
            elif value >= 0:
                if count == 0:
                    minimum = maximum = value
                else:
                    minimum = min(minimum, value)
                    maximum = max(maximum, value)
                total += value
                count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if count == 0:
        average = 0
    else:
        average = total / count
    return minimum, maximum, total, average

#T07.PY
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0

    another_day = 'Y'

    day = 1
    while another_day.upper() == 'Y':
        print(f'For Day {day}\n')
        breakfast_cost = float(input("How much was breakfast? $"))
        lunch_cost = float(input("How much was lunch? $"))
        supper_cost = float(input("How much was supper? $"))

        day_total = breakfast_cost + lunch_cost + supper_cost

        print(f'Your total for the day was ${day_total:.2f}\n')

        b_total += breakfast_cost
        l_total += lunch_cost
        s_total += supper_cost
        a_total += day_total

        another_day = input("Were you away another day (Y/N)? ")
        day += 1

    return b_total, l_total, s_total, a_total

#T10.PY
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    total = 0 
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625
    count = 0 
    
    while True:
        employee_ID = int(input("Enter Employee ID number (or 0 to exit): "))
        if employee_ID == 0:
            break
        count += 1
        hourlywage_rate = float(input("Enter hourly wage rate: "))
        num_worked = int(input("Enter number of hours worked during the week: "))
        
        if num_worked > 40:
            OVERTIME = num_worked - 40
            salary = (40 * hourlywage_rate) + (OVERTIME * (OVERTIME_RATE * hourlywage_rate))
            tax_deduction = salary * TAX_RATE
            gross_salary = salary - tax_deduction
        else:
            salary = (hourlywage_rate * num_worked)
            tax_deduction = salary * TAX_RATE
            gross_salary = salary - tax_deduction 
            
        print(f"Net payment for employee {employee_ID}: ${gross_salary:.2f}")
        
        total += gross_salary 
    
    average = total / count 
    return total, average 

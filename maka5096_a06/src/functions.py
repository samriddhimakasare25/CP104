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

def total_wins():
    """
    -------------------------------------------------------
    Counts the number of "purple" and "gold" strings in user input.
    Use: purple_count, gold_count = total_wins()
    -------------------------------------------------------
    Returns:
        purple_count - The count of "purple" strings (int)
        gold_count - The count of "gold" strings (int)
    ------------------------------------------------------
    """
    purple_count = 0
    gold_count = 0
    continue_input = True

    while continue_input:
        user_input = input("Enter a game result (purple, gold, or press Enter to finish): ")

        if user_input == "":
            continue_input = False
        elif user_input == "purple":
            purple_count += 1
        elif user_input == "gold":
            gold_count += 1

    return purple_count, gold_count

def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if number <= 1:
        result = False
    elif number == 2:
        result = True
    elif number % 2 == 0:
        result = False
    else:
        i = 3
        while i * i <= number:
            if number % i == 0:
                result = False
            i += 2
        result = True

    return result

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    principal = principal_amount
    rate = interest_rate
    month = 1

    print("Principal: $%.2f Interest rate: %.1f%% Monthly payment: $%.2f" % (principal, rate, payment))
    print("--------------------------------------------------")
    print("Month Interest Payment Balance")
    print("--------------------------------------------------")

    while principal > 0:
        interest = (principal * rate / 100) / 12
        principal = principal + interest - payment
        if principal < 0:
            payment = payment + principal
            principal = 0
        print("%d %.2f %.2f %.2f" % (month, interest, payment, principal))
        month += 1

    
    return

def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if number == 0:
        digits = 1
    if number < 0:
        number = -number
    while number > 0:
        digits += 1
        number //= 10
    
    return digits

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1

    while i < number:
        if number % i == 0:
            total += i
        i += 1

    return total








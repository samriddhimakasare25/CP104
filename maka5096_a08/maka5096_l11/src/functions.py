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
import random
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    if value_type == "int":
        matrix = [[random.randint(int(low), int(high)) for _ in range(cols)] for _ in range(rows)]
    elif value_type == "float":
        matrix = [[random.uniform(low, high) for _ in range(cols)] for _ in range(rows)]
    else:
        raise ValueError("Invalid value_type. Use 'int' or 'float'.")

    return matrix

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(" ", end="")    
    for x in range(len(matrix[0])):        
        print("{:>7d}".format(x), end="")   
    print()    
    if(value_type == "float"):        
        for x in range(len(matrix)):            
            print("{:>2.0f}".format(x), end="")            
            for y in range(len(matrix[x])):                
                num = matrix[x][y]                
                print("{:>7.2f}".format(float(num)), end="")           
            print()    
    if(value_type == "int"):        
        for x in range(len(matrix)):            
            print("{:>2d}".format(x), end="")            
            for y in range(len(matrix[x])):                
                print("{:>7d}".format(matrix[x][y]), end="")            
                print()    
    return

def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            num = matrix[x][y]
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
            total += num
            count += 1

    average = total / count
    return smallest, largest, total, average

def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0

    for row in matrix:
        for col in row:
            if col == char:
                count += 1

    return count

def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = []
    for x in range(len(matrix[0])):
        transposed.append([])
        for y in range(len(matrix)):
            num = matrix[y][x]
            transposed[x].append(num)
    return transposed



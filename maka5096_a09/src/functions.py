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

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line_count = 0
    while line_count < count:
        line = file_handle.readline()
        if not line:
            break  # End of file reached
        print(line.strip())
        line_count += 1
    return
def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for line in file_handle:
        for token in line.split(","):
            try:
                number = int(token.strip())
                if number > 0:
                    number_list.append(number)
            except ValueError:
                pass
    return number_list
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = lcount = dcount = wcount = rcount = 0
    for char in file_handle.read():
        if char.isupper():
            ucount += 1
        elif char.islower():
            lcount += 1
        elif char.isdigit():
            dcount += 1
        elif char.isspace():
            wcount += 1
        else:
            rcount += 1
    return ucount, lcount, dcount, wcount, rcount
def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
        # initialize line_number to 0
    line_number = 0

    # iterate through each line in the input file
    for line in fh_read:
        # if the line is not empty
        if line != "\n":
            # write line number, then a space, then the entire line to the output file
            fh_write.write('[{}] {}'.format(line_number, line))
        else:
            # write just the line number to the output file for empty lines
            fh_write.write('[{}]\n'.format(line_number))

        # increment line number
        line_number += 1

    # Only one return statement at the end of the function
    return None
    
def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
        # Initialize variables to keep track of lowest mark, highest mark, and total marks
    lowest_mark = float('inf')  # Initialize to positive infinity to ensure any mark will be lower
    highest_mark = float('-inf')  # Initialize to negative infinity to ensure any mark will be higher
    total_marks = 0
    count = 0

    # Read each line from the file
    for line in file_handle:
        # Split the line into components: surname, forename, id, mark
        components = line.strip().split(',')

        # Extract the mark as a float
        mark = float(components[3])

        # Update lowest and highest marks
        if mark < lowest_mark:
            lowest_mark = mark
            l_id = components[2]  # Update lowest ID

        if mark > highest_mark:
            highest_mark = mark
            h_id = components[2]  # Update highest ID

        # Update total marks and count
        total_marks += mark
        count += 1

    # Calculate average mark
    avg = total_marks / count if count > 0 else 0.0

    # Return the results
    return l_id, h_id, avg
    
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
def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = sentence[0]
    for i in range(1, len(sentence)):
        ch = sentence[i]
        if ch.isupper():
            spaced += " " + ch.lower()
        else:
            spaced += ch
            
    return spaced
#T02.PY
def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    pluralized = ""
    
    if string.endswith ("s") is True:
        pluralized += string + "es"
    elif string.endswith ("sh") is True: 
        pluralized += string + "es"
    elif string.endswith ("ch") is True: 
        pluralized += string + "es"
        
    if string.endswith ("y") is True:
        if string.endswith ("ay") is True:
            pluralized += string + "s"
        elif string.endswith ("oy") is True: 
            pluralized += string + "s"
        else:
            pluralized = string.replace ("y","ies")
            
    return pluralized 
 
#T03.PY       
def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ""
    x = -1 
    while str1[x]==str2[x]:
        suffix = str1[x]+suffix
        x-=1
    return suffix

#TO4.PY
def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    x = set("0123456789-")  
    isbn_split = isbn.split("-")
    result = True
    if len(isbn) != 17:
        result = False
    if any(char not in x for char in isbn):
        result = False
    if len(isbn_split) != 5:
        result = False
    if isbn_split[0] not in ['978', '979']:
        result = False
    if not isbn_split[4].isdigit() or len(isbn_split[4]) != 1:
        result = False
    if '--' in isbn:
        result = False
    return result

def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(words) < 2:
        result = False
    else:
        result = True
        i = 0

        while i < len(words) - 1:
            if words[i][-1] != words[i + 1][0]:
                result = False
                break  
            i += 1

    return result
    
    
    
    
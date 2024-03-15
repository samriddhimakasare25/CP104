"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Imports

SECOND_PER_MINUTE=60
time = int(input("Number of seconds:"))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("Day",day,("Hour:") ,hour,("Minutes:") ,minutes, ("Second:"),seconds)
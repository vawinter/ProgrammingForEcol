# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:35:44 2022

Lesson 4: Functions

@author: V. Winter
"""
# julian date:
# user defines month
month = int(input("give a month (numeric): "))
# user defines date
date = int(input("What is the day of the month for the date you want to convert?"))

# define julian
julian = 0

# loop over defined month
for i in range(1, month):
    # if these months, then 30 days
    if i in [4, 6, 9, 11]:
        x = 30 
        # ifelse not 2, then 31 days
    elif i in [2]:
        x = 31 
        # otherwise 28 days
    else:
        x = 28 
        # julian = julian plus days
    julian = julian + x
    # julian plus date user gave
julian = julian + date
# print final output
print("\nJulian date for ", month, "/", date, " is: ", julian, sep = "")


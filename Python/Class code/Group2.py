# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:12:49 2022

Group coding: Group 2

Veronica, Jayden, Alice
"""

# Bring in library
import time 

# Question 1: Blink
# Write a program that will output “blink” every x seconds, where the user will decide x. 
# Write another program that will “blink” once every odd second and “blink” twice every even 
# second. 
# You can use the time library and the time.sleep(x) function, where x is the number
# of seconds. 
# Both programs should run for 10 seconds. 

# Part 1
# Have user define a number
# num = int(input("how many seconds between blinks? "))
# # #time.sleep(num)
# # print(time.sleep(num), "blink")

# # for loop
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 + 1]:
#     # tell the nmber to pause between
#     time.sleep(num)
#     # Idea: subtact defined number by i and print blink next to it
#     print(i - num, "blink")

# printed numbers and blinks but not appropriate 
# Part 2
# # Define even and odd
# if num % 1: 
#    #indent = run these is TRUE
#    print("blink")
# else:
#     print("blink blink")


# Solution from JK:
#import time
print("\nProgram 1:")   

# user defines seconds between blnks
x = int(input("how many seocnds between blinks? "))
# time starts at 0
t = 0
# While t less than 0
while t < 10:
    # pausing for x number of seconds
    time.sleep(x)   
    # increment by 1
    t += x
    # if less than 10 seconds
    if t <= 10:
        # blink time
        print(t, "blink", sep = "\t")


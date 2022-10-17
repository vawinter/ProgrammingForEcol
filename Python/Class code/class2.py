# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:01:38 2022

@author: VAW

Conditions, loops, and Realations
"""
# Conditionals
#x = int(input("Enter a number: "))

#if x > 0: 
    # indent = run these is TRUE
 #  print("number is positive")
#elif x < 0:
#    print("number is negative")
#else:
#    print("tf, number is zero")
#print("indentation is important")
 # always prints  
#print("this line always prints")


# Loops
# correct = False
# while not correct:
#     answer = int(input("what is 4 + 1? "))
#     if answer == 5:
#         print("you are gr8")
#         correct = True
#     else:
#         print("seek help")

# For loops
# lst = [1, 2, 3, 4, 5]

# for i in (lst):
#     print("Number", i)
   
# for i in range(1, 10 + 1):
    # print(i)
 
    
# x = 10
# counter = 1
# while counter <= x:
#     print(counter)
#     counter += 1 #counter = counter + 1 
    
# for i in range(10, 0, -1):
#      print(i)
# print("What the f***")
 
# Can loop through and simultaneously assign variables

# Nested for loop
for year in range(2019, 2024 + 1):
    print("Year: ", year)
    for month in range(1, 12 + 1):
        print("Month", month)
        # if else
        if month in [1, 2, 3]:
            print("Winter")
        elif month in [4, 5, 6]:
            print("Spring")
        elif month in [7, 8, 9]:
            print("Summer")
        else:
            print("Fall")
 
    
 
    
 
    
 
    
    
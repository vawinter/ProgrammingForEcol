# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:11:30 2022

@author: Veronica, Sara, Tyler

Group assign. 4
"""

# Recursion 
# Recursion is when a function calls itself. Let’s try a pretty standard example. The factorial 
# (symbolized with an exclamation mark, !) of a number, n, is equal to the product of all the 
# numbers in the range from 1 to n. In other words: 
# n! = n * (n - 1) * (n - 2) * (n - 3) ... * 1 
# 0! = 1 
 
# Another way of expressing it is: 
#     n! = n*(n -1)! 
#   0! = 1 
 
# Write a program that will calculate the factorial of any positive number. The main part of the 
# program should ask the user to input a number and then call a recursive function to do the 
# actual calculation. The main part of the program will then print the answer. 
 
# Function: 
def factorial(n):
    if n != 0:
       return n * factorial(n - 1)
    elif n == 0:
         return(1)
   
   
    
# Main program
num = int(input("Please give a number: "))
factorial(num)
print(num, "! = ", factorial(num), sep = '')
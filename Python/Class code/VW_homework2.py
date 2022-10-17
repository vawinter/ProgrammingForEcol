# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 10:24:44 2022

Hoemwork 3: conditionals, loops

Veronica A. Winter
"""

# # Question 1: Even/Odd
# print("\nQuestion 1: even/odd")   

# # a. user defines seconds between blnks
# x = int(input("Please enter a starting number: "))
# y = int(input("Please enter an ending number: "))
# typ = str(input("Would you like odd or even numbers (odd/even): "))

# for i in range(x, y): 
# 	num = int(input()) 
#  	if(num%2): 
#  		total+=num 
#  		count+=1 
# print(total,total/count)

# def even(x, y):
#     if x > y:
#         return
#     print(x, end=" ")
#     return even(x +2, y)
# x = x; y = y
# even(x, y)



# # b. for loop to implement printing based on above commands
# for i in range(x, y + 1):
#     # c. create a logical statement to print only even/odd
#     if y % 2 == 0:
#         print(i, sep = "", end = "")
#     print()

 
# def even(num1,num2):
#     if num1>num2:
#         return
#     print(num1,end=" ")
#     return even(num1+2,num2)
# num1=4;num2=15
# even(num1,num2)

# Question 2: Final grade
# print("\nQuestion 2: Final grade")
# x = float(input("Final grade percentage: "))

# if x > 90:
#     print("A")
# elif x < 90 and x > 80:
#     print("B")
# elif x < 80 and x > 70:
#     print("C")
# elif x < 70 and x > 65:
#     print("D")
# else:
#    print("F")
    
    
# # Question 3: multiplication table
# print("\nQuestion 3: Multiplication table")

# # nested for loop
# for i in range (1, 10):
#     for m in range (1, 10):
#         # multiply i by m and seperate to create table format
#      print(i * m, end = "\t")
#     print('')

# Done!!
    
# # Question 4: prime numbers
# print("\nQuestion 4: prime numbers")

# # loop over to output prime numbers: create ranfe     
# for prime in range (1, 100 + 1):
#     # define start count
#     num = 0
#     # math for whole numbers
#     for i in range(2, (prime//2 + 1)):
#         if(prime % i == 0):
#             num = num + 1
# # if statement for is count is 0 and prime is not 1 then output prime table
#     if (num == 0 and prime != 1):
#         print(" %d" %prime, end = '  ')

print("\nDone")
# Done!





    
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:33:56 2022

Homework 7: Object-oriented programing
Author: Veronica Winter

Last Update: 10/7/2022
Description:  Answers to homework assignment 7.

"""
print("\nstart: Correct change")
# 2.   (40pts) Write a program that will calculate the correct change to give back to a shopper at a 
# fruit market. Set up a class fruit to do this. The class ‘fruit’ will have three attributes 
# (variables): name, price, and number, as well as two methods: addFruit and totalCost (for 
# that type of fruit).  

# Define the class
class fruit:
    # when object is initiated....
    def __init__(self, nm, pr):
    # variables: attributes in fruit
        self.name = nm
        self.price = pr
        self.num = 0
              
    def printInfo(self):
        print("Fruit:", self.name, "-", self.price, "-", self.number)
        
    def addFruit(self, addFruit):
        self.num = addFruit + self.num 
    def totalCost(self):
        return (self.num * self.price)
     
# Apples are sold for $1.15 each, oranges for $1.75 each, mangoes for $2.35 each. 

# Define the fruit above with the class fun
apple = fruit("apple", 1.15)
orange = fruit("orange", 1.75)
mango = fruit("mango", 2.35)
 
# With a while loop, ask the user how much of each fruit they would like to buy, one fruit at a 
# time. In other words, ask how many apples, how many oranges, how many mangoes. Then 
# show them what they have in their cart, and ask them if they would like to continue 
# shopping. If yes, cycle back through so they can add more fruit. If no, exit the loop and tell 
# them their total cost (there is no sales tax in PA on fruit). 
 
# Main program
# Start of while loop
print("Welcome to the fruit market:")
start = input("Would you like to add fruit to your cart (y/n): ")
while start == "y":
#  User defines how many of each fruit they would like:
    apple.addFruit(int(input("How many apples would you like to add to cart?: ")))
    orange.addFruit(int(input("How many oranges would you like to add to cart?: ")))
    mango.addFruit(int(input("How many mangeos would you like to add to cart?: ")))

# Tell user amount of fruit in catrr
    print("Your cart: ", "Apples:", apple.num, "Oranges: ", orange.num, "Mango: ", mango.num, sep = "\n")
# Tell user total cost thusfar
    totalCart = apple.totalCost() + orange.totalCost() + mango.totalCost()
    print("Your cart total is: $", round(totalCart, 2), sep = '')
# ask to continue adding or not
    start = input("Would you like to add fruit to your cart (y/n): ")
   # end while loop
  
# User defines payment
pay = float(input("Please enter amount you will pay with: "))
# Then have the user enter the amount they will pay with. Calculate the difference (the 
# amount they get back) and output that to the user.  
restOfChange = pay - totalCart 

def numCoins(x, rate): 
    return int(x // rate) 
 
dollars = numCoins(restOfChange, 1) 
restOfChange = round(restOfChange - dollars * 1, 2) 
quarters = numCoins(restOfChange, 0.25) 
restOfChange = round(restOfChange - quarters * 0.25, 2) 
dimes = numCoins(restOfChange, 0.10) 
restOfChange = round(restOfChange - dimes * 0.10, 2) 
nickles = numCoins(restOfChange, 0.05) 
pennies = int(round(restOfChange - nickles * 0.05, 2) * 
100) 

# what user is owed 
print("OK, here is your change:") 
print(dollars, "dollars", quarters, "quarters", dimes,  
      "dimes", nickles, "nickles", pennies, "pennies") 


# End of main program
print("\nend: Correct change")